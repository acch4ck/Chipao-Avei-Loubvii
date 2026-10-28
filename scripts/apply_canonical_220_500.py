import json
import re
import os
import sys

sys.path.append(os.path.abspath("scripts"))
from parse_full_hymns import (
    PDF_PATH, extract_half_pages, segment_hymns, parse_full_hymn
)

JSON_PATH = r"app\src\main\assets\hymns.json"

def main():
    print("1. Parsing all 281 hymns from PDF (220 to 500)...")
    all_halves = extract_half_pages(PDF_PATH)
    hymns_raw = segment_hymns(all_halves)

    new_hymns_map = {}
    for hid in range(220, 501):
        h = parse_full_hymn(hid, hymns_raw[hid])
        new_hymns_map[hid] = h

    print(f"Parsed {len(new_hymns_map)} hymns.")

    print("\n2. Loading existing hymns.json...")
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        existing_hymns = json.load(f)

    print(f"Existing hymns.json has {len(existing_hymns)} hymns.")

    # Create updated list
    updated_hymns = []
    updated_count = 0
    for h in existing_hymns:
        hid = h['id']
        if hid in new_hymns_map:
            updated_hymns.append(new_hymns_map[hid])
            updated_count += 1
        else:
            updated_hymns.append(h)

    print(f"Replaced {updated_count} hymns in hymns.json.")

    print("\n3. Validating updated dataset...")
    assert len(updated_hymns) == 500, f"Expected 500 hymns, got {len(updated_hymns)}"
    for idx, h in enumerate(updated_hymns, start=1):
        assert h['id'] == idx, f"Hymn id mismatch at index {idx}: {h['id']}"
        assert h['title'], f"Empty title in hymn {idx}"
        assert h['verses'], f"Empty verses in hymn {idx}"
        assert h['firstLine'], f"Empty firstLine in hymn {idx}"

    print("All 500 hymns successfully validated.")

    print("\n4. Writing updated hymns.json...")
    with open(JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(updated_hymns, f, ensure_ascii=False, indent=2)

    file_size = os.path.getsize(JSON_PATH)
    print(f"Written {file_size} bytes to {JSON_PATH}.")

    print("\n5. Updating hymn_builder python scripts...")
    # Update parts 5..10 in scripts/hymn_builder
    # part5: 201..250
    # part6: 251..300
    # part7: 301..350
    # part8: 351..400
    # part9: 401..450
    # part10: 451..500
    
    parts_ranges = [
        (5, 201, 250),
        (6, 251, 300),
        (7, 301, 350),
        (8, 351, 400),
        (9, 401, 450),
        (10, 451, 500)
    ]

    for part_num, start_id, end_id in parts_ranges:
        part_hymns = [updated_hymns[i - 1] for i in range(start_id, end_id + 1)]
        part_file = f"scripts/hymn_builder/part{part_num}.py"
        raw_json_str = json.dumps(part_hymns, ensure_ascii=False, indent=2)
        with open(part_file, 'w', encoding='utf-8') as pf:
            pf.write(f"# Auto-generated canonical hymnal data for hymns {start_id} to {end_id}\n")
            pf.write(f"# From official Chipao Avei Loubvü scan\n")
            pf.write("import json\n\n")
            pf.write(f"_DATA = r'''{raw_json_str}'''\n\n")
            pf.write(f"def get_part{part_num}():\n")
            pf.write(f"    return json.loads(_DATA)\n")
        print(f"Updated {part_file} with {len(part_hymns)} hymns ({start_id}..{end_id}).")

    print("\nDone! Canonical data applied to both hymns.json and hymn_builder scripts.")

if __name__ == '__main__':
    main()
