from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path not in ("/v1/generate", "/v1/outputs"):
            self.send_response(404); self.end_headers(); return
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length).decode()
        try:
            j = json.loads(body)
            inp = str(j.get("input", "") or j.get("prompt", ""))
            label = "greeting" if any(w in inp.lower() for w in ("hi","hello","hey")) else "other"
            out = {"output": label, "debug_input": inp}
        except Exception as e:
            out = {"error": str(e)}
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(out).encode())

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8080), Handler)
    print("Mock LM server running at http://localhost:8080 (Ctrl-C to stop)")
    server.serve_forever()
