import json

with open('patient_dataset.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

output_lines = []

for entry in data:
    persona = entry['persona']
    for response in entry['responses']:
        prompt = f"Persona: {persona}\nPatient:"
        output = {
            "prompt": prompt,
            "response": response
        }
        output_lines.append(output)

# Save as JSONL (one JSON object per line)
with open('formatted_dataset.jsonl', 'w', encoding='utf-8') as f:
    for item in output_lines:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

