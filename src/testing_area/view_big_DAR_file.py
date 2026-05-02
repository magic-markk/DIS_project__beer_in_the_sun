from pathlib import Path
import json
import ijson

DATA_DIR = Path.cwd().parents[1] / 'data'
FILEPATH = DATA_DIR / 'DAR_V3_Adresse_TotalDownload_json_Bitemporal_615.json'
OUTPUT_PATH = DATA_DIR / 'DAR_Adresse_snippet.json'

results = []

with open(FILEPATH, "r", encoding="utf-8") as f:
    for obj in ijson.items(f, "item"):
        results.append({
            "id_lokalId": obj.get("id_lokalId"),
            "adressebetegnelse": obj.get("adressebetegnelse")
        })

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("Done")