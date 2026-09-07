#!/usr/bin/env python3
"""Minimal Gemini image gen. ponytail: curl-equivalent, no SDK install."""
import base64, json, os, sys, urllib.request

KEY = os.environ["GK"]
MODEL = os.environ.get("MODEL", "gemini-3-pro-image")
prompt_file, out_path = sys.argv[1], sys.argv[2]
ratio = sys.argv[3] if len(sys.argv) > 3 else "16:9"

body = {
    "contents": [{"parts": [{"text": open(prompt_file).read()}]}],
    "generationConfig": {"imageConfig": {"aspectRatio": ratio, "imageSize": "2K"}},
}
req = urllib.request.Request(
    f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={KEY}",
    data=json.dumps(body).encode(), headers={"Content-Type": "application/json"},
)
try:
    resp = json.load(urllib.request.urlopen(req, timeout=300))
except urllib.error.HTTPError as e:
    print("HTTP", e.code, e.read().decode()[:600]); sys.exit(1)

for part in resp["candidates"][0]["content"]["parts"]:
    if "inlineData" in part:
        open(out_path, "wb").write(base64.b64decode(part["inlineData"]["data"]))
        print("WROTE", out_path, os.path.getsize(out_path), "bytes"); sys.exit(0)
print("NO IMAGE:", json.dumps(resp)[:800]); sys.exit(1)
