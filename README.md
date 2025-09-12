# Virtual Patient Persona Generator for Rural Medical VR Training

## Overview

The Government of India seeks to improve medical education in rural areas with limited patient access by investing in a VR training system. This project aims to create realistic, persona-driven virtual patients for such a system, using synthetic doctor-patient conversation scripts to train or fine-tune a dialogue model. The model generates patient responses in various personalities—calm, anxious, rude, overly patient, etc.—to simulate real-life scenarios.

## Video OverView



https://github.com/user-attachments/assets/ff31c31e-9c35-497c-b9a3-43fb1ed732e4


Key goals:
- Train or fine-tune a conversational AI model with provided scripts.
- Support multiple patient personas.
- Use lightweight or quantized models suitable for limited compute (e.g., Ollama with Gemma or LLaMA-based models).
- Provide easy setup, demo, and documentation.

---

## Features

- **Persona-based Response Generation:** Model produces patient replies according to specified personality traits.
- **Lightweight Model Support:** Compatible with quantized models for edge or resource-limited deployment.
- **Extensible Script Input:** Uses synthetic scripts for flexible persona/response adaptation.
  
---

## Setup Instructions

### Prerequisites

- Python 3.8+
- Ollama (for running quantized models locally): [Ollama Installation Guide](https://ollama.com/download)
- Model weights (e.g., Gemma, LLaMA-based) downloaded or accessible
- Required Python packages: `pip install -r requirements.txt`

### Clone the Repository

```bash
git clone https://github.com/ritik-gupta001/ChatBot-With-UI.git
cd ChatBot-With-UI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Ollama Model Server

Ensure Ollama is running and your desired model (e.g., gemma:2b) is available.

```bash
ollama run gemma:2b
```


---

## Usage

- Select a persona (e.g., calm, anxious, rude) in the UI.
- Initiate a doctor-patient conversation.
- Observe model-generated patient responses reflecting chosen persona.

---

## Model Choice and Approach

- **Model Selection:** Gemma-2B or LLaMA-2 7B (quantized) for efficient local inference.
- **Training/Fine-Tuning:** Synthetic scripts are used to tune persona-specific response patterns.
- **Inference:** Persona is set as a context variable, guiding response style.

---

## Challenges & Improvements

- **Challenge:** Achieving high persona fidelity with limited script data.
- **Solution:** Data augmentation and prompt engineering for personality consistency.
- **Challenge:** Running large models on resource-constrained hardware.
- **Solution:** Use quantized models via Ollama and optimize inference pipeline.
- **Possible Improvements:**
  - Expand persona diversity via additional scripts.
  - Integrate multimodal VR cues (emotion, gesture).
  - Deploy as an API for broader VR system integration.

---

## License

[Specify license here]

## Contact

For questions or contributions, open an issue or contact [ritik-gupta001](https://github.com/ritik-gupta001).
