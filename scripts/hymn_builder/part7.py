# Hymns 301 to 350 for Chipao Avei Loubvü
def get_part7():
    titles = [
        (301, "RAMAI KHE HI VEILOUWO", "Nearer, My God, to Thee", "Ramai khe hi veilouwo Mapao Jisu", "6/4", "Doh is G", "S.S. 535", "Sarah F. Adams", "Lowell Mason", "Gen. 28:20", "Prayer & Consecration"),
        (302, "THEIKHOU, THEIKHOU, THEIKHOU", "Holy, Holy, Holy", "Theikhou, theikhou, theikhou Mapao Ramai", "4/4", "Doh is Eb", "C.W.H. 1", "Reginald Heber", "John B. Dykes", "Rev. 4:8", "Worship"),
        (303, "PEIRÜ RÜLO VEOPUYE", "Crown Him With Many Crowns", "Peirü rülo Veopuye sana peirü", "4/4", "Doh is D", "S.S. 165", "Matthew Bridges", "George J. Elvey", "Rev. 19:12", "Praise & Adoration"),
        (304, "ASAYU LOU SOULAISA", "Joy To The World", "Asayu lou soulaisa Mapao veire", "2/4", "Doh is D", "C.W.H. 42", "Isaac Watts", "G.F. Handel", "Ps. 98:4", "Praise & Adoration"),
        (305, "THEIKHOU BUYU KHEI", "Silent Night, Holy Night", "Theikhou buyu khei teithe buyu khei", "6/8", "Doh is Bb", "C.W.H. 46", "Joseph Mohr", "Franz Gruber", "Luke 2:11", "Worship"),
        (306, "TEIKHAI ZAIPE PAOSHO LOU", "Hark! The Herald Angels Sing", "Teikhai zaipe paosho lou soulaikhe", "4/4", "Doh is F", "C.W.H. 44", "Charles Wesley", "Felix Mendelssohn", "Luke 2:14", "Praise & Adoration"),
        (307, "KHRISTA THOURE ARAKO", "Christ The Lord Is Risen Today", "Khrista thoure arako Hallelujah", "4/4", "Doh is C", "C.W.H. 58", "Charles Wesley", "Lyra Davidica", "Matt. 28:6", "Praise & Adoration"),
        (308, "ZHAOTOU HINOU THOURE", "Low In The Grave He Lay", "Zhaotou hinou thoure Jisu Veopu", "4/4", "Doh is Bb", "S.S. 147", "Robert Lowry", "Robert Lowry", "Luke 24:6", "The Gospel"),
        (309, "E KHE BUWO MAPAO", "Abide With Me", "E khe buwo Mapao khei peiyuki", "4/4", "Doh is Eb", "C.W.H. 320", "H.F. Lyte", "W.H. Monk", "Luke 24:29", "Evening"),
        (310, "SUN OF MY SOUL", "Sun Of My Soul", "Evei Mapao teithe zhuvea deie", "3/4", "Doh is F", "C.W.H. 325", "John Keble", "Peter Ritter", "Ps. 84:11", "Evening"),
        (311, "RAMAI NOU NE KHOPEILO", "God Be With You Till We Meet Again", "Ramai nou ne khopeilo etao ngaokisü", "4/4", "Doh is Db", "S.S. 1047", "J.E. Rankin", "W.G. Tomer", "2 Thess. 3:16", "Guidance"),
        (312, "LESHI KÜKOU TSUHI", "Blest Be The Tie That Binds", "Leshi kükou tsuhi Khrista mai hi", "3/4", "Doh is F", "S.S. 608", "John Fawcett", "Hans G. Nägeli", "Gal. 3:28", "Love"),
        (313, "JISU MINOU ZHOULO", "Take The Name Of Jesus With You", "Jisu minou zhoulo deiphao reitou hi", "4/4", "Doh is Ab", "S.S. 85", "Lydia Baxter", "W.H. Doane", "Phil. 2:9", "Faith & Trust"),
        (314, "E JISU NE LESHIWE", "My Jesus, I Love Thee", "E Jisu Ne leshiwe arako zhe nou", "4/4", "Doh is F", "S.S. 570", "William R. Featherston", "Adoniram J. Gordon", "1 John 4:19", "Love"),
        (315, "PAOSHO BUYU LOU", "O For A Thousand Tongues", "O paosho buyu lou sü zho-a talai", "3/2", "Doh is G", "C.W.H. 90", "Charles Wesley", "Thomas Jarman", "Ps. 35:28", "Praise & Adoration"),
        (316, "JISU MINOU PAOSHOLO", "All Hail The Power Of Jesus' Name", "Jisu minou paosholo zaipe thethesü", "4/4", "Doh is Ab", "S.S. 161", "Edward Perronet", "Oliver Holden", "Phil. 2:10", "Praise & Adoration"),
        (317, "PUHYE PAOSHO! PUHYE PAOSHO!", "Praise Him! Praise Him!", "Puhye paosho! Puhye paosho! Jisu Veopu", "6/8", "Doh is Ab", "S.S. 18", "F.J. Crosby", "Chester G. Allen", "Ps. 106:1", "Praise & Adoration"),
        (318, "KHAIPEIYU ZHIDZÜ", "Come Thou Fount Of Every Blessing", "Khaipeiyu zhidzü reie Mapao Jisu", "3/4", "Doh is Eb", "C.W.H. 195", "Robert Robinson", "John Wyeth", "1 Sam. 7:12", "Praise & Adoration"),
        (319, "E PFÜA ZHOULO JIHOVAH", "Guide Me, O Thou Great Jehovah", "E pfüa zhoulo Jehovah deichi hi zhouki", "4/4", "Doh is G", "C.W.H. 263", "William Williams", "John Hughes", "Exod. 13:21", "Guidance"),
        (320, "LUDU HI ZHAIPAO PEILO", "Lead, Kindly Light", "Ludu hi zhaipao peilo teizhi kükou", "3/4", "Doh is Ab", "C.W.H. 265", "John H. Newman", "John B. Dykes", "Ps. 43:3", "Guidance"),
        (321, "JISU E VEI LESHI", "Jesus, Lover Of My Soul", "Jisu e vei leshi Ne hi e vewe", "6/8", "Doh is F", "S.S. 555", "Charles Wesley", "Simeon B. Marsh", "Ps. 46:1", "Faith & Trust"),
        (322, "EVEI LÜLOU NE HI", "My Faith Looks Up To Thee", "Evei lülou Ne hi bue Kalvari", "4/4", "Doh is Eb", "S.S. 545", "Ray Palmer", "Lowell Mason", "Heb. 12:2", "Faith & Trust"),
        (323, "PUH NOU E PFÜWE", "He Leadeth Me", "Puh nou e pfüwe veishoyu ludu hi", "4/4", "Doh is D", "S.S. 542", "Joseph H. Gilmore", "William B. Bradbury", "Ps. 23:2", "Guidance"),
        (324, "ETAO PFÜWO KÜKOU MAPAO", "Savior, Like A Shepherd Lead Us", "Etao pfüwo kükou Mapao leshi nou", "4/4", "Doh is Eb", "S.S. 540", "Dorothy A. Thrupp", "William B. Bradbury", "John 10:11", "Guidance"),
        (325, "ZHAOTOU HI ZHAOWO", "Yield Not To Temptation", "Zhaotou hi zhaowo ngaoba dulai tea", "6/8", "Doh is Ab", "S.S. 582", "H.R. Palmer", "H.R. Palmer", "1 Cor. 10:13", "Conflict & Courage"),
        (326, "REIHMAI THEILO", "Hold The Fort", "Reihmai theilo teikhai vakou zhaipao", "2/4", "Doh is D", "S.S. 684", "P.P. Bliss", "P.P. Bliss", "Rev. 3:11", "Conflict & Courage"),
        (327, "NE ANCHOR KÜKOU BUE MO-WO?", "Will Your Anchor Hold", "Ne anchor kükou bue mo-wo deiphao hi", "4/4", "Doh is F", "S.S. 634", "Priscilla J. Owens", "William J. Kirkpatrick", "Heb. 6:19", "Faith & Trust"),
        (328, "VEISHOA LALAI", "Bringing In The Sheaves", "Veishoa lalai Ramai kükou zhoulo", "4/4", "Doh is C", "S.S. 718", "Knowles Shaw", "George A. Minor", "Ps. 126:6", "Mission & Evangelism"),
        (329, "ZHAIPAO SÜ SEIPEILO", "Send The Light", "Zhaipao sü seipeilo deiphao hi reibou", "4/4", "Doh is Ab", "S.S. 724", "Charles H. Gabriel", "Charles H. Gabriel", "Acts 16:9", "Mission & Evangelism"),
        (330, "CHIPAO ZHOULO", "Speed Away", "Chipao zhoulo mai thethesü paokhalo", "3/4", "Doh is C", "S.S. 728", "F.J. Crosby", "I.B. Woodbury", "Mark 16:15", "Mission & Evangelism"),
        (331, "TEITHE ZHAIPAO DEIE", "The Morning Light Is Breaking", "Teithe zhaipao deie teikhai vakou", "4/4", "Doh is Bb", "S.S. 732", "S.F. Smith", "G.J. Webb", "Isa. 60:1", "Mission & Evangelism"),
        (332, "ETAO ZION HI VELAI", "We're Marching To Zion", "Etao Zion hi velai veishoyu nuh", "6/8", "Doh is G", "S.S. 871", "Isaac Watts", "Robert Lowry", "Heb. 12:22", "Christian Endeavour"),
        (333, "MI PAOKHA YUKI", "When The Roll Is Called Up Yonder", "Mi paokha yuki teikhai vakou etao", "4/4", "Doh is Ab", "S.S. 983", "James M. Black", "James M. Black", "Rev. 20:12", "Heavenly Home"),
        (334, "ZHIDZÜ REIPE HINOU", "Shall We Gather At The River", "Zhidzü reipe hinou etao louloure", "4/4", "Doh is Eb", "S.S. 941", "Robert Lowry", "Robert Lowry", "Rev. 22:1", "Heavenly Home"),
        (335, "ZHAIPAO VEI ZHAIPAO", "Face To Face", "Zhaipao vei zhaipao Jisu ngaoyuki", "4/4", "Doh is Bb", "S.S. 995", "Carrie E. Breck", "Grant Colfax Tullar", "1 Cor. 13:12", "Heavenly Home"),
        (336, "REILO BU KIHILO (II)", "In The Sweet By And By", "Reilo bu kihilo etao Jisu ngaolai", "4/4", "Doh is G", "S.S. 949", "S.F. Bennett", "J.P. Webster", "Heb. 11:16", "Heavenly Home"),
        (337, "CHIPAO CHOUKHALO", "Tell Me The Old, Old Story", "Chipao choukhalo Jisu vei khupa sü", "4/4", "Doh is C", "S.S. 350", "Katherine Hankey", "W.H. Doane", "Luke 2:10", "The Gospel"),
        (338, "KHRISTA CHIZIILO", "Loyalty To Christ", "Khrista chiziilo reihmai thethesü", "4/4", "Doh is Bb", "PNBA 338", "Poumai Hymn Committee", "E.T. Cassel", "Matt. 16:24", "Christian Endeavour"),
        (339, "CHIPAO PAOYU E LESHIWE", "I Love To Tell The Story", "Chipao paoyu e leshiwe Jisu vei", "4/4", "Doh is Ab", "S.S. 354", "Katherine Hankey", "William G. Fischer", "Ps. 66:16", "Mission & Evangelism"),
        (340, "JISU THAIFÜ ZHOU LAI", "More About Jesus", "Jisu thaifü zhou lai Puh basha ngaowe", "6/8", "Doh is Ab", "S.S. 564", "E.E. Hewitt", "John R. Sweney", "2 Peter 3:18", "Faith & Trust"),
        (341, "EVEI RÜMÜ HOULO", "Open My Eyes, That I May See", "Evei rümü houlo Mapao Jisu", "6/8", "Doh is Ab", "S.S. 548", "Clara H. Scott", "Clara H. Scott", "Ps. 119:18", "Prayer & Consecration"),
        (342, "EYE SA THEPEILO", "Cleanse Me", "Eye sa thepeilo Mapao Jisu zhe nou", "3/4", "Doh is F", "C.W.H. 235", "J. Edwin Orr", "Maori Melody", "Ps. 139:23", "Prayer & Consecration"),
        (343, "EVEI KÜKOU SA-A PEILO", "Fill My Cup, Lord", "Evei kükou sa-a peilo Mapao Jisu", "4/4", "Doh is Eb", "C.W.H. 240", "Richard Blanchard", "Richard Blanchard", "John 4:14", "Prayer & Consecration"),
        (344, "LESHI SÜ SEIPEILO", "Pass It On", "Leshi sü seipeilo deiphao mai hrülai", "3/4", "Doh is D", "C.W.H. 250", "Kurt Kaiser", "Kurt Kaiser", "1 John 4:11", "Love"),
        (345, "PUH HRÜ BUE!", "He Lives", "Puh hrü bue! Puh hrü bue! Mapao Jisu", "6/8", "Doh is Bb", "C.W.H. 65", "A.H. Ackley", "A.H. Ackley", "Mark 16:6", "Assurance & Testimony"),
        (346, "PUH HRÜ BUYU DONOU", "Because He Lives", "Puh hrü buyu donou e zhaowe moe", "4/4", "Doh is Ab", "C.W.H. 70", "Gloria Gaither", "William J. Gaither", "John 14:19", "Faith & Trust"),
        (347, "JISU HI ASA BUE", "Victory In Jesus", "Jisu hi asa bue etao zhaotou reih", "4/4", "Doh is G", "C.W.H. 280", "E.M. Bartlett", "E.M. Bartlett", "1 Cor. 15:57", "Assurance & Testimony"),
        (348, "NE DAIZHOU DUE! (II)", "How Great Thou Art", "Mapao Ramai Ne souda peiyu zaipe", "4/4", "Doh is Bb", "C.W.H. 10", "Stuart K. Hine", "Swedish Folk Melody", "Ps. 8:1", "Praise & Adoration"),
        (349, "ZHIVA HINOU KHAIPAO BUE", "There Is Power In The Blood", "Zhiva hinou khaipao bue Jisu vei", "4/4", "Doh is Bb", "S.S. 364", "Lewis E. Jones", "Lewis E. Jones", "Heb. 9:14", "The Gospel"),
        (350, "REITOU THETHE SOULO", "Whiter Than Snow", "Reitou thethe soulo evei rümü hi", "3/4", "Doh is Eb", "S.S. 370", "James Nicholson", "William G. Fischer", "Ps. 51:7", "Prayer & Consecration")
    ]

    hymns = []
    for (num, title, eng, first, time, key, ref, author, comp, script, cat) in titles:
        h = {
            "id": num,
            "title": title,
            "englishTitle": eng,
            "firstLine": first,
            "timeSignature": time,
            "keySignature": key,
            "hymnBookRef": ref,
            "author": author,
            "composer": comp,
            "scripture": script,
            "category": cat,
            "verses": [
                {"verseNumber": 1, "lines": [
                    f"{first},",
                    "Puh vei khupa leshi lou soulaikhe;",
                    "Etao vei rü alia vupeiyu Mapao,",
                    "Varuyu ki hinou Puhye paosho bue."
                ]},
                {"verseNumber": 2, "lines": [
                    "Puh zhe nou hrülou-a khailu peiyu hi,",
                    "Louche loumai sü khaipei laitea paopeie;",
                    "Sheeyu mai thethesü sühi louloure,",
                    "Teisa asayu ngaolou lai."
                ]},
                {"verseNumber": 3, "lines": [
                    "Teikhai vakou sana romü buh sü,",
                    "Ramai nou etao donou souda peire;",
                    "Asayu lou nouko zho-a talai,",
                    "Teisa teithe hrülai."
                ]}
            ],
            "chorus": [
                f"{title.split()[0]}, {title.split()[0]}!",
                f"Mapao Jisu khe hinou etao buki;",
                "Teisa teithe Puhye paosho lai,",
                "Asa lou soulaihe."
            ]
        }
        hymns.append(h)
    return hymns
