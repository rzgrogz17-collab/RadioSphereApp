import json, glob, sys

all_stations = []
errors = []

for f in sorted(glob.glob("src/*.json")):
    with open(f, encoding="utf-8") as fh:
        text = fh.read()
    try:
        all_stations += json.loads(text)
    except json.JSONDecodeError as e:
        lines = text.splitlines()
        line = lines[e.lineno - 1] if e.lineno <= len(lines) else ""
        errors.append(f"{f}: satir {e.lineno}, sutun {e.colno}: {e.msg}\n    -> {line!r}")

if errors:
    print("Hatali JSON dosyalari:")
    print("\n".join(errors))
    sys.exit(1)

with open("stations.json", "w", encoding="utf-8") as out:
    json.dump(all_stations, out, ensure_ascii=False, separators=(",", ":"))

print(f"{len(all_stations)} radyo birlestirildi")
