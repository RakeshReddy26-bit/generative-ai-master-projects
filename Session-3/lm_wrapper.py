import os
import requests

LM_HOST = os.getenv("LM_STUDIO_HOST", "http://localhost:8080").rstrip("/")
DEFAULT_TIMEOUT = 60

def call_lm(prompt: str, model: str, request_path="/v1/generate", params: dict=None, timeout:int=DEFAULT_TIMEOUT):
    url = LM_HOST + request_path
    payload = {"model": model, "input": prompt}
    if params:
        payload["parameters"] = params
    headers = {"Content-Type": "application/json"}
    resp = requests.post(url, json=payload, headers=headers, timeout=timeout)
    resp.raise_for_status()
    j = resp.json()
    if isinstance(j, dict):
        for k in ("output","text","result","response"):
            if k in j:
                return j[k]
        return j
    return j
