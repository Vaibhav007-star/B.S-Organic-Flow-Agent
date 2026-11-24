"""Canonical Master Seeder for B.S Organic Characters Database.
Consolidates all 132 agricultural and horticultural mascots into a single source.
Can inspect, validate, or re-seed characters.json at any time.
"""

import json
from pathlib import Path

CHAR_FILE = Path(__file__).parent / "characters.json"

MASTER_DATA = {
  "brand": "B.S Organic",
  "default_style": "High-end 3D animated Pixar-DreamWorks aesthetic, Octane 3D render, subsurface scattering, tactile organic textures, vertical 9:16 aspect ratio, warm cinematic sunlight, shallow depth of field, 8K resolution",
  "negative_prompt": "no text, no captions, no logos, no watermark, no human face, no 2D flat drawing, no grotesque realism, no low poly, no deformed eyes",
  "characters": [
    {
      "id": "captain_wiggly",
      "name": "Captain Wiggly (Kenchua Bro)",
      "tagline": "The Soil Super-Chef & Organic Vermicompost Mascot",
      "state": "Pan-India (Universal)",
      "category": "Hero Mascot",
      "visual_identity": {
        "species": "Red Wiggler Earthworm (Eisenia fetida)",
        "body": "Cute, glossy reddish-pink segmented worm body with a velvety pearlescent sheen, big expressive sparkling cartoon eyes, joyful warm smile",
        "clothing": "Miniature burlap farmer hat tilted on head, tiny emerald-green gardener bandana tied neatly around neck",
        "props": "Holds a tiny golden gardening trowel in hand",
        "setting": "Perched playfully atop a mound of steaming, nutrient-dense crumbly dark brown vermicompost surrounded by green sprout shoots"
      },
      "transformation": {
        "before_organic": "Lethargic, hiding deep under hard cracked grey clay soil with zero moisture",
        "after_organic": "Energetic, glowing with vitality, aerating loose spongy black loam soil with a sparkling organic aura"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated Pixar character portrait of Captain Wiggly, an adorable friendly red-wiggler earthworm. Glossy segmented reddish-pink body with subtle subsurface scattering, large expressive sparkling hazel eyes, warm cheerful smile. Wearing a tiny textured burlap sunhat and an emerald-green gardener neck scarf, holding a miniature polished golden trowel. Sitting proudly atop a rich mound of moist, dark brown crumbly vermicompost teeming with tiny green sprouts and soft golden morning rim lighting. Organic garden farm background with soft cinematic bokeh. Hyper-detailed 3D render, Octane lighting, tactile organic textures, 8k quality, no text, no watermark, no captions.",
      "video_prompt_hook_8s": "Vertical 9:16, 3D animated macro cinema: Captain Wiggly the adorable pink earthworm wearing a tiny burlap hat pops out of moist dark crumbly vermicompost with an energetic wave, blinking happily. Key light illuminates rich soil texture. Close-mic ASMR soft earthy rustle and cheerful chime. No text, no logos."
    },
    {
      "id": "bs_organic_gold",
      "name": "B.S. Organic Vermicompost Bag (Official)",
      "tagline": "Pure 100% Chemical-Free Neem & Cow-Urine Enriched Vermicompost",
      "state": "Pan-India (Universal)",
      "category": "Hero Product",
      "reference_image": "assets/bs_organic_bag_reference.jpg",
      "visual_identity": {
        "packaging": "Glossy forest-green woven polypropylene agricultural sack tied tightly at the top with white string, covered in scattered white and light-green leaf silhouettes, with a vertical white strip on the left border reading 'B.S. Organic VERMICOMPOST'",
        "front_branding": "Large central white cloud-shaped logo with bold dark-green text 'B.S. Organic' and a green leaf icon, top-right '100% CHEMICAL FREE ✓' mark, horizontal white Hindi banner 'केंचुओ द्वारा निर्मित प्राकृतिक खाद', bold white text 'VERMICOMPOST', Hindi tagline 'प्रकृति के लिए प्राकृतिक', and bottom circular speech bubble 'नीम व गाय मूत्र युक्त'",
        "content": "Rich, velvety dark-black crumbly vermicompost resembling moist dark coffee grounds, teeming with golden microbiological nutrients and airy earthworm castings",
        "setting": "Lush fertile Indian farmland in golden-hour sunlight, standing proudly on rich dark brown loamy soil"
      },
      "transformation": {
        "before_organic": "Dead, grey, cracked compacted chemical dirt blocks, barren and dusty",
        "after_organic": "Instant transformation into porous, moisture-retaining, dark spongy black loam teeming with beneficial microbes"
      },
      "image_prompt_9_16": "Vertical 9:16, photoreal premium agriculture commercial hero shot: The official B.S. Organic vermicompost bag (exact reference: dark-green glossy woven poly sack tied at top with white string, scattered leaf silhouettes, central white cloud logo reading 'B.S. Organic' with leaf icon, '100% CHEMICAL FREE ✓' mark, white Hindi banner 'केंचुओ द्वारा निर्मित प्राकृतिक खाद', bold white 'VERMICOMPOST', and round badge 'नीम व गाय मूत्र युक्त'). Standing proudly on rich, moist dark-brown crumbly vermicompost soil in an Indian farm field. Macro slow-motion of dark fluffy organic compost spilling softly beside the bag with golden sunlight god-rays and sparkling nutrient particles. Hyper-realistic 8K commercial photography, shallow depth of field, no text, no watermark, no captions.",
      "video_prompt_hook_8s": "Vertical 9:16, slow-motion commercial hero reveal: 180-degree smooth orbit around the official dark-green glossy B.S. Organic vermicompost bag standing on dark loamy soil. Golden-hour sunlight creates warm lens flare and glowing nutrient sparkles around the bag as dark crumbly compost spills softly onto the earth. ASMR soft compost cascade whoosh and gentle acoustic folk chord. No people, no hands, no watermark."
    },
    {
      "id": "tommy_tomato",
      "name": "Tommy Tomato",
      "tagline": "From Wilting Vine to Juicy Ruby Giant",
      "state": "Pan-India / Terrace & Kitchen Garden",
      "category": "Vegetable",
      "visual_identity": {
        "body": "Chubby, perfectly round 3D animated tomato character with glossy ruby-red skin, bright cheerful cartoon eyes, and a cute leaf calyx crown for hair",
        "colors": [
          "Vibrant Crimson Red",
          "Emerald Leaf Green",
          "Glistening Dew Gold"
        ],
        "props": "Clusters of baby tomato friends peeking from vines behind him",
        "setting": "Lush home terrace kitchen garden wooden planter box filled with dark vermicompost"
      },
      "transformation": {
        "before_organic": "Small, dull orange-yellow skin with wrinkles, droopy leaf crown, sad frown in cracked dry grey chemical soil",
        "after_organic": "Giant, plump, mirror-gloss ruby red, laughing cheerfully on sturdy emerald vine heavy with ripe fruit clusters"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated Pixar character portrait of Tommy Tomato. Plump, perfectly round tomato character with mirror-gloss deep ruby-red skin and glistening natural dew drops. Adorable big expressive cartoon eyes and a proud joyful smile, with a spiky fresh emerald-green leafy calyx haircut. Standing happily in a terrace wooden garden planter bed filled with rich, moist dark brown vermicompost. Lush green tomato vines with glowing yellow blossoms in the blurred background. Warm golden hour rim lighting, tactile fruit texture, 8k render, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, 3D animated time-lapse: Sad pale droopy Tommy Tomato sits in dry cracked dirt. Suddenly dark B.S Organic vermicompost feeds his base. Water and nutrients surge up the stem; Tommy swells rapidly, skin turns incandescent ruby red with a cheerful gasp! ASMR soil drink and crisp leaf pop. No text, no captions."
    },
    {
      "id": "chintu_carrot",
      "name": "Chintu Carrot",
      "tagline": "The Deep-Rooting Soil Explorer",
      "state": "Punjab & Haryana & Rajasthan",
      "category": "Vegetable",
      "visual_identity": {
        "body": "Cute elongated tapering cartoon carrot character with vivid neon-orange skin, soft horizontal root ridges, big curious eyes and a bushy emerald feather top-knot",
        "colors": [
          "Sunburst Vivid Orange",
          "Forest Green Leaf Crown",
          "Dark Brown Earth"
        ],
        "props": "Pair of tiny gardening goggles pushed up on his forehead",
        "setting": "Deep organic raised farm bed with loose, fluffy vermicompost-enriched soil"
      },
      "transformation": {
        "before_organic": "Short, twisted, stunted root blocked by hard clay rocks, struggling with pale yellowish foliage",
        "after_organic": "Straight, thick, crunchy, ultra-sweet vibrant orange taproot extending effortlessly 30cm deep into airy black soil"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated character portrait of Chintu Carrot, an adorable cartoon carrot character. Thick, tapered vibrant neon-orange root body with natural micro-ridges, cheerful big sparkling black eyes and friendly grin. Pushed-up miniature brass pilot goggles on his forehead and a tall, feathery emerald-green leaf tuft. Peeking halfway out of deep, loose, spongy dark brown organic vermicompost soil. Sunlight glints off moist soil granules, soft garden atmosphere, 3D Octane render, Pixar quality, 8k resolution, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, split underground macro view: Chintu Carrot wriggles his root effortlessly down through fluffy dark vermicompost, humming with joy as roots branch out like golden threads. He pops his head out of the soil with a cheerful wink! ASMR soft soil crunch and underground pop. No text, no watermark."
    },
    {
      "id": "chilli_chacha",
      "name": "Chilli Chacha",
      "tagline": "The Fiery Spicy Organic Protector",
      "state": "Andhra Pradesh & Telangana & Gujarat",
      "category": "Vegetable",
      "visual_identity": {
        "body": "Slim, dynamic, curved hot pepper character, half fiery glossy red and half crisp emerald green, wearing a twirly curved stem like an elegant handlebar mustache",
        "colors": [
          "Fiery Gloss Crimson",
          "Glossy Lime Green",
          "Earthy Black Loam"
        ],
        "props": "Tiny flaming aura or spicy spark hovering above his stem tip",
        "setting": "Organic vegetable patch under bright sunny sky"
      },
      "transformation": {
        "before_organic": "Wilted pale green pepper, curled leaves from pest attack, dull matte skin",
        "after_organic": "Standing upright with glossy mirror shine, fiery natural pest resistance, loaded with heavy spicy pepper bunches"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated Pixar character portrait of Chilli Chacha, a charismatic hot pepper character. Sleek curved body with deep glossy fire-engine red skin transitioning into crisp emerald green at the stem. Big lively cartoon eyes with a confident playful wink, and a stem curved like an energetic swirl. Standing tall on a sturdy plant branch rooted in rich black vermicompost earth. Warm dramatic side lighting, photorealistic skin sheen, 8k Octane 3D render, no text, no captions.",
      "video_prompt_hook_8s": "Vertical 9:16, high-energy 3D animation: Chilli Chacha flexes on his vine, absorbing rich vermicompost nutrients. His skin turns glossy fiery red with a sizzle sound, sending out tiny golden organic protection rings that keep pests away! ASMR snappy crunch and crackle. No text, no logos."
    },
    {
      "id": "potato_pandu",
      "name": "Potato Pandu",
      "tagline": "The Underground Multiplier",
      "state": "Uttar Pradesh & West Bengal & Punjab",
      "category": "Vegetable",
      "visual_identity": {
        "body": "Chubby, lovable golden-brown potato character with cute dimples, sleepy friendly smile, and gentle rosy cheeks",
        "colors": [
          "Warm Russet Gold",
          "Velvety Dark Soil Brown",
          "Pale Green Sproutlet"
        ],
        "props": "Surrounded by a cuddly cluster of baby potato tubers underground",
        "setting": "Underground cross-section in moist, aerated dark vermicompost loam"
      },
      "transformation": {
        "before_organic": "Single rock-hard, scabby tuber trapped in dense compacted yellow clay",
        "after_organic": "A thriving family of smooth, flawless, golden organic tubers multiplying comfortably in loose crumbly black soil"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated underground cross-section portrait of Potato Pandu. Chubby, adorable golden-russet potato character with gentle smiling eyes, rosy cartoon cheeks, and tiny rootlet hands. Snuggled cozily inside soft, porous dark brown vermicompost soil surrounded by five glowing baby potato tubers. Soft warm underground lighting highlighting the airy, worm-aerated texture of the soil. Pixar cinematic style, subsurface light scattering, 8k resolution, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, underground macro view: In soft dark B.S Organic vermicompost, Potato Pandu chuckles warmly as tiny root runners rapidly sprout into a dozen smooth golden baby potatoes around him. ASMR soft earthen shift and bubbling pop. No text, no captions."
    },
    {
      "id": "nashik_pyaz",
      "name": "Nashik Lal Pyaz (Ruby Onion)",
      "tagline": "The Multi-Layered Kitchen Champion",
      "state": "Maharashtra",
      "category": "Vegetable",
      "visual_identity": {
        "body": "Sturdy, tear-drop bulb character with glistening layers of vibrant magenta-purple papery skin, proud cheerful smile, and sprightly green shoots for a top crown",
        "colors": [
          "Vivid Magenta Purple",
          "Crisp Spring Green",
          "Dark Loam Black"
        ],
        "props": "Glistening silver rootlet beard anchored firmly in dark compost",
        "setting": "Sunny Maharashtra farm field with raised beds enriched with B.S Organic vermicompost"
      },
      "transformation": {
        "before_organic": "Soft, rot-prone yellowing bulb suffering from fungal root decay in hard chemical soil",
        "after_organic": "Dense, crisp, oversized purple-red bulb with tight shiny skin and thick sweet rings"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated Pixar character portrait of Nashik Lal Pyaz, a plump, proud red onion character. Rich glossy magenta-purple outer papery skin with translucent onion layers, big sparkling eyes, and a confident wide smile. A spray of healthy tubular green onion stalks sprouting straight up from the top. Sitting firmly half-buried in moist, spongy black organic vermicompost with healthy white root hairs drinking nutrients. Sunny morning field lighting, 8k Octane 3D render, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, macro time-lapse: Nashik Lal Pyaz drinks from the dark vermicompost bed. His papery skin tightens into radiant purple-red silk with a crisp papery rustle, swelling to double its size! ASMR crisp onion peel rustle and satisfying earth thud. No text, no logos."
    },
    {
      "id": "malwa_lahsun",
      "name": "Malwa Lahsun (Pearl Garlic)",
      "tagline": "The Natural Immunity & Pest Shield",
      "state": "Madhya Pradesh & Rajasthan",
      "category": "Vegetable",
      "visual_identity": {
        "body": "Chubby, bulbous garlic bulb character composed of tightly hugged gleaming pearl-white cloves, wearing a small scholar's glasses and a wise cheerful smile",
        "colors": [
          "Pearl Ivory White",
          "Silvery Sheen",
          "Dark Charcoal Soil"
        ],
        "props": "Radiates a soft natural antiseptic aroma bubble",
        "setting": "Fertile raised garden bed in Malwa region"
      },
      "transformation": {
        "before_organic": "Single puny bulb with loose cloves and yellowing leaf tips",
        "after_organic": "Giant, tight, heavy bulb packed with 12 fat cloves bursting with sharp organic pungency"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated character portrait of Malwa Lahsun, an adorable pearl-white garlic bulb character. Tight, glistening white cloves with delicate papery translucent violet streaks, wearing cute round wireframe glasses and a wise beaming smile. Green shoots rising from the apex. Resting atop dark, airy vermicompost soil with morning dew drops on surrounding leaves. Soft volumetric sunlight, 8k Octane render, Pixar quality, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, 3D animation: Malwa Lahsun taps his root into deep black B.S Organic soil. A protective aromatic ring pulses out, gently waving away pests while the bulb swells into massive pearly cloves! ASMR crisp bulb snap and morning bell chime. No text, no captions."
    },
    {
      "id": "palak_rani",
      "name": "Palak Rani (Velvet Spinach)",
      "tagline": "The Iron-Rich Green Queen",
      "state": "Pan-India / Kitchen & Terrace Garden",
      "category": "Vegetable",
      "visual_identity": {
        "body": "Graceful leafy character formed from lush, broad, crinkled emerald-green spinach leaves, sparkling with dew drops, gentle welcoming smile and leafy tiara",
        "colors": [
          "Deep Emerald Green",
          "Crisp Mint Green",
          "Moist Black Loam"
        ],
        "props": "Holds a miniature organic watering can",
        "setting": "Terrace pot or balcony planter filled with rich vermicompost"
      },
      "transformation": {
        "before_organic": "Pale yellow, pest-riddled thin leaves with bitter taste in nutrient-deficient soil",
        "after_organic": "Broad, velvety, dark-green crinkled leaves bursting with natural iron and sweet tender crunch"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated Pixar character portrait of Palak Rani, the Queen of Spinach. Elegant, adorable character made of broad, lush emerald-green spinach leaves with rich natural vein textures, sparkling dewdrops, and a sweet smiling face. Green leafy tiara adorning her crown. Rooted in deep, moist black vermicompost soil inside an urban balcony ceramic trough. Golden morning sunlight glowing through translucent leaf edges, 8k 3D render, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, rapid time-lapse: Palak Rani springs up from tiny seed in B.S Organic vermicompost; broad velvet-green leaves fan out gracefully in seconds with dewdrops glistening like diamonds! ASMR crisp leaf unfolding and water droplet chime. No text, no logos."
    },
    {
      "id": "bhindi_birju",
      "name": "Bhindi Birju (Crispy Okra)",
      "tagline": "The Tender High-Yield Star",
      "state": "Pan-India / Gujarat & UP & MP",
      "category": "Vegetable",
      "visual_identity": {
        "body": "Slender, ridged pentagonal green okra character with a jaunty tilted cap stem, lively dancing posture, and a friendly toothy grin",
        "colors": [
          "Vibrant Apple Green",
          "Forest Green Ridges",
          "Warm Yellow Blossom"
        ],
        "props": "Yellow hibiscus-like okra flower tucked behind ear",
        "setting": "Sunny summer farm bed with lush organic foliage"
      },
      "transformation": {
        "before_organic": "Hard, fibrous, woody pod covered in yellow vein mosaic virus",
        "after_organic": "Tender, snap-crisp, bright green five-ridged pods growing in rapid abundance every day"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated character portrait of Bhindi Birju, a cheerful okra ladyfinger character. Slender, crisp bright green five-sided ribbed body with tender velvety peach fuzz, wearing a fresh pale-yellow okra flower behind his stem cap, beaming toothy smile. Standing proudly on an upright organic okra plant rooted in crumbly dark vermicompost. High-noon sunny farm warmth, 8k Octane 3D render, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, fast-paced 3D animation: In soft vermicompost soil, Bhindi Birju springs upward; fresh flowers bloom and drop within seconds, replaced by crisp tender green okras that snap crisply with zero fiber! ASMR clean veggie snap sound and sunny rustle. No text, no captions."
    },
    {
      "id": "matar_mohan",
      "name": "Matar Mohan (Sweet Pea Pod)",
      "tagline": "The Sweet Green Pearl Cluster",
      "state": "Punjab & Uttar Pradesh & Madhya Pradesh",
      "category": "Vegetable",
      "visual_identity": {
        "body": "Plump, curved green pea pod character split slightly open to reveal a row of seven cute, giggling baby green pea brothers peeking out with wide happy eyes",
        "colors": [
          "Fresh Sweetpea Green",
          "Lime Highlights",
          "Dark Earth Soil"
        ],
        "props": "Delicate curling tendrils that grasp garden trellises playfully",
        "setting": "Winter morning kitchen garden with delicate frost mist"
      },
      "transformation": {
        "before_organic": "Flat, empty, yellowed pod with underdeveloped shriveled seeds",
        "after_organic": "Fat, swollen, sweet-as-sugar pods stuffed full of seven giant round green pearls"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated Pixar character portrait of Matar Mohan. A plump, curved glossy green pea pod that is partially unzipped, showing seven adorable, round, giggling baby pea characters inside with big cartoon eyes and joyful smiles. Curled climbing tendrils wrapping playfully around a bamboo garden stake. Rooted in steaming dark black vermicompost earth with winter morning mist in the garden background. Soft golden rim lighting, 8k Octane render, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, macro slow reveal: Matar Mohan's pod unzips with a delightful pop! Seven plump sweet green pea brothers giggle in unison as the morning sun hits their smooth skins. ASMR sweet pod snap and cheerful baby giggles. No text, no logos."
    },
    {
      "id": "himachali_seb",
      "name": "Shebu Seb (Himachali Apple)",
      "tagline": "The Crisp Mountain Sweetheart",
      "state": "Himachal Pradesh & Jammu & Kashmir",
      "category": "Fruit",
      "visual_identity": {
        "body": "Plump, conical Royal Delicious apple character with deep crimson-red skin speckled with natural golden lenticel dots, wearing a cute woolen Himachali cap (topi)",
        "colors": [
          "Royal Crimson Red",
          "Snow White Flesh",
          "Woolen Green Cap"
        ],
        "props": "Delicate pine needle and snowdrop accents on tree branch",
        "setting": "High-altitude mountain orchard in Shimla or Kullu with snow-capped peaks in the background"
      },
      "transformation": {
        "before_organic": "Small, dull brown scab-marked fruit with cracked skin from nutrient deficiency",
        "after_organic": "Oversized, mirror-gloss deep red apple with crisp honeyed crunch and snow-clean organic purity"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated Pixar character portrait of Shebu Seb, a charming mountain apple character. Plump, deep crimson-red Royal Delicious apple with natural golden micro-speckles, wearing a traditional green patterned woolen Himachali cap tilted proudly, big sparkling cartoon eyes, and rosy cheeks. Hanging from an apple tree branch overlooking a misty Himalayan valley with snow-capped mountains. Soil basin around the tree base is enriched with dark spongy vermicompost. Crisp alpine morning sunlight, 8k render, no text, no captions.",
      "video_prompt_hook_8s": "Vertical 9:16, cinematic mountain shot: Cool Himalayan breeze blows as dark B.S Organic vermicompost nurtures the orchard basin. Shebu Seb swells into a dazzling crimson globe with a crisp icy crunch sound! ASMR crisp apple bite sound and mountain wind chimes. No text, no logos."
    },
    {
      "id": "nagpur_santra",
      "name": "Nagpur Santra (Juicy Orange)",
      "tagline": "The Citrus Capital Superstar",
      "state": "Maharashtra",
      "category": "Fruit",
      "visual_identity": {
        "body": "Spherical, bright neon-orange citrus character with easy-peel pebbled skin, wearing traditional orange Kolhapuri pheta (turban), big sunny smile",
        "colors": [
          "Neon Tangerine Orange",
          "Leaf Green",
          "Rich Dark Loam"
        ],
        "props": "Splashes of sweet, fragrant citrus juice droplets floating around him",
        "setting": "Famous Nagpur orange grove under golden autumn sunshine"
      },
      "transformation": {
        "before_organic": "Dry, thick-skinned, acidic fruit that drops prematurely before ripening",
        "after_organic": "Thin-skinned, bursting with overflowing honey-sweet juice packets and aromatic natural essential oils"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated Pixar character portrait of Nagpur Santra, an energetic bright orange citrus character. Perfectly round, radiant tangerine-orange body with juicy pebbled skin texture, wearing a miniature festive saffron headwrap, big friendly smiling eyes. Resting on a sturdy orchard branch with heavy clusters of glowing oranges around him. Tree trunk surrounded by a deep ring of black crumbly vermicompost. Warm autumn golden hour sunlight, 8k Octane 3D render, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, high-speed macro: A burst of vermicompost nutrition surges up the orange tree; Nagpur Santra glows radiant neon orange, releasing a refreshing spiral of fragrant citrus juice droplets! ASMR juicy burst sound and refreshing splash. No text, no captions."
    },
    {
      "id": "bhagwa_anar",
      "name": "Bhagwa Anar (Jewel Pomegranate)",
      "tagline": "The Ruby Gem of the Orchard",
      "state": "Maharashtra & Gujarat & Rajasthan",
      "category": "Fruit",
      "visual_identity": {
        "body": "Majestic, burnished crimson-red pomegranate character with a natural crown calyx on top, split slightly to reveal rows of glowing ruby-red aril jewel teeth",
        "colors": [
          "Burnished Crimson Red",
          "Glistening Ruby Arils",
          "Deep Black Earth"
        ],
        "props": "Wears his calyx like an ancient royal maharaja crown",
        "setting": "Solapur or Nashik high-density pomegranate orchard"
      },
      "transformation": {
        "before_organic": "Bacterial blight spots, cracked dry rind, pale tasteless arils",
        "after_organic": "Unblemished gloss-crimson leather skin packed tight with deep-red, soft-seeded juicy ruby jewels"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated character portrait of Bhagwa Anar, the Royal Pomegranate character. Deep burnished crimson-ruby fruit with a magnificent natural multi-pointed calyx crown, smiling warmly as a small window in his rind reveals a treasure trove of glistening ruby arils glowing like cut gems. Rooted in black vermicompost soil. Dramatic side lighting catching the jewel-like highlights on arils, 8k Octane render, Pixar aesthetic, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, macro slow motion: Bhagwa Anar receives B.S Organic nutrition at the roots. His skin blushes into deep glossy ruby; the crown points stand tall, and arils inside burst with sparkling crimson nectar! ASMR crisp fruit crack and pressurized juice squelch. No text, no logos."
    },
    {
      "id": "nashik_angoor",
      "name": "Nashik Angoor (Royal Grapes)",
      "tagline": "The Sweet Export-Quality Cluster",
      "state": "Maharashtra",
      "category": "Fruit",
      "visual_identity": {
        "body": "Lush, heavy hanging bunch of deep midnight-purple and emerald-green grape brothers clustered together like a cheerful musical choir, covered in delicate natural silver bloom wax",
        "colors": [
          "Midnight Royal Purple",
          "Emerald Frost Green",
          "Silver Wax Bloom"
        ],
        "props": "Delicate curling vine tendrils with musical notes made of dew",
        "setting": "Picturesque vineyard arbor with sunlight filtering through grape trellises"
      },
      "transformation": {
        "before_organic": "Loose, shriveled, berry-drop bunches affected by powdery mildew",
        "after_organic": "Tight, uniform, giant berry clusters with 22+ Brix natural sweetness and flawless silvery bloom"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated Pixar character portrait of Nashik Angoor. A tight, magnificent cluster of plump midnight-purple and glowing green grapes, each individual grape having a cute tiny smiling cartoon face singing happily together. Covered in natural powdery silver wax bloom. Hanging from an old woody vine under an arched garden trellis rooted in dark moist vermicompost. Dappled afternoon vineyard sunlight, 8k Octane 3D render, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, macro glide: Camera glides under vineyard canopy. The grape cluster drinks up B.S Organic vermicompost tea; each grape swells into a translucent purple gem that plumps up with a harmonic chime! ASMR grape skin pop and gentle vineyard breeze. No text, no captions."
    },
    {
      "id": "kesar_keri",
      "name": "Kesar Keri (Gir Saffron Mango)",
      "tagline": "The Queen of Fragrance",
      "state": "Gujarat",
      "category": "Fruit",
      "visual_identity": {
        "body": "Curved, elegant golden-yellow mango character with a distinctive curved beak tip, bright saffron-orange blush, charming smiling eyes, and a fresh green stem cap",
        "colors": [
          "Saffron Gold",
          "Tangerine Sunset",
          "Forest Green"
        ],
        "props": "Swirl of intoxicating mango aroma waves around her",
        "setting": "Foothills of Gir forest in Gujarat under clear sunny skies"
      },
      "transformation": {
        "before_organic": "Small sour fruit dropping off during heatwaves, chemical fertilizer burns",
        "after_organic": "Heavy, golden-saffron queen fruit with unmatched natural sweetness and pulp density"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated character portrait of Kesar Keri, the Queen of Gujarat Mangoes. Beautiful curved golden mango character with a glowing saffron-orange cheek, cheerful twinkling eyes, and a sweet gracious smile. Tucked amidst glossy dark green mango leaves on a sturdy tree branch with rich black vermicompost soil visible below. Golden hour tropical lighting, tactile smooth mango skin, 8k 3D Octane render, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, slow-motion reveal: Kesar Keri sways in the summer breeze. As dark vermicompost nourishes the tree roots, her skin blushes into intense saffron gold, releasing thick aromatic nectar! ASMR sweet summer breeze and nectar drip sound. No text, no logos."
    },
    {
      "id": "nendran_kela",
      "name": "Nendran Kela (Kerala Banana)",
      "tagline": "The Golden Potassium Giant",
      "state": "Kerala & Tamil Nadu",
      "category": "Fruit",
      "visual_identity": {
        "body": "Thick, long, curved golden-yellow banana character with solid green tip, muscular confident stance, and a cheerful warm smile",
        "colors": [
          "Rich Golden Yellow",
          "Lush Jungle Green",
          "Dark Peat Soil"
        ],
        "props": "Big broad tropical banana leaf umbrella held overhead",
        "setting": "Lush tropical Kerala homestead backyard garden"
      },
      "transformation": {
        "before_organic": "Weak pseudo-stem buckling under wind, small dry finger bananas",
        "after_organic": "Massive 30kg bunch of heavy, thick golden Nendran bananas on a sturdy wind-resistant trunk"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated Pixar character portrait of Nendran Kela, the giant Kerala banana character. Long, thick, muscular golden-yellow banana body with gentle curved ridges, smiling warmly with confident friendly eyes, holding a broad tropical green banana leaf like an umbrella. Standing proudly in front of a giant banana tree cluster rooted in dark, moist black vermicompost. Lush tropical Kerala monsoon garden background with soft diffused rain light, 8k render, no text, no captions.",
      "video_prompt_hook_8s": "Vertical 9:16, dynamic 3D zoom: B.S Organic vermicompost feeds the heavy banana trunk; a giant bunch of golden Nendran bananas uncurls effortlessly under broad green leaves with immense strength! ASMR tropical leaf rustle and heavy bunch thud. No text, no logos."
    },
    {
      "id": "allahabad_amrood",
      "name": "Amrood Amar (Allahabad Guava)",
      "tagline": "The Sweet Pink-Core Apple Guava",
      "state": "Uttar Pradesh",
      "category": "Fruit",
      "visual_identity": {
        "body": "Round, bumpy pale-green guava character with smooth yellowish skin, wearing a tiny red scarf, smiling widely to show a peek of sweet baby-pink pulp inside",
        "colors": [
          "Pale Lime Green",
          "Cotton Candy Pink",
          "Earthy Loam"
        ],
        "props": "Glistening dew drops and sweet floral aroma aura",
        "setting": "Traditional Allahabad orchard with sprawling shady trees"
      },
      "transformation": {
        "before_organic": "Hard, stony fruit infested with fruit flies, yellowing leaves",
        "after_organic": "Soft-fleshed, fragrant, oversized guava with sweet melting pink core and zero pests"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated character portrait of Amrood Amar, the Allahabad Safeda guava character. Round, textured pale-green fruit with soft golden highlights, cheerful smiling eyes, and a gentle natural seam showing a glimpse of mouthwatering pink interior pulp. Resting on a guava branch surrounded by smooth green leaves and dark crumbly vermicompost soil around the base. Soft morning garden sunshine, 8k Octane 3D render, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, macro bloom: Amrood Amar takes in rich vermicompost moisture; his skin softens into creamy lime-gold as the sweet pink center swells with heavenly fragrance! ASMR crisp skin squeeze and sweet aroma chime. No text, no captions."
    },
    {
      "id": "pip_strawberry",
      "name": "Pip Strawberry",
      "tagline": "The Sweet Balcony Terrace Queen",
      "state": "Maharashtra (Mahabaleshwar) & Himachal Pradesh",
      "category": "Fruit",
      "visual_identity": {
        "body": "Adorable heart-shaped strawberry girl with glistening ruby skin, golden recessed seed sparkles, big shiny anime-Pixar eyes, and a frilly leafy collar",
        "colors": [
          "Vivid Strawberry Ruby",
          "Glittering Gold Seeds",
          "Mint Green Calyx"
        ],
        "props": "Wearing a crown of tiny white strawberry blossoms",
        "setting": "Balcony vertical planter tower bathed in soft morning sunlight"
      },
      "transformation": {
        "before_organic": "Small pale white-green berry with dry tip, tasteless and sour",
        "after_organic": "Massive, heart-shaped, intensely fragrant, glowing with natural sugar and deep crimson color"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated Pixar character portrait of Pip Strawberry. Adorable heart-shaped strawberry character with deep glistening ruby-red skin embedded with hundreds of tiny golden seeds. Big bright sparkling anime-style cartoon eyes, sweet radiant smile, and a ruffled crown of mint-green leaves and tiny white blossoms. Nestled happily in a terracotta pot filled with steamy dark black vermicompost. Soft morning dew drops, warm sunlight bokeh, 8k Octane 3D render, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, macro 3D bloom: Pip Strawberry takes a deep drink of B.S Organic enriched water from the dark compost base. In seconds, her color transforms from pale green to glistening candy-red, puffing up like a sweet juicy heart! ASMR juicy stretch and dew drop splash. No text, no logos."
    },
    {
      "id": "lemon_leo",
      "name": "Lemon Leo",
      "tagline": "The Citrus Powerhouse",
      "state": "Andhra Pradesh & Gujarat & Punjab",
      "category": "Fruit",
      "visual_identity": {
        "body": "Zesty bright sunshine-yellow lemon character with pebbled textured skin, wearing cool green leaf sunglasses and an energetic grin",
        "colors": [
          "Electric Sunshine Yellow",
          "Glossy Lime Green",
          "Dark Soil Brown"
        ],
        "props": "Fresh aromatic citrus vapor mist swirling around him",
        "setting": "Subtropical organic orchard tree branch in full bloom"
      },
      "transformation": {
        "before_organic": "Small dry pale green pebble with fruit-drop syndrome",
        "after_organic": "Plump heavy golden lemon packed with vitamin-rich organic juice oils, shining under bright sunshine"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated character portrait of Lemon Leo, an upbeat lemon character. Bright sunshine-yellow citrus body with realistic pebbled peel texture, wearing stylish miniature leaf-shaped sunglasses, wide joyful grin. Hanging comfortably from a sturdy leafy citrus branch rooted in rich black vermicompost soil below. Fresh fine mist of citrus aroma droplets suspended in golden morning light. Pixar 3D aesthetic, vibrant dynamic colors, 8k quality, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, high-speed macro: A splash of organic vermicompost tea feeds the roots; Lemon Leo on the branch swells with fresh juice, turning brilliant neon yellow with a satisfying pop and a refreshing citrus mist burst! ASMR pressurized squelch and crisp leaf rustle. No text, no logos."
    },
    {
      "id": "alphonso_mango",
      "name": "Alphonso Mango",
      "tagline": "The Golden Organic King of Fruits",
      "state": "Maharashtra (Konkan / Ratnagiri)",
      "category": "Fruit",
      "visual_identity": {
        "body": "Regal, plump golden-saffron mango character with gentle red blush on shoulders, noble friendly expression, wearing a miniature golden leaf crown",
        "colors": [
          "Golden Saffron Yellow",
          "Sunset Coral Blush",
          "Lush Forest Green"
        ],
        "props": "Tiny royal cape made of fresh mango leaves",
        "setting": "Traditional organic mango orchard at golden hour"
      },
      "transformation": {
        "before_organic": "Fallen blossom, blackened nursery sapling leaves from chemical burn",
        "after_organic": "Magnificent fragrant fruit loaded with rich natural sweetness, zero chemical residues"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated character portrait of Alphonso Mango, the King of Fruits. Plump, smooth saffron-gold mango character with a delicate sunset-coral blush, wearing a small natural crown woven from fresh green leaves. Dignified yet warm smiling cartoon eyes. Perched proudly on an orchard tree branch with rich dark black vermicompost soil carpeted beneath the tree. Sunset golden hour backlight, cinematic atmosphere, 8k Octane render, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, cinematic slow reveal: Golden sunlight bathes the orchard. B.S Organic vermicompost feeds the tree base, and Alphonso Mango glows with a golden aura, turning velvety saffron sweet. ASMR gentle breeze and sweet aromatic chime. No text, no captions."
    },
    {
      "id": "rozy_rose",
      "name": "Rozy Rose",
      "tagline": "The Terrace Garden Showstopper",
      "state": "Pan-India / Balcony & Terrace Gardens",
      "category": "Flower",
      "visual_identity": {
        "body": "Elegant, velvety deep-crimson rose bloom character with layered spiral petals, graceful feminine eyelashes, sweet welcoming smile, and a sturdy emerald stem",
        "colors": [
          "Velvety Deep Crimson",
          "Burgundy Shading",
          "Deep Emerald Foliage"
        ],
        "props": "Glistening crystal dew drops resting like diamonds on her petals",
        "setting": "Luxury terrace balcony garden in a stylish terracotta urn filled with vermicompost"
      },
      "transformation": {
        "before_organic": "Withered dry brown bud infested with aphids, drooping on a yellowed stem",
        "after_organic": "Exploding into a massive 40-petal velvety crimson bloom with intoxicating natural scent and glossy pest-free foliage"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated Pixar character portrait of Rozy Rose. Breathtaking rose blossom character with hundreds of layered, velvety deep crimson petals forming an elegant smiling face with gentle eyelashes. Glistening morning dew drops resting on petals like tiny lenses reflecting garden light. Sturdy emerald stem with healthy thornless leaves rooted in moist, dark crumbly black vermicompost inside an ornate terracotta pot. Dreamy morning garden background, shallow depth of field, 8k render, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, time-lapse macro bloom: A tight, sad rose bud sits surrounded by dry soil. Dark B.S Organic vermicompost is sprinkled around the base; water activates the microbes. The bud unfurls gracefully into a giant velvety crimson rose with a joyful smile! ASMR petal stretch, dew drip, and fragrant harp chime. No text, no logos."
    },
    {
      "id": "genda_marigold",
      "name": "Genda (Mighty Marigold)",
      "tagline": "The Festive Pest-Repelling Sunburst",
      "state": "Pan-India / Bengal & UP & Maharashtra",
      "category": "Flower",
      "visual_identity": {
        "body": "Super-fluffy, layered bright orange-gold marigold character resembling a festive golden pom-pom with wide cheerful eyes and boundless sunny energy",
        "colors": [
          "Bright Saffron Gold",
          "Tangerine Orange",
          "Spring Green"
        ],
        "props": "Natural golden aromatic aura that gently repels garden pests",
        "setting": "Traditional Indian courtyard terrace garden in festival season"
      },
      "transformation": {
        "before_organic": "Single sad flat flower with pale yellow color",
        "after_organic": "Gigantic, ultra-dense 100-petal golden sphere radiating festive vitality"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated Pixar character portrait of Genda Marigold. Super-dense, fluffy spherical marigold character made of hundreds of ruffled golden-saffron and tangerine petals. Big joyful cartoon eyes, energetic beaming smile, sitting in a painted clay pot filled with rich, spongy dark brown vermicompost. Sunlight illuminates translucent petal edges with festive golden warmth. 8k Octane 3D render, tactile ruffled petal texture, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, dynamic 3D explosion: Genda Marigold absorbs fresh vermicompost nutrition through the roots, puffing up like a giant fluffy golden firework, scattering sweet natural fragrance across the garden! ASMR soft ruffle fluff sound and festive bells. No text, no logos."
    },
    {
      "id": "kashmiri_kesar",
      "name": "Kesar Kali (Kashmiri Saffron)",
      "tagline": "The Golden Thread of the Valley",
      "state": "Jammu & Kashmir (Pampore)",
      "category": "Flower & Spice",
      "visual_identity": {
        "body": "Enchanting violet crocus flower character with three glowing, velvety crimson-gold stigmas that look like magical golden threads, gentle serene smile",
        "colors": [
          "Royal Saffron Violet",
          "Glowing Crimson Stigmas",
          "Deep Dark Loam"
        ],
        "props": "Radiates a golden spice mist that glints in the mountain air",
        "setting": "Famous plateau saffron karewas of Pampore with snow peaks in the distance"
      },
      "transformation": {
        "before_organic": "Weak stunted corms choking in dry depleted clay, failing to sprout",
        "after_organic": "Plump organic saffron corms producing multiple violet blooms with long, thick, potent red-gold threads"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated Pixar character portrait of Kesar Kali, the Kashmiri Saffron Crocus character. Delicate, royal violet petals cradling three luminous, deep-crimson and golden saffron stigmas standing proudly in the center. Serene smiling cartoon eyes. Rooted in deep, aerated black vermicompost soil in a high-altitude Himalayan field under crisp violet dusk light. Photorealistic 3D render, subsurface glow on saffron threads, 8k quality, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, macro slow reveal: In rich black vermicompost, the violet crocus opens under morning mountain mist; three glowing crimson saffron threads extend gracefully into the sun with an ethereal golden glow! ASMR delicate blossom uncurl and crystalline wind chime. No text, no logos."
    },
    {
      "id": "madurai_malli",
      "name": "Madurai Malli (Sacred Jasmine)",
      "tagline": "The Crown of Southern Temples",
      "state": "Tamil Nadu & Karnataka",
      "category": "Flower",
      "visual_identity": {
        "body": "Pristine, porcelain-white multi-petaled jasmine bud character with thick pointed petals, adorned with a miniature golden garland, radiating divine serene fragrance",
        "colors": [
          "Porcelain Pure White",
          "Deep Emerald Foliage",
          "Warm Gold Aura"
        ],
        "props": "Delicate white fragrant ribbons wafting in the air",
        "setting": "Traditional South Indian temple garden courtyard"
      },
      "transformation": {
        "before_organic": "Brown-tipped unopened buds falling off, weak pale leaves",
        "after_organic": "Dense clusters of heavy, thick, incredibly fragrant white blossoms opening in unison"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated Pixar character portrait of Madurai Malli, the sacred jasmine character. Thick, multi-layered pristine ivory-white jasmine blossom with porcelain-like petals and peaceful smiling eyes, wearing a tiny gold-accented temple flower garland. Rooted in moist, spongy black vermicompost inside a brass South Indian urn. Warm brass oil lamps and soft morning temple courtyard light in the background. 8k Octane 3D render, no text, no captions.",
      "video_prompt_hook_8s": "Vertical 9:16, serene dawn macro: In dark B.S Organic vermicompost, Madurai Malli's tight pearl buds drink in organic tea and unfurl with a soft divine glow, releasing thick ribbons of heavenly temple fragrance! ASMR soft petal stretch and distant temple bell chime. No text, no watermark."
    },
    {
      "id": "tulsi_shrimati",
      "name": "Tulsi Shrimati (Sacred Holy Basil)",
      "tagline": "The Household Guardian & Immunity Herb",
      "state": "Pan-India (Universal Indian Courtyards)",
      "category": "Herb & Sacred Plant",
      "visual_identity": {
        "body": "Graceful Krishna-tulsi character with deep purple-green serrated leaves, tiny purple flower spikes (manjari), wearing a tiny red bindi and a serene benevolent smile",
        "colors": [
          "Deep Purple Green",
          "Lavender Blossom Spikes",
          "Terracotta Red"
        ],
        "props": "Protected by a miniature traditional carved Tulsi Vrindavan pot",
        "setting": "Sunlit Indian home courtyard bathed in spiritual morning light"
      },
      "transformation": {
        "before_organic": "Drooping, bug-bitten yellowed leaves in hard alkaline cement-like soil",
        "after_organic": "Bushy, vibrant, fragrant purple-green foliage loaded with healing oils and fresh seed spikes"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated Pixar character portrait of Tulsi Shrimati, the Sacred Holy Basil character. Graceful, bushy character with textured deep purple-green serrated leaves and upright lavender flower spikes, gentle benevolent smiling eyes, and a small red tilak on her leafy forehead. Growing inside an ornate traditional terracotta Tulsi Vrindavan pot filled with rich, moist black vermicompost. Warm spiritual sunrise rays, soft morning mist, 8k Octane render, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, peaceful morning slow pan: Pure water activates dark B.S Organic vermicompost in the Tulsi pot; Tulsi Shrimati flourishes, leaves turning rich deep purple-green as golden morning light radiates around her! ASMR gentle earthen water soak and calming morning chime. No text, no logos."
    },
    {
      "id": "pili_sarson",
      "name": "Sarson Simran (Mustard Bloom)",
      "tagline": "The Golden Winter Sea of the North",
      "state": "Punjab & Haryana & Rajasthan",
      "category": "Cash Crop & Oilseed",
      "visual_identity": {
        "body": "Lively, dancing bright-yellow four-petaled mustard blossom character with cheerful twinkling eyes, wearing a rustic Punjabi phulkari scarf, swaying in the wind",
        "colors": [
          "Vibrant Saffron Yellow",
          "Lush Mustard Green",
          "Black Silt Earth"
        ],
        "props": "Surrounded by a golden halo of busy friendly bumblebee friends",
        "setting": "Endless blooming yellow mustard fields of Punjab under winter sun"
      },
      "transformation": {
        "before_organic": "Sparse yellow flowers with empty seed pods due to chemical soil exhaustion",
        "after_organic": "Dense sea of 6-foot tall mustard plants bowed down with thick pods packed with high-oil organic seeds"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated Pixar character portrait of Sarson Simran, the energetic Mustard Flower character. Bright, glowing neon-yellow four-petaled blossom with big joyful cartoon eyes and a beaming smile, wearing a miniature colourful Punjabi Phulkari scarf. Waving proudly atop a tall, thick green mustard stalk rooted in fertile, dark black vermicompost earth. Vast yellow mustard fields stretching to the horizon under a soft winter sun. 8k 3D Octane render, no text, no captions.",
      "video_prompt_hook_8s": "Vertical 9:16, sweeping farm camera: Winter wind blows across Punjab fields. Deep roots drink from B.S Organic black soil; Sarson Simran twirls happily as thousands of golden mustard flowers explode into bloom like a yellow sea! ASMR whispering winter breeze and joyful folk flute chime. No text, no logos."
    },
    {
      "id": "ganna_guruji",
      "name": "Ganna Guruji (Sweet Sugarcane)",
      "tagline": "The Tower of Pure Organic Jaggery",
      "state": "Uttar Pradesh & Maharashtra & Haryana",
      "category": "Cash Crop",
      "visual_identity": {
        "body": "Tall, sturdy, multi-jointed dark purple and emerald sugarcane stalk character with friendly elder eyes, graying leafy mustache, and a strong upright posture",
        "colors": [
          "Deep Royal Purple",
          "Juicy Lime Joint Rings",
          "Rich Dark Soil"
        ],
        "props": "Holds a miniature walking cane made of pure crystal jaggery",
        "setting": "Dense sugarcane field with towering 12-foot organic stalks"
      },
      "transformation": {
        "before_organic": "Thin, stunted, dry canes attacked by red rot fungus in exhausted soil",
        "after_organic": "Massive 2-inch thick, solid juicy purple canes packed with record-high natural sucrose and sweet juice"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated Pixar character portrait of Ganna Guruji, the wise Sugarcane character. Sturdy, tall segmented purple-and-green sugarcane stalk with smooth nodes, friendly grandfatherly smiling eyes, and a cute leaf mustache. Tall green leafy plume flowing on his head. Deeply rooted in aerated, moist black vermicompost soil. Dense towering sugarcane plantation behind him with sunlight streaming through the leaves. 8k Octane 3D render, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, vertical tilt-up shot: Camera tilts up a massive, thick purple cane rooted in dark vermicompost. Ganna Guruji winks as sweet sugary juice fills every segment to the brim! ASMR satisfying solid cane snap and rushing juice sound. No text, no captions."
    },
    {
      "id": "basmati_raja",
      "name": "Basmati Raja (The Grain of Kings)",
      "tagline": "The Fragrant Long-Grain Royal",
      "state": "Punjab & Haryana",
      "category": "Cash Crop",
      "visual_identity": {
        "body": "Regal, slender, extra-long golden rice grain character wearing a tiny maharaja turban with an emerald plume, bowing graciously with a warm smile",
        "colors": [
          "Pearl Cream White",
          "Golden Husk",
          "Fertile Black Loam"
        ],
        "props": "Aroma ribbons of fragrant cooked basmati floating in the air",
        "setting": "Lush water-reflected paddy field under soft sunrise"
      },
      "transformation": {
        "before_organic": "Chalky, brittle grains that break during milling, stunted yellowing tillers",
        "after_organic": "Extra-long, slender, pearlescent grains with world-renowned natural aroma and zero chemical residue"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated Pixar character portrait of Basmati Raja, the Royal Rice character. Slender, extra-long golden-husked rice grain character with a smiling dignified face, wearing an ornate miniature royal turban with a tiny emerald jewel. Swaying gracefully on a lush green paddy ear rooted in rich, fertile organic black soil with water reflections. Early morning golden sunrise over lush Punjab fields. 8k Octane 3D render, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, slow-motion farm pan: B.S Organic enriched soil feeds the paddy roots; the rice stalk bends gracefully under the weight of hundreds of extra-long golden Basmati grains glinting in the sun! ASMR gentle water ripple and rustling grain whispers. No text, no logos."
    },
    {
      "id": "peet_mungfali",
      "name": "Mungfali Munna (Groundnut Champ)",
      "tagline": "The Underground Golden Nut",
      "state": "Gujarat & Andhra Pradesh",
      "category": "Cash Crop & Oilseed",
      "visual_identity": {
        "body": "Cheeky, figure-eight shaped textured tan groundnut pod character with cute dimples, curious sparkling eyes, and tiny leaf hands",
        "colors": [
          "Tan Husk Brown",
          "Golden Kernel",
          "Moist Black Loam"
        ],
        "props": "Peeking out from underground soil with a mischievous wink",
        "setting": "Sandy loam coastal farm in Saurashtra, Gujarat"
      },
      "transformation": {
        "before_organic": "Empty pods (pops) with shriveled bitter nuts in hard-packed dirt",
        "after_organic": "Heavy, tightly packed pods with two giant plump golden oil-rich nuts inside loose black vermicompost"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated underground character portrait of Mungfali Munna, the groundnut character. Figure-eight shaped netted tan shell with realistic pod texture, big mischievous cartoon eyes, and a cute wide grin. Nestled comfortably underground in airy, crumbly black vermicompost soil with a cluster of fat healthy groundnut pods around him. Soft underground golden lighting, 8k Octane 3D render, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, underground macro view: In soft spongy vermicompost, Mungfali Munna cracks open with a satisfying crunch to reveal two giant, glossy golden nuts bursting with rich organic oil! ASMR crisp peanut crack sound and soil rumble. No text, no captions."
    },
    {
      "id": "sona_gehun",
      "name": "Sona Gehun (Golden Wheat)",
      "tagline": "The Farmer's Pride Cash Crop",
      "state": "Madhya Pradesh (Sharbati) & Punjab & Haryana",
      "category": "Cash Crop",
      "visual_identity": {
        "body": "Tall, proud, golden wheat ear character with symmetrical shimmering grain kernels, waving happily in the wind with a strong rustic farmer spirit",
        "colors": [
          "Burnished Amber Gold",
          "Warm Wheat Straw",
          "Black Earth Soil"
        ],
        "props": "Wearing a tiny rustic red cotton farmer scarf",
        "setting": "Expansive organic farm field under open blue sky"
      },
      "transformation": {
        "before_organic": "Thin, yellowed, brittle stalk with empty grain husks in saline chemical-crusted land",
        "after_organic": "Thick heavy golden stalks bowed down with full, dense, nutritious organic grain kernels"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated Pixar character portrait of Sona Gehun, a heroic golden wheat character. Symmetrical, full amber-gold grain head with crisp golden awns (bristles), smiling proudly with strong rustic charm, wearing a tiny red farmer scarf. Rooted deeply in rich, fertile, dark black organic vermicompost soil. Endless sunny golden wheat fields in the soft-focus background with blue sky and fluffy white clouds. 8k Octane 3D render, natural grain texture, cinematic lighting, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, sweeping farm camera: Deep roots drink from black vermicompost earth; the wheat stalk surges upward, kernels swelling into heavy golden grain that glints in the sun with a wave of farmer pride! ASMR whispering wheat field breeze and full grain rustle. No text, no logos."
    },
    {
      "id": "kapas_cotton",
      "name": "Kapas (Fluffy Cotton)",
      "tagline": "The Cloud of the Farm",
      "state": "Gujarat & Maharashtra & Telangana",
      "category": "Cash Crop",
      "visual_identity": {
        "body": "Super-soft, fluffy cloud-like white cotton boll character nestled inside a dry star-shaped sepia pod, big bubbly innocent eyes and cheerful giggles",
        "colors": [
          "Pure Cloud White",
          "Sepia Brown Pod",
          "Deep Black Loam"
        ],
        "props": "Soft white fluff floating gently like miniature clouds",
        "setting": "Organic cotton field ready for harvest"
      },
      "transformation": {
        "before_organic": "Pest-eaten, bollworm damaged dark shriveled boll",
        "after_organic": "Snow-white, oversized, pristine organic cotton boll bursting effortlessly into four puffy clouds"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated character portrait of Kapas Cotton. Incredibly fluffy, pure-white cloud-like cotton boll character with big round friendly cartoon eyes, resting inside a star-shaped dry brown pod. Soft tactile fiber textures, individual cotton wisps catching the warm afternoon sunlight. Plant rooted in fertile, dark black vermicompost soil. Pixar 3D aesthetic, ultra-soft subsurface scattering, 8k resolution, no text, no watermark.",
      "video_prompt_hook_8s": "Vertical 9:16, macro slow motion: The pod splits open as a burst of pure-white, fluffy Kapas Cotton expands like a marshmallow cloud, giggling with organic health! ASMR soft cotton puff sound and sunny breeze. No text, no captions."
    },
    {
      "id": "chai_patti",
      "name": "Chai Rani (Darjeeling Tea Shoot)",
      "tagline": "The Fragrant Two-Leaves-and-a-Bud",
      "state": "Assam & West Bengal (Darjeeling)",
      "category": "Cash Crop",
      "visual_identity": {
        "body": "Charming, delicate tea shoot character consisting of two glossy tender lime-green leaves and an upright silver velvety bud, wearing a traditional miniature woven bamboo basket on her back",
        "colors": [
          "Tender Tea Lime",
          "Velvety Silver Bud",
          "Mist Green Mountain"
        ],
        "props": "Fresh mountain morning dew droplets resting like pearls on the leaves",
        "setting": "Misty rolling green tea slopes of Darjeeling or Assam at dawn"
      },
      "transformation": {
        "before_organic": "Tough, scorched, bitter leaves from chemical pesticide overdosing",
        "after_organic": "Ultra-tender, fragrant shoots packed with sweet muscatel aroma and rich natural catechins"
      },
      "image_prompt_9_16": "Vertical 9:16, 3D animated character portrait of Chai Rani, the Tea Shoot character. Two tender, glossy lime-green tea leaves cupping an upright velvety silver bud with a sweet smiling face. Wearing a miniature woven wicker tea-plucking basket on her back. Rooted in dark, moisture-rich organic vermicompost on a terraced mountain slope. Rolling green tea hills covered in ethereal morning mist with dawn light filtering through. 8k Octane 3D render, no text, no captions.",
      "video_prompt_hook_8s": "Vertical 9:16, cinematic mountain dawn: Morning mist rolls over tea gardens. As B.S Organic vermicompost nourishes the tea bush roots, Chai Rani uncurls with a glistening dewdrop, radiating fresh muscatel tea fragrance! ASMR gentle tea leaf snap and soothing flute melody. No text, no logos."
    },
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
    },
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
    }
  ]
}

def seed_database(force: bool = False):
    """Seeds or updates characters.json with the full canonical roster."""
    if CHAR_FILE.exists() and not force:
        with open(CHAR_FILE, "r", encoding="utf-8") as f:
            existing = json.load(f)
        existing_ids = {c["id"] for c in existing.get("characters", [])}
        print(f"Existing database has {len(existing_ids)} characters.")
        to_add = [c for c in MASTER_DATA["characters"] if c["id"] not in existing_ids]
        if to_add:
            existing["characters"].extend(to_add)
            with open(CHAR_FILE, "w", encoding="utf-8") as f:
                json.dump(existing, f, indent=2, ensure_ascii=False)
            print(f"Added {len(to_add)} missing characters. Total now: {len(existing['characters'])}")
        else:
            print("Database is already up to date with all 132 characters!")
    else:
        with open(CHAR_FILE, "w", encoding="utf-8") as f:
            json.dump(MASTER_DATA, f, indent=2, ensure_ascii=False)
        print(f"Database cleanly seeded with {len(MASTER_DATA['characters'])} characters!")


if __name__ == "__main__":
    seed_database()
