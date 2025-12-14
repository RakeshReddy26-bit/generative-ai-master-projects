# main_full.py - runs MTOP intent eval with 3 prompting strategies
import argparse, json, os, re
from datasets import load_dataset
from sklearn.metrics import f1_score
from tqdm import tqdm
from lm_wrapper import call_lm

def normalize_label(s):
    if s is None: return ""
    s = str(s).strip().lower()
    s = re.sub(r'^[^a-z0-9]+|[^a-z0-9]+$', '', s)
    return s

def build_prompt(strategy, utterance):
    if strategy=="reward":
        return f"You will earn points for correct classification. Task: output the single intent label.\nUtterance: \"{utterance}\"\nOnly respond with the intent label."
    if strategy=="affirmation":
        return f"You are accurate and careful. Extract the intent label.\nUtterance: \"{utterance}\"\nAnswer with the single intent label."
    if strategy=="reasoning":
        return f"Step-by-step: list possibilities, pick the best, then output the label.\nUtterance: \"{utterance}\"\nReason briefly then on last line write ONLY the intent label."
    return f"Utterance: \"{utterance}\"\nOutput intent label:"

def extract_label(out):
    if isinstance(out, dict):
        for k in ("output","text","result","response"):
            if k in out: return normalize_label(out[k])
        return normalize_label(json.dumps(out))
    if isinstance(out, list): return normalize_label(out[0]) if out else ""
    return normalize_label(out)

def load_samples(lang="de", split="validation", sample_size=50):
    ds = load_dataset("mteb/mtop_intent", lang)
    if split not in ds: split=list(ds.keys())[0]
    data = ds[split]
    records=[]
    for ex in data:
        utter = ex.get("utterance") or ex.get("query") or ex.get("input")
        intent = ex.get("intent") or ex.get("label")
        if utter is not None and intent is not None:
            records.append({"utterance":utter, "intent":intent})
        if len(records)>=sample_size: break
    if not records: raise RuntimeError("Couldn't extract utterance/intent from dataset sample.")
    return records

def predict(samples, model, strategy):
    preds=[]
    for s in tqdm(samples, desc=f"{model}:{strategy}"):
        prompt = build_prompt(strategy, s["utterance"])
        out = call_lm(prompt, model=model)
        preds.append(extract_label(out))
    return preds

def save_results(model, strategy, samples, preds):
    y_true=[normalize_label(s["intent"]) for s in samples]
    y_pred=preds
    f1_macro = f1_score(y_true, y_pred, average="macro")
    f1_weighted = f1_score(y_true, y_pred, average="weighted")
    os.makedirs("results", exist_ok=True)
    summary = {"model":model,"strategy":strategy,"n":len(samples),"f1_macro":float(f1_macro),"f1_weighted":float(f1_weighted)}
    json_path = f"results/{model.replace('/','-')}_{strategy}.json"
    with open(json_path,"w") as f: json.dump(summary, f, indent=2)
    csv_path = f"results/{model.replace('/','-')}_{strategy}.csv"
    with open(csv_path,"w") as f:
        f.write("utterance,true,pred\n")
        for s, t, p in zip(samples, y_true, y_pred):
            utt = s["utterance"].replace('"', "'")
            f.write(f'"{utt}","{t}","{p}"\n')
    return summary, json_path, csv_path

def interactive_yesno(prompt="Proceed? (yes/no): "):
    ans = input(prompt).strip().lower()
    return ans in ("y","yes")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model", default=os.getenv("LM_MODEL","phi-3.1-mini"))
    p.add_argument("--lang", default="de")
    p.add_argument("--sample-size", type=int, default=50)
    args = p.parse_args()

    print(f"Model: {args.model}, lang: {args.lang}, sample-size: {args.sample_size}")
    if not interactive_yesno("If you want to proceed with prediction say 'yes': "):
        print("say me"); return

    samples = load_samples(lang=args.lang, sample_size=args.sample_size)
    strategies = ["reward","affirmation","reasoning"]
    for strat in strategies:
        preds = predict(samples, args.model, strat)
        summary, jpath, cpath = save_results(args.model, strat, samples, preds)
        print(f"Saved {jpath} / {cpath} -> F1 macro: {summary['f1_macro']:.4f}")

if __name__ == "__main__":
    main()
