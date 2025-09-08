import subprocess

def query_ollama(prompt):
    result = subprocess.run(
        ["ollama", "run", "virtual-patient"],
        input=prompt.encode(),
        stdout=subprocess.PIPE
    )
    print(result.stdout.decode())

# Example test
#persona = "Anxious"
#prompt = f"Persona: {persona}\nPatient:"
#query_ollama(prompt)


personas = ["Anxious", "Depressed", "Forgetful", "Impatient"]

for p in personas:
    prompt = f"Persona: {p}\nPatient:"
    print(f"--- Testing {p} ---")
    query_ollama(prompt)
    print("\n")
    
# python test_model.py
