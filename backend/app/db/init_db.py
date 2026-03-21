# Simulating a database to keep the architecture clean without needing external files
MOCK_DB = {
    "sore throat": {
        "triage": {
            "urgency_level": "Low (unless accompanied by high fever)",
            "possible_causes": ["viral infection", "allergies", "strep throat"],
            "self_care": ["hydration", "rest", "warm salt water gargle"],
            "when_to_see_doctor": "Symptoms worsen, last > 3 days, or high fever."
        },
        "medications": [
            {
                "name": "Acetaminophen",
                "used_for": "Mild to moderate pain, fever",
                "dosage": "500–1000 mg every 4–6 hours",
                "side_effects": "Rare when taken as directed.",
                "warnings": "Do not exceed daily limit. Avoid alcohol."
            }
        ]
    }
}

def initialize_database():
    print("Database connection initialized. Knowledge base loaded.")