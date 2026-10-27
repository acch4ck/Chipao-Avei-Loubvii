# Hymns 451 to 500 for Chipao Avei Loubvü
def get_part10():
    titles = [
        (451, "ZHAOTOU MAI KHAILULO (II)", "Rescue The Perishing (II)", "Zhaotou mai khailulo deiphao hi reibou", "4/4", "Doh is Bb", "S.S. 699", "F.J. Crosby", "W.H. Doane", "Jude 1:23", "Mission & Evangelism"),
        (452, "KHAILU PEIYU TSUHI SEILO", "Throw Out The Life-Line", "Khailu peiyu tsuhi seilo deiphao hi", "6/8", "Doh is G", "S.S. 700", "Edward S. Ufford", "Edward S. Ufford", "Acts 27:31", "Mission & Evangelism"),
        (453, "ZHAIPAO THETHE HOUPEILO", "Let The Lower Lights Be Burning", "Zhaipao thethe houpeilo deiphao kükou", "9/8", "Doh is Bb", "S.S. 701", "P.P. Bliss", "P.P. Bliss", "Matt. 5:16", "Mission & Evangelism"),
        (454, "PUO RAMAI VEI BASHA ZHAIPAO", "Brightly Beams Our Father's Mercy", "Puo Ramai vei basha zhaipao deie", "3/4", "Doh is Bb", "S.S. 702", "P.P. Bliss", "P.P. Bliss", "Luke 1:78", "Mission & Evangelism"),
        (455, "DEIPHAOJÜ HINOU PAOKHALO", "Tell The Whole World", "Deiphaojü hinou paokhalo Jisu vei", "4/4", "Doh is F", "S.S. 703", "A.H. Ackley", "B.D. Ackley", "Mark 16:15", "Mission & Evangelism"),
        (456, "DEIKHO HINOU PAOKHALO", "Go, Tell It On The Mountain", "Deikho hinou paokhalo Jisu thoure", "4/4", "Doh is F", "Traditional", "John W. Work Jr.", "Traditional Spiritual", "Luke 2:10", "Mission & Evangelism"),
        (457, "ETAO CHIPAO PAOYU BUE", "We've A Story To Tell To The Nations", "Etao chipao paoyu bue deiphao mai", "4/4", "Doh is Eb", "C.W.H. 285", "H. Colin Sterne", "H. Colin Sterne", "Ps. 96:3", "Mission & Evangelism"),
        (458, "JISU NOU VEOPU SOUDA LAI", "Jesus Shall Reign", "Jisu nou Veopu souda lai deiphao hi", "4/4", "Doh is D", "C.W.H. 286", "Isaac Watts", "John Hatton", "Ps. 72:8", "Mission & Evangelism"),
        (459, "DEIPHAO DEICHI THETHE HINOU", "From Greenland's Icy Mountains", "Deiphao deichi thethe hinou etao zhoulo", "7/6", "Doh is F", "C.W.H. 288", "Reginald Heber", "Lowell Mason", "Acts 16:9", "Mission & Evangelism"),
        (460, "TEIKHAI ZHAIPAO DEIE", "Hail To The Brightness", "Teikhai zhaipao deie teikhai vakou", "3/4", "Doh is D", "C.W.H. 289", "Thomas Hastings", "Lowell Mason", "Isa. 60:1", "Mission & Evangelism"),
        (461, "MAPAO VEI KROS PFÜA ZHOULO", "Fling Out The Banner", "Mapao vei Kros pfüa zhoulo asahra poa", "4/4", "Doh is Eb", "C.W.H. 291", "George W. Doane", "J. Baptiste Calkin", "Ps. 60:4", "Mission & Evangelism"),
        (462, "DEIPHAO DONOU KHRISTA SHOLO", "Christ For The World We Sing", "Deiphao donou Khrista sholo maihrülai", "6/4", "Doh is F", "C.W.H. 292", "Samuel Wolcott", "Felice de Giardini", "John 3:16", "Mission & Evangelism"),
        (463, "ZION MAI ASAHRA POALO", "O Zion, Haste", "Zion mai asahra poalo chipao sü", "4/4", "Doh is Bb", "C.W.H. 294", "Mary A. Thomson", "James Walch", "Isa. 52:7", "Mission & Evangelism"),
        (464, "CHIPAO SÜ SEIPEILO", "Speed The Gospel", "Chipao sü seipeilo deiphao mai hrülai", "4/4", "Doh is G", "S.S. 705", "F.J. Crosby", "Ira D. Sankey", "2 Thess. 3:1", "Mission & Evangelism"),
        (465, "KHAIPAO ZHIDZÜ REIE MAPAO", "Send A Great Revival", "Khaipao zhidzü reie Mapao etao hi", "4/4", "Doh is Ab", "C.W.H. 295", "B.B. McKinney", "B.B. McKinney", "Hab. 3:2", "Prayer & Consecration"),
        (466, "PAOPU JISU VELOURE", "The Master Has Come", "Paopu Jisu veloure etao kükou", "4/4", "Doh is C", "S.S. 706", "Sarah Doudney", "Ira D. Sankey", "John 11:28", "Gospel Invitation"),
        (467, "KHEI VELAITEA VAH SOULO", "Work, For The Night Is Coming", "Khei velaitea vah soulo Mapao Jisu donou", "4/4", "Doh is F", "S.S. 708", "Anna L. Coghill", "Lowell Mason", "John 9:4", "Christian Endeavour"),
        (468, "VAH SOULO RAMAI KÜKOU", "To The Work, To The Work", "Vah soulo Ramai kükou asahra poalo", "4/4", "Doh is F", "S.S. 709", "F.J. Crosby", "William H. Doane", "1 Cor. 15:58", "Christian Endeavour"),
        (469, "VAH SOULO JISU DONOU", "Labor On", "Vah soulo Jisu donou teithe thethe hi", "4/4", "Doh is G", "S.S. 711", "C.R. Blackall", "W.H. Doane", "Gal. 6:9", "Christian Endeavour"),
        (470, "NEVEI DAIZHO ZHOU PUH HI PEIE", "Give Of Your Best To The Master", "Nevei daizho zhou Puh hi peie Mapao", "4/4", "Doh is C", "S.S. 713", "Howard B. Grose", "Charlotte A. Barnard", "2 Tim. 2:15", "Christian Endeavour"),
        (471, "BAFÜ KHOLOU E VELAIMOE", "Must I Go, And Empty-Handed?", "Bafü kholou e velaimoe Mapao Jisu hi", "4/4", "Doh is C", "S.S. 714", "C.C. Luther", "George C. Stebbins", "Dan. 12:3", "Christian Endeavour"),
        (472, "VEISHOA LALAI JISU DONOU", "Bringing In The Sheaves (II)", "Veishoa lalai Jisu donou zhoulo mai thethe", "4/4", "Doh is C", "S.S. 718", "Knowles Shaw", "George A. Minor", "Ps. 126:6", "Mission & Evangelism"),
        (473, "TEITHE ZHAIPAO HINOU ZAIPE", "Sowing In The Morning", "Teithe zhaipao hinou zaipe souda peilo", "4/4", "Doh is C", "S.S. 719", "Knowles Shaw", "George A. Minor", "Eccles. 11:6", "Mission & Evangelism"),
        (474, "SANA VEISHOA LALAI", "Golden Sheaves", "Sana veishoa lalai Ramai kükou zhoulo", "4/4", "Doh is G", "S.S. 720", "Traditional", "Traditional", "Matt. 13:30", "Mission & Evangelism"),
        (475, "REITOU TEITHE THAIPUELAI", "The Harvest Is Passing", "Reitou teithe thaipuelai arako lülouwo", "4/4", "Doh is Eb", "S.S. 721", "F.J. Crosby", "William H. Doane", "Jer. 8:20", "Gospel Invitation"),
        (476, "ASAYU MAI THETHE VELO", "Come, Ye Thankful People, Come", "Asayu mai thethe velo reitou souda peire", "4/4", "Doh is F", "C.W.H. 335", "Henry Alford", "George J. Elvey", "Mark 4:29", "Praise & Adoration"),
        (477, "JISU THAIFÜ LAITEA", "I Have Decided To Follow Jesus", "Jisu thaifü laitea e paochere", "4/4", "Doh is F", "S.S. 477", "Sadhu Sundar Singh", "Indian Folk Melody", "Luke 9:23", "Christian Endeavour"),
        (478, "AKI VEI JUBILEE LOU", "Church Anniversary Hymn", "Aki vei jubilee lou sousho laisa", "4/4", "Doh is G", "PNBA 478", "Poumai Hymn Committee", "Traditional", "Lev. 25:10", "Dedication & Church Foundation Day"),
        (479, "JUBILEE TEITHE VELOURE", "Jubilee Chant", "Jubilee teithe veloure etao aki hi", "4/4", "Doh is D", "PNBA 479", "Poumai Literature Society", "Traditional", "Lev. 25:9", "Dedication & Church Foundation Day"),
        (480, "MAPAO VEI VAHSOUMAI", "Pastoral Installation", "Mapao vei vahsoumai kükou etao pfüwo", "4/4", "Doh is Eb", "PNBA 480", "Poumai Baptist Association", "Traditional", "1 Tim. 3:1", "Dedication & Church Foundation Day"),
        (481, "BAPTISMA LÜLOUYU LOU", "Baptismal Confession", "Baptisma lülouyu lou etao Jisu hi", "4/4", "Doh is F", "PNBA 481", "Poumai Baptist Association", "Traditional", "Rom. 6:4", "Christian Endeavour"),
        (482, "ASHI THETHE VEI LOU", "Wedding Choral", "Ashi thethe vei lou Ramai kükou buki", "4/4", "Doh is C", "PNBA 482", "Poumai Literature Society", "Traditional", "Matt. 19:6", "Love"),
        (483, "HRÜNA THETHE JISU SHOLO", "Children's Praise", "Hrüna thethe Jisu sholo asayu lou nou", "4/4", "Doh is G", "PNBA 483", "Poumai Sunday School Dept", "Traditional", "Matt. 21:16", "Praise & Adoration"),
        (484, "PUO THETHE VEI LOU", "Mothers' Society Hymn", "Puo thethe vei lou etao kükou buki", "4/4", "Doh is Bb", "PNBA 484", "Poumai Women Society", "Traditional", "Prov. 31:30", "Christian Endeavour"),
        (485, "PUO RAMAI VEI KHUPA (II)", "Fathers' Day Song", "Puo Ramai vei khupa aki hi reie", "4/4", "Doh is Eb", "PNBA 485", "Poumai Baptist Association", "Traditional", "Ps. 103:13", "Christian Endeavour"),
        (486, "SUNDAY SCHOOL LOU", "Sunday School Song", "Sunday School lou etao asayu soulai", "4/4", "Doh is C", "PNBA 486", "Poumai Sunday School Dept", "Traditional", "2 Tim. 3:15", "Christian Endeavour"),
        (487, "REITOU ASAYU LOU", "Harvest Thanksgiving", "Reitou asayu lou Ramaiye paosho bue", "4/4", "Doh is F", "PNBA 487", "Poumai Baptist Association", "Traditional", "Ps. 67:6", "Praise & Adoration"),
        (488, "TEIKHOU THETHE VEI LOU", "New Year Choral", "Teikhou thethe vei lou Ramai basha ngaowe", "4/4", "Doh is G", "PNBA 488", "Poumai Literature Society", "Traditional", "Ps. 65:11", "New Year"),
        (489, "POUMAI NAGA LOU", "Poumai Naga Unity Hymn", "Poumai Naga lou etao thethe soulo", "4/4", "Doh is D", "PNBA 489", "Poumai Naga Baptist Association", "Traditional Naga Melody", "Ps. 133:1", "Christian Endeavour"),
        (490, "THAOTHOU JISU DONOU", "All For Jesus", "Thaothou Jisu donou etao hrüyu peie", "4/4", "Doh is F", "C.W.H. 296", "Mary D. James", "J. Mountain", "Rom. 12:1", "Prayer & Consecration"),
        (491, "NEWO EVEI DAIZHO ZHOU", "Thou My All In All", "Newo evei daizho zhou Mapao Jisu bue", "4/4", "Doh is G", "C.W.H. 298", "Dennis Jernigan", "Dennis Jernigan", "Col. 3:11", "Worship"),
        (492, "MAI PHOUMAI", "Fishers Of Men", "Mai phoumai e ne souda peilai", "4/4", "Doh is C", "S.S. 712", "Harry D. Clarke", "Harry D. Clarke", "Matt. 4:19", "Mission & Evangelism"),
        (493, "HALLELUJAH! MAPAO JISU", "Hallelujah Chorus", "Hallelujah! Hallelujah! Mapao Jisu sholo", "4/4", "Doh is D", "C.W.H. 350", "G.F. Handel", "G.F. Handel", "Rev. 19:6", "Praise & Adoration"),
        (494, "THEIKHOU RAMAI SHOLO", "Holy God We Praise Thy Name (Full)", "Theikhou Ramai sholo zaipe thethesü", "3/4", "Doh is F", "C.W.H. 352", "Ignaz Franz", "Katholisches Gesangbuch", "Isa. 6:3", "Praise & Adoration"),
        (495, "MAPAO BASHA NE SHOU BUWO", "Choral Benediction", "Mapao basha ne shou buwo etao velouki", "4/4", "Doh is C", "Traditional", "Traditional Liturgy", "Traditional", "Num. 6:24", "Worship"),
        (496, "KHRISTA BASHA ETAO SHOU", "May The Grace Of Christ Our Savior", "Khrista basha etao shou buwo teisa teithe", "4/4", "Doh is F", "C.W.H. 354", "John Newton", "Ludwig van Beethoven", "2 Cor. 13:14", "Worship"),
        (497, "MAPAO NOU NE KHOPEILO (II)", "The Lord Bless You And Keep You", "Mapao nou ne khopeilo Ne shou pasholo", "4/4", "Doh is C", "C.W.H. 356", "Biblical Text", "Peter C. Lutkin", "Num. 6:24-26", "Worship"),
        (498, "RAMAIYE PAOSHOLO (OLD 100TH)", "Praise God, From Whom All Blessings Flow", "Ramaiye paosholo deiphao mai thethesü", "4/4", "Doh is G", "C.W.H. 100", "Thomas Ken", "Louis Bourgeois", "Ps. 100:1-5", "Praise & Adoration"),
        (499, "RAMAIYE PAOSHOLO DAIZHO ZHOU", "To God Be The Glory (Grand Finale)", "Ramaiye paosholo daizho zhou souda peire", "3/4", "Doh is Ab", "S.S. 23", "F.J. Crosby", "W.H. Doane", "Ps. 126:3", "Praise & Adoration"),
        (500, "AMEN, HALLELUJAH, AMEN", "The Grand Amen", "Amen, Hallelujah, Amen! Mapao Jisu sholo", "4/4", "Doh is D", "PNBA 500", "Poumai Hymn Committee", "Traditional Choral", "Rev. 19:4", "Worship")
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
            ] if "Amen" not in title else None
        }
        hymns.append(h)
    return hymns
