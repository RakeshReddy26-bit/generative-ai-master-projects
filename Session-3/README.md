Run (dry-run uses mock server):
1) Start mock: python mock_server.py
2) Run:
   printf "yes\n" | LM_STUDIO_HOST="http://localhost:8080" python main_full.py --model phi-3.1-mini --lang de --sample-size 20
