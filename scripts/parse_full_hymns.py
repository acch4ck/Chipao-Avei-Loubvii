import json
import re
import os
import pypdf

PDF_PATH = r"C:\Users\MEC-Oni\.gemini\antigravity\brain\e2e67671-24b4-4903-8fe7-8645ee02122a\.user_uploaded\media_1793179628974_d48713ab.pdf"

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
    clean = key_sig.replace("Doh is", "").replace("Doh Is", "").replace("Key", "").replace("key", "").replace("is", "").strip()
    clean = clean.replace(" ", "")
    if clean.endswith('b'):
        clean = clean[0].upper() + 'b'
    elif clean.endswith('#'):
        clean = clean[0].upper() + '#'
    else:
        clean = clean[:1].upper()
    return KEY_PITCH.get(clean, 440.0), clean

REF_PATTERN = r'\s*\(?\b(S\.S\.|K\.K\.|Red\.|Alex\.|Ins\.\s*H\.|Ins\.|M\.H\.|CSH\.?|C\.S\.H\.|C\.H\.|S\.G\.S\.|STL\.|STTH\.|C\.W\.H\.|B\.C\.S\.|H\.C\.|B\.H\.|CAL\.)\s*(\d+[A-Za-z]?)\)?'

FOOTER_CATEGORY_PATTERNS = [
    r'^\s*\(?.*?\)?\s*Mission & Evangelism.*',
    r'^\s*\(?.*?\)?\s*Conflict & Courage.*',
    r'^\s*\(?.*?\)?\s*Christian Endeavour.*',
    r'^\s*\(?.*?\)?\s*C\s*hristian Endeavour.*',
    r'^\s*\(?.*?\)?\s*Heavenly Home.*',
    r'^\s*\(?.*?\)?\s*Heveanly Home.*',
    r'^\s*\(?.*?\)?\s*Repentance,\s*Commitment & Hope.*',
    r'^\s*\(?.*?\)?\s*Second Coming & Rapture.*',
    r'^\s*\(?.*?\)?\s*Funeral,\s*Life to Come.*',
    r'^\s*\(?.*?\)?\s*Baptismal.*',
    r'^\s*\(?.*?\)?\s*Christmas.*',
    r'^\s*\(?.*?\)?\s*Closing Worship.*',
    r'^\s*\(?.*?\)?\s*New Year.*',
    r'^\s*\(?.*?\)?\s*Palm Sunday.*',
    r'^\s*\(?.*?\)?\s*Good Friday & Easter Sunday.*',
    r'^\s*\(?.*?\)?\s*Lord[\'’]?s\s*Supper.*',
    r'^\s*\(?.*?\)?\s*Christian Experience.*',
    r'^\s*\(?.*?\)?\s*C\s*hristian Experience.*',
    r'^\s*\(?.*?\)?\s*Wedding.*',
    r'^\s*\(?.*?\)?\s*Mother[\'’]?s & Father[\'’]?s Day.*',
    r'^\s*\(?.*?\)?\s*Offeratory.*',
    r'^\s*\(?.*?\)?\s*Revival,\s*Choruses & Social.*',
    r'^\s*\(?.*?\)?\s*Revival,\s*Choruses & Social\s*$',
    r'^\s*\(Conflict & Courage\).*',
    r'^\s*\(Christian Endeavour\).*',
    r'^\s*\(Praise & Adoration\).*',
    r'^\s*\(Assurance & Testimony\).*',
    r'^\s*\(Dedication\).*',
    r'^\s*\(Funeral\).*',
    r'^\s*\(Worship Closing\s*\).*',
    r'^-\s*\(\s*\d*\s*\)\s*-$',
    r'^-\s*\(\s*\)\s*-$',
    r'^\s*HALLELUYAH\s+CHORUS\s*$'
]

def is_footer_or_header_line(line):
    l_str = line.strip()
    if not l_str:
        return True
    for pat in FOOTER_CATEGORY_PATTERNS:
        if re.match(pat, l_str, re.IGNORECASE):
            return True
    return False

def clean_text_line(line):
    l = line.strip()
    # Normalize dot spaces: "S.G .S." -> "S.G.S.", "Dr ." -> "Dr."
    l = re.sub(r'([A-Za-z])\s+\.', r'\1.', l)
    l = re.sub(r'\b([A-Z]\.)\s+([A-Z]\.)', r'\1\2', l)
    l = re.sub(r'\b([A-Z]\.)\s+([A-Z]\.)', r'\1\2', l) # 2nd pass for 3-part abbreviations
    
    # Common words
    l = re.sub(r'\bY\s+ou\b', 'You', l)
    l = re.sub(r'\bY\s+our\b', 'Your', l)
    l = re.sub(r'\bI\s*\.\s*D\s*\.\s*S\b', 'I.D.S', l)
    l = re.sub(r'\bC\s*\.\s*F\s*\.\s*Handel\b', 'C.F. Handel', l)
    return l

