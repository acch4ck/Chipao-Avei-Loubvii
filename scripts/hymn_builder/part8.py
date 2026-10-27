# Hymns 351 to 400 for Chipao Avei Loubvü
def get_part8():
    titles = [
        (351, "BASHA DAIZHOU DUE", "Grace Greater Than Our Sin", "Basha daizhou due etao zhaotou vanou", "4/4", "Doh is G", "S.S. 385", "Julia H. Johnston", "Daniel B. Towner", "Rom. 5:20", "Faith & Trust"),
        (352, "JISU VEI BASHA KÜKOU", "Wonderful Grace Of Jesus", "Jisu vei basha kükou daizhou leshie", "4/4", "Doh is C", "S.S. 386", "Haldor Lillenas", "Haldor Lillenas", "Eph. 1:7", "Faith & Trust"),
        (353, "JISU DONOU HRÜLAI", "Living For Jesus", "Jisu donou hrülai etao deiphao hi", "4/4", "Doh is F", "C.W.H. 290", "Thomas O. Chisholm", "C. Harold Lowden", "2 Cor. 5:15", "Christian Endeavour"),
        (354, "VASHO ALI SOULO", "Make Me A Blessing", "Vasho ali soulo deiphao mai hrülai", "6/8", "Doh is Bb", "S.S. 750", "Ira B. Wilson", "George S. Schuler", "Gen. 12:2", "Christian Endeavour"),
        (355, "PUH VEI BASHA SEIPEILO", "Channels Only", "Puh vei basha seipeilo deiphao hi", "3/4", "Doh is F", "S.S. 755", "Mary E. Maxwell", "Ada R. Green", "2 Cor. 4:7", "Christian Endeavour"),
        (356, "EVEI RÜMÜ THEILO", "Search Me, O God", "Evei rümü theilo Mapao Jisu arako", "3/4", "Doh is F", "C.W.H. 236", "J. Edwin Orr", "Maori Melody", "Ps. 139:23", "Prayer & Consecration"),
        (357, "EVEI HRÜYU NE HI PEIE", "Take My Life And Let It Be", "Evei hrüyu Ne hi peie Mapao Jisu", "2/4", "Doh is F", "S.S. 591", "Frances R. Havergal", "H.A. Cesar Malan", "Rom. 12:1", "Prayer & Consecration"),
        (358, "NE DONOU E SÜH PEIRE", "I Gave My Life For Thee", "Ne donou E süh peire Kros koute", "6/8", "Doh is C", "S.S. 589", "Frances R. Havergal", "P.P. Bliss", "Gal. 2:20", "The Gospel"),
        (359, "NE DONOU BUH BUE", "Room For Thee", "Ne donou buh bue Mapao Jisu hi", "4/4", "Doh is C", "S.S. 391", "Emily E.S. Elliott", "Ira D. Sankey", "Luke 2:7", "Gospel Invitation"),
        (360, "HRÜYU KHAIPAO BAPHEILO", "Break Thou The Bread Of Life", "Hrüyu khaipao bapheilo etao Mapao", "4/4", "Doh is Eb", "S.S. 288", "Mary A. Lathbury", "William F. Sherwin", "Matt. 14:19", "Prayer & Consecration"),
        (361, "NEVEI PAOSHO BUYU HI", "According To Thy Word", "Nevei paosho buyu hi etao loulai", "4/4", "Doh is G", "C.W.H. 310", "James Montgomery", "Thomas Hastings", "Luke 22:19", "Worship"),
        (362, "KROS THAIFÜ ZHOU LAI", "Beneath The Cross Of Jesus", "Kros thaifü zhou lai Kalvari koute", "4/4", "Doh is Db", "S.S. 110", "Elizabeth C. Clephane", "Frederick C. Maker", "Gal. 6:14", "The Gospel"),
        (363, "KROS KÜKOU E NGAOYUKI", "When I Survey The Wondrous Cross", "Kros kükou e ngaoyuki Jisu süh re", "3/4", "Doh is F", "C.W.H. 50", "Isaac Watts", "Lowell Mason", "Gal. 6:14", "The Gospel"),
        (364, "JISU VEI ZHIVA SEIPEIE", "Alas! And Did My Savior Bleed", "Jisu vei zhiva seipeie Kalvari", "3/4", "Doh is Ab", "S.S. 108", "Isaac Watts", "Hugh Wilson", "Luke 23:44", "The Gospel"),
        (365, "ZHAOTOU MAI VEI MAPAO", "Man Of Sorrows", "Zhaotou mai vei Mapao Jisu Veopu", "4/4", "Doh is Bb", "S.S. 112", "Philip P. Bliss", "Philip P. Bliss", "Isa. 53:3", "The Gospel"),
        (366, "KROS KOUTE PUH SÜH RE", "Stricken, Smitten And Afflicted", "Kros koute Puh süh re etao donou", "4/4", "Doh is D", "C.W.H. 52", "Thomas Kelly", "Geistliche Lieder", "Isa. 53:4", "The Gospel"),
        (367, "THEIKHOU BUYU MAPAO", "O Sacred Head, Now Wounded", "Theikhou buyu Mapao Kalvari koute", "4/4", "Doh is C", "C.W.H. 54", "Bernard of Clairvaux", "Hans Leo Hassler", "Matt. 27:29", "The Gospel"),
        (368, "HALLELUJAH! KHAILUPEIYU", "Hallelujah! What A Savior", "Hallelujah! Khailupeiyu Jisu süh re", "4/4", "Doh is Bb", "S.S. 114", "P.P. Bliss", "P.P. Bliss", "1 Tim. 1:15", "Praise & Adoration"),
        (369, "JISU NOU THAOTHOU SA-A PEIRE", "Jesus Paid It All", "Jisu nou thaothou sa-a peire etao donou", "3/4", "Doh is Eb", "S.S. 116", "Elvina M. Hall", "John T. Grape", "Heb. 9:28", "The Gospel"),
        (370, "KALVARI HI E PFÜLO", "Lead Me To Calvary", "Kalvari hi e pfülo Mapao Jisu", "4/4", "Doh is Eb", "S.S. 118", "Jennie E. Hussey", "William J. Kirkpatrick", "Matt. 27:33", "Prayer & Consecration"),
        (371, "KROS KOUTE", "At The Cross", "Kros koute Kros koute e ngaoyuki", "4/4", "Doh is Eb", "S.S. 120", "Isaac Watts", "Ralph E. Hudson", "Gal. 6:14", "The Gospel"),
        (372, "ZHIDZÜ PEISHOTHO BUE", "There Is A Fountain", "Zhidzü peishotho bue Kalvari koute", "4/4", "Doh is C", "S.S. 124", "William Cowper", "Traditional American", "Zech. 13:1", "The Gospel"),
        (373, "DAISOU NOU E KÜKOULAI?", "Nothing Between", "Daisou nou e kükoulai Mapao Jisu vanou", "3/4", "Doh is G", "S.S. 595", "C.A. Tindley", "C.A. Tindley", "Rom. 8:35", "Prayer & Consecration"),
        (374, "EVEI LÜLOU CHUHDU HI", "My Hope Is Built", "Evei lülou chuhdu hi tholo buyu", "3/4", "Doh is F", "S.S. 632", "Edward Mote", "William B. Bradbury", "1 Cor. 3:11", "Faith & Trust"),
        (375, "KÜKOU BUYU CHUHDU", "The Solid Rock", "Kükou buyu chuhdu Jisu Veopu bue", "3/4", "Doh is G", "S.S. 633", "Edward Mote", "William B. Bradbury", "Matt. 7:24", "Faith & Trust"),
        (376, "VEISHOYU KI (II)", "Happy The Home", "Veishoyu ki Ramai kükou buki", "4/4", "Doh is G", "C.W.H. 340", "Henry Ware Jr.", "John B. Dykes", "Ps. 128:1", "Guidance"),
        (377, "KHUPA THETHESÜ", "O Perfect Love", "Khupa thethesü teikhai vakou reie", "4/4", "Doh is Eb", "C.W.H. 342", "Dorothy F. Gurney", "Joseph Barnby", "1 John 4:12", "Love"),
        (378, "REITOU SOUDA PEIYU", "Lord Of The Harvest", "Reitou souda peiyu Mapao Jisu bue", "4/4", "Doh is F", "S.S. 710", "John S.B. Monsell", "Arthur S. Sullivan", "Matt. 9:38", "Mission & Evangelism"),
        (379, "POUMAI KHRISTA REIHMAI", "Poumai Christian Youth", "Poumai Khrista reihmai thethesü asahra", "4/4", "Doh is Bb", "PNBA 379", "Poumai Literature Society", "Traditional Naga Air", "1 Tim. 4:12", "Christian Endeavour"),
        (380, "KHAIPEIYU ZHIDZÜ PEILO", "Lord, Dismiss Us With Thy Blessing", "Khaipeiyu zhidzü peilo etao velouki", "4/4", "Doh is F", "C.W.H. 330", "John Fawcett", "Sicilian Melody", "Luke 2:29", "Worship"),
        (381, "NE MINOU ETAO VELAI", "Savior, Again To Thy Dear Name", "Ne minou etao velai kükou bue tea", "4/4", "Doh is Eb", "C.W.H. 332", "John Ellerton", "Edward J. Hopkins", "Num. 6:26", "Worship"),
        (382, "TEITHE ZHAOWE TEIKHAI VAKOU", "Day Is Dying In The West", "Teithe zhaowe teikhai vakou khei velai", "6/8", "Doh is Ab", "C.W.H. 322", "Mary A. Lathbury", "William F. Sherwin", "Ps. 141:2", "Evening"),
        (383, "NEVEI TEITHE THAIPUELAI", "The Day Thou Gavest", "Nevei teithe thaipuelai Mapao Jisu", "3/4", "Doh is G", "C.W.H. 324", "John Ellerton", "Clement C. Scholefield", "Ps. 113:3", "Evening"),
        (384, "TEITHE THAIPUELAI ARAKO", "Now The Day Is Over", "Teithe thaipuelai arako khei veloure", "4/4", "Doh is Bb", "C.W.H. 326", "Sabine Baring-Gould", "Joseph Barnby", "Prov. 3:24", "Evening"),
        (385, "PUO RAMAIYE PAOSHO", "Gloria Patri", "Puo Ramaiye paosho Nah Jisu ye sholo", "4/4", "Doh is C", "Traditional", "Ancient Liturgy", "Henry W. Greatorex", "Rom. 11:36", "Worship"),
        (386, "RAMAIYE PAOSHOLO", "Doxology (Old 100th)", "Ramaiye paosholo zaipe thethesü", "4/4", "Doh is G", "C.W.H. 100", "Thomas Ken", "Louis Bourgeois", "Ps. 100:1-5", "Praise & Adoration"),
        (387, "ETAO PUO RAKI VAMAYE", "The Lord's Prayer", "Etao Puo raki vamaye Ne mi thethe bue", "4/4", "Doh is F", "Scripture", "Biblical Text", "Traditional Chant", "Matt. 6:9-13", "Prayer & Consecration"),
        (388, "E LÜLOUWE PUO RAMAIYE", "Apostles' Creed In Song", "E lülouwe Puo Ramaiye deiphao soupei", "4/4", "Doh is D", "Traditional", "Apostolic Fathers", "John Merbecke", "1 Cor. 15:3-4", "Worship"),
        (389, "MAPAO NOU NE KHOPEILO", "Aaronic Benediction I", "Mapao nou ne khopeilo Ne shou pasholo", "4/4", "Doh is C", "Num. 6:24", "Biblical Text", "Peter C. Lutkin", "Num. 6:24-26", "Worship"),
        (390, "KHRISTA VEI BASHA", "Apostolic Benediction II", "Khrista vei basha Puo Ramai vei khupa", "4/4", "Doh is F", "2 Cor. 13:14", "Biblical Text", "Traditional Chant", "2 Cor. 13:14", "Worship"),
        (391, "SEVENFOLD AMEN", "Sevenfold Amen", "Amen, Amen, Amen, Amen, Amen, Amen", "4/4", "Doh is G", "Traditional", "John Stainer", "John Stainer", "Rev. 7:12", "Worship"),
        (392, "THREEFOLD AMEN", "Threefold Amen", "Amen, Amen, Amen!", "4/4", "Doh is C", "Traditional", "Danish Melody", "Traditional", "2 Cor. 1:20", "Worship"),
        (393, "RAMAIYE PAOSHOLO (II)", "Holy God We Praise Thy Name", "Ramaiye paosholo deiphao mai thethesü", "3/4", "Doh is F", "Traditional", "Ignaz Franz", "Katholisches Gesangbuch", "Ps. 150:6", "Praise & Adoration"),
        (394, "KHOUKO BUYU VEOPU", "Come Thou Almighty King", "Khouko buyu Veopu etao hi velo", "3/4", "Doh is F", "C.W.H. 2", "Anonymous", "Felice de Giardini", "1 Tim. 6:15", "Worship"),
        (395, "PUO RAMAI NE KUYU", "Father, Whatever of Earthly Bliss", "Puo Ramai Ne kuyu pai etao choe", "4/4", "Doh is C", "S.S. 520", "Anne Steele", "Lowell Mason", "Ps. 73:25", "Prayer & Consecration"),
        (396, "NE VAH SOUYU DAIZHOU LESHIE", "Sweet Is The Work, My God, My King", "Ne vah souyu daizhou leshie Mapao", "3/2", "Doh is G", "C.W.H. 15", "Isaac Watts", "John Hatton", "Ps. 92:1", "Worship"),
        (397, "JEHOVAH KHOUKO BUYU", "Before Jehovah's Awful Throne", "Jehovah khouko buyu Mapao bue tea", "4/4", "Doh is G", "C.W.H. 18", "Isaac Watts", "John Hatton", "Ps. 100:3", "Worship"),
        (398, "BETHEL RAMAI ETAO PFÜWO", "O God Of Bethel", "Bethel Ramai etao pfüwo ludu hi", "4/4", "Doh is D", "C.W.H. 260", "Philip Doddridge", "Thomas Clark", "Gen. 28:20", "Guidance"),
        (399, "EVEI ZHAIPAO SOULO MAPAO", "Be Thou My Vision", "Evei zhaipao soulo Mapao Jisu Veopu", "3/4", "Doh is Eb", "Ancient Irish", "Dallan Forgaill", "Traditional Irish", "Ps. 27:1", "Guidance"),
        (400, "KHRISTA NOU AKI SOUDA", "The Church's One Foundation", "Khrista nou aki souda peire zhaotou vanou", "4/4", "Doh is Eb", "C.W.H. 220", "Samuel J. Stone", "Samuel S. Wesley", "1 Cor. 3:11", "Dedication & Church Foundation Day")
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
                    "Puh nou khopeiyu thaonou paolou süe?",
                    "Teikhai hinou süe teiva hinou süe;",
                    "Deichi hi reitoutao deikho hi kükoue,",
                    "Veishoyu zidzü nou kükou soushee peie."
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
                "Mapao Jisu khe hinou etao buki;",
                "Teisa teithe Puhye paosho lai,",
                "Asa lou soulaihe."
            ] if "Amen" not in title and "Benediction" not in eng else None
        }
        hymns.append(h)
    return hymns
