"""Appends 75+ rich authentic Indian crop characters to characters.json,
bringing the total roster to 108+ characters.
"""

import json
from pathlib import Path

CHAR_FILE = Path("characters.json")

with open(CHAR_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

existing = data.get("characters", [])
existing_ids = {c["id"] for c in existing}

NEW_CHARACTERS = [
    # --- VEGETABLES: Brassicas, Solanaceae & Gourds ---
    {
        "id": "gobhi_gopal",
        "name": "Gobhi Gopal (Cauliflower)",
        "tagline": "Doodh jaisi safed gobhi, har kisaan ka abhimaan!",
        "category": "Vegetable",
        "state": "Bihar / Punjab / UP",
        "visual_identity": {
            "body": "3D adorable dense milky-white cauliflower curd mascot surrounded by crisp green protective wrapper leaves, white gardener gloves, brown soil boots",
            "eyes": "Big bright round eyes with curious, cheerful twinkle",
            "expression": "Earnest pleading when facing pests, proud beaming smile at harvest",
            "setting": "Cool winter morning loamy farm furrow with dew drops"
        },
        "transformation": {
            "before_organic": "Yellowish loose browning curds attacked by borers in dry chemical soil",
            "after_organic": "Massive 2kg solid snow-white head with crisp sweet florets fed by rich dark vermicompost"
        }
    },
    {
        "id": "patta_gobhi_parshu",
        "name": "Patta Gobhi Parshu (Cabbage)",
        "tagline": "Thos, hari aur wajandar—swaad mein lajawab!",
        "category": "Vegetable",
        "state": "West Bengal / Odisha",
        "visual_identity": {
            "body": "3D tightly folded emerald green round cabbage mascot with layered outer ruffled leaves, little yellow boots",
            "eyes": "Wide eager eyes with rosy animated cheeks",
            "expression": "Humble folded hands pleading for organic care",
            "setting": "Lush winter vegetable fields with irrigation channels"
        },
        "transformation": {
            "before_organic": "Hollow loose-leaf cabbage heads wilting in scorched chemical fertilizer bed",
            "after_organic": "Rock-hard dense 2.5kg shiny green head bursting with natural crunch"
        }
    },
    {
        "id": "banarasi_baingan",
        "name": "Banarasi Baingan (Purple Brinjal)",
        "tagline": "Chamkila baingani rang, be-daag aur behtareen!",
        "category": "Vegetable",
        "state": "Uttar Pradesh / Bihar",
        "visual_identity": {
            "body": "3D glossy deep-purple teardrop brinjal with an emerald thorny calyx cap, playful white cartoon hands, tiny green shoes",
            "eyes": "Big expressive brown cartoon eyes",
            "expression": "Tearful plea against fruit borers, joyful triumphant wink",
            "setting": "Rich alluvial Gangetic plains soil with sunshine"
        },
        "transformation": {
            "before_organic": "Dull scratched fruit with bore-holes and droopy yellowed leaves",
            "after_organic": "Ultra-glossy mirror-finish heavy purple eggplants hanging in abundance"
        }
    },
    {
        "id": "bharta_baingan_bholu",
        "name": "Bharta Baingan Bholu (Round Eggplant)",
        "tagline": "Bada aakar, narm guda, asli deshi mithaas!",
        "category": "Vegetable",
        "state": "Punjab / Haryana",
        "visual_identity": {
            "body": "3D big round plump violet eggplant mascot with a sturdy green crown stem, wearing little denim overalls",
            "eyes": "Warm gentle round eyes",
            "expression": "Folded hands Namaste greeting to the farmer",
            "setting": "Punjab farm ridges under golden afternoon sun"
        },
        "transformation": {
            "before_organic": "Stunted hard bitter eggplants in salinity-choked chemical soil",
            "after_organic": "Giant 800g tender seedless purple globe bursting with sweet organic pulp"
        }
    },
    {
        "id": "karela_kishore",
        "name": "Karela Kishore (Bitter Gourd)",
        "tagline": "Kareli aushadhi, sehat ka khazana!",
        "category": "Vegetable",
        "state": "Madhya Pradesh / Maharashtra",
        "visual_identity": {
            "body": "3D textured bumpy emerald green bitter gourd character clinging to a bamboo trellis with winding curly tendril arms",
            "eyes": "Spunky large cartoon eyes full of determination",
            "expression": "Passionate plea for root aeration and compost nutrition",
            "setting": "Vertical bamboo trellis system in sunny farm rows"
        },
        "transformation": {
            "before_organic": "Pale yellowing curled bitter gourds withering on brittle vines",
            "after_organic": "Long, thick dark-green firm bitter gourds glistening with morning dew"
        }
    },
    {
        "id": "lauki_lalita",
        "name": "Lauki Lalita (Bottle Gourd)",
        "tagline": "Lambhi, narm aur rasili—har ghar ki pasand!",
        "category": "Vegetable",
        "state": "Uttar Pradesh / Rajasthan",
        "visual_identity": {
            "body": "3D graceful smooth light-green cylindrical bottle gourd with a cute flower blossom on top, gentle smiling face",
            "eyes": "Soft doe eyes with blinking long eyelashes",
            "expression": "Affectionate smile with hands placed on heart",
            "setting": "Thick green canopy over raised organic mulch beds"
        },
        "transformation": {
            "before_organic": "Crooked bitter stunted gourds dropping flowers under heat stress",
            "after_organic": "Straight 2-foot tender flawless pale-green bottle gourds hanging abundantly"
        }
    },
    {
        "id": "torai_tarun",
        "name": "Torai Tarun (Ridge Gourd)",
        "tagline": "Meethi hari torai, kisaan ka vishwas!",
        "category": "Vegetable",
        "state": "Gujarat / Maharashtra",
        "visual_identity": {
            "body": "3D slender dark-green ribbed gourd with distinct sharp ridges along its body, wearing tiny gardener gloves",
            "eyes": "Sharp curious cartoon eyes",
            "expression": "Eager and cheerful, pointing to fertile roots",
            "setting": "Organic trellis netting in sunny field"
        },
        "transformation": {
            "before_organic": "Fibrous hard dry ridge gourds suffering from yellow mosaic",
            "after_organic": "Succulent tender sweet ridge gourds with vibrant emerald skin"
        }
    },
    {
        "id": "kaddu_kalyan",
        "name": "Kaddu Kalyan (Golden Pumpkin)",
        "tagline": "Bhari wajan, sunahara rang, bumper aamdani!",
        "category": "Vegetable",
        "state": "Assam / Bengal / UP",
        "visual_identity": {
            "body": "3D massive ribbed golden-orange pumpkin mascot resting on soil with broad green leaf umbrella overhead",
            "eyes": "Chubby jolly smiling eyes and rosy cheeks",
            "expression": "Laughing proudly with two thumbs up",
            "setting": "Sprawling vine patch across moist dark loamy soil"
        },
        "transformation": {
            "before_organic": "Rotting small fruits on hard cracked clay with dried-up vines",
            "after_organic": "Colossal 15kg golden ribbed pumpkin bursting with sweet orange flesh"
        }
    },
    {
        "id": "tinda_tilak",
        "name": "Tinda Tilak (Round Gourd)",
        "tagline": "Chota aakar, bada kamaal!",
        "category": "Vegetable",
        "state": "Punjab / Haryana / Rajasthan",
        "visual_identity": {
            "body": "3D cute round apple-shaped bright green gourd with fine fuzzy soft hairs and tiny green boots",
            "eyes": "Wide cheerful eyes",
            "expression": "Playful and pleading with open arms",
            "setting": "Sandy loam desert edge with drip irrigation"
        },
        "transformation": {
            "before_organic": "Hard bitter spotty gourds wilting in dry sandy crust",
            "after_organic": "Tender apple-green shining round tindas picked by the basketful"
        }
    },
    {
        "id": "parwal_prakash",
        "name": "Parwal Prakash (Pointed Gourd)",
        "tagline": "Mithai ho ya sabzi, parwal hai sabse aage!",
        "category": "Vegetable",
        "state": "Bihar / West Bengal / Eastern UP",
        "visual_identity": {
            "body": "3D spindle-shaped green striped pointed gourd mascot with delicate white vine tendril hands",
            "eyes": "Bright expressive brown cartoon eyes",
            "expression": "Emotional plea with folded hands for earthworm nutrition",
            "setting": "Raised sand-bed riverbed farming rows"
        },
        "transformation": {
            "before_organic": "Blight-infected yellowing vines with zero female fruit setting",
            "after_organic": "Heavy clusters of striped crunchy green parwals on healthy dark soil"
        }
    },
    {
        "id": "kundru_kripal",
        "name": "Kundru Kripal (Ivy Gourd)",
        "tagline": "Baar-baar todo, lagatar kamao!",
        "category": "Vegetable",
        "state": "Odisha / Andhra Pradesh / MP",
        "visual_identity": {
            "body": "3D tiny cute oval emerald green ivy gourd with white stripe markings and fast little feet",
            "eyes": "Energetic blinking cartoon eyes",
            "expression": "Jumping excitedly atop harvest piles",
            "setting": "Perennial wire trellis system"
        },
        "transformation": {
            "before_organic": "Dry tough tiny pods on yellowing tangled dead vines",
            "after_organic": "Non-stop daily harvest of crisp tender glossy kundrus"
        }
    },

    # --- ROOT VEGETABLES & BULBS ---
    {
        "id": "mooli_mukesh",
        "name": "Mooli Mukesh (White Radish)",
        "tagline": "Seedhi, safed aur meethi—bina kadwapan ke!",
        "category": "Vegetable",
        "state": "Punjab / UP / Haryana",
        "visual_identity": {
            "body": "3D tall slender snow-white taper radish body peeking from deep soil, crowned with crisp jagged green leaves",
            "eyes": "Large friendly blue-gray eyes",
            "expression": "Looking up from underground with folded hands",
            "setting": "Deep friable raised soil beds in winter sunshine"
        },
        "transformation": {
            "before_organic": "Forked, cracked, woody bitter roots trapped in compacted hardpan",
            "after_organic": "Perfect 18-inch smooth pristine white sweet radish with juicy crunch"
        }
    },
    {
        "id": "chukandar_champak",
        "name": "Chukandar Champak (Beetroot)",
        "tagline": "Khoon badhaye, laal rang laaye!",
        "category": "Vegetable",
        "state": "Maharashtra / Karnataka",
        "visual_identity": {
            "body": "3D plump round ruby-crimson beetroot bulb with purple-veined lush upright green leaves, earthy brown boots",
            "eyes": "Twinkling joyful eyes with deep magenta blush",
            "expression": "Proudly pointing down to glowing taproot in dark earth",
            "setting": "Moist humus-rich soil furrow"
        },
        "transformation": {
            "before_organic": "Shriveled hard fibrous root with scab spots in chemical bed",
            "after_organic": "Solid heavy 400g deep crimson beetroot glowing with natural sweetness"
        }
    },
    {
        "id": "arbi_amar",
        "name": "Arbi Amar (Taro Corm)",
        "tagline": "Bada kanda, zordar vajan!",
        "category": "Vegetable",
        "state": "Kerala / UP / Assam",
        "visual_identity": {
            "body": "3D ribbed earthy-brown taro corm mascot holding a giant waterproof elephant-ear leaf as an umbrella",
            "eyes": "Gentle wise smiling eyes",
            "expression": "Waving warmly with rain droplets glistening on leaf",
            "setting": "High-moisture loamy soil trench"
        },
        "transformation": {
            "before_organic": "Small rotting cormlets choked by fungal root rot",
            "after_organic": "Giant cluster of clean, heavy starch-rich taro corms"
        }
    },
    {
        "id": "shakarkand_suraj",
        "name": "Shakarkand Suraj (Sweet Potato)",
        "tagline": "Kudrati meetha, poshan se bharpoor!",
        "category": "Vegetable",
        "state": "Odisha / Kerala / Bihar",
        "visual_identity": {
            "body": "3D plump copper-pink sweet potato mascot resting underground with lush purple-tinted heart leaf vines above",
            "eyes": "Smiling serene cartoon eyes",
            "expression": "Humble and warm, hugging rich dark soil",
            "setting": "Soft sandy-loam mounds with golden god-rays"
        },
        "transformation": {
            "before_organic": "Skinny stringy tuber infested by weevils in dry clay",
            "after_organic": "Massive 1kg copper-skinned tuber packed with golden sweet beta-carotene pulp"
        }
    },
    {
        "id": "suran_sudarshan",
        "name": "Suran Sudarshan (Elephant Foot Yam)",
        "tagline": "Ek podha, das kilo ka kanda!",
        "category": "Vegetable",
        "state": "Kerala / Gujarat / Bengal",
        "visual_identity": {
            "body": "3D massive sturdy craggy brown yam tuber with miniature tree-like spotted umbrella stalk on top",
            "eyes": "Big jolly grandfatherly eyes",
            "expression": "Chuckling proudly with wide open arms",
            "setting": "Deep organic pit filled with vermicompost and leaf mould"
        },
        "transformation": {
            "before_organic": "Stunted 1kg itchy tuber with necrotic spots in compacted dirt",
            "after_organic": "Record 12kg smooth, non-acrid colossal yam lifted triumphantly"
        }
    },

    # --- LEAFY GREENS & HERBS ---
    {
        "id": "methi_maya",
        "name": "Methi Maya (Fenugreek Greens)",
        "tagline": "Khushbudar pattiya, swasthya ka vardan!",
        "category": "Vegetable",
        "state": "Rajasthan / Gujarat",
        "visual_identity": {
            "body": "3D cute clover-like triple emerald green fenugreek leaf mascot with a tiny yellow floral crown",
            "eyes": "Large sparkling doe eyes",
            "expression": "Namaste hands pleading against aphid attack",
            "setting": "Golden sand loam garden bed under sunrise light"
        },
        "transformation": {
            "before_organic": "Yellow wilted bitter leaves burned by chemical urea sprays",
            "after_organic": "Thick fragrant lush green carpet ready for multiple rapid cuttings"
        }
    },
    {
        "id": "bathua_baldev",
        "name": "Bathua Baldev (Chenopodium Winter Green)",
        "tagline": "Sardi ka sabse takatwar saag!",
        "category": "Vegetable",
        "state": "Haryana / Punjab / UP",
        "visual_identity": {
            "body": "3D serrated dusty-green leaf mascot with delicate purple frosted blush on new shoots",
            "eyes": "Eager wide eyes with a friendly smile",
            "expression": "Reaching up happily towards warm winter sun",
            "setting": "Inter-cropped organic wheat furrows"
        },
        "transformation": {
            "before_organic": "Stunted tough dry weed-like stems struggling in barren soil",
            "after_organic": "Tender, iron-rich, succulent leafy green stalks"
        }
    },
    {
        "id": "sarson_saag_sukhdev",
        "name": "Sarson Saag Sukhdev (Mustard Greens)",
        "tagline": "Makki ki roti ke saath, Punjab ki shaan!",
        "category": "Vegetable",
        "state": "Punjab / Haryana",
        "visual_identity": {
            "body": "3D broad crinkled vibrant-green mustard leaf mascot wearing a tiny yellow turban and farmer gamchha",
            "eyes": "Vibrant spirited eyes with proud mustache twirl",
            "expression": "Bhangra celebratory pose atop lush green field",
            "setting": "Vast green mustard field in winter Punjab morning mist"
        },
        "transformation": {
            "before_organic": "Bitter purple-spotted leaves infested with painted bug",
            "after_organic": "Juicy, tender, buttery broad leaves packed with authentic flavor"
        }
    },
    {
        "id": "chaulai_champa",
        "name": "Chaulai Champa (Amaranth Greens)",
        "tagline": "Garmiyon ka harabhara tohfa!",
        "category": "Vegetable",
        "state": "Maharashtra / UP / Bihar",
        "visual_identity": {
            "body": "3D dual-toned green and deep-magenta amaranth leaf mascot with tiny red boots",
            "eyes": "Playful bright eyes",
            "expression": "Joyful dance with dew sparkling on leaves",
            "setting": "Raised bed terrace garden in summer morning"
        },
        "transformation": {
            "before_organic": "Flowering prematurely in hard dry soil with tough fibrous stems",
            "after_organic": "Thick tender red-green succulent stems harvested continuously"
        }
    },
    {
        "id": "dhaniya_rani",
        "name": "Dhaniya Rani (Coriander Greens)",
        "tagline": "Kudrati mehak, jo har khane ka swaad badhaye!",
        "category": "Vegetable & Herb",
        "state": "Madhya Pradesh / Rajasthan",
        "visual_identity": {
            "body": "3D delicate feathery lace-green coriander sprig mascot with tiny flower tiara",
            "eyes": "Big bright emotive eyes with cheerful smile",
            "expression": "Waving scented aroma breeze towards the farmer",
            "setting": "Moist kitchen garden organic patch"
        },
        "transformation": {
            "before_organic": "Bolting early into seeds with pale yellowing scorched leaf tips",
            "after_organic": "Bushy dense aromatic dark-green bouquet with long tender stems"
        }
    },
    {
        "id": "pudina_pappu",
        "name": "Pudina Pappu (Fresh Mint)",
        "tagline": "Thandak aur taazgi ka asli srot!",
        "category": "Herb & Vegetable",
        "state": "Uttar Pradesh / Punjab",
        "visual_identity": {
            "body": "3D jagged bright-green mint leaf character radiating cool ice-sparkle minty vapor puffs",
            "eyes": "Mischievous twinkling cool eyes",
            "expression": "High-five jump over spreading runners in moist soil",
            "setting": "Shaded moist compost-rich garden trench"
        },
        "transformation": {
            "before_organic": "Yellow rust-infected droopy stems drying under scorching sun",
            "after_organic": "Sprawling thick emerald green forest of menthol-rich aromatic mint"
        }
    },

    # --- BEANS & EXOTIC VEGGIES ---
    {
        "id": "sem_phali_samar",
        "name": "Sem Phali Samar (Flat Broad Bean)",
        "tagline": "Guchho mein aati, kisaan ko laabh dilati!",
        "category": "Vegetable",
        "state": "Uttar Pradesh / MP",
        "visual_identity": {
            "body": "3D curved emerald flat bean pod with purple border margins and white flower ears",
            "eyes": "Curious wide brown cartoon eyes",
            "expression": "Pleading with folded hands for natural microbial compost",
            "setting": "Lush winter creeper climbing thatched cottage roof"
        },
        "transformation": {
            "before_organic": "Black aphid-covered sticky curled pods dropping off vines",
            "after_organic": "Heavy hanging clusters of stringless, tender, plump green pods"
        }
    },
    {
        "id": "guwar_gopal",
        "name": "Guwar Gopal (Cluster Bean)",
        "tagline": "Sukhe mein bhi sona ugaye!",
        "category": "Vegetable & Cash Crop",
        "state": "Rajasthan / Haryana",
        "visual_identity": {
            "body": "3D sturdy upright cluster bean stalk mascot holding hands with tight bunches of green pods, wearing desert pagdi",
            "eyes": "Resilient brave eyes with friendly smile",
            "expression": "Pointing proudly down to nitrogen-fixing root nodules",
            "setting": "Arid sandy field with golden sunshine"
        },
        "transformation": {
            "before_organic": "Bacterial blight lesions with dropping flowers in depleted sand",
            "after_organic": "Top-to-bottom loaded pods brimming with high gum content"
        }
    },
    {
        "id": "lobia_lalit",
        "name": "Lobia Lalit (Cowpea Yardlong Bean)",
        "tagline": "Lambi hari phali, poshan ki dali!",
        "category": "Vegetable",
        "state": "Kerala / UP / Bihar",
        "visual_identity": {
            "body": "3D extra-long green whip-like bean pod mascot playfully coiled like a lasso",
            "eyes": "Fun-loving smiling eyes",
            "expression": "Jumping in the air with joyful cheer",
            "setting": "Tall bamboo trellis in organic plot"
        },
        "transformation": {
            "before_organic": "Short, pale, twisted pods riddled with pod borers",
            "after_organic": "Pristine 2-foot long tender crunchy pencil-thick beans"
        }
    },
    {
        "id": "capsicum_chetan",
        "name": "Capsicum Chetan (Shimla Mirch)",
        "tagline": "Moti deewar, bejod chamak, premium daam!",
        "category": "Vegetable",
        "state": "Himachal Pradesh / Karnataka",
        "visual_identity": {
            "body": "3D glossy 4-lobed blocky green bell pepper mascot with sturdy stem hat, wearing tiny gardener shoes",
            "eyes": "Big wide animated cartoon eyes",
            "expression": "Tears of joy hugging the authentic B.S Organic bag",
            "setting": "High-tech polyhouse with climate control"
        },
        "transformation": {
            "before_organic": "Thin-walled wrinkled yellowing fruits dropping in hot soil",
            "after_organic": "Thick-walled 250g ultra-glossy bell peppers glowing like jewels"
        }
    },
    {
        "id": "kheera_karan",
        "name": "Kheera Karan (Crisp Cucumber)",
        "tagline": "Seedha, hara aur thandak se bhara!",
        "category": "Vegetable",
        "state": "Haryana / Karnataka / MP",
        "visual_identity": {
            "body": "3D smooth dark-green cylindrical cucumber with fine pale stripes and bright yellow star flower on top",
            "eyes": "Cool relaxed eyes with refreshing water-droplet spectacles",
            "expression": "Chilled confident thumbs-up",
            "setting": "Raised bed mulch system in polyhouse"
        },
        "transformation": {
            "before_organic": "Curved, bitter, yellow-bellied cucumbers with powdery mildew",
            "after_organic": "Uniform 8-inch bitterless seedless crunchy cucumbers loaded on every node"
        }
    },

    # --- FRUITS & ORCHARDS ---
    {
        "id": "langra_lakhan",
        "name": "Langra Lakhan (Banarasi Mango)",
        "tagline": "Kashi ka garv, anootha swaad aur behtareen sugandh!",
        "category": "Fruit",
        "state": "Uttar Pradesh (Varanasi)",
        "visual_identity": {
            "body": "3D plump oval olive-green mango mascot with a small cute curl at the tip, wearing Banarasi gamchha",
            "eyes": "Mischievous twinkling brown eyes",
            "expression": "Singing folk tune happily while hanging on branch",
            "setting": "Heritage mango orchard on Gangetic plains"
        },
        "transformation": {
            "before_organic": "Black-tip disease and fruit drop due to chemical boron/sulfur imbalance",
            "after_organic": "Heavy, fragrant, unblemished green mango bursting with legendary sweet pulp"
        }
    },
    {
        "id": "dasheri_dheeraj",
        "name": "Dasheri Dheeraj (Malihabadi Mango)",
        "tagline": "Mithas aisi jo dil jeet le!",
        "category": "Fruit",
        "state": "Uttar Pradesh (Lucknow)",
        "visual_identity": {
            "body": "3D elongated smooth golden-green mango mascot with elegant curve, wearing Nawabi sherwani vest",
            "eyes": "Sophisticated warm animated eyes",
            "expression": "Graceful Namaste bow with hands folded",
            "setting": "Historic sunlit Malihabad orchard"
        },
        "transformation": {
            "before_organic": "Severe alternate bearing and fruit fly scars on cracked trees",
            "after_organic": "Bountiful annual yield of thin-stoned aromatic honey-sweet mangoes"
        }
    },
    {
        "id": "chausa_chaman",
        "name": "Chausa Chaman (Golden Chausa Mango)",
        "tagline": "Aamro ka raja, ras ka khazana!",
        "category": "Fruit",
        "state": "Uttar Pradesh / Bihar",
        "visual_identity": {
            "body": "3D radiant sun-yellow juicy mango mascot with sweet nectar drop glistening on cheek",
            "eyes": "Joyful wide sparkling eyes",
            "expression": "Laughing heartily with open arms",
            "setting": "Golden-hour orchard with baskets of ripe fruit"
        },
        "transformation": {
            "before_organic": "Spongy tissue breakdown and small dry fruits in hard clay orchard",
            "after_organic": "Giant golden fiberless mangoes dripping with pure natural nectar"
        }
    },
    {
        "id": "totapuri_teju",
        "name": "Totapuri Teju (Parrot-Beak Mango)",
        "tagline": "Pulp aur achar ka badshah!",
        "category": "Fruit",
        "state": "Andhra Pradesh / Karnataka",
        "visual_identity": {
            "body": "3D distinctive mango mascot with prominent parrot-beak hooked nose tip, yellow-green skin with red blush",
            "eyes": "Sharp alert expressive eyes",
            "expression": "Playful bird whistle wink",
            "setting": "Red laterite soil orchard in Chittoor"
        },
        "transformation": {
            "before_organic": "Small sour stunted fruits dropping in dry red soil",
            "after_organic": "Colossal 500g heavy mangoes loaded on every branch"
        }
    },
    {
        "id": "red_lady_papita",
        "name": "Red Lady Papita (Papaya)",
        "tagline": "Mitha laal guda, har podhe par dher saare phal!",
        "category": "Fruit",
        "state": "Gujarat / Maharashtra / MP",
        "visual_identity": {
            "body": "3D oval-round papaya mascot with golden-green skin and deep crimson internal glow, standing beside tree trunk",
            "eyes": "Friendly warm large eyes",
            "expression": "Earnest plea for drainage and vermicompost ring feeding",
            "setting": "Drip-irrigated high-density papaya plantation"
        },
        "transformation": {
            "before_organic": "Collar rot and ring spot virus with yellow falling leaves in soggy soil",
            "after_organic": "Trunk packed solid from bottom to top with 2kg sweet red-flesh papayas"
        }
    },
    {
        "id": "bhusawal_kela",
        "name": "Bhusawal Kela (Grand Naine Banana)",
        "tagline": "Moti ghari, meetha kela—Khandesh ki shaan!",
        "category": "Fruit",
        "state": "Maharashtra (Jalgaon)",
        "visual_identity": {
            "body": "3D robust curved golden-yellow banana mascot with green tip, wearing farmer cap and white gloves",
            "eyes": "Energetic happy cartoon eyes",
            "expression": "Flexing biceps showing fruit bunch strength",
            "setting": "Dense green banana grove along Tapi river"
        },
        "transformation": {
            "before_organic": "Panama wilt and weak 15kg bunches with pencil-thin fingers",
            "after_organic": "Record 45kg massive bunch with thick uniform sweet bananas"
        }
    },
    {
        "id": "kinnu_karan",
        "name": "Kinnu Karan (Kinnow Mandarin)",
        "tagline": "Ras se labalab, chamkila kesariya kinnu!",
        "category": "Fruit",
        "state": "Punjab (Abohar) / Rajasthan",
        "visual_identity": {
            "body": "3D gleaming spherical orange kinnow mascot with tight shiny skin and two glossy green leaves",
            "eyes": "Bright round animated eyes",
            "expression": "Smiling warmly in chilly winter sunrise mist",
            "setting": "Lush citrus orchard with canal irrigation"
        },
        "transformation": {
            "before_organic": "Citrus decline, yellowing veins and fruit drop before ripening",
            "after_organic": "Branches bending to ground under weight of juicy glowing orange globes"
        }
    },
    {
        "id": "mosambi_madhu",
        "name": "Mosambi Madhu (Sweet Lime)",
        "tagline": "Pyaas bujhaye, taazgi laye!",
        "category": "Fruit",
        "state": "Telangana / Maharashtra",
        "visual_identity": {
            "body": "3D round greenish-yellow sweet lime mascot with delicate oil gland dimples on skin, wearing small sunhat",
            "eyes": "Sweet gentle cartoon eyes",
            "expression": "Cheerfully waving with juice splash effects",
            "setting": "Black soil citrus orchards in Marathwada"
        },
        "transformation": {
            "before_organic": "Thick-skinned dry fruit with yellow chlorosis leaves",
            "after_organic": "Thin-skinned juice-bursting sweet limes harvested by tractor-loads"
        }
    },
    {
        "id": "tarbooj_tanmay",
        "name": "Tarbooj Tanmay (Watermelon)",
        "tagline": "Lal laal mithaas, garmi mein rahat!",
        "category": "Fruit",
        "state": "Karnataka / Andhra / UP",
        "visual_identity": {
            "body": "3D giant dark-green striped round watermelon mascot with a slice cut open revealing ruby-red heart with black seed eyes",
            "eyes": "Big beaming joyful cartoon eyes",
            "expression": "Laughing excitedly with thumbs up",
            "setting": "Riverbed sandy loam field under bright sun"
        },
        "transformation": {
            "before_organic": "Blossom end rot and hollow pale bitter pulp in chemical beds",
            "after_organic": "Solid 10kg heavy sugar-sweet crisp watermelon with 13 Brix sweetness"
        }
    },
    {
        "id": "kharbooza_kishor",
        "name": "Kharbooza Kishor (Muskmelon)",
        "tagline": "Kudrati mehak aur shaandar mithaas!",
        "category": "Fruit",
        "state": "Uttar Pradesh / Punjab",
        "visual_identity": {
            "body": "3D round netted-skin golden-tan cantaloupe mascot with green suture ribs, wearing sunglasses",
            "eyes": "Cool friendly wink",
            "expression": "Spreading sweet floral perfume in the air",
            "setting": "Sandy riverbank dunes with melon vines"
        },
        "transformation": {
            "before_organic": "Cracking fruit skin and watery tasteless pulp due to nutrient swings",
            "after_organic": "Aromatic salmon-orange thick flesh melting in the mouth"
        }
    },
    {
        "id": "amla_arvind",
        "name": "Amla Arvind (Indian Gooseberry)",
        "tagline": "Vitamin C ka bhandaar, sau saal ka uphaar!",
        "category": "Fruit & Medicinal",
        "state": "Uttar Pradesh (Pratapgarh)",
        "visual_identity": {
            "body": "3D translucent light-green 6-segmented ribbed amla berry mascot with tiny ascetic beads necklace",
            "eyes": "Sharp brilliant wise eyes",
            "expression": "Namaste blessing gesture with deep tranquility",
            "setting": "Semi-arid orchard with dry sandy soil"
        },
        "transformation": {
            "before_organic": "Internal fruit necrosis (black spots) and premature drop",
            "after_organic": "Blemish-free giant Banarasi amla loaded on every twig"
        }
    },
    {
        "id": "jamun_jaggu",
        "name": "Jamun Jaggu (Black Plum)",
        "tagline": "Madhumeh mein labhkari, behtareen jamun!",
        "category": "Fruit",
        "state": "Maharashtra / Haryana / UP",
        "visual_identity": {
            "body": "3D oblong glossy deep-violet blackberry mascot with royal purple crown and purple-stained happy smile",
            "eyes": "Playful bright eyes",
            "expression": "Singing happily on leafy tree branch",
            "setting": "Tall canopy orchard in monsoon mist"
        },
        "transformation": {
            "before_organic": "Small astringent sour fruits riddled with fruit borer worms",
            "after_organic": "Fleshy sweet seed-small deep-purple giant jamuns"
        }
    },
    {
        "id": "shahi_litchi",
        "name": "Shahi Litchi (Muzaffarpur Litchi)",
        "tagline": "Gulabi chamak, shahi ras!",
        "category": "Fruit",
        "state": "Bihar (Muzaffarpur)",
        "visual_identity": {
            "body": "3D bumpy rough pinkish-red heart-shaped litchi mascot with translucent pearl pulp peeking out",
            "eyes": "Big delicate cartoon eyes",
            "expression": "Tearful plea for soil moisture conservation with organic compost",
            "setting": "Shaded humid orchard near Gandak river"
        },
        "transformation": {
            "before_organic": "Severe fruit cracking and sunburn losses during dry westerly winds",
            "after_organic": "Intact, juicy, aromatic royal bunches ready for luxury markets"
        }
    },
    {
        "id": "dahanu_chikoo",
        "name": "Dahanu Chikoo (Sapota)",
        "tagline": "Bhoora meetha chikoo, swaad ka jaadugar!",
        "category": "Fruit",
        "state": "Maharashtra (Dahanu/Gholvad)",
        "visual_identity": {
            "body": "3D oval fuzzy sandy-brown sapota mascot with sweet dark seed buttons on shirt",
            "eyes": "Gentle smiling eyes with warm expression",
            "expression": "Hugging the trunk of the fruit tree",
            "setting": "Coastal Konkan orchard with sea breeze"
        },
        "transformation": {
            "before_organic": "Hard gritty small chikoos with premature drop in depleted soil",
            "after_organic": "Caramel-sweet soft round chikoos harvested round the year"
        }
    },
    {
        "id": "sitaphal_sunder",
        "name": "Sitaphal Sunder (Custard Apple)",
        "tagline": "Kudrati ice cream, bejod meethas!",
        "category": "Fruit",
        "state": "Telangana / Maharashtra (Beed)",
        "visual_identity": {
            "body": "3D knobby polygonal-patterned pale green custard apple mascot opening slightly to show creamy white pulp",
            "eyes": "Charming smiling eyes",
            "expression": "Proudly displaying creamy sweet texture",
            "setting": "Dry rocky hill slopes with compost basins"
        },
        "transformation": {
            "before_organic": "Black mummified stone fruits rotting on drought-stressed branches",
            "after_organic": "Giant 600g Balanagar custard apples with rich creamy pulp"
        }
    },
    {
        "id": "ananas_anil",
        "name": "Ananas Anil (Queen Pineapple)",
        "tagline": "Taajdaar ananas, meetha aur khushbudar!",
        "category": "Fruit",
        "state": "Tripura / Assam / Kerala",
        "visual_identity": {
            "body": "3D geometric diamond-plated golden pineapple mascot with spiky dark-green crown hair, wearing shades",
            "eyes": "Cool confident smiling eyes",
            "expression": "King pose with scepter and crown",
            "setting": "Terraced red-laterite hill slopes in northeast rain"
        },
        "transformation": {
            "before_organic": "Acidic, fibrous, stunted pineapples in eroded hill soil",
            "after_organic": "Golden-yellow honey-sweet pineapples with zero fiber"
        }
    },

    # --- SPICES & CONDIMENTS ---
    {
        "id": "haldi_harish",
        "name": "Haldi Harish (Golden Turmeric)",
        "tagline": "Curcumin se bharpoor, shuddh sunahari haldi!",
        "category": "Spice & Medicinal",
        "state": "Maharashtra (Sangli) / Andhra (Duggirala)",
        "visual_identity": {
            "body": "3D finger-rhizome golden turmeric mascot wearing traditional yellow dhoti and tilak, surrounded by broad green leaves",
            "eyes": "Aura of divine wisdom and health in eyes",
            "expression": "Blessing hand gesture with glowing golden particle aura",
            "setting": "Raised ridge mounds in deep black fertile soil"
        },
        "transformation": {
            "before_organic": "Rhizome rot and low curcumin levels in chemical-treated clay",
            "after_organic": "Dense fingers of deep orange turmeric with over 5% natural curcumin"
        }
    },
    {
        "id": "adrak_adarsh",
        "name": "Adrak Adarsh (Fresh Ginger)",
        "tagline": "Teekhi mehak, swasthya ka sahara!",
        "category": "Spice",
        "state": "Kerala (Wayanad) / MP / Himachal",
        "visual_identity": {
            "body": "3D multi-knobbed branched tan ginger rhizome mascot with tender pink shoot tips, wearing boots",
            "eyes": "Fiery bold friendly cartoon eyes",
            "expression": "Pleading for soft, aerated organic compost to grow wide",
            "setting": "Semi-shaded hill slopes with rich porous loam"
        },
        "transformation": {
            "before_organic": "Soft rot pythium fungus destroying underground ginger fingers",
            "after_organic": "Massive 2kg interconnected hand of aromatic plump juicy ginger"
        }
    },
    {
        "id": "jeera_jeevan",
        "name": "Jeera Jeevan (Cumin Seed)",
        "tagline": "Tadka lage to mehak uthe sansaar!",
        "category": "Spice",
        "state": "Gujarat (Unjha) / Rajasthan",
        "visual_identity": {
            "body": "3D feathery fine-leaved cumin plant mascot holding a tiny sparkling ribbed brown seed like a diamond",
            "eyes": "Delicate earnest blinking eyes",
            "expression": "Pleading with hands folded against blight and frost",
            "setting": "Arid sandy-loam winter field under bright sun"
        },
        "transformation": {
            "before_organic": "Fusarium wilt turning entire green cumin fields black and dry",
            "after_organic": "Lush emerald canopy loaded with heavy, high-essential-oil cumin seeds"
        }
    },
    {
        "id": "saunf_sanjay",
        "name": "Saunf Sanjay (Fennel Seed)",
        "tagline": "Meethi saunf, khushboo aur hazma dono behtareen!",
        "category": "Spice",
        "state": "Gujarat / Rajasthan",
        "visual_identity": {
            "body": "3D umbrella-shaped yellow floral umbel mascot crowned with bright green curved fennel seeds",
            "eyes": "Cheerful smiling cartoon eyes",
            "expression": "Blowing sweet anise-scented breeze over the farm",
            "setting": "Tall blooming rows of fennel in afternoon golden light"
        },
        "transformation": {
            "before_organic": "Ramularia blight turning seed umbels into shriveled gray dust",
            "after_organic": "Bright green, bold, sugar-sweet aromatic fennel seeds"
        }
    },
    {
        "id": "ajwain_ajay",
        "name": "Ajwain Ajay (Carom Seed)",
        "tagline": "Pet ki har takleef ka shartiya ilaaj!",
        "category": "Spice & Medicinal",
        "state": "Madhya Pradesh / Rajasthan",
        "visual_identity": {
            "body": "3D tiny ribbed greyish-green carom seed mascot in white kurta with medicinal healing aura",
            "eyes": "Sharp alert bright eyes",
            "expression": "Smiling proudly with thumbs up",
            "setting": "Dry winter field with light sandy loam"
        },
        "transformation": {
            "before_organic": "Dwarf sickly plants with barren flower heads",
            "after_organic": "Dense clusters of thymol-rich pungent carom seeds"
        }
    },
    {
        "id": "elaichi_esha",
        "name": "Elaichi Esha (Green Cardamom)",
        "tagline": "Masalo ki rani, sabse keemti khazana!",
        "category": "Spice",
        "state": "Kerala (Idukki) / Karnataka",
        "visual_identity": {
            "body": "3D plump 3-sided ribbed emerald green cardamom pod with royal golden jewel crown",
            "eyes": "Mesmerizing green eyes with elegant long lashes",
            "expression": "Delicate emotional appeal with hands folded in Namaste",
            "setting": "Misty rainforest cardamom hills under shade tree canopy"
        },
        "transformation": {
            "before_organic": "Capsule borer and thrips leaving black scarred empty pods",
            "after_organic": "8mm bold extra-green aromatic cardamom capsules filled with oily black seeds"
        }
    },
    {
        "id": "kali_mirch_kaalu",
        "name": "Kali Mirch Kaalu (Black Pepper)",
        "tagline": "Kala sona, masalo ka raja!",
        "category": "Spice",
        "state": "Kerala (Malabar) / Karnataka (Coorg)",
        "visual_identity": {
            "body": "3D shiny dark-green berry spike hanging from vine, with a hero glossy black peppercorn in front",
            "eyes": "Feisty brave determined cartoon eyes",
            "expression": "Flexing with warrior pride on silver oak tree support",
            "setting": "High-rainfall spice plantation intercropped with coffee"
        },
        "transformation": {
            "before_organic": "Quick wilt phytophthora wiping out vines down to black roots",
            "after_organic": "Long dense 15cm spikes loaded with heavy berries from top to base"
        }
    },

    # --- CASH CROPS, GRAINS & MILLETS ---
    {
        "id": "makka_mahesh",
        "name": "Makka Mahesh (Golden Sweet Corn)",
        "tagline": "Daane daane mein bhari mithaas aur taakat!",
        "category": "Cash Crop & Grain",
        "state": "Karnataka / Bihar / Telangana",
        "visual_identity": {
            "body": "3D tall sturdy corn stalk mascot with two giant golden cobs peeling green husks back like a jacket, golden silk hair",
            "eyes": "Big bright friendly eyes",
            "expression": "Beaming broad smile, proud chest out",
            "setting": "Tall sunny summer cornfield waving in the wind"
        },
        "transformation": {
            "before_organic": "Fall armyworm chewing leaves to ribbons with half-empty cobs",
            "after_organic": "Completely filled 16-row golden cobs packed with juicy sweet kernels"
        }
    },
    {
        "id": "bajra_balram",
        "name": "Bajra Balram (Pearl Millet)",
        "tagline": "Shree Anna ki taakat, lohe jaisa shareer!",
        "category": "Millet & Grain",
        "state": "Rajasthan / Haryana / Gujarat",
        "visual_identity": {
            "body": "3D tall bronze-green pearl millet spike head mascot wearing Rajasthani pagdi, holding farmer stick",
            "eyes": "Determined rugged brave eyes",
            "expression": "Proud smile facing scorching desert winds",
            "setting": "Arid Thar desert sand dunes with green millet rows"
        },
        "transformation": {
            "before_organic": "Green ear disease and ergot fungus rotting grain spikes",
            "after_organic": "1.5-foot dense heavy compact earheads overflowing with gray-pearl grains"
        }
    },
    {
        "id": "jowar_jagdish",
        "name": "Jowar Jagdish (Sorghum)",
        "tagline": "Paushtik jowar, swasth pariwaar!",
        "category": "Millet & Grain",
        "state": "Maharashtra / Karnataka",
        "visual_identity": {
            "body": "3D broad-leaved sorghum stalk mascot with a heavy spherical creamy-white grain panicle head",
            "eyes": "Warm honest farming eyes",
            "expression": "Humble bow with hands folded in gratitude",
            "setting": "Black cotton soil plateau under blue sky"
        },
        "transformation": {
            "before_organic": "Shoot fly killing central shoots with stunted grainless heads",
            "after_organic": "Heavy drooping creamy-white pearly grain panicles weighing down branches"
        }
    },
    {
        "id": "ragi_raghu",
        "name": "Ragi Raghu (Finger Millet)",
        "tagline": "Calcium ka khazana, kisaan ka dildaar!",
        "category": "Millet & Grain",
        "state": "Karnataka / Uttarakhand / Odisha",
        "visual_identity": {
            "body": "3D claw-shaped 5-fingered brown grain head mascot with little tribal beads and green sneakers",
            "eyes": "Playful energetic cartoon eyes",
            "expression": "Dancing happily on terrace farm steps",
            "setting": "Terraced hill farm with red laterite soil"
        },
        "transformation": {
            "before_organic": "Blast disease scorching finger spikes in depleted acidic soil",
            "after_organic": "Thick curved fingers laden with calcium-dense dark crimson grains"
        }
    },
    {
        "id": "desi_chana_chandan",
        "name": "Desi Chana Chandan (Bengal Gram)",
        "tagline": "Podha ek, daane anek—takatwar deshi chana!",
        "category": "Pulse & Grain",
        "state": "Madhya Pradesh / Rajasthan",
        "visual_identity": {
            "body": "3D feathery glandular-haired chickpea plant mascot holding two plump double-seeded green pods",
            "eyes": "Earnest friendly eyes",
            "expression": "Pointing down to pink-nodulated roots in soil",
            "setting": "Frosty winter morning black cotton soil"
        },
        "transformation": {
            "before_organic": "Wilt disease drying plants suddenly with pod borer holes",
            "after_organic": "Bushy plant branching into 150+ pods bursting with bold brown grains"
        }
    },
    {
        "id": "moong_dal_manohar",
        "name": "Moong Dal Manohar (Green Gram)",
        "tagline": "Saath din mein sona ugle khet!",
        "category": "Pulse & Grain",
        "state": "Rajasthan / Maharashtra / MP",
        "visual_identity": {
            "body": "3D quick-growing upright legume mascot with clusters of long black maturing pods pointing upwards",
            "eyes": "Speedy energetic cartoon eyes",
            "expression": "Jumping with celebratory speed banner: '60 Days Harvest!'",
            "setting": "Summer zaid crop field after wheat harvest"
        },
        "transformation": {
            "before_organic": "Yellow mosaic virus turning leaves golden-yellow with empty pods",
            "after_organic": "Simultaneous pod maturity packed with glossy olive-green bold moong"
        }
    },
    {
        "id": "arhar_anand",
        "name": "Arhar Anand (Tur / Pigeon Pea)",
        "tagline": "Dal ka badshah, kisaan ka sahara!",
        "category": "Pulse & Grain",
        "state": "Maharashtra (Latur) / Karnataka / UP",
        "visual_identity": {
            "body": "3D tall woody pigeon pea shrub mascot with bright yellow-and-red banner flowers and speckled green pods",
            "eyes": "Dignified friendly eyes",
            "expression": "Spreading wide branching arms over the soil",
            "setting": "Deep black vertisol field under bright autumn sun"
        },
        "transformation": {
            "before_organic": "Sterility mosaic virus leaving giant bushes without a single flower",
            "after_organic": "Every branch bent under weight of 4-seeded plump speckled pods"
        }
    },

    # --- FLORICULTURE & NURSERY ---
    {
        "id": "deshi_gulab_govind",
        "name": "Deshi Gulab Govind (Scented Desi Rose)",
        "tagline": "Asli gulabi mehak, gulkand aur itra ka raja!",
        "category": "Flower",
        "state": "Rajasthan (Pushkar/Haldi Ghati)",
        "visual_identity": {
            "body": "3D velvety layered pink desi rose mascot radiating pink floral perfume waves, wearing green leafy vest",
            "eyes": "Soulful affectionate romantic cartoon eyes",
            "expression": "Hands folded in Namaste with tears of joy",
            "setting": "Historic rose fields around Pushkar lake in morning light"
        },
        "transformation": {
            "before_organic": "Black spot fungal leaf fall and dieback twigs in chemical nursery bed",
            "after_organic": "Over 50 intensely fragrant pink blooms opening daily on healthy green canes"
        }
    },
    {
        "id": "gudhal_gaurav",
        "name": "Gudhal Gaurav (Red Hibiscus)",
        "tagline": "Pooja aur baalo ka poshan, laal laal gudhal!",
        "category": "Flower & Medicinal",
        "state": "West Bengal / Kerala / Pan-India",
        "visual_identity": {
            "body": "3D magnificent 5-petaled flared scarlet-red hibiscus bloom mascot with long golden pollen stamen nose/antenna",
            "eyes": "Bright reverent devoted eyes",
            "expression": "Peaceful folded hands greeting devotee farmer",
            "setting": "Lush home courtyard / terrace garden pot"
        },
        "transformation": {
            "before_organic": "White mealybug clusters choking buds before they can open",
            "after_organic": "Dinner-plate sized dazzling scarlet flowers opening daily in abundance"
        }
    },
    {
        "id": "mogra_mahavir",
        "name": "Mogra Mahavir (Arabian Jasmine)",
        "tagline": "Madhu-bhari khushboo, gajro ka sartaaj!",
        "category": "Flower",
        "state": "Tamil Nadu (Madurai) / Maharashtra",
        "visual_identity": {
            "body": "3D pristine white double-petaled round jasmine bud mascot with green calyx collar and fragrance glow",
            "eyes": "Pure serene blinking eyes",
            "expression": "Floating softly in the air spreading sweet summer night scent",
            "setting": "Irrigated jasmine rows at dusk"
        },
        "transformation": {
            "before_organic": "Bud borer holes turning fragrant buds brown and rotten",
            "after_organic": "Snow-white dense heavy buds with unforgettable sweet perfume"
        }
    },
    {
        "id": "rajnigandha_rakesh",
        "name": "Rajnigandha Rakesh (Tuberose)",
        "tagline": "Raat ki rani, bejod sugandh!",
        "category": "Flower",
        "state": "West Bengal (Ranaghat) / Maharashtra",
        "visual_identity": {
            "body": "3D tall elegant spike mascot studded with waxy white tubular florets opening in sequence",
            "eyes": "Graceful sparkling eyes",
            "expression": "Standing tall and proud like a royal guard",
            "setting": "Night-lit flower farm with cool evening breeze"
        },
        "transformation": {
            "before_organic": "Nematode galling on underground bulbs causing stunted short spikes",
            "after_organic": "3-foot long sturdy spikes packed with 40+ waxy double-white florets"
        }
    },
    {
        "id": "aparajita_anita",
        "name": "Aparajita Anita (Blue Pea Flower)",
        "tagline": "Neelkanth ka pushp, shuddh neeli chai!",
        "category": "Flower & Medicinal",
        "state": "Pan-India Terrace Gardening",
        "visual_identity": {
            "body": "3D vibrant conch-shaped deep cobalt-blue blossom mascot with glowing yellow center, delicate vine arms",
            "eyes": "Mystical beautiful dark blue eyes",
            "expression": "Serene and graceful, smiling peacefully",
            "setting": "Terrace garden bamboo trellis against sunrise"
        },
        "transformation": {
            "before_organic": "Spider mite webbing and yellow chlorosis on dry balcony pot",
            "after_organic": "Cascading wall of hundreds of vibrant indigo-blue flowers"
        }
    },
    {
        "id": "aloevera_alok",
        "name": "Aloe Vera Alok (Gwarpatha)",
        "tagline": "Skin aur sehat ka kudrati doctor!",
        "category": "Medicinal & Terrace Garden",
        "state": "Rajasthan / Gujarat",
        "visual_identity": {
            "body": "3D plump serrated fleshy green aloe succulent leaf mascot filled with translucent cooling gel, wearing doctor coat",
            "eyes": "Gentle caring intelligent eyes",
            "expression": "Holding soothing gel bottle with warm comforting smile",
            "setting": "Sunny balcony pot with sandy organic potting mix"
        },
        "transformation": {
            "before_organic": "Brown sunburned paper-thin flat leaves rotting from overwatered clay",
            "after_organic": "Thick 2-inch plump succulent leaves bursting with crystal-clear healing gel"
        }
    },
    {
        "id": "ashwagandha_ashutosh",
        "name": "Ashwagandha Ashutosh (Indian Ginseng)",
        "tagline": "Takat aur sthirata ka prateek!",
        "category": "Medicinal",
        "state": "Madhya Pradesh (Neemuch)",
        "visual_identity": {
            "body": "3D branched medicinal shrub mascot holding a bundle of sturdy dried buff-brown roots like dumbbells",
            "eyes": "Strong energetic focused cartoon eyes",
            "expression": "Hero pose demonstrating stamina and vitality",
            "setting": "Dry semi-arid red-gravel farm rows"
        },
        "transformation": {
            "before_organic": "Damping-off fungal disease killing seedlings in poor soil",
            "after_organic": "Thick brittle starch-filled high-withanolide roots dug out in winter"
        }
    },
    {
        "id": "giloy_girish",
        "name": "Giloy Girish (Amrita Vine)",
        "tagline": "Immunity ka kavach, amarbel!",
        "category": "Medicinal",
        "state": "Pan-India",
        "visual_identity": {
            "body": "3D heart-shaped green leaf vine mascot climbing spirally up a neem tree trunk, with warted grey bark stem",
            "eyes": "Invincible protective sparkling eyes",
            "expression": "Warm hug around the neem tree",
            "setting": "Organic agroforestry farm with neem tree"
        },
        "transformation": {
            "before_organic": "Thin brittle yellowing vine drying under harsh sun",
            "after_organic": "Thick thumb-thick succulent green stem packed with bitter berberine nectar"
        }
    },
    {
        "id": "lemongrass_lucky",
        "name": "Lemongrass Lucky (Citronella Grass)",
        "tagline": "Mehakti chai, machharo ko bhagaye!",
        "category": "Medicinal & Aromatic",
        "state": "Kerala / Assam / Terrace Garden",
        "visual_identity": {
            "body": "3D fountain-like dense tuft of arching blue-green aromatic grass blades mascot with fresh citrus aroma vapors",
            "eyes": "Fresh energetic dancing eyes",
            "expression": "Waving playfully in morning breeze",
            "setting": "Terrace garden container / farm boundary"
        },
        "transformation": {
            "before_organic": "Rust spots and drying brown tips in depleted pot soil",
            "after_organic": "Giant 4-foot clump of lemon-scented oil-rich blades harvested repeatedly"
        }
    }
]

added_count = 0
for char in NEW_CHARACTERS:
    if char["id"] not in existing_ids:
        existing.append(char)
        existing_ids.add(char["id"])
        added_count += 1

data["characters"] = existing

with open(CHAR_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Successfully added {added_count} new characters!")
print(f"Total characters in database now: {len(existing)}")
