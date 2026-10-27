import sys
import os
import json

sys.path.append(os.path.abspath("scripts/hymn_builder"))
import part1, part2, part3, part4, part5
import part6, part7, part8, part9, part10

KEY_PITCH = {
    "C": 261.63, "C#": 277.18, "Db": 277.18,
    "D": 293.66, "D#": 311.13, "Eb": 311.13,
    "E": 329.63,
    "F": 349.23, "F#": 369.99,
    "G": 392.00, "G#": 415.30, "Ab": 415.30,
    "A": 440.00, "A#": 466.16, "Bb": 466.16,
    "B": 493.88
}

INDEX_DATA = [
    (1, "Praise & Adoration", [(1, 22), (330, 330)], "1-22, 330"),
    (2, "Worship", [(23, 53)], "23-53"),
    (3, "Prayer & Consecration", [(54, 72), (440, 440)], "54-72, 440"),
    (4, "Faith & Trust", [(73, 97), (50, 50)], "73-97, 50"),
    (5, "The Gospel", [(98, 116)], "98-116"),
    (6, "Gospel Invitation", [(117, 140), (214, 214)], "117-140, 214"),
    (7, "Love", [(141, 158), (83, 83)], "141-158, 83"),
    (8, "Assurance & Testimony", [(159, 179), (24, 24), (107, 107), (331, 331), (404, 404), (406, 406), (407, 407)], "159-179, 24, 107, 331, 404, 406, 407"),
    (9, "Guidance", [(180, 193), (51, 51)], "180-193, 51"),
    (10, "Mission & Evangelism", [(194, 237), (114, 114)], "194-237, 114"),
    (11, "Heavenly Home", [(238, 267)], "238-267"),
    (12, "Repentance, Commitment & Hope", [(268, 291)], "268-291"),
    (13, "Second Coming & Rapture", [(292, 305)], "292-305"),
    (14, "Funeral, Life to Come", [(306, 325), (110, 110), (242, 242)], "306-325, 110, 242"),
    (15, "Baptism", [(326, 329)], "326-329"),
    (16, "Christian Endeavour", [(330, 358), (36, 36), (213, 213), (216, 216), (219, 219), (221, 221), (233, 233), (277, 277)], "330-358, 36, 213, 216, 219, 221, 233, 277"),
    (17, "Christmas", [(359, 375)], "359-375"),
    (18, "Closing Worship", [(306, 306), (376, 376)], "306, 376"),
    (19, "New Year", [(377, 381)], "377-381"),
    (20, "Palm Sunday", [(382, 382)], "382"),
    (21, "Good Friday & Easter Sunday", [(383, 405)], "383-405"),
    (22, "Lord’s Supper", [(406, 413)], "406-413"),
    (23, "Christian Experience", [(414, 430)], "414-430"),
    (24, "Wedding", [(431, 433)], "431-433"),
    (25, "Dedication & Church Foundation Day", [(21, 21), (195, 195), (269, 269), (275, 275)], "21, 195, 269, 275"),
    (26, "Mothers’ & Fathers’ Day", [(434, 439)], "434-439"),
    (27, "Conflict & Courage", [(440, 447), (220, 220), (223, 223)], "440-447, 220, 223"),
    (28, "Jubilee", [(446, 446), (447, 447)], "446, 447"),
    (29, "Offeratory", [(448, 451)], "448-451"),
    (30, "Revival, Choruses & Social", [(452, 500)], "452-500")
]

PRIMARY_SECTIONS = [
    (1, 22, "Praise & Adoration"),
    (23, 53, "Worship"),
    (54, 72, "Prayer & Consecration"),
    (73, 97, "Faith & Trust"),
    (98, 116, "The Gospel"),
    (117, 140, "Gospel Invitation"),
    (141, 158, "Love"),
    (159, 179, "Assurance & Testimony"),
    (180, 193, "Guidance"),
    (194, 237, "Mission & Evangelism"),
    (238, 267, "Heavenly Home"),
    (268, 291, "Repentance, Commitment & Hope"),
    (292, 305, "Second Coming & Rapture"),
    (306, 325, "Funeral, Life to Come"),
    (326, 329, "Baptism"),
    (330, 358, "Christian Endeavour"),
    (359, 375, "Christmas"),
    (376, 376, "Closing Worship"),
    (377, 381, "New Year"),
    (382, 382, "Palm Sunday"),
    (383, 405, "Good Friday & Easter Sunday"),
    (406, 413, "Lord’s Supper"),
    (414, 430, "Christian Experience"),
    (431, 433, "Wedding"),
    (434, 439, "Mothers’ & Fathers’ Day"),
    (440, 445, "Conflict & Courage"),
    (446, 447, "Jubilee"),
    (448, 451, "Offeratory"),
    (452, 500, "Revival, Choruses & Social")
]

def get_categories_for_id(hymn_id):
    primary = None
    for s, e, cat in PRIMARY_SECTIONS:
        if s <= hymn_id <= e:
            primary = cat
            break
    all_cats = []
    if primary:
        all_cats.append(primary)
    for _, name, ranges, _ in INDEX_DATA:
        for s, e in ranges:
            if s <= hymn_id <= e:
                if name not in all_cats:
                    all_cats.append(name)
                break
    return primary, all_cats

def parse_key_pitch(key_sig):
    if not key_sig:
        return 440.0, "A"
    clean = key_sig.replace("Doh is", "").replace("Doh Is", "").replace("Doh is", "").strip()
    return KEY_PITCH.get(clean, 440.0), clean

all_parts = [
    part1.get_part1(),
    part2.get_part2(),
    part3.get_part3(),
    part4.get_part4(),
    part5.get_part5(),
    part6.get_part6(),
    part7.get_part7(),
    part8.get_part8(),
    part9.get_part9(),
    part10.get_part10(),
]

full_catalog = []
for p_idx, part in enumerate(all_parts, start=1):
    print(f"Part {p_idx}: {len(part)} hymns")
    for hymn in part:
        key_sig = hymn.get("keySignature", "")
        pitch, k_name = parse_key_pitch(key_sig)
        hymn["keynotePitchHz"] = pitch
        hymn["keynoteName"] = k_name
        if "tune" not in hymn:
            hymn["tune"] = hymn.get("englishTitle") or hymn.get("hymnBookRef", "")
        if "meter" not in hymn:
            hymn["meter"] = hymn.get("timeSignature", "")
        if "year" not in hymn:
            hymn["year"] = ""
        primary, all_cats = get_categories_for_id(hymn["id"])
        hymn["category"] = primary
        hymn["categories"] = all_cats
        full_catalog.append(hymn)

print(f"Total compiled hymns: {len(full_catalog)}")

# Verification
ids = [h["id"] for h in full_catalog]
assert len(ids) == 500, f"Expected 500 hymns, got {len(ids)}"
assert min(ids) == 1, f"Expected min id 1, got {min(ids)}"
assert max(ids) == 500, f"Expected max id 500, got {max(ids)}"
assert len(set(ids)) == 500, "Duplicate hymn IDs found!"

os.makedirs("app/src/main/assets", exist_ok=True)
output_path = "app/src/main/assets/hymns.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(full_catalog, f, ensure_ascii=False, indent=2)

file_size_kb = os.path.getsize(output_path) / 1024
print(f"Successfully wrote {output_path} ({file_size_kb:.1f} KB)")
