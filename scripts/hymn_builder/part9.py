# Hymns 401 to 450 for Chipao Avei Loubvü
def get_part9():
    titles = [
        (401, "KROS VEI REIHMAI E SÜMO-WO?", "Am I A Soldier Of The Cross", "Kros vei reihmai e sümo-wo Mapao", "3/2", "Doh is G", "C.W.H. 270", "Isaac Watts", "Thomas A. Arne", "2 Tim. 2:3", "Conflict & Courage"),
        (402, "SHEEYU REIH SÜ DULO", "Fight The Good Fight", "Sheeyu reih sü dulo asahra poa", "4/4", "Doh is F", "C.W.H. 272", "J.S.B. Monsell", "William Boyd", "1 Tim. 6:12", "Conflict & Courage"),
        (403, "ETAO PUOTAO LÜLOUYU", "Faith Of Our Fathers", "Etao puotao lülouyu kükou bue", "3/4", "Doh is Ab", "C.W.H. 210", "Frederick W. Faber", "Henri F. Hemy", "Jude 1:3", "Faith & Trust"),
        (404, "RAMAI KÜKOU CHUHDU BUE", "A Mighty Fortress Is Our God", "Ramai kükou chuhdu bue etao donou", "4/4", "Doh is C", "Martin Luther", "Martin Luther", "Martin Luther", "Ps. 46:1", "Faith & Trust"),
        (405, "REIH VEI TÜ SÜ KHOLO", "Sound The Battle Cry", "Reih vei tü sü kholo asahra poa", "4/4", "Doh is Bb", "S.S. 682", "William F. Sherwin", "William F. Sherwin", "1 Cor. 14:8", "Conflict & Courage"),
        (406, "KHRISTA REIHMAI ASAHRA", "Soldiers Of Christ, Arise", "Khrista reihmai asahra Mapao basha", "4/4", "Doh is G", "C.W.H. 274", "Charles Wesley", "George J. Elvey", "Eph. 6:10", "Conflict & Courage"),
        (407, "THAONOU MAPAO KHE HINOU?", "Who Is On The Lord's Side?", "Thaonou Mapao khe hinou tholo lai?", "4/4", "Doh is Bb", "S.S. 685", "Frances R. Havergal", "J.W. Arr. Carrott", "1 Chron. 12:18", "Christian Endeavour"),
        (408, "RÜMÜ THETHE NOU JISU", "True-Hearted, Whole-Hearted", "Rümü thethe nou Jisu paosho bulai", "6/8", "Doh is F", "S.S. 686", "Frances R. Havergal", "George C. Stebbins", "Ps. 9:1", "Christian Endeavour"),
        (409, "DANIEL KHE HI THOLO", "Dare To Be A Daniel", "Daniel khe hi tholo asahra poa", "4/4", "Doh is Bb", "S.S. 690", "P.P. Bliss", "P.P. Bliss", "Dan. 1:8", "Christian Endeavour"),
        (410, "REIH REIPE HINOU THOLO", "Keep On The Firing Line", "Reih reipe hinou tholo Khrista reihmai", "4/4", "Doh is Ab", "S.S. 692", "C.B. Strouse", "C.B. Strouse", "2 Tim. 4:7", "Conflict & Courage"),
        (411, "ZHAOWE MOE REIHMAI", "Courage, Brother", "Zhaowe moe reihmai Mapao nou pfüwe", "4/4", "Doh is G", "C.W.H. 276", "Norman Macleod", "Arthur Sullivan", "Josh. 1:9", "Conflict & Courage"),
        (412, "KÜKOU BUYU HI THOLO", "Stand Fast", "Kükou buyu hi tholo Jisu Veopu", "4/4", "Doh is D", "S.S. 694", "E.A. Hoffman", "J.H. Tenney", "1 Cor. 16:13", "Conflict & Courage"),
        (413, "KHORAYE MOE MAPAO", "Never Give Up", "Khoraye moe Mapao nou etao pfüwe", "4/4", "Doh is F", "S.S. 696", "F.J. Crosby", "I. Allan Sankey", "Gal. 6:9", "Conflict & Courage"),
        (414, "JISU DONOU BUE E", "I Need Jesus", "Jisu donou bue e teithetsü Puh", "6/8", "Doh is Bb", "S.S. 550", "George O. Webster", "Charles H. Gabriel", "John 15:5", "Prayer & Consecration"),
        (415, "DAISOU NOU E CHOULOU MOE", "No One Understands Like Jesus", "Daisou nou e choulou moe Jisu süe", "4/4", "Doh is Eb", "C.W.H. 255", "John W. Peterson", "John W. Peterson", "Heb. 4:15", "Faith & Trust"),
        (416, "RAMAI NOU NE KHOPEIE", "God Will Take Care Of You", "Ramai nou ne khopeie deiphao teithe", "6/8", "Doh is Bb", "S.S. 560", "Civilla D. Martin", "W. Stillman Martin", "1 Peter 5:7", "Faith & Trust"),
        (417, "EVEI RÜMÜ KÜKOU BUWO", "Be Still, My Soul", "Evei rümü kükou buwo Mapao bue", "4/4", "Doh is F", "C.W.H. 266", "Katharina von Schlegel", "Jean Sibelius", "Ps. 46:10", "Faith & Trust"),
        (418, "ZHIDZÜ PEISHOYU SÜ", "Like A River Glorious", "Zhidzü peishoyu sü Ramai vei asayu", "4/4", "Doh is F", "S.S. 562", "Frances R. Havergal", "James Mountain", "Isa. 66:12", "Peace"),
        (419, "ASAYU THETHESÜ", "Peace, Perfect Peace", "Asayu thethesü deiphao zhaotou hi", "4/4", "Doh is Bb", "C.W.H. 268", "Edward H. Bickersteth", "George T. Caldbeck", "Isa. 26:3", "Peace"),
        (420, "NE VAH SÜ SOUTHEI THEILO", "Revive Thy Work, O Lord", "Ne vah sü southei theilo Mapao Jisu", "4/4", "Doh is G", "S.S. 238", "Albert Midlane", "James McGranahan", "Hab. 3:2", "Prayer & Consecration"),
        (421, "KROS VEI LUDU", "The Way Of The Cross", "Kros vei ludu hi etao zhou talai", "4/4", "Doh is G", "S.S. 650", "Jessie B. Pounds", "Charles H. Gabriel", "Matt. 16:24", "The Gospel"),
        (422, "RAMAI VEI RÜMÜ SEIPEILO", "Breathe On Me, Breath Of God", "Ramai vei rümü seipeilo evei rümü", "4/4", "Doh is F", "C.W.H. 150", "Edwin Hatch", "Robert Jackson", "John 20:22", "Prayer & Consecration"),
        (423, "HRÜYU RAMAI VEI RÜMÜ", "Spirit Of The Living God", "Hrüyu Ramai vei rümü etao hi velo", "4/4", "Doh is F", "C.W.H. 151", "Daniel Iverson", "Daniel Iverson", "2 Cor. 3:3", "Prayer & Consecration"),
        (424, "RÜMÜ THETHE E SHOU BUWO", "Hover O'er Me, Holy Spirit", "Rümü thethe e shou buwo Mapao Jisu", "3/4", "Doh is Eb", "S.S. 252", "Elwood H. Stokes", "John R. Sweney", "Gen. 1:2", "Prayer & Consecration"),
        (425, "THEIKHOU BUYU RÜMÜ", "Spirit Divine, Attend Our Prayers", "Theikhou buyu rümü etao kükou velo", "4/4", "Doh is G", "C.W.H. 152", "Andrew Reed", "Johann C. Schicht", "Acts 2:1-4", "Prayer & Consecration"),
        (426, "ZHAIPAO PEIYU THEIKHOU RÜMÜ", "Holy Ghost, With Light Divine", "Zhaipao peiyu theikhou rümü e shou buwo", "3/4", "Doh is C", "C.W.H. 154", "Andrew Reed", "Louis M. Gottschalk", "Ps. 43:3", "Prayer & Consecration"),
        (427, "BASHA PEIYU THEIKHOU RÜMÜ", "Gracious Spirit, Dove Divine", "Basha peiyu theikhou rümü deiphao hi", "3/4", "Doh is F", "C.W.H. 156", "John Stocker", "Ignaz Pleyel", "Matt. 3:16", "Prayer & Consecration"),
        (428, "MAPAO JISU E DONOU", "Lord Jesus, Think On Me", "Mapao Jisu e donou kükou souraye", "4/4", "Doh is F", "C.W.H. 158", "Synesius of Cyrene", "William Damon", "Luke 23:42", "Prayer & Consecration"),
        (429, "ETAO PUO LESHIYU MAPAO", "Dear Lord And Father Of Mankind", "Etao Puo leshiyu Mapao deiphao soupei", "4/4", "Doh is Eb", "C.W.H. 160", "John G. Whittier", "Frederick C. Maker", "1 Kings 19:12", "Prayer & Consecration"),
        (430, "RAMAI RÜMÜ E RÜMÜ HI", "Spirit Of God, Descend Upon My Heart", "Ramai rümü e rümü hi zhaipao pasholo", "4/4", "Doh is C", "C.W.H. 162", "George Croly", "Frederick C. Atkinson", "Gal. 5:25", "Prayer & Consecration"),
        (431, "THEIKHOU RÜMÜ ETAO HI VELO", "Come, Holy Spirit, Heavenly Dove", "Theikhou rümü etao hi velo deiphao", "3/2", "Doh is G", "C.W.H. 164", "Isaac Watts", "John B. Dykes", "Rom. 8:26", "Prayer & Consecration"),
        (432, "HRÜYU RÜMÜ SEIPEILO", "O Breath Of Life", "Hrüyu rümü seipeilo etao rümü hi", "4/4", "Doh is Eb", "C.W.H. 166", "Bessie P. Head", "Traditional Welsh", "Ezek. 37:9", "Prayer & Consecration"),
        (433, "EVEI HRÜYU SA-A PEILO", "Fill Thou My Life", "Evei hrüyu sa-a peilo Mapao Jisu zhe", "3/4", "Doh is F", "C.W.H. 168", "Horatius Bonar", "Thomas Armstrong", "Ps. 104:33", "Prayer & Consecration"),
        (434, "NEVEI LUDU E PAOKHALO", "Teach Me Thy Way", "Nevei ludu e paokhalo Mapao Jisu", "4/4", "Doh is Bb", "C.W.H. 170", "B. Mansell Ramsey", "B. Mansell Ramsey", "Ps. 27:11", "Guidance"),
        (435, "PAOPU NE KHE HINOU ZHOULO", "O Master, Let Me Walk With Thee", "Paopu Ne khe hinou zhoulo deiphao hi", "3/4", "Doh is Eb", "C.W.H. 172", "Washington Gladden", "H. Percy Smith", "Gen. 5:24", "Guidance"),
        (436, "THEIKHOU BUYU TEITHE ZHOULO", "Take Time To Be Holy", "Theikhou buyu teithe zhoulo Mapao hi", "6/8", "Doh is F", "S.S. 576", "William D. Longstaff", "George C. Stebbins", "1 Peter 1:16", "Prayer & Consecration"),
        (437, "THEIKHOU DAIZHOU E PEILO", "More Holiness Give Me", "Theikhou daizhou e peilo Mapao Jisu", "12/8", "Doh is Eb", "S.S. 578", "P.P. Bliss", "P.P. Bliss", "Phil. 1:9", "Prayer & Consecration"),
        (438, "RÜMÜ THETHE SOUPUELAI", "Purer In Heart", "Rümü thethe soupuelai Kalvari koute", "6/4", "Doh is G", "S.S. 580", "Mrs. A.L. Davison", "J.H. Fillmore", "Ps. 51:10", "Prayer & Consecration"),
        (439, "NE KHE HINOU DAIZHOU", "Nearer, Still Nearer", "Ne khe hinou daizhou Mapao Jisu e velai", "4/4", "Doh is Db", "C.W.H. 205", "Lelia N. Morris", "Lelia N. Morris", "James 4:8", "Prayer & Consecration"),
        (440, "E PFÜA VELO KROS KOUTE", "Draw Me Nearer", "E pfüa velo Kros koute Mapao Jisu", "4/4", "Doh is Ab", "S.S. 546", "F.J. Crosby", "W.H. Doane", "Heb. 10:22", "Prayer & Consecration"),
        (441, "ZAIPE HINOU E LOULAI", "In The Garden", "Zaipe hinou e loulai Jisu khe hinou", "6/8", "Doh is Ab", "C.W.H. 244", "C. Austin Miles", "C. Austin Miles", "John 20:15", "Faith & Trust"),
        (442, "RAMAI KHE HINOU BUKI", "Alone With God", "Ramai khe hinou buki daizhozhou veie", "4/4", "Doh is D", "C.W.H. 242", "B.D. Ackley", "B.D. Ackley", "Mark 1:35", "Prayer & Consecration"),
        (443, "ASAYU THETHE RAMAI VEI", "Sweet Peace, The Gift Of God's Love", "Asayu thethe Ramai vei e rümü reie", "4/4", "Doh is Ab", "S.S. 855", "P.P. Bilhorn", "P.P. Bilhorn", "John 14:27", "Faith & Trust"),
        (444, "EVEI RAMAI E PFÜA", "My God And I", "Evei Ramai e pfüa zhou buyu deiphao hi", "3/4", "Doh is G", "C.W.H. 246", "I.B. Sergei", "Austris A. Wihtol", "Gen. 5:24", "Faith & Trust"),
        (445, "TAKHAIO, KIHI", "Sail Home", "Takhaio kihi teikhai vakou Jordan reipe", "6/8", "Doh is Eb", "S.S. 985", "W.O. Cushing", "William F. Sherwin", "Heb. 6:19", "Guidance"),
        (446, "JERUSALEM SANA NUH", "Jerusalem The Golden", "Jerusalem sana nuh zhuvea deie", "4/4", "Doh is Eb", "C.W.H. 345", "Bernard of Cluny", "Alexander Ewing", "Rev. 21:2", "Heavenly Home"),
        (447, "JERUSALEM VEISHOYU NUH", "O Mother Dear, Jerusalem", "Jerusalem veishoyu nuh etao kihi", "4/4", "Doh is C", "C.W.H. 346", "F.B.P.", "Traditional English", "Rev. 21:10", "Heavenly Home"),
        (448, "EVEI KIHI ZHUVEA DEIE", "My Heavenly Home Is Bright And Fair", "Evei kihi zhuvea deie teikhai vakou", "4/4", "Doh is G", "S.S. 962", "William Hunter", "William Hunter", "2 Cor. 5:1", "Heavenly Home"),
        (449, "E DEIPHAO MAI HRÜLAI", "I'm A Pilgrim And A Stranger", "E deiphao mai hrülai kihi vewe", "4/4", "Doh is F", "S.S. 964", "Mary S.B. Dana", "Traditional Italian", "Heb. 11:13", "Heavenly Home"),
        (450, "ETAO NUH SÜHI VELAI", "We Are Going To That City", "Etao nuh sühi velai sana romü buh", "4/4", "Doh is Bb", "S.S. 966", "F.J. Crosby", "W.H. Doane", "Heb. 11:10", "Heavenly Home")
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
                "Mapao Jisu khe hinou etao buki;",
                "Teisa teithe Puhye paosho lai,",
                "Asa lou soulaihe."
            ]
        }
        hymns.append(h)
    return hymns
