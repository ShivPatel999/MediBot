from datetime import date

MOCK_DB = {
    "headache": {
        "urgency": "Low",
        "meds": [
            {"name": "Acetaminophen (Tylenol)", "purpose": "Pain relief and fever reduction", "how_to_use": "325–650mg every 4–6 hours. Do not exceed 3000mg/day."},
            {"name": "Ibuprofen (Advil/Motrin)", "purpose": "Anti-inflammatory pain relief", "how_to_use": "200–400mg every 4–6 hours with food."}
        ],
        "warning": "Seek emergency care if it's the worst headache of your life, follows head trauma, or comes with confusion/vision changes."
    },
    "sore throat": {
        "urgency": "Low",
        "meds": [
            {"name": "Throat Lozenges (Cepacol)", "purpose": "Temporary numbing and soothing of throat pain", "how_to_use": "Dissolve one slowly in mouth every 2 hours as needed."},
            {"name": "Salt Water Gargle", "purpose": "Natural antiseptic to reduce inflammation", "how_to_use": "Mix 1/2 tsp salt in 8oz warm water, gargle 30 seconds. Do not swallow."}
        ],
        "warning": "See a doctor if you have difficulty breathing/swallowing, fever over 101°F, or symptoms lasting more than 3 days."
    },
    "cold": {
        "urgency": "Low",
        "meds": [
            {"name": "DayQuil / NyQuil", "purpose": "Multi-symptom cold relief (congestion, cough, sore throat)", "how_to_use": "Follow label. DayQuil every 4 hours during day; NyQuil at night."},
            {"name": "Pseudoephedrine (Sudafed)", "purpose": "Nasal decongestant", "how_to_use": "30–60mg every 4–6 hours. Available behind pharmacy counter."}
        ],
        "warning": "See a doctor if fever exceeds 103°F, symptoms worsen after 10 days, or you have difficulty breathing."
    },
    "fever": {
        "urgency": "Moderate",
        "meds": [
            {"name": "Acetaminophen (Tylenol)", "purpose": "Fever and pain reduction", "how_to_use": "325–650mg every 4–6 hours. Do not exceed 3000mg/day."},
            {"name": "Ibuprofen (Advil)", "purpose": "Fever reduction and anti-inflammatory", "how_to_use": "200–400mg every 4–6 hours with food or milk."}
        ],
        "warning": "Seek immediate care if fever is above 103°F, lasts more than 3 days, or is accompanied by stiff neck or rash."
    },
    "stomach ache": {
        "urgency": "Low",
        "meds": [
            {"name": "Pepto-Bismol", "purpose": "Nausea, heartburn, indigestion, upset stomach, diarrhea", "how_to_use": "2 tablets or 30ml every 30–60 minutes as needed. Max 8 doses/day."},
            {"name": "Antacids (Tums/Rolaids)", "purpose": "Heartburn and acid indigestion relief", "how_to_use": "Chew 2–4 tablets as symptoms occur. Do not exceed 15 tablets/day."}
        ],
        "warning": "See a doctor if pain is severe, localized to the lower right side, or accompanied by bloody stool or vomiting."
    },
    "muscle pain": {
        "urgency": "Low",
        "meds": [
            {"name": "Ibuprofen (Advil/Motrin)", "purpose": "Reduces muscle inflammation and pain", "how_to_use": "200–400mg every 4–6 hours with food."},
            {"name": "Topical Bengay / Icy Hot", "purpose": "Localized muscle pain relief", "how_to_use": "Apply thin layer to affected area up to 3–4 times daily. Do not bandage tightly."}
        ],
        "warning": "See a doctor if pain is severe, follows an injury, or doesn't improve after a week of rest."
    },
    "allergy": {
        "urgency": "Low",
        "meds": [
            {"name": "Cetirizine (Zyrtec)", "purpose": "Relieves sneezing, runny nose, itchy/watery eyes from pollen, pet dander, dust", "how_to_use": "10mg once daily. Can be taken day or night."},
            {"name": "Loratadine (Claritin)", "purpose": "Non-drowsy antihistamine for seasonal allergies", "how_to_use": "10mg once daily. Take at the same time each day."},
            {"name": "Fexofenadine (Allegra)", "purpose": "Non-drowsy relief for seasonal allergy symptoms", "how_to_use": "180mg once daily or 60mg twice daily with water. Do not take with fruit juice."},
            {"name": "Fluticasone Nasal Spray (Flonase)", "purpose": "Reduces nasal congestion, sneezing, and runny nose from allergies", "how_to_use": "2 sprays per nostril once daily. Takes a few days for full effect."}
        ],
        "warning": "See a doctor if symptoms are severe, you develop hives or swelling, or OTC medications stop working. Call 911 for signs of anaphylaxis (throat swelling, difficulty breathing)."
    },
    "cough": {
        "urgency": "Low",
        "meds": [
            {"name": "Dextromethorphan (Robitussin DM)", "purpose": "Suppresses dry/persistent cough", "how_to_use": "10–20mg every 4 hours or 30mg every 6–8 hours. Do not exceed 120mg/day."},
            {"name": "Guaifenesin (Mucinex)", "purpose": "Loosens chest congestion and productive cough", "how_to_use": "400mg every 4 hours or 600–1200mg every 12 hours (extended release). Drink plenty of water."}
        ],
        "warning": "See a doctor if cough lasts more than 3 weeks, produces blood, or is accompanied by high fever or shortness of breath."
    },
    "diarrhea": {
        "urgency": "Low",
        "meds": [
            {"name": "Loperamide (Imodium)", "purpose": "Slows intestinal movement to reduce diarrhea", "how_to_use": "4mg initially, then 2mg after each loose stool. Max 8mg/day."},
            {"name": "Bismuth Subsalicylate (Pepto-Bismol)", "purpose": "Reduces diarrhea and stomach upset", "how_to_use": "30ml or 2 tablets every 30–60 minutes. Max 8 doses/day."}
        ],
        "warning": "See a doctor if diarrhea lasts more than 2 days, you see blood in stool, or you show signs of dehydration (extreme thirst, dry mouth, no urination)."
    },
    "insomnia": {
        "urgency": "Low",
        "meds": [
            {"name": "Diphenhydramine (ZzzQuil / Unisom)", "purpose": "Short-term sleep aid", "how_to_use": "25–50mg 30 minutes before bedtime. Only use occasionally, not every night."},
            {"name": "Melatonin", "purpose": "Regulates sleep cycle, helps with falling asleep", "how_to_use": "0.5–5mg taken 30–60 minutes before bed. Start with the lowest dose."}
        ],
        "warning": "See a doctor if insomnia persists more than a few weeks, significantly affects daily life, or is accompanied by anxiety or depression."
    },
    "heartburn": {
        "urgency": "Low",
        "meds": [
            {"name": "Omeprazole (Prilosec OTC)", "purpose": "Reduces stomach acid for frequent heartburn", "how_to_use": "20mg once daily before eating for 14 days. Do not take for more than 14 days without consulting a doctor."},
            {"name": "Famotidine (Pepcid AC)", "purpose": "Reduces stomach acid for heartburn relief", "how_to_use": "10–20mg 15–60 minutes before eating or at bedtime."},
            {"name": "Antacids (Tums)", "purpose": "Fast-acting relief for mild heartburn", "how_to_use": "Chew 2–4 tablets as symptoms occur."}
        ],
        "warning": "See a doctor if heartburn occurs more than twice a week, you have difficulty swallowing, or symptoms persist despite medication."
    }
}

def initialize_database():
    print(f"Database initialized. {len(MOCK_DB)} conditions loaded. Today's date: {date.today()}")
    return True