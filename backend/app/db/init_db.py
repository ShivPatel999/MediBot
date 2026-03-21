from datetime import date

MOCK_DB = {
    "allergy": {
        "urgency": "Low to Moderate",
        "aliases": ["pollen allergy", "seasonal allergy", "hay fever", "allergies", "itchy eyes",
                    "watery eyes", "sneezing", "alergy", "allergie", "dust allergy", "pet allergy",
                    "runny nose from allergies", "allergic reaction"],
        "symptoms": ["Sneezing", "Runny or stuffy nose", "Itchy/watery eyes", "Itchy throat or skin",
                     "Coughing", "Hives", "Fatigue", "Headache"],
        "causes": "Immune system overreaction to allergens like pollen, mold, pet dander, dust, or food.",
        "meds": [
            {"name": "Cetirizine (Zyrtec)", "purpose": "Relieves sneezing, runny nose, itchy/watery eyes", "how_to_use": "10mg once daily. Can be taken day or night."},
            {"name": "Loratadine (Claritin)", "purpose": "Non-drowsy antihistamine for seasonal allergies", "how_to_use": "10mg once daily at the same time each day."},
            {"name": "Fexofenadine (Allegra)", "purpose": "Non-drowsy relief for seasonal allergy symptoms", "how_to_use": "180mg once daily. Do not take with fruit juice."},
            {"name": "Fluticasone Nasal Spray (Flonase)", "purpose": "Reduces nasal congestion, sneezing, runny nose", "how_to_use": "2 sprays per nostril once daily. Takes a few days for full effect."},
            {"name": "Diphenhydramine (Benadryl)", "purpose": "Fast-acting antihistamine for allergic reactions and hives", "how_to_use": "25-50mg every 4-6 hours as needed. Causes drowsiness."},
            {"name": "Ketotifen Eye Drops (Zaditor)", "purpose": "Relieves itchy, watery allergy eyes", "how_to_use": "1 drop in each affected eye twice daily, every 8-12 hours."}
        ],
        "warning": "Seek emergency care (call 911) immediately for signs of anaphylaxis: throat swelling, difficulty breathing, rapid pulse, or fainting. See a doctor if symptoms are severe or OTC medications stop working."
    },
    "anaphylaxis": {
        "urgency": "EMERGENCY",
        "aliases": ["severe allergic reaction", "throat swelling", "cant breathe after eating",
                    "epipen", "severe allergy", "anaphylatic", "anaphalaxis"],
        "symptoms": ["Difficulty breathing or wheezing", "Throat tightening or swelling",
                     "Hives over the body", "Rapid or weak pulse", "Dizziness or fainting",
                     "Nausea or vomiting", "Abdominal pain", "Pale or bluish skin"],
        "causes": "Severe whole-body allergic reaction triggered by foods (peanuts, shellfish), insect stings, medications (penicillin, aspirin), or latex.",
        "meds": [
            {"name": "Epinephrine Auto-Injector (EpiPen)", "purpose": "EMERGENCY: First-line treatment to reverse anaphylaxis immediately", "how_to_use": "Inject into outer thigh, even through clothing. Call 911 immediately after use."},
            {"name": "Diphenhydramine (Benadryl)", "purpose": "Secondary antihistamine AFTER epinephrine - not a substitute", "how_to_use": "25-50mg after epinephrine as directed by emergency personnel only."}
        ],
        "warning": "CALL 911 IMMEDIATELY. Anaphylaxis is life-threatening. Do not wait. If an EpiPen is available, use it right away."
    },
    "asthma": {
        "urgency": "Moderate to High",
        "aliases": ["asthma attack", "wheezing", "cant breathe", "shortness of breath",
                    "tight chest", "asma", "breathing problems", "inhaler needed"],
        "symptoms": ["Wheezing", "Shortness of breath", "Chest tightness or pain",
                     "Coughing especially at night", "Difficulty talking due to breathlessness"],
        "causes": "Inflammation and narrowing of airways triggered by allergens, exercise, cold air, respiratory infections, smoke, or stress.",
        "meds": [
            {"name": "Primatene Mist (OTC Inhaler)", "purpose": "OTC epinephrine inhaler for mild intermittent asthma symptoms", "how_to_use": "2 puffs every 4 hours as needed for adults. Not for children under 12."},
            {"name": "Albuterol Inhaler — Rx required", "purpose": "Fast-acting bronchodilator that opens airways during an attack", "how_to_use": "Requires prescription. 2 puffs every 4-6 hours as needed."}
        ],
        "warning": "Go to the emergency room immediately if lips turn blue, you cannot speak in full sentences, or symptoms do not improve after using an inhaler. Call 911 for severe attacks."
    },
    "hives": {
        "urgency": "Low to Moderate",
        "aliases": ["urticaria", "welts", "itchy bumps", "skin welts", "hivs",
                    "red bumps itchy", "skin rash with bumps"],
        "symptoms": ["Red or skin-colored raised welts", "Intense itching",
                     "Welts that change shape and move", "Swelling", "Skin turns white when pressed"],
        "causes": "Allergic reaction to foods, medications, insect bites, or pollen. Also triggered by stress, cold, heat, or infections.",
        "meds": [
            {"name": "Diphenhydramine (Benadryl)", "purpose": "Fast-acting antihistamine for hives", "how_to_use": "25-50mg every 4-6 hours as needed. Causes drowsiness."},
            {"name": "Cetirizine (Zyrtec)", "purpose": "Non-drowsy antihistamine for chronic hives", "how_to_use": "10mg once daily."},
            {"name": "Loratadine (Claritin)", "purpose": "Non-drowsy option for mild hives", "how_to_use": "10mg once daily."},
            {"name": "Hydrocortisone Cream 1%", "purpose": "Reduces local itching and inflammation", "how_to_use": "Apply thin layer to affected area 2-4 times daily."},
            {"name": "Calamine Lotion", "purpose": "Soothes itching and discomfort from hives", "how_to_use": "Apply to affected area up to 4 times daily. Let dry before covering."}
        ],
        "warning": "Call 911 immediately if hives are accompanied by throat swelling, difficulty breathing, or fainting. See a doctor if hives persist more than 6 weeks."
    },
    "food allergy": {
        "urgency": "Moderate to High",
        "aliases": ["allergic to food", "peanut allergy", "nut allergy", "shellfish allergy",
                    "milk allergy", "egg allergy", "wheat allergy", "ate something allergic"],
        "symptoms": ["Hives or itching within minutes to 2 hours of eating",
                     "Swelling of lips, tongue, or face", "Hoarse voice or wheezing",
                     "Abdominal pain, nausea, or diarrhea", "Dizziness or fainting"],
        "causes": "Immune system produces IgE antibodies against specific foods. Most common: peanuts, tree nuts, shellfish, eggs, milk, wheat, and soy.",
        "meds": [
            {"name": "Diphenhydramine (Benadryl)", "purpose": "Fast-acting antihistamine for mild food allergy reactions", "how_to_use": "25-50mg immediately for mild symptoms. NOT sufficient for severe reactions."},
            {"name": "Epinephrine Auto-Injector (EpiPen) — Rx required", "purpose": "EMERGENCY treatment for severe food allergy reactions", "how_to_use": "If prescribed, inject into outer thigh at first sign of severe reaction. Call 911 immediately."}
        ],
        "warning": "Call 911 immediately for difficulty breathing, throat tightening, or whole-body reaction after eating. Use epinephrine if prescribed — do not wait for symptoms to worsen."
    },
    "headache": {
        "urgency": "Low",
        "aliases": ["head pain", "head hurts", "migraine", "headace", "hedache", "my head hurts",
                    "pounding head", "head pressure", "tension headache", "head is killing me"],
        "symptoms": ["Throbbing or pulsing pain", "Pressure around forehead or temples",
                     "Sensitivity to light or noise", "Nausea with migraine"],
        "causes": "Tension, dehydration, lack of sleep, eye strain, sinus congestion, caffeine withdrawal, or migraine triggers.",
        "meds": [
            {"name": "Acetaminophen (Tylenol)", "purpose": "Pain relief and fever reduction", "how_to_use": "325-650mg every 4-6 hours. Do not exceed 3000mg/day."},
            {"name": "Ibuprofen (Advil/Motrin)", "purpose": "Anti-inflammatory pain relief", "how_to_use": "200-400mg every 4-6 hours with food."},
            {"name": "Aspirin", "purpose": "Pain relief and anti-inflammatory", "how_to_use": "325-650mg every 4-6 hours. Not for children under 12."},
            {"name": "Excedrin Migraine", "purpose": "Specifically targets migraine headaches", "how_to_use": "2 tablets every 6 hours. Max 2 doses/day."}
        ],
        "warning": "Seek emergency care for: worst headache of your life, sudden severe onset, headache after head trauma, or headache with fever and stiff neck."
    },
    "sore throat": {
        "urgency": "Low",
        "aliases": ["throat hurts", "throat pain", "scratchy throat", "soar throat", "throut",
                    "painful swallowing", "throat is killing me", "strep throat"],
        "symptoms": ["Pain or scratchiness in throat", "Worsened pain when swallowing",
                     "Swollen tonsils", "Hoarse voice", "Mild fever"],
        "causes": "Viral infections (cold, flu) or bacterial infections (strep). Also caused by allergies or dry air.",
        "meds": [
            {"name": "Throat Lozenges (Cepacol/Halls)", "purpose": "Temporary numbing and soothing", "how_to_use": "Dissolve one slowly in mouth every 2 hours as needed."},
            {"name": "Chloraseptic Spray", "purpose": "Instant throat numbing spray", "how_to_use": "Spray 5 times to throat, wait 15 seconds then spit. Every 2 hours as needed."},
            {"name": "Salt Water Gargle", "purpose": "Natural antiseptic to reduce inflammation", "how_to_use": "Mix 1/2 tsp salt in 8oz warm water. Gargle 30 seconds, do not swallow."},
            {"name": "Acetaminophen (Tylenol)", "purpose": "Reduces throat pain and fever", "how_to_use": "325-650mg every 4-6 hours as needed."},
            {"name": "Ibuprofen (Advil)", "purpose": "Reduces throat inflammation and pain", "how_to_use": "200-400mg every 4-6 hours with food."}
        ],
        "warning": "See a doctor if: difficulty breathing or swallowing, fever over 101F, white patches on tonsils, or symptoms lasting more than 3 days. Strep throat requires prescription antibiotics."
    },
    "cold": {
        "urgency": "Low",
        "aliases": ["runny nose", "stuffy nose", "congestion", "common cold", "sniffles",
                    "stuffed up", "coldd", "blocked nose", "nasal congestion"],
        "symptoms": ["Runny or stuffy nose", "Sneezing", "Sore throat", "Mild cough",
                     "Low-grade fever", "Mild body aches", "Fatigue"],
        "causes": "Viral infection. Most commonly rhinovirus. Spreads through airborne droplets or contaminated surfaces.",
        "meds": [
            {"name": "DayQuil / NyQuil", "purpose": "Multi-symptom cold relief", "how_to_use": "Follow label. DayQuil every 4 hours during day; NyQuil at night only."},
            {"name": "Pseudoephedrine (Sudafed)", "purpose": "Nasal decongestant", "how_to_use": "30-60mg every 4-6 hours. Available behind pharmacy counter."},
            {"name": "Saline Nasal Spray", "purpose": "Clears nasal passages naturally", "how_to_use": "2 sprays per nostril as needed. Safe for frequent use."},
            {"name": "Zinc Lozenges (Zicam)", "purpose": "May reduce cold duration if taken early", "how_to_use": "1 lozenge every 3 hours while awake. Start within 24 hours of symptoms."}
        ],
        "warning": "See a doctor if fever exceeds 103F, symptoms worsen after 10 days, or you have difficulty breathing."
    },
    "flu": {
        "urgency": "Moderate",
        "aliases": ["influenza", "flu symptoms", "body aches and fever", "flue",
                    "flu like symptoms", "i have the flu", "sick with flu"],
        "symptoms": ["Sudden high fever 100-104F", "Severe body and muscle aches",
                     "Extreme fatigue", "Headache", "Dry cough", "Chills"],
        "causes": "Influenza A or B virus. More severe than common cold with sudden onset.",
        "meds": [
            {"name": "Acetaminophen (Tylenol)", "purpose": "Fever and body ache relief", "how_to_use": "325-650mg every 4-6 hours. Do not exceed 3000mg/day."},
            {"name": "Ibuprofen (Advil)", "purpose": "Fever and body ache relief", "how_to_use": "200-400mg every 4-6 hours with food."},
            {"name": "DayQuil / NyQuil", "purpose": "Multi-symptom flu relief", "how_to_use": "Follow label. DayQuil every 4 hours during day; NyQuil at night."},
            {"name": "Electrolyte Drinks (Gatorade/Pedialyte)", "purpose": "Replenishes fluids and electrolytes", "how_to_use": "Drink throughout the day. Aim for at least 8 cups of fluid daily."}
        ],
        "warning": "See a doctor immediately for: difficulty breathing, persistent chest pain, confusion, or symptoms that improve then return with fever and worsened cough."
    },
    "fever": {
        "urgency": "Moderate",
        "aliases": ["high temperature", "feel hot", "chills", "temperature", "feaver", "fevr",
                    "body temp high", "running a fever"],
        "symptoms": ["Body temperature above 100.4F", "Chills and shivering",
                     "Sweating", "Headache", "Muscle aches", "Fatigue"],
        "causes": "Body's immune response to infection. Also caused by inflammation, heat exhaustion, or medications.",
        "meds": [
            {"name": "Acetaminophen (Tylenol)", "purpose": "Fever and pain reduction", "how_to_use": "325-650mg every 4-6 hours. Do not exceed 3000mg/day."},
            {"name": "Ibuprofen (Advil/Motrin)", "purpose": "Fever reduction and anti-inflammatory", "how_to_use": "200-400mg every 4-6 hours with food or milk."},
            {"name": "Aspirin (adults only)", "purpose": "Fever and pain reduction", "how_to_use": "325-650mg every 4-6 hours. Never give to children."}
        ],
        "warning": "Seek immediate care if: fever above 103F in adults, any fever in infant under 3 months, lasting more than 3 days, or accompanied by stiff neck, rash, or confusion."
    },
    "stomach ache": {
        "urgency": "Low",
        "aliases": ["stomach pain", "belly ache", "tummy ache", "nausea", "upset stomach",
                    "stomache", "stomack", "abdomen pain", "cramps", "abdominal pain",
                    "tummy hurts", "belly pain", "stomach cramps"],
        "symptoms": ["Cramping or dull aching in abdomen", "Nausea", "Bloating or gas",
                     "Diarrhea or constipation", "Loss of appetite", "Vomiting"],
        "causes": "Indigestion, gas, food intolerance, viral gastroenteritis, food poisoning, or stress.",
        "meds": [
            {"name": "Pepto-Bismol", "purpose": "Nausea, heartburn, indigestion, diarrhea", "how_to_use": "2 tablets or 30ml every 30-60 minutes as needed. Max 8 doses/day."},
            {"name": "Antacids (Tums/Rolaids)", "purpose": "Heartburn and acid indigestion relief", "how_to_use": "Chew 2-4 tablets as symptoms occur. Do not exceed 15 tablets/day."},
            {"name": "Simethicone (Gas-X)", "purpose": "Relieves gas and bloating", "how_to_use": "40-125mg after meals and at bedtime as needed."},
            {"name": "Ginger Tea / Ginger Chews", "purpose": "Natural nausea relief", "how_to_use": "Sip warm ginger tea slowly or chew 1 ginger chew as needed."}
        ],
        "warning": "See a doctor immediately if: pain is severe or localizes to lower right side, accompanied by bloody stool, vomiting blood, or lasts more than 2 days."
    },
    "muscle pain": {
        "urgency": "Low",
        "aliases": ["muscle ache", "body ache", "sore muscles", "back pain", "joint pain",
                    "muscl pain", "mussel pain", "aching muscles", "muscle soreness"],
        "symptoms": ["Dull or sharp pain in muscles", "Tenderness when touched",
                     "Swelling or bruising", "Limited range of motion"],
        "causes": "Overexertion, injury, tension, viral illness, dehydration, or fibromyalgia.",
        "meds": [
            {"name": "Ibuprofen (Advil/Motrin)", "purpose": "Reduces muscle inflammation and pain", "how_to_use": "200-400mg every 4-6 hours with food."},
            {"name": "Naproxen (Aleve)", "purpose": "Longer-lasting anti-inflammatory pain relief", "how_to_use": "220mg every 8-12 hours. Max 2 doses in 8-12 hours."},
            {"name": "Topical Bengay / Icy Hot", "purpose": "Localized muscle pain relief", "how_to_use": "Apply thin layer to affected area up to 3-4 times daily."},
            {"name": "Acetaminophen (Tylenol)", "purpose": "Pain relief when anti-inflammatories are not suitable", "how_to_use": "500-1000mg every 4-6 hours. Do not exceed 3000mg/day."}
        ],
        "warning": "See a doctor if: pain is severe, follows a significant injury, does not improve after a week, or is accompanied by significant swelling or fever."
    },
    "cough": {
        "urgency": "Low",
        "aliases": ["coughing", "dry cough", "wet cough", "chest cough", "coff",
                    "coughing a lot", "persistent cough", "hacking cough"],
        "symptoms": ["Dry or productive cough", "Chest tightness", "Wheezing",
                     "Sore throat from coughing"],
        "causes": "Viral infections, allergies, asthma, acid reflux, postnasal drip, or irritants like smoke.",
        "meds": [
            {"name": "Dextromethorphan (Robitussin DM)", "purpose": "Suppresses dry or persistent cough", "how_to_use": "10-20mg every 4 hours. Do not exceed 120mg/day."},
            {"name": "Guaifenesin (Mucinex)", "purpose": "Loosens chest congestion for productive cough", "how_to_use": "400mg every 4 hours or 600-1200mg every 12 hours extended release. Drink plenty of water."},
            {"name": "Honey (1-2 tsp)", "purpose": "Natural cough suppressant especially for nighttime cough", "how_to_use": "1-2 teaspoons directly or in warm tea. Not for children under 1 year."},
            {"name": "Menthol Cough Drops (Halls)", "purpose": "Soothes throat irritation and mild cough", "how_to_use": "Dissolve one in mouth as needed."}
        ],
        "warning": "See a doctor if: cough lasts more than 3 weeks, produces blood, or is accompanied by high fever or significant chest pain."
    },
    "skin rash": {
        "urgency": "Low",
        "aliases": ["rash", "itchy skin", "skin irritation", "eczema", "dry skin",
                    "skin itch", "rashh", "red skin", "dermatitis"],
        "symptoms": ["Red inflamed skin", "Itching or burning", "Blistering or crusting",
                     "Dry scaly patches", "Raised bumps or welts"],
        "causes": "Contact with irritants or allergens, eczema, psoriasis, fungal infection, heat, or medication reactions.",
        "meds": [
            {"name": "Hydrocortisone Cream 1%", "purpose": "Reduces itching and inflammation from rashes", "how_to_use": "Apply thin layer to affected area 2-4 times daily. Do not use on face more than 7 days."},
            {"name": "Diphenhydramine (Benadryl)", "purpose": "Oral antihistamine for allergic rashes and hives", "how_to_use": "25-50mg every 4-6 hours as needed. Causes drowsiness."},
            {"name": "Calamine Lotion", "purpose": "Soothes itching from rashes and poison ivy", "how_to_use": "Apply to affected area up to 4 times daily. Let dry before covering."},
            {"name": "Colloidal Oatmeal Cream (Aveeno)", "purpose": "Soothes and moisturizes irritated itchy skin", "how_to_use": "Apply liberally to affected area as needed."}
        ],
        "warning": "See a doctor if: rash spreads rapidly, is accompanied by fever or difficulty breathing, or appears after starting a new medication."
    },
    "heartburn": {
        "urgency": "Low",
        "aliases": ["acid reflux", "indigestion", "chest burning", "gerd", "heartbrun",
                    "heart burn", "acid in throat", "burning chest"],
        "symptoms": ["Burning sensation in chest", "Sour or bitter taste in mouth",
                     "Difficulty swallowing", "Worsened when lying down"],
        "causes": "Stomach acid flows back into esophagus. Triggers include large meals, spicy food, alcohol, caffeine, smoking, or obesity.",
        "meds": [
            {"name": "Omeprazole (Prilosec OTC)", "purpose": "Reduces stomach acid for frequent heartburn", "how_to_use": "20mg once daily before eating for 14 days. Do not exceed 14 days without a doctor."},
            {"name": "Famotidine (Pepcid AC)", "purpose": "Reduces stomach acid for heartburn relief", "how_to_use": "10-20mg 15-60 minutes before eating or at bedtime."},
            {"name": "Antacids (Tums/Rolaids)", "purpose": "Fast-acting relief for mild heartburn", "how_to_use": "Chew 2-4 tablets as symptoms occur."}
        ],
        "warning": "See a doctor if: heartburn occurs more than twice a week, you have difficulty swallowing, or symptoms persist despite medication."
    },
    "diarrhea": {
        "urgency": "Low",
        "aliases": ["loose stool", "watery stool", "runs", "diarrhoea", "diarrea",
                    "frequent bathroom", "loose bowels"],
        "symptoms": ["Loose or watery stools", "Frequent bowel movements", "Abdominal cramping",
                     "Nausea", "Signs of dehydration"],
        "causes": "Viral gastroenteritis, food poisoning, bacterial infection, food intolerance, medications, or irritable bowel syndrome.",
        "meds": [
            {"name": "Loperamide (Imodium)", "purpose": "Slows intestinal movement to reduce diarrhea", "how_to_use": "4mg initially, then 2mg after each loose stool. Max 8mg/day for adults."},
            {"name": "Bismuth Subsalicylate (Pepto-Bismol)", "purpose": "Reduces diarrhea and stomach upset", "how_to_use": "30ml or 2 tablets every 30-60 minutes. Max 8 doses/day."},
            {"name": "Oral Rehydration Salts (Pedialyte)", "purpose": "Replenishes fluids and electrolytes", "how_to_use": "Sip slowly throughout the day. Essential to prevent dehydration."},
            {"name": "Probiotics (Culturelle/Align)", "purpose": "Restores healthy gut bacteria", "how_to_use": "1 capsule daily with or without food."}
        ],
        "warning": "See a doctor if: diarrhea lasts more than 2 days, you see blood in stool, have a fever above 102F, or show signs of severe dehydration."
    },
    "insomnia": {
        "urgency": "Low",
        "aliases": ["cant sleep", "trouble sleeping", "sleeplessness", "insomia",
                    "not sleeping", "sleep issues", "waking up at night", "can't sleep"],
        "symptoms": ["Difficulty falling asleep", "Waking up frequently at night",
                     "Waking up too early", "Daytime fatigue", "Difficulty concentrating"],
        "causes": "Stress, anxiety, depression, irregular sleep schedule, caffeine, screen time, or pain.",
        "meds": [
            {"name": "Melatonin (0.5-5mg)", "purpose": "Regulates sleep cycle helps with falling asleep", "how_to_use": "Take 30-60 minutes before bed. Start with lowest dose 0.5mg."},
            {"name": "Diphenhydramine (ZzzQuil/Unisom)", "purpose": "Short-term sleep aid", "how_to_use": "25-50mg 30 minutes before bedtime. Use occasionally only not every night."},
            {"name": "Valerian Root (supplement)", "purpose": "Natural sleep aid may reduce time to fall asleep", "how_to_use": "300-600mg taken 30 minutes to 2 hours before bedtime."},
            {"name": "Magnesium Glycinate (supplement)", "purpose": "Promotes relaxation and may improve sleep quality", "how_to_use": "200-400mg taken 1 hour before bedtime."}
        ],
        "warning": "See a doctor if: insomnia persists more than a few weeks, significantly affects daily functioning, or is accompanied by depression or anxiety."
    },
    "eye irritation": {
        "urgency": "Low",
        "aliases": ["red eyes", "itchy eyes", "dry eyes", "pink eye", "eye pain",
                    "eye redness", "eyes hurt", "conjunctivitis", "eye discharge"],
        "symptoms": ["Redness in the white of the eye", "Itching or burning",
                     "Watery discharge", "Gritty feeling", "Sensitivity to light"],
        "causes": "Allergies, dry air, contact lens irritation, viral conjunctivitis, bacterial infection, or exposure to chemicals.",
        "meds": [
            {"name": "Artificial Tears (Visine/Refresh)", "purpose": "Lubricates and soothes dry or irritated eyes", "how_to_use": "1-2 drops in affected eye(s) as needed up to 4 times daily."},
            {"name": "Ketotifen Eye Drops (Zaditor/Alaway)", "purpose": "Relieves allergy-related itchy eyes", "how_to_use": "1 drop in each eye twice daily every 8-12 hours."},
            {"name": "Tetrahydrozoline (Visine Original)", "purpose": "Reduces eye redness quickly", "how_to_use": "1-2 drops up to 4 times daily. Do not use for more than 3 days continuously."}
        ],
        "warning": "See a doctor if: vision changes, severe eye pain, significant yellow/green discharge, injury to the eye, or symptoms do not improve within 48 hours."
    },
    "toothache": {
        "urgency": "Moderate",
        "aliases": ["tooth pain", "tooth ache", "dental pain", "jaw pain", "tooth hurts", "toothace"],
        "symptoms": ["Sharp or throbbing tooth pain", "Pain when biting or chewing",
                     "Sensitivity to hot or cold", "Swollen gums", "Jaw swelling"],
        "causes": "Tooth decay, cracked tooth, exposed root, gum disease, tooth abscess, or grinding teeth.",
        "meds": [
            {"name": "Ibuprofen (Advil)", "purpose": "Most effective OTC for dental pain reduces inflammation", "how_to_use": "200-400mg every 4-6 hours with food."},
            {"name": "Acetaminophen (Tylenol)", "purpose": "Pain relief when ibuprofen is not suitable", "how_to_use": "500-1000mg every 4-6 hours as needed."},
            {"name": "Orajel (Benzocaine Gel)", "purpose": "Topical numbing directly on the tooth/gum", "how_to_use": "Apply small amount directly to affected area every 4 hours as needed."},
            {"name": "Clove Oil", "purpose": "Natural numbing agent for temporary tooth pain relief", "how_to_use": "Dab small amount on cotton ball and apply to affected tooth/gum."}
        ],
        "warning": "See a dentist as soon as possible. Seek emergency care for severe face or jaw swelling or high fever which are signs of dental abscess."
    },
    "back pain": {
        "urgency": "Low to Moderate",
        "aliases": ["lower back pain", "upper back pain", "backache", "back ache",
                    "spine pain", "back hurts", "back is killing me"],
        "symptoms": ["Dull aching in lower or upper back", "Sharp pain when bending or lifting",
                     "Stiffness", "Pain radiating to legs", "Muscle spasms"],
        "causes": "Muscle strain from lifting, poor posture, prolonged sitting, herniated disc, sciatica, or arthritis.",
        "meds": [
            {"name": "Ibuprofen (Advil/Motrin)", "purpose": "Reduces back inflammation and pain", "how_to_use": "200-400mg every 4-6 hours with food."},
            {"name": "Naproxen (Aleve)", "purpose": "Longer-lasting anti-inflammatory for back pain", "how_to_use": "220mg every 8-12 hours with food."},
            {"name": "Acetaminophen (Tylenol)", "purpose": "Pain relief without anti-inflammatory effect", "how_to_use": "500-1000mg every 4-6 hours. Do not exceed 3000mg/day."},
            {"name": "Topical Voltaren Gel (Diclofenac)", "purpose": "OTC topical anti-inflammatory applied directly to back", "how_to_use": "Apply 2g to affected area 4 times daily. Wash hands after."},
            {"name": "Lidocaine Patches (Salonpas)", "purpose": "Numbs localized back pain area", "how_to_use": "Apply one patch to painful area for up to 8-12 hours."}
        ],
        "warning": "See a doctor if: pain follows a fall or injury, accompanied by leg weakness or numbness, loss of bladder or bowel control, fever, or is severe and constant at rest."
    },
    "dehydration": {
        "urgency": "Low to Moderate",
        "aliases": ["dehydrated", "not drinking enough water", "thirsty", "dry mouth",
                    "dizzy from heat", "heat exhaustion", "dehidration"],
        "symptoms": ["Extreme thirst", "Dry mouth and lips", "Dark yellow urine or no urination",
                     "Dizziness", "Fatigue", "Headache"],
        "causes": "Inadequate fluid intake, excessive sweating, vomiting, diarrhea, fever, or hot weather.",
        "meds": [
            {"name": "Oral Rehydration Salts (Pedialyte)", "purpose": "Replenishes water electrolytes and glucose", "how_to_use": "Sip slowly over 4 hours. Better than plain water for moderate dehydration."},
            {"name": "Sports Drinks (Gatorade/Powerade)", "purpose": "Replenishes electrolytes and fluids for mild dehydration", "how_to_use": "Drink throughout the day."},
            {"name": "Water", "purpose": "Essential for rehydration", "how_to_use": "Drink small sips frequently. Adults need 8+ cups daily."},
            {"name": "Electrolyte Tablets (Nuun)", "purpose": "Convenient electrolyte replacement dissolved in water", "how_to_use": "Dissolve 1 tablet in 16oz water. Drink as needed."}
        ],
        "warning": "Seek emergency care for: confusion, no urination for 8+ hours, sunken eyes, rapid breathing, or inability to keep fluids down. Severe dehydration requires IV fluids."
    },
    "depression": {
        "urgency": "Moderate - See a doctor",
        "aliases": ["feeling depressed", "sad all the time", "no motivation", "feel hopeless",
                    "depressed", "depression symptoms", "feeling empty", "cant get out of bed",
                    "feel worthless", "depresion", "i feel depressed", "feeling down",
                    "nothing makes me happy", "lost interest in everything"],
        "symptoms": ["Persistent sadness or empty feeling", "Loss of interest in activities once enjoyed",
                     "Fatigue and low energy", "Changes in appetite or weight",
                     "Sleep problems (too much or too little)", "Difficulty concentrating",
                     "Feelings of worthlessness or guilt", "Thoughts of death or suicide"],
        "causes": "Combination of genetics, brain chemistry imbalances (serotonin, dopamine), trauma, chronic stress, grief, isolation, chronic illness, or hormonal changes.",
        "meds": [
            {"name": "St. John's Wort (supplement)", "purpose": "Natural herb with mild antidepressant effects for mild-to-moderate depression", "how_to_use": "300mg three times daily with meals. Takes 4-6 weeks. Do NOT combine with prescription antidepressants."},
            {"name": "Omega-3 Fatty Acids (Fish Oil)", "purpose": "Supports brain health and may reduce depression symptoms", "how_to_use": "1000-2000mg EPA+DHA daily with food."},
            {"name": "Vitamin D3 (supplement)", "purpose": "Low vitamin D is linked to depression", "how_to_use": "1000-2000 IU daily with a meal containing fat."},
            {"name": "Magnesium Glycinate (supplement)", "purpose": "Supports mood regulation and reduces anxiety-related depression", "how_to_use": "200-400mg daily preferably in the evening."},
            {"name": "SSRIs / SNRIs - Rx required", "purpose": "Prescription antidepressants (Prozac, Zoloft, Lexapro) are the most effective treatment", "how_to_use": "Requires a doctor prescription. Takes 4-8 weeks to work. Do not stop suddenly."}
        ],
        "warning": "Seek immediate help if you have thoughts of suicide or self-harm. Call or text 988 (Suicide and Crisis Lifeline) anytime. See a doctor or therapist — depression is a medical condition that responds well to professional treatment."
    },
    "anxiety": {
        "urgency": "Low to Moderate",
        "aliases": ["anxious", "panic attack", "nervousness", "worried all the time",
                    "anxety", "feeling anxious", "panic", "stressed out", "constant worry",
                    "racing thoughts", "fear", "overthinking", "anxiety attack",
                    "heart racing from stress", "cant stop worrying"],
        "symptoms": ["Excessive worry or fear that is hard to control", "Racing heartbeat",
                     "Sweating and trembling", "Shortness of breath", "Chest tightness",
                     "Difficulty concentrating", "Irritability", "Muscle tension",
                     "Sleep problems", "Avoiding situations due to fear"],
        "causes": "Genetics, brain chemistry, chronic stress, trauma, major life changes, caffeine overuse, lack of sleep, or underlying medical conditions.",
        "meds": [
            {"name": "L-Theanine (supplement)", "purpose": "Natural amino acid that promotes calm without drowsiness", "how_to_use": "100-200mg as needed. Often combined with magnesium for better effect."},
            {"name": "Magnesium Glycinate (supplement)", "purpose": "Calms the nervous system and reduces physical anxiety symptoms", "how_to_use": "200-400mg daily preferably in the evening."},
            {"name": "Ashwagandha (supplement)", "purpose": "Adaptogen herb that reduces cortisol stress hormone levels", "how_to_use": "300-600mg daily with food. Takes 4-8 weeks for full effect."},
            {"name": "Valerian Root (supplement)", "purpose": "Natural calming herb for mild anxiety and sleep disruption", "how_to_use": "300-600mg up to 3 times daily as needed."},
            {"name": "Chamomile (supplement or tea)", "purpose": "Mild calming effect for general anxiety", "how_to_use": "400-1600mg supplement daily or 1-2 cups of chamomile tea as needed."},
            {"name": "SSRIs / Buspirone - Rx required", "purpose": "Prescription medications are most effective for anxiety disorders", "how_to_use": "Requires a doctor prescription. Therapy (CBT) combined with medication is the gold standard."}
        ],
        "warning": "See a doctor if anxiety significantly interferes with daily life, work, or relationships. Seek immediate help for panic attacks with chest pain. Call 988 if anxiety leads to thoughts of self-harm."
    },
    "stress": {
        "urgency": "Low",
        "aliases": ["stressed", "overwhelmed", "burnt out", "burnout", "too much stress",
                    "work stress", "stres", "feeling stressed", "under pressure", "exhausted mentally",
                    "mentally exhausted", "i am stressed"],
        "symptoms": ["Headaches", "Muscle tension especially neck and shoulders", "Fatigue",
                     "Irritability or mood swings", "Difficulty sleeping",
                     "Stomach upset", "Difficulty concentrating", "Feeling overwhelmed"],
        "causes": "Work pressure, relationship problems, financial stress, major life changes, health concerns, or chronic overcommitment.",
        "meds": [
            {"name": "Ashwagandha (supplement)", "purpose": "Reduces cortisol and supports stress resilience", "how_to_use": "300-600mg daily with food. Effects build over 4-8 weeks."},
            {"name": "Magnesium Glycinate (supplement)", "purpose": "Replenishes magnesium depleted by stress promotes relaxation", "how_to_use": "200-400mg daily in the evening."},
            {"name": "L-Theanine (supplement)", "purpose": "Promotes calm focus without sedation", "how_to_use": "100-200mg as needed during stressful periods."},
            {"name": "Rhodiola Rosea (supplement)", "purpose": "Adaptogen that improves stress tolerance and reduces fatigue", "how_to_use": "200-400mg daily in the morning. Avoid taking in the evening."},
            {"name": "B-Complex Vitamins", "purpose": "Supports nervous system function and energy during stress", "how_to_use": "1 B-complex tablet daily with food."}
        ],
        "warning": "See a doctor if stress leads to depression, panic attacks, physical symptoms like chest pain, or you use alcohol or substances to cope. Chronic unmanaged stress increases risk of heart disease and high blood pressure."
    },
    "ptsd": {
        "urgency": "Moderate - See a doctor",
        "aliases": ["trauma", "traumatic stress", "flashbacks", "nightmares from trauma",
                    "post traumatic stress", "ptsd symptoms", "traumatized", "bad memories",
                    "reliving trauma", "post traumatic"],
        "symptoms": ["Flashbacks or intrusive memories of traumatic event", "Nightmares",
                     "Severe anxiety when reminded of trauma", "Emotional numbness",
                     "Avoiding people or places related to trauma",
                     "Hypervigilance (always feeling on guard)", "Irritability",
                     "Difficulty sleeping", "Feeling detached from others"],
        "causes": "Exposure to traumatic events such as combat, sexual assault, accidents, natural disasters, or childhood abuse. Not everyone who experiences trauma develops PTSD.",
        "meds": [
            {"name": "Omega-3 Fatty Acids (Fish Oil)", "purpose": "Supports brain recovery and may reduce PTSD symptom severity", "how_to_use": "1000-2000mg EPA+DHA daily with food."},
            {"name": "Magnesium Glycinate (supplement)", "purpose": "Reduces hyperarousal and supports sleep", "how_to_use": "200-400mg in the evening."},
            {"name": "Ashwagandha (supplement)", "purpose": "Reduces stress response and anxiety associated with PTSD", "how_to_use": "300-600mg daily with food."},
            {"name": "SSRIs (Sertraline/Paroxetine) - Rx required", "purpose": "FDA-approved prescription medications for PTSD", "how_to_use": "Requires prescription. Most effective when combined with trauma-focused therapy such as EMDR or CPT."}
        ],
        "warning": "PTSD requires professional treatment. Therapy such as EMDR and Cognitive Processing Therapy is the most effective approach. Call 988 if you have thoughts of suicide. Veterans can contact the Veterans Crisis Line: 988 then press 1."
    },
    "bipolar disorder": {
        "urgency": "Moderate - See a doctor",
        "aliases": ["bipolar", "manic depression", "mood swings extreme", "mania",
                    "manic episode", "bipolr", "extreme mood swings", "bipolar symptoms",
                    "i think i am bipolar"],
        "symptoms": ["Extreme mood swings between highs mania and lows depression",
                     "During mania: decreased need for sleep, racing thoughts, impulsivity",
                     "During depression: sadness, fatigue, hopelessness",
                     "Irritability", "Poor decision making during manic episodes"],
        "causes": "Genetics play a strong role. Brain chemistry differences. Triggered or worsened by stress, sleep disruption, substance use, or major life events.",
        "meds": [
            {"name": "Omega-3 Fatty Acids (Fish Oil)", "purpose": "May help stabilize mood as an add-on to prescription treatment", "how_to_use": "1000-2000mg EPA+DHA daily with food."},
            {"name": "Magnesium (supplement)", "purpose": "Supports mood stability and sleep", "how_to_use": "200-400mg daily in the evening."},
            {"name": "Mood Stabilizers (Lithium/Valproate) - Rx required", "purpose": "Prescription medications are essential for managing bipolar disorder", "how_to_use": "Requires a psychiatrist prescription and regular blood monitoring."}
        ],
        "warning": "Bipolar disorder requires professional psychiatric care. Do not rely on supplements alone. Never stop prescribed medications without a doctor guidance. Seek emergency help for severe manic episodes or suicidal thoughts. Call 988 for crisis support."
    },
    "ocd": {
        "urgency": "Low to Moderate - See a doctor",
        "aliases": ["obsessive compulsive", "intrusive thoughts", "compulsions", "ocd symptoms",
                    "repeating behaviors", "obsessive thoughts", "checking things repeatedly",
                    "o.c.d", "cant stop repeating things"],
        "symptoms": ["Unwanted intrusive and repetitive thoughts (obsessions)",
                     "Repetitive behaviors to reduce anxiety (compulsions) such as handwashing checking counting",
                     "Significant distress and time lost to rituals",
                     "Difficulty functioning at work or in relationships"],
        "causes": "Genetics, brain chemistry (serotonin dysregulation), and environmental factors. Often begins in childhood or early adulthood. Stress can worsen symptoms.",
        "meds": [
            {"name": "Inositol (supplement)", "purpose": "Supports serotonin signaling may reduce OCD symptoms mildly", "how_to_use": "12-18g daily in divided doses in powder form mixed in water. Takes weeks to show effect."},
            {"name": "N-Acetyl Cysteine NAC (supplement)", "purpose": "May reduce compulsive behaviors by modulating glutamate", "how_to_use": "600-1800mg daily with food. Takes 8-12 weeks to evaluate effectiveness."},
            {"name": "SSRIs (Fluvoxamine/Sertraline) - Rx required", "purpose": "First-line prescription treatment for OCD", "how_to_use": "Requires psychiatrist prescription. ERP therapy combined with SSRIs is most effective."}
        ],
        "warning": "OCD is best treated with Exposure and Response Prevention (ERP) therapy combined with medication. See a psychiatrist or psychologist. OTC supplements are supportive only and do not replace professional treatment."
    },
    "adhd": {
        "urgency": "Low - See a doctor for diagnosis",
        "aliases": ["attention deficit", "cant focus", "hyperactive", "adhd symptoms",
                    "trouble concentrating", "add", "attention deficit disorder",
                    "easily distracted", "forgetful", "i think i have adhd",
                    "always losing things", "cant sit still"],
        "symptoms": ["Difficulty sustaining attention on tasks", "Easily distracted",
                     "Forgetfulness in daily activities", "Difficulty organizing tasks",
                     "Hyperactivity and restlessness", "Impulsivity",
                     "Procrastination", "Often losing things"],
        "causes": "Genetics (highly heritable), differences in brain development and dopamine regulation. Not caused by parenting or diet alone though these can worsen symptoms.",
        "meds": [
            {"name": "Caffeine (moderate use)", "purpose": "Mild stimulant that can temporarily improve focus", "how_to_use": "1-2 cups of coffee or tea in the morning. Avoid afternoon use to protect sleep."},
            {"name": "Omega-3 Fatty Acids (Fish Oil)", "purpose": "Supports brain function with some evidence for mild ADHD symptom reduction", "how_to_use": "1000-2000mg EPA+DHA daily with food."},
            {"name": "L-Theanine + Caffeine combo", "purpose": "Improves calm focus without jitteriness", "how_to_use": "100-200mg L-theanine paired with 100mg caffeine. Available as combined supplements."},
            {"name": "Zinc and Magnesium (supplements)", "purpose": "Deficiencies in both are common in ADHD and supplementing may help", "how_to_use": "Zinc 15-25mg daily with food. Magnesium 200-400mg daily in the evening."},
            {"name": "Stimulants (Adderall/Ritalin) - Rx required", "purpose": "Prescription stimulants are the most effective ADHD treatment", "how_to_use": "Requires evaluation and prescription from a doctor."}
        ],
        "warning": "ADHD diagnosis requires professional evaluation. OTC options provide minimal support only. See a doctor for proper assessment and treatment options including behavioral therapy and medication."
    },
    "grief": {
        "urgency": "Low - Supportive care",
        "aliases": ["grieving", "loss of loved one", "mourning", "bereavement",
                    "someone died", "lost a family member", "coping with death", "grieve",
                    "lost someone", "someone i love died"],
        "symptoms": ["Intense sadness and crying", "Feelings of emptiness or numbness",
                     "Disbelief or denial", "Anger or guilt", "Fatigue",
                     "Changes in sleep and appetite", "Withdrawing from others",
                     "Longing for the person who died"],
        "causes": "Natural response to loss of a loved one, end of a relationship, job loss, or major life change. Grief is a normal human experience not a disorder.",
        "meds": [
            {"name": "Melatonin (supplement)", "purpose": "Supports sleep disrupted by grief", "how_to_use": "0.5-5mg 30-60 minutes before bed."},
            {"name": "Magnesium Glycinate (supplement)", "purpose": "Supports nervous system and reduces physical symptoms of stress", "how_to_use": "200-400mg in the evening."},
            {"name": "Omega-3 Fatty Acids", "purpose": "Supports emotional regulation and brain health", "how_to_use": "1000-2000mg daily with food."},
            {"name": "Chamomile Tea", "purpose": "Gentle calming and comfort during emotional distress", "how_to_use": "1-2 cups as needed especially in the evening."}
        ],
        "warning": "Grief is normal and takes time. Seek professional support such as a grief counselor or therapist if grief is overwhelming your daily function for months. Call 988 if grief leads to thoughts of suicide or self-harm."
    },
    "eating disorder": {
        "urgency": "High - See a doctor",
        "aliases": ["anorexia", "bulimia", "binge eating", "not eating", "eating too much",
                    "food restriction", "purging", "eating disoder", "body image issues",
                    "scared of food", "i think i have an eating disorder"],
        "symptoms": ["Restrictive eating or fear of gaining weight (anorexia)",
                     "Binge eating followed by purging (bulimia)",
                     "Obsession with food weight calories or body image",
                     "Distorted body image", "Social withdrawal around food",
                     "Physical signs: fatigue dizziness hair loss dental erosion"],
        "causes": "Complex combination of psychological, genetic, social, and cultural factors. Often linked to anxiety, perfectionism, trauma, or societal pressure around body image.",
        "meds": [
            {"name": "Multivitamin with Iron", "purpose": "Replenishes nutrients depleted from restrictive eating", "how_to_use": "One daily multivitamin with food. Not a substitute for proper treatment."},
            {"name": "Omega-3 Fatty Acids", "purpose": "Supports brain health and mood", "how_to_use": "1000mg daily with food."},
            {"name": "Electrolyte Supplements (Pedialyte)", "purpose": "Replenishes electrolytes if intake is very low", "how_to_use": "As needed especially if dizzy or weak."}
        ],
        "warning": "Eating disorders are serious and can be life-threatening. Please seek professional help immediately. Contact the National Alliance for Eating Disorders helpline: 1-866-662-1235. Call 911 for fainting, irregular heartbeat, or extreme weakness."
    },
    "loneliness": {
        "urgency": "Low - Supportive care",
        "aliases": ["lonely", "isolated", "no friends", "feel alone", "social isolation",
                    "feeling lonely", "lonley", "nobody cares", "feel disconnected",
                    "i have no one", "i feel alone"],
        "symptoms": ["Persistent feeling of being alone even around others",
                     "Feeling misunderstood or disconnected", "Low motivation",
                     "Sadness", "Physical fatigue", "Difficulty reaching out to others"],
        "causes": "Life transitions such as moving or divorce, social anxiety, remote work, limited social opportunities, or depression. Chronic loneliness increases risk of depression and anxiety.",
        "meds": [
            {"name": "Vitamin D3 (supplement)", "purpose": "Low vitamin D is linked to low mood common in those who spend little time outdoors", "how_to_use": "1000-2000 IU daily with a fatty meal."},
            {"name": "Omega-3 Fatty Acids", "purpose": "Supports mood and brain health", "how_to_use": "1000-2000mg daily with food."},
            {"name": "Ashwagandha (supplement)", "purpose": "Reduces stress and social anxiety that can worsen loneliness", "how_to_use": "300-600mg daily with food."}
        ],
        "warning": "If loneliness leads to depression or thoughts of self-harm please reach out to a mental health professional or call 988. Consider joining community groups volunteering or online communities. Therapy can help build social confidence."
    }
}