def extract_half_pages(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    all_halves = []
    for s_idx, page in enumerate(reader.pages):
        left_items, right_items = [], []
        def visitor(text, cm, tm, fontDict, fontSize):
            if text.strip():
                x, y = tm[4], tm[5]
                if x < 420:
                    left_items.append((y, x, text))
                else:
                    right_items.append((y, x, text))
        page.extract_text(visitor_text=visitor)

        def group_lines(items):
            if not items:
                return []
            items.sort(key=lambda it: (-it[0], it[1]))
            lines = []
            cur_line = []
            cur_y = None
            for y, x, t in items:
                if cur_y is None or abs(cur_y - y) <= 3.0:
                    cur_line.append((x, t))
                    if cur_y is None:
                        cur_y = y
                else:
                    cur_line.sort(key=lambda it: it[0])
                    lines.append(' '.join(it[1].strip() for it in cur_line if it[1].strip()))
                    cur_line = [(x, t)]
                    cur_y = y
            if cur_line:
                cur_line.sort(key=lambda it: it[0])
                lines.append(' '.join(it[1].strip() for it in cur_line if it[1].strip()))
            return lines

        left_l = group_lines(left_items)
        right_l = group_lines(right_items)
        all_halves.append((s_idx + 1, 'L', left_l))
        all_halves.append((s_idx + 1, 'R', right_l))
    return all_halves

def segment_hymns(all_halves):
    hymns_raw = {}
    current_id = None
    current_lines = []
    current_category = ""

    all_content = []
    for sheet, side, lines in all_halves:
        all_content.append((sheet, side, lines))

    for sheet, side, lines in all_content:
        page_category = ""
        cleaned_lines = []
        for l in lines:
            if re.match(r'^-\s*\(\s*\d*\s*\)\s*-$', l.strip()) or re.match(r'^-\s*\(\s*\)\s*-$', l.strip()):
                continue
            cleaned_lines.append(l)

        i = 0
        while i < len(cleaned_lines):
            line = cleaned_lines[i]
            m = re.match(r'^(\d{3})\s+([A-Z\u00dc\u00fc\s\',.!?-]+)', line)
            if not m:
                m = re.match(r'^(\d{3})([A-Z\u00dc\u00fc].*)', line)
            h_id = None
            if m:
                cand = int(m.group(1))
                if 220 <= cand <= 500:
                    h_id = cand
            elif '500' in line:
                m5 = re.search(r'\b500\b', line)
                if m5:
                    h_id = 500

            if h_id is not None:
                if current_id is not None:
                    hymns_raw[current_id] = {
                        'category': current_category,
                        'lines': current_lines
                    }
                current_id = h_id
                current_lines = [line]
                if i > 0:
                    prev = cleaned_lines[i-1].strip()
                    if not re.match(r'^\d', prev) and len(prev) > 3 and not prev.startswith('('):
                        current_category = prev
                    elif prev.startswith('(') and i > 1:
                        prev2 = cleaned_lines[i-2].strip()
                        current_category = f"{prev2} {prev}"
                elif page_category:
                    current_category = page_category
            else:
                if current_id is not None:
                    current_lines.append(line)
                else:
                    if len(line.strip()) > 3 and not line.strip().startswith('1.'):
                        page_category = line.strip()
            i += 1

    if current_id is not None:
        hymns_raw[current_id] = {
            'category': current_category,
            'lines': current_lines
        }

    return hymns_raw

def clean_poula_title(title_raw):
    t = title_raw.strip()
    t = re.sub(r'\bV\s+AHSOUO\b', 'VAHSOUO', t)
    t = re.sub(r'\bV\s+AH\b', 'VAH', t)
    t = re.sub(r'\bJIHOV\s+AH\b', 'JIHOVAH', t)
    t = re.sub(r'\bEHT\s+AO\b', 'ETAO', t)
    t = re.sub(r'\bP\s+A\b', 'PA', t)
    t = re.sub(r'\bCHIP\s+AO\b', 'CHIPAO', t)
    t = re.sub(r'\bKAL\s+V\s+ARI\b', 'KALVARI', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t

def parse_full_hymn(h_id, raw_data):
    raw_lines = [clean_text_line(l) for l in raw_data['lines'] if l.strip()]

    if h_id == 500:
        return parse_hymn_500(raw_lines)

    title = ""
    ref = ""
    eng_title = ""
    scripture = ""
    time_sig = ""
    key_sig = ""
    author = ""
    composer = ""
    verses = []
    chorus = []

    line0 = raw_lines[0]
    line0_clean = re.sub(r'^\s*' + str(h_id) + r'\s*', '', line0).strip()
    
    # Check for Ref in line0
    m_ref = re.search(REF_PATTERN, line0_clean, re.IGNORECASE)
    if m_ref:
        ref = m_ref.group(0).strip(' ()')
        title = line0_clean[:m_ref.start()].strip()
    else:
        title = line0_clean

    title = clean_poula_title(title)

    # Process header lines
    body_start_idx = 1
    for idx in range(1, min(5, len(raw_lines))):
        cur = raw_lines[idx]
        
        # Stop if explicit verse/chorus marker
        if re.match(r'^(1\.|1\s+[A-Z\u00dc\u00fc]|Khoras|Chorus)\b', cur, re.IGNORECASE):
            body_start_idx = idx
            break

        is_header = False

        # Check for English Title (usually in parentheses)
        eng_match = re.search(r'\(([^)]+)\)', cur)
        if eng_match:
            cand_eng = eng_match.group(1).strip()
            lower_cand = cand_eng.lower()
            if not re.search(r'\b(arr|times|repeat|ref)\b', lower_cand):
                if not eng_title:
                    eng_title = cand_eng
                    is_header = True

            # Check if there is scripture or ref on this line
            rest = (cur[:eng_match.start()] + ' ' + cur[eng_match.end():]).strip()
            sc_match = re.search(r'\b([I|II|III]?\s*[A-Za-z]+\.?\s*\d+:\d+(?:-\d+)?)\b', rest)
            if sc_match:
                scripture = sc_match.group(1).strip()
                is_header = True
            if not ref:
                m_ref2 = re.search(REF_PATTERN, rest, re.IGNORECASE)
                if m_ref2:
                    ref = m_ref2.group(0).strip(' ()')
                    is_header = True
        else:
            # Maybe English title without parentheses (e.g. Hymn 386 'Calvary Lk. 3:33')
            sc_match = re.search(r'\b([I|II|III]?\s*[A-Za-z]+\.?\s*\d+:\d+(?:-\d+)?)\b', cur)
            if sc_match:
                scripture = sc_match.group(1).strip()
                cand_title = cur[:sc_match.start()].strip()
                if cand_title and not eng_title and not re.match(r'^\d', cand_title):
                    eng_title = cand_title
                is_header = True

        # Check for Key signature (e.g. "Doh is ...")
        key_match = re.search(r'\b(?:Doh\s+is|Key)\s+([A-G]\s*(?:b|\#)?)', cur, re.IGNORECASE)
        if key_match:
            is_header = True
            raw_k = key_match.group(1).replace(' ', '')
            key_sig = f"Doh is {raw_k}"
            
            # Meter / Time signature on same line
            m_meter = re.search(r'\b(\d/\d|C)\b', cur)
            if m_meter:
                time_sig = m_meter.group(1).strip()

            before_key = cur[:key_match.start()].strip()
            after_key = cur[key_match.end():].strip()
            if m_meter and m_meter.start() < key_match.start():
                auth_cand = before_key[:m_meter.start()].strip()
            else:
                auth_cand = before_key

            if auth_cand and not re.match(r'^\d', auth_cand) and not auth_cand.startswith('('):
                author = auth_cand
            if after_key and not re.match(r'^\d', after_key) and not after_key.startswith('('):
                composer = after_key
        else:
            # Check for solitary author/composer lines like 'Gabriel' or 'Rev.R.L.Tennyson'
            if any(name in cur for name in ['Gabriel', 'Tennyson', 'Lowry', 'Sankey', 'Bliss', 'Stebbins']):
                is_header = True
                if not composer:
                    composer = cur
            elif re.search(r'^\s*[A-Z\.]+\s+(\d/\d|C)\s+[A-Za-z\.]+', cur):
                # e.g. 'S.P.P. 4/4 S.P.Puni'
                is_header = True
                m_meter = re.search(r'\b(\d/\d|C)\b', cur)
                if m_meter:
                    time_sig = m_meter.group(1)
                    author = cur[:m_meter.start()].strip()
                    composer = cur[m_meter.end():].strip()

        # Check for scripture on its own line (e.g. 'Gen.2:22')
        if not scripture:
            sc_alone = re.match(r'^\s*([I|II|III]?\s*[A-Za-z]+\.?\s*\d+:\d+(?:-\d+)?)\s*$', cur)
            if sc_alone:
                scripture = sc_alone.group(1).strip()
                is_header = True

        if not is_header:
            body_start_idx = idx
            break
        else:
            body_start_idx = idx + 1

    # Extract body lines, filtering footer categories
    body_lines = []
    for l in raw_lines[body_start_idx:]:
        if is_footer_or_header_line(l):
            continue
        body_lines.append(l)

    # Parse verses & chorus
    current_verse_num = None
    current_verse_lines = []
    in_chorus = False

    for l in body_lines:
        if re.match(r'^(Khoras|Chorus)\b', l, re.IGNORECASE):
            if current_verse_num is not None and current_verse_lines:
                verses.append({
                    'verseNumber': current_verse_num,
                    'lines': current_verse_lines
                })
                current_verse_num = None
                current_verse_lines = []
            in_chorus = True
            rest = re.sub(r'^(Khoras|Chorus)\s*:?\s*', '', l, flags=re.IGNORECASE).strip()
            if rest:
                chorus.append(rest)
            continue

        vm = re.match(r'^(\d+)\.\s*(.*)', l)
        if not vm:
            vm = re.match(r'^(\d+)\s+([A-Z\u00dc\u00fc].*)', l)
        
        if vm:
            if in_chorus:
                in_chorus = False
            elif current_verse_num is not None and current_verse_lines:
                verses.append({
                    'verseNumber': current_verse_num,
                    'lines': current_verse_lines
                })
            current_verse_num = int(vm.group(1))
            current_verse_lines = []
            if vm.group(2).strip():
                current_verse_lines.append(vm.group(2).strip())
            continue

        if in_chorus:
            chorus.append(l)
        elif current_verse_num is not None:
            current_verse_lines.append(l)
        else:
            if not current_verse_lines:
                current_verse_num = 1
            current_verse_lines.append(l)

    if current_verse_num is not None and current_verse_lines:
        verses.append({
            'verseNumber': current_verse_num,
            'lines': current_verse_lines
        })

    if not verses and body_lines:
        verses.append({
            'verseNumber': 1,
            'lines': body_lines
        })

    first_line = ""
    if verses and verses[0]['lines']:
        first_line = verses[0]['lines'][0].strip().rstrip(',;.:')

    primary_cat, all_cats = get_categories_for_id(h_id)
    pitch_hz, keynote = parse_key_pitch(key_sig)

    return {
        "id": h_id,
        "title": title,
        "englishTitle": eng_title,
        "firstLine": first_line,
        "timeSignature": time_sig,
        "keySignature": key_sig,
        "hymnBookRef": ref,
        "author": author,
        "composer": composer,
        "scripture": scripture,
        "category": primary_cat,
        "verses": verses,
        "chorus": chorus if chorus else None,
        "keynotePitchHz": pitch_hz,
        "keynoteName": keynote,
        "tune": eng_title,
        "meter": time_sig,
        "year": "",
        "categories": all_cats
    }

def parse_hymn_500(raw_lines):
    primary_cat, all_cats = get_categories_for_id(500)
    pitch_hz, keynote = parse_key_pitch("Doh is D")

    # Clean lines for 500
    v_lines = []
    for l in raw_lines:
        if is_footer_or_header_line(l):
            continue
        if re.match(r'^(500|Doh is D|C\.F\. Handel)\b', l):
            continue
        v_lines.append(l)

    return {
        "id": 500,
        "title": "HALLELUYAH CHORUS",
        "englishTitle": "Hallelujah Chorus",
        "firstLine": "Hallelujah, Hallelujah, Hallelujah",
        "timeSignature": "4/4",
        "keySignature": "Doh is D",
        "hymnBookRef": "",
        "author": "",
        "composer": "C.F. Handel",
        "scripture": "Rev. 19:6",
        "category": primary_cat,
        "verses": [
            {
                "verseNumber": 1,
                "lines": v_lines
            }
        ],
        "chorus": None,
        "keynotePitchHz": pitch_hz,
        "keynoteName": keynote,
        "tune": "Hallelujah Chorus",
        "meter": "4/4",
        "year": "",
        "categories": all_cats
    }
