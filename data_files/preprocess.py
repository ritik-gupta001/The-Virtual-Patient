import json

with open('csvjson.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

output = []
for item in data:
    text = item['text']
    persona = text.split('\n')[0].split(':')[1].strip()
    patient_dialogue = []
    for line in text.split('\n'):
        if line.strip().startswith("**Patient**:"):
            patient_dialogue.append(line.replace("**Patient**:", "").strip())
    output.append({"persona": persona, "responses": patient_dialogue})

with open('patient_dataset.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=2)