MEDICAL_QA = {
    "what causes allergies": "Allergies occur when the immune system overreacts to harmless substances like pollen, dust, pet dander, or food. The body releases histamine causing sneezing, itching, and runny nose.",
    "what is anaphylaxis": "Anaphylaxis is a severe life-threatening whole-body allergic reaction. It causes airway tightening and drop in blood pressure and can be fatal without immediate epinephrine and emergency care.",
    "what causes asthma": "Asthma is caused by airway inflammation and narrowing triggered by allergens, exercise, cold air, smoke, stress, or respiratory infections.",
    "what are hives": "Hives (urticaria) are raised itchy red welts on the skin caused by an allergic reaction. They turn white when pressed and can appear anywhere on the body.",
    "difference between cold and flu": "The flu comes on suddenly with high fever, severe body aches, and extreme fatigue. Colds develop gradually with milder symptoms mainly affecting the nose and throat.",
    "how to treat fever at home": "Rest, stay hydrated, take acetaminophen or ibuprofen to reduce fever, use a cool damp cloth on forehead. See a doctor for fever above 103F or lasting more than 3 days.",
    "what is heartburn": "Heartburn (acid reflux) is a burning sensation in the chest caused by stomach acid flowing back into the esophagus. Triggers include large meals, spicy food, alcohol, and lying down after eating.",
    "how to treat diarrhea": "Stay hydrated with Pedialyte or water. Take loperamide (Imodium) for adults. Avoid dairy and fatty foods. Eat bland foods such as bananas, rice, applesauce, and toast.",
    "what causes back pain": "Back pain most commonly comes from muscle strain, poor posture, lifting incorrectly, herniated disc, or prolonged sitting. Most cases improve with rest, OTC pain relievers, and gentle movement.",
    "how to treat a cold": "Rest, stay hydrated, use saline nasal spray, take OTC cold medications for symptom relief. Antibiotics do not work on colds since they are viral. Most colds resolve in 7-10 days.",
    "what is depression": "Depression is a medical condition causing persistent sadness, loss of interest, fatigue, and other symptoms. It is caused by brain chemistry imbalances, genetics, trauma, or stress. It responds well to therapy and medication.",
    "what is anxiety": "Anxiety is excessive worry or fear that interferes with daily life. It causes racing heartbeat, sweating, and difficulty concentrating. Therapy and medication are the most effective treatments.",
    "what is ptsd": "PTSD (Post-Traumatic Stress Disorder) develops after experiencing or witnessing traumatic events. Symptoms include flashbacks, nightmares, and hypervigilance. Trauma-focused therapy is the most effective treatment.",
    "what is adhd": "ADHD (Attention Deficit Hyperactivity Disorder) is a neurodevelopmental condition causing difficulty with attention, impulse control, and hyperactivity. It is highly heritable and responds well to medication and behavioral therapy.",
    "how to deal with stress": "Manage stress through regular exercise, adequate sleep, limiting caffeine, mindfulness or meditation, social connection, and setting boundaries. Supplements like ashwagandha and magnesium can provide mild support.",
    "what is bipolar disorder": "Bipolar disorder causes extreme mood swings between mania (high energy, impulsivity) and depression (low mood, fatigue). It requires professional psychiatric care and mood stabilizing medications."
}

def initialize_database():
    print(f"Database initialized. {len(MOCK_DB)} conditions loaded. Today's date: {date.today()}")
    return True