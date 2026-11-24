"""Add an additional 35 unique agricultural/horticultural characters to characters.json
to surpass 130+ characters in the database.
"""

import json
from pathlib import Path

CHAR_FILE = Path("characters.json")

with open(CHAR_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

existing = data.get("characters", [])
existing_ids = {c["id"] for c in existing}

MORE_CHARACTERS = [
    # --- SPICES & CONDIMENTS ---
    {
        "id": "jeera_jaggu",
        "name": "Jeera Jaggu (Cumin)",
        "tagline": "Khushboo aisi jo har thali ko mehkaye!",
        "category": "Spice",
        "state": "Gujarat / Rajasthan",
        "visual_identity": {
            "body": "3D tiny boat-shaped fragrant cumin seed mascot with golden-brown ribbed texture, wearing little Rajasthani pagri and vest",
            "eyes": "Sharp lively bright brown eyes",
            "expression": "Earnest appeal for sandy loam soil aeration and organic protection against blight",
            "setting": "Arid sunny desert farm rows with drip irrigation"
        },
        "transformation": {
            "before_organic": "Blight-infected blackened small seeds in burnt salty soil",
            "after_organic": "Aromatic golden-brown dense seed umbels brimming with essential oils"
        }
    },
    {
        "id": "saunf_santosh",
        "name": "Saunf Santosh (Fennel)",
        "tagline": "Meethi thandak aur behtareen sugandh!",
        "category": "Spice",
        "state": "Gujarat / Rajasthan",
        "visual_identity": {
            "body": "3D pale green plump ribbed fennel seed mascot with feathery green leafy antennae, wearing tiny white gardening gloves",
            "eyes": "Calm, gentle smiling green eyes",
            "expression": "Folded hands appealing to the farmer for moisture retention",
            "setting": "Sunny Gujarat crop field under bright blue sky"
        },
        "transformation": {
            "before_organic": "Hollow withered fennel seeds plagued by powdery mildew",
            "after_organic": "Plump heavy green fennel umbels heavy with sweet aromatic seed heads"
        }
    },
    {
        "id": "dhania_dhani",
        "name": "Dhania Dhani (Coriander Seed)",
        "tagline": "Sugandhit daane, har khet ki shaan!",
        "category": "Spice",
        "state": "Madhya Pradesh / Rajasthan",
        "visual_identity": {
            "body": "3D twin globular golden-yellow coriander seed mascot with fine vertical ribs, wearing a green leafy cape",
            "eyes": "Sparkling animated cheerful eyes",
            "expression": "Tearful plea against chemical wilt, joyful laughter at harvest",
            "setting": "Gentle breeze swaying fragrant white coriander flower beds"
        },
        "transformation": {
            "before_organic": "Wilted stem-gall infested brownish premature grains",
            "after_organic": "Lustrous round aromatic golden coriander seeds in massive bunches"
        }
    },
    {
        "id": "methi_mukesh",
        "name": "Methi Mukesh (Fenugreek Seed)",
        "tagline": "Aushadhiya guna, be-misaal taazgi!",
        "category": "Spice / Leafy",
        "state": "Rajasthan / Madhya Pradesh",
        "visual_identity": {
            "body": "3D angular golden-amber fenugreek seed character with deep groove, sporting a yellow bandana and tiny sturdy boots",
            "eyes": "Determined and hopeful animated eyes",
            "expression": "Passionate plea for root mycorrhizae and vermicompost humus",
            "setting": "Winter Rajasthan farm ridges with crisp morning mist"
        },
        "transformation": {
            "before_organic": "Stunted seedlings yellowing in alkaline crusty hardpan soil",
            "after_organic": "Tall lush green aromatic plants bearing long healthy pods packed with golden grains"
        }
    },
    {
        "id": "ajwain_anand",
        "name": "Ajwain Anand (Carom Seed)",
        "tagline": "Hazme ki takat, khet ki barkat!",
        "category": "Spice",
        "state": "Gujarat / Rajasthan",
        "visual_identity": {
            "body": "3D oval greyish-brown tiny striped carom seed mascot with dynamic energetic limbs and miniature spectacles",
            "eyes": "Wise friendly twinkling eyes",
            "expression": "Reassuring warm gesture towards the hardworking farmer",
            "setting": "Loamy soil beds under clear autumn sunlight"
        },
        "transformation": {
            "before_organic": "Shattered empty umbels on moisture-stressed cracked earth",
            "after_organic": "Sturdy branching plants laden with dense clusters of high-thymol seeds"
        }
    },
    {
        "id": "kali_mirch_karan",
        "name": "Kali Mirch Karan (Black Pepper)",
        "tagline": "Masalo ka raja, Malabar ki shan!",
        "category": "Spice",
        "state": "Kerala / Karnataka",
        "visual_identity": {
            "body": "3D textured wrinkled black peppercorn mascot clinging to an areca palm vine with green vine arms, wearing tiny traditional mundu",
            "eyes": "Bold fiery animated black eyes",
            "expression": "Proud and resilient, appealing for natural canopy compost",
            "setting": "Misty Western Ghats spice plantation with dripping emerald leaves"
        },
        "transformation": {
            "before_organic": "Quick-wilt rot dropping immature black berries on depleted soil",
            "after_organic": "Long drooping 15cm spike clusters packed with heavy pungent black peppercorns"
        }
    },
    {
        "id": "chhoti_elaichi_elena",
        "name": "Chhoti Elaichi Elena (Green Cardamom)",
        "tagline": "Khushboo ki rani, anmol swaad!",
        "category": "Spice",
        "state": "Kerala / Tamil Nadu",
        "visual_identity": {
            "body": "3D plump three-sided vivid green cardamom pod mascot with delicate longitudinal ridges, wearing a tiny floral garland",
            "eyes": "Large graceful sparkling hazel eyes",
            "expression": "Gentle folded hands praying for rich forest humus and mulch",
            "setting": "Shaded humid high-altitude cardamom hill reserve"
        },
        "transformation": {
            "before_organic": "Thrip-scarred faded pale pods with dry empty seed cavities",
            "after_organic": "Vibrant emerald bold 8mm+ pods bursting with aromatic black oil-rich seeds"
        }
    },

    # --- PULSES & LEGUMES ---
    {
        "id": "moong_manoj",
        "name": "Moong Manoj (Green Gram)",
        "tagline": "Choti daal, sabse badi shakti!",
        "category": "Pulse",
        "state": "Rajasthan / Maharashtra / MP",
        "visual_identity": {
            "body": "3D cylindrical tiny olive-green moong bean mascot with a clean white hilum eye and green runner sneakers",
            "eyes": "Bright spirited energetic eyes",
            "expression": "Eager and enthusiastic appeal to fix nitrogen in living soil",
            "setting": "Summer zayed crop fields with sunny breeze"
        },
        "transformation": {
            "before_organic": "Yellow mosaic infected leaves and dried empty pods in depleted ground",
            "after_organic": "Lush emerald canopy loaded with 10-12 filled pods per cluster"
        }
    },
    {
        "id": "urad_umesh",
        "name": "Urad Umesh (Black Gram)",
        "tagline": "Paushtik urad, kisaan ka sachha sathi!",
        "category": "Pulse",
        "state": "Madhya Pradesh / Andhra Pradesh / UP",
        "visual_identity": {
            "body": "3D matte-black cylindrical pulse bean with bright white eye spot, wearing miniature boxing gloves",
            "eyes": "Strong resolute animated eyes",
            "expression": "Pleading for healthy root nodules over synthetic chemical sprays",
            "setting": "Black cotton soil ridges after monsoon rains"
        },
        "transformation": {
            "before_organic": "Powdery mildew covering leaves and shrivelled grey beans",
            "after_organic": "Stout bushes packed with upright hairy black pods brimming with protein"
        }
    },
    {
        "id": "tur_dal_tarun",
        "name": "Tur Dal Tarun (Pigeon Pea / Arhar)",
        "tagline": "Unchi paidawar, har rasoi ki pasand!",
        "category": "Pulse",
        "state": "Maharashtra / Karnataka / MP",
        "visual_identity": {
            "body": "3D plump golden-buff arhar seed mascot perched on a woody pigeon pea stalk, wearing tiny yellow farmer turban",
            "eyes": "Warm and hopeful brown eyes",
            "expression": "Emotional plea against pod borer damage, proud victory at harvest",
            "setting": "Tall 6-foot pigeon pea field during winter flowering"
        },
        "transformation": {
            "before_organic": "Sterility mosaic virus causing bushy stunted leaves with zero pod set",
            "after_organic": "Massive branching tree-like crop laden with thousands of healthy speckled pods"
        }
    },
    {
        "id": "masoor_madhav",
        "name": "Masoor Madhav (Red Lentil)",
        "tagline": "Lal masoor, sehat aur poshan se bharpoor!",
        "category": "Pulse",
        "state": "Uttar Pradesh / Bihar / MP",
        "visual_identity": {
            "body": "3D lens-shaped terracotta-orange split lentil mascot inside a delicate papery pod husk, wearing tiny blue scarf",
            "eyes": "Kind, emotive expressive eyes",
            "expression": "Humble folded palms thanking the kisan",
            "setting": "Cool rabi season alluvial loam furrows"
        },
        "transformation": {
            "before_organic": "Rust-infected drooping stems on parched hard soil",
            "after_organic": "Dense field of delicate pink-flowering plants loaded with double-seeded pods"
        }
    },
    {
        "id": "rajma_raghav",
        "name": "Rajma Raghav (Kidney Bean)",
        "tagline": "Pahadi swaad, lajawab poshan!",
        "category": "Pulse",
        "state": "Jammu & Kashmir / Himachal Pradesh / Uttarakhand",
        "visual_identity": {
            "body": "3D kidney-shaped deep maroon-red bean mascot with mottled crimson spots, wearing a warm Himachali woollen topi",
            "eyes": "Gentle earnest sparkling eyes",
            "expression": "Emotional plea for rich organic soil on mountain terrace slopes",
            "setting": "Misty mountain step-terraces with mountain streams"
        },
        "transformation": {
            "before_organic": "Pale undersized beans in eroded thin hillside topsoil",
            "after_organic": "Giant glossy maroon beans filling long sturdy pods on lush climbing vines"
        }
    },
    {
        "id": "soyabean_soma",
        "name": "Soyabean Soma (Soybean)",
        "tagline": "Protein ki khan, kisaan ka vardaan!",
        "category": "Oilseed / Pulse",
        "state": "Madhya Pradesh / Maharashtra",
        "visual_identity": {
            "body": "3D creamy-yellow round soybean mascot with prominent brown hilum, wearing farmer overalls and sturdy boots",
            "eyes": "Cheerful and determined animated eyes",
            "expression": "Earnest appeal for soil organic carbon to survive dry spells",
            "setting": "Vast Malwa plateau black soil fields under monsoon clouds"
        },
        "transformation": {
            "before_organic": "Yellowed stunted soybean plants suffering from charcoal rot",
            "after_organic": "Dense three-pod clusters from base to tip dripping with heavy yellow seeds"
        }
    },
    {
        "id": "mungfali_mangal",
        "name": "Mungfali Mangal (Groundnut)",
        "tagline": "Dharti ke bheetar chupa sona!",
        "category": "Oilseed",
        "state": "Gujarat / Andhra Pradesh / Tamil Nadu",
        "visual_identity": {
            "body": "3D reticulated hourglass golden-tan peanut shell mascot peeking out of fertile sandy loam, wearing miniature miner helmet",
            "eyes": "Curious bright peeping eyes",
            "expression": "Pleading for soft, aerated organic soil so pegging roots can penetrate easily",
            "setting": "Saurashtra red loam furrows bathed in morning golden light"
        },
        "transformation": {
            "before_organic": "Compact hardpan soil preventing pegging, yielding single pops (empty shells)",
            "after_organic": "Clusters of 40+ double-kernel heavy pods per plant filled with sweet oil-rich nuts"
        }
    },
    {
        "id": "til_tararam",
        "name": "Til Tararam (Sesame)",
        "tagline": "Chota daana, bada tel aur taakat!",
        "category": "Oilseed",
        "state": "Gujarat / Rajasthan / West Bengal",
        "visual_identity": {
            "body": "3D flat pear-shaped pearly-white sesame seed character with golden sheen, wearing white scarf and tiny sandals",
            "eyes": "Alert cheerful cartoon eyes",
            "expression": "Folded hands appealing for organic defense against phyllody",
            "setting": "Sunny dryland field with bell-shaped white and purple sesame blossoms"
        },
        "transformation": {
            "before_organic": "Phyllody turning flowers into sterile green leafy masses",
            "after_organic": "Erect tall stems packed with 4-lobed dehiscent capsules bursting with white sesame"
        }
    },
    {
        "id": "sarson_shyam",
        "name": "Sarson Shyam (Mustard)",
        "tagline": "Peela sona, har dil ko lubhaye!",
        "category": "Oilseed",
        "state": "Rajasthan / Haryana / Punjab / MP",
        "visual_identity": {
            "body": "3D spherical glossy brown-black mustard seed nestled in a bright yellow mustard flower crown, wearing traditional yellow kurta",
            "eyes": "Joyful bright twinkling eyes",
            "expression": "Emotional plea for sulphur-rich vermicompost to fight aphid attacks",
            "setting": "Endless cinematic yellow mustard fields under clear blue winter sky"
        },
        "transformation": {
            "before_organic": "Aphid-smothered sticky stunted siliquae on chemical-parched land",
            "after_organic": "6-foot tall thick-stemmed branching plants bearing thousands of seed pods with 42% oil content"
        }
    },
    {
        "id": "surajmukhi_suraj",
        "name": "Surajmukhi Suraj (Sunflower)",
        "tagline": "Sooraj ki kiran, khet ka tejaswi taara!",
        "category": "Oilseed",
        "state": "Karnataka / Andhra Pradesh / Maharashtra",
        "visual_identity": {
            "body": "3D radiant golden sunflower disk mascot with bright ray petals forming a lion-like mane, wearing sunglasses and green gloves",
            "eyes": "Beaming charismatic brown eyes",
            "expression": "Sunny confident smile transitioning to deep gratitude to the farmer",
            "setting": "Deccan plateau sunlit field tracking the golden morning sun"
        },
        "transformation": {
            "before_organic": "Drooping small heads with hollow chaffy centers due to micro-nutrient deficiency",
            "after_organic": "Giant 30cm upright heavy sunflower heads packed solid with black oil-rich seeds"
        }
    },

    # --- FRUITS & PLANTATION ---
    {
        "id": "amla_ashok",
        "name": "Amla Ashok (Indian Gooseberry)",
        "tagline": "Amrit tulya amla, arogya ka srot!",
        "category": "Fruit",
        "state": "Uttar Pradesh (Pratapgarh) / MP",
        "visual_identity": {
            "body": "3D translucent jade-green ribbed round amla mascot with 6 vertical striations, wearing a small Ayurvedic sage garland",
            "eyes": "Wise luminous animated eyes",
            "expression": "Serene and benevolent appeal for natural tree basin mulch",
            "setting": "Orchard of Pratapgarh with sunlight filtering through feathery leaves"
        },
        "transformation": {
            "before_organic": "Necrotic brown spots and fruit drop on hard-packed soil",
            "after_organic": "Glassy flawless giant Banarasi amlas hanging in thick emerald clusters"
        }
    },
    {
        "id": "amrood_anand",
        "name": "Amrood Anand (Allahabadi Guava)",
        "tagline": "Safeda ki mithaas, laal gude ka swaad!",
        "category": "Fruit",
        "state": "Uttar Pradesh / Madhya Pradesh",
        "visual_identity": {
            "body": "3D round crisp yellow-green guava mascot with a rosy pink blush and dried calyx bottom, wearing white cartoon gloves",
            "eyes": "Cheeky cheerful sparkling eyes",
            "expression": "Folded hands asking the kisan for fruit-fly organic protection",
            "setting": "Allahabad guava orchard with white bagged fruits on healthy branches"
        },
        "transformation": {
            "before_organic": "Hard gritty fruit infested with fruit fly maggots in dry depleted soil",
            "after_organic": "Jumbo 400g crisp melting-sweet Safeda guava with snowy fragrant pulp"
        }
    },
    {
        "id": "anar_arjun",
        "name": "Anar Arjun (Bhagwa Pomegranate)",
        "tagline": "Laal mani jaisa dana, Sholapur ka garv!",
        "category": "Fruit",
        "state": "Maharashtra (Solapur) / Gujarat",
        "visual_identity": {
            "body": "3D glossy saffron-red pomegranate mascot with a prominent crown calyx, peeking open to show ruby arils like gemstones",
            "eyes": "Radiant passionate eyes",
            "expression": "Pleading against bacterial blight (oily spot), celebrating harvest joy",
            "setting": "Drip-irrigated arid Deccan orchard rows with fertile tree basins"
        },
        "transformation": {
            "before_organic": "Cracked fruit shells with black bacteriosis spots on chemical-burnt orchard",
            "after_organic": "Flawless heavy crimson 500g Bhagwa pomegranates filled with soft-seeded sweet ruby arils"
        }
    },
    {
        "id": "sitaphal_shankar",
        "name": "Sitaphal Shankar (Custard Apple)",
        "tagline": "Balanagar ki mithaas, makhmali guda!",
        "category": "Fruit",
        "state": "Maharashtra / Telangana / MP",
        "visual_identity": {
            "body": "3D bumpy knobby green heart-shaped custard apple mascot with white creamy crevices showing through, wearing green boots",
            "eyes": "Warm and sweet animated eyes",
            "expression": "Earnest appeal for organic root moisture during fruit swell",
            "setting": "Hilly semi-arid scrub farm under gentle monsoon sunshine"
        },
        "transformation": {
            "before_organic": "Mummified black undersized fruits clinging to desiccated bare branches",
            "after_organic": "Super-sized Balanagar sitaphal with wide creamy eyes and thick fragrant custard pulp"
        }
    },
    {
        "id": "papita_pankaj",
        "name": "Papita Pankaj (Taiwan 786 Papaya)",
        "tagline": "Laal guda, meetha swaad, sabse tezi se labh!",
        "category": "Fruit",
        "state": "Gujarat / MP / Maharashtra",
        "visual_identity": {
            "body": "3D elongated golden-orange papaya mascot with emerald green shoulders and starry green umbrella leaf crown",
            "eyes": "Friendly, bright animated brown eyes",
            "expression": "Emotional plea for ring-spot prevention via soil immunity",
            "setting": "Uniform orchard rows of dwarf papaya trees loaded with fruit columns"
        },
        "transformation": {
            "before_organic": "Ring-spot virus blistering leaves and dropping immature rotting fruits",
            "after_organic": "Stems stacked tightly with 50+ uniform 2kg red-pulped sweet fruits"
        }
    },
    {
        "id": "alphonso_aamir",
        "name": "Alphonso Aamir (Hapus Mango)",
        "tagline": "Aamon ka samrat, Konkan ki shaan!",
        "category": "Fruit",
        "state": "Maharashtra (Ratnagiri / Devgad)",
        "visual_identity": {
            "body": "3D saffron-golden ovate mango mascot with a delicate carmine blush and green stem cap, wearing a royal crown",
            "eyes": "Regal yet deeply affectionate expressive eyes",
            "expression": "Hands folded in humble respect to the coastal Konkan farmer",
            "setting": "Red laterite hill slopes overlooking the Arabian Sea"
        },
        "transformation": {
            "before_organic": "Spongy tissue formation and thrip scarring from heavy chemical paclobutrazol over-use",
            "after_organic": "Pure golden-yellow fiberless aromatic Hapus mango with divine natural sweetness"
        }
    },
    {
        "id": "dasheri_deepak",
        "name": "Dasheri Deepak (Malihabadi Mango)",
        "tagline": "Malihabad ki virasat, meethi chashni!",
        "category": "Fruit",
        "state": "Uttar Pradesh (Lucknow / Malihabad)",
        "visual_identity": {
            "body": "3D long slender jade-yellow mango mascot with elegant curve and sweet smile, wearing traditional Awadhi cap",
            "eyes": "Poetic dreamy animated eyes",
            "expression": "Warm plea to protect old heritage orchard roots with B.S Organic vermicompost",
            "setting": "Ancient sprawling mango groves of Malihabad with birds chirping"
        },
        "transformation": {
            "before_organic": "Black-tip disease caused by brick-kiln fumes and nutrient starvation",
            "after_organic": "Long golden-green blemish-free mangoes dripping with rich honey nectar"
        }
    },
    {
        "id": "kela_kanhaiya",
        "name": "Kela Kanhaiya (Grand Naine Banana)",
        "tagline": "Bhari lound, mota daana, har mandee mein danka!",
        "category": "Fruit",
        "state": "Maharashtra (Jalgaon) / Gujarat / Tamil Nadu",
        "visual_identity": {
            "body": "3D curved sunny-yellow banana mascot with green tip wearing blue bandana and little yellow boots",
            "eyes": "Energetic, playful wide cartoon eyes",
            "expression": "Folded hands asking for potassium and humus nutrition",
            "setting": "Jalgaon banana plantation with huge pendulous bunch hanging under purple flower bell"
        },
        "transformation": {
            "before_organic": "Panama wilt yellowing leaves and choking stem vascular bundles",
            "after_organic": "Massive 35kg heavy bunch with 12 hands of spotless uniform thick bananas"
        }
    },
    {
        "id": "chikoo_chaman",
        "name": "Chikoo Chaman (Kalipatti Sapota)",
        "tagline": "Gholwad ka mitha chikoo, daanedaar swaad!",
        "category": "Fruit",
        "state": "Maharashtra (Palghar) / Gujarat",
        "visual_identity": {
            "body": "3D oval fuzzy brown sapota mascot with sandy skin texture, wearing brown baker apron and white gloves",
            "eyes": "Sweet gentle sparkling eyes",
            "expression": "Pleading for regular compost nourishment year-round",
            "setting": "Coastal orchard with dark green glossy Kalipatti leaves"
        },
        "transformation": {
            "before_organic": "Hard stone-like undersized chikoos dropping prematurely during heatwaves",
            "after_organic": "Heavy brown clusters of melting brown-sugar sweet sapotas bursting with energy"
        }
    },
    {
        "id": "anjeer_ashwin",
        "name": "Anjeer Ashwin (Poona Fig)",
        "tagline": "Rajewadi anjeer, swasthya ka bhandar!",
        "category": "Fruit",
        "state": "Maharashtra (Pune / Purandar)",
        "visual_identity": {
            "body": "3D bell-shaped reddish-purple fig mascot with a tiny honey eye at the apex, wearing little marathi pagdi",
            "eyes": "Kind, affectionate animated eyes",
            "expression": "Hands folded in reverence to the hardworking farmer",
            "setting": "Sun-drenched rocky Purandar foothills with terraced fig orchards"
        },
        "transformation": {
            "before_organic": "Fruit splitting and rust-damaged leaves due to erratic moisture",
            "after_organic": "Large fleshy honey-filled purple figs with tender skin and pink crunchy seeds"
        }
    },
    {
        "id": "jamun_jitendra",
        "name": "Jamun Jitendra (Black Plum)",
        "tagline": "Madhumeha-nashak, kudarat ka anmol uphar!",
        "category": "Fruit",
        "state": "Uttar Pradesh / Maharashtra / Haryana",
        "visual_identity": {
            "body": "3D oblong glossy deep-purple-black jamun mascot with a rich magenta blush, wearing little white gloves",
            "eyes": "Dignified friendly cartoon eyes",
            "expression": "Emotional plea for soil rejuvenation around deep tree taproots",
            "setting": "Sprawling tall jamun trees flanking countryside canal banks"
        },
        "transformation": {
            "before_organic": "Dry astringent insect-pierced small fruit drop on barren clay",
            "after_organic": "Massive fleshy seed-small jamuns with sweet astringent juice staining fingers violet"
        }
    },
    {
        "id": "litchi_lalita",
        "name": "Litchi Lalita (Shahi Litchi)",
        "tagline": "Muzaffarpur ki rani, shahi mithaas!",
        "category": "Fruit",
        "state": "Bihar (Muzaffarpur)",
        "visual_identity": {
            "body": "3D heart-shaped strawberry-red bumpy litchi mascot with translucent snowy pulp peeking out, wearing floral tiara",
            "eyes": "Gorgeous sparkling wide eyes",
            "expression": "Tearful plea against scorching loo winds and fruit cracking",
            "setting": "Misty orchards of Muzaffarpur during early summer dawn"
        },
        "transformation": {
            "before_organic": "Sunburnt cracked brittle brown shells leaking dry pulp",
            "after_organic": "Rose-scented crimson clusters overflowing with crystalline sweet juice"
        }
    },

    # --- ROOT & SPECIALTY VEGETABLES ---
    {
        "id": "palak_pawan",
        "name": "Palak Pawan (Spinach)",
        "tagline": "Iron ki shakti, hari taazgi ka khazana!",
        "category": "Vegetable (Leafy)",
        "state": "Punjab / Haryana / UP",
        "visual_identity": {
            "body": "3D broad succulent forest-green spinach leaf mascot with emerald veins and superhero cape, wearing yellow sneakers",
            "eyes": "Strong energetic sparkling eyes",
            "expression": "Pleading for chemical-free clean vermicompost nutrition",
            "setting": "Crisp morning vegetable beds glistening with water spray"
        },
        "transformation": {
            "before_organic": "Yellow-veined leaf spot infested papery thin leaves",
            "after_organic": "Gigantic fleshy dark-green crinkled leaves packed with organic minerals"
        }
    },
    {
        "id": "mooli_manohar",
        "name": "Mooli Manohar (Radish)",
        "tagline": "Kari-safed, meethi-teekhi, har bite mein crunch!",
        "category": "Vegetable (Root)",
        "state": "Punjab / Bihar / West Bengal",
        "visual_identity": {
            "body": "3D pure snow-white tapered cylindrical radish mascot with a tuft of vibrant green serrated foliage, wearing tiny denim overalls",
            "eyes": "Cheerful playful cartoon eyes",
            "expression": "Namaste hands emerging from deep rich loam",
            "setting": "Raised bed ridges in frosty winter morning vegetable farm"
        },
        "transformation": {
            "before_organic": "Forked fibrous pungent hollow roots in hard rocky chemical soil",
            "after_organic": "Pencil-straight 1.5-foot crisp juicy sweet white radishes pulling out effortlessly"
        }
    },
    {
        "id": "chukandar_chhotu",
        "name": "Chukandar Chhotu (Beetroot)",
        "tagline": "Khoon badhane wala lal-surkh chukandar!",
        "category": "Vegetable (Root)",
        "state": "Tamil Nadu / Karnataka / UP",
        "visual_identity": {
            "body": "3D globular ruby-crimson beetroot mascot with purple-veined green leaves on top, wearing little red gardening boots",
            "eyes": "Bubbly cute wide eyes with rosy cheeks",
            "expression": "Earnest appeal for loose organic beds and boron nutrition",
            "setting": "Cool climate loamy ridges under soft morning sun"
        },
        "transformation": {
            "before_organic": "Internal black heart rot and scabby surface in alkaline hardpan",
            "after_organic": "Smooth flawless dark-blood-red sweet round roots heavy with vitality"
        }
    },
    {
        "id": "sahjan_suraj",
        "name": "Sahjan Suraj (Moringa / Drumstick)",
        "tagline": "Kudarat ka superfood, hazar bimariyon ka tod!",
        "category": "Vegetable",
        "state": "Tamil Nadu / Andhra Pradesh / Gujarat",
        "visual_identity": {
            "body": "3D long slender grooved green drumstick pod mascot with delicate white flowers, wearing a karate headband",
            "eyes": "Dynamic agile animated eyes",
            "expression": "Respectful bow appealing for living microbial soil health",
            "setting": "Fast-growing moringa trees laden with 2-foot long green pods"
        },
        "transformation": {
            "before_organic": "Hairy caterpillar defoliation and brittle yellowing pod drop",
            "after_organic": "Heavy clusters of fleshy tender non-fibrous drumsticks swaying gently in the breeze"
        }
    },
    {
        "id": "suran_sudarshan",
        "name": "Suran Sudarshan (Elephant Foot Yam)",
        "tagline": "Bhaari kanda, kisaan ka bachat bhandaar!",
        "category": "Vegetable (Tuber)",
        "state": "Kerala / West Bengal / Bihar / UP",
        "visual_identity": {
            "body": "3D massive rugged hemispherical brown tuber mascot with a bright pink central sprout bud, wearing a weightlifter belt",
            "eyes": "Sturdy honest kind eyes",
            "expression": "Folded hands asking for deep soil organic carbon and mulch",
            "setting": "Shady rich forest-garden floor with tropical canopy"
        },
        "transformation": {
            "before_organic": "Collar rot turning tubers soft and foul in waterlogged chemical soil",
            "after_organic": "Colossal 8kg solid disease-free tubers with rich acrid-free golden-orange flesh"
        }
    }
]

added_count = 0
for char in MORE_CHARACTERS:
    if char["id"] not in existing_ids:
        existing.append(char)
        existing_ids.add(char["id"])
        added_count += 1

data["characters"] = existing

with open(CHAR_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Successfully added {added_count} more characters!")
print(f"Total characters in characters.json is now: {len(existing)}")
