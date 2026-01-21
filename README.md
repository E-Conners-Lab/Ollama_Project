# Ollama for Network Engineers - Lab Files

Companion files for "Ollama for Network Engineers" guide by The Tech-E LLC.

## Setup

```bash
# Create project directory
mkdir -p ~/ollama-projects
cd ~/ollama-projects

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install ollama
```

## Lab 2: Create Custom Model

```bash
# Copy Modelfile-neteng to ~/ollama-models/
mkdir -p ~/ollama-models
cp Modelfile-neteng ~/ollama-models/

# Build the model
cd ~/ollama-models
ollama create neteng -f Modelfile-neteng

# Test it
ollama run neteng "Block SSH and Telnet from 192.168.100.0/24"
```

## Lab 4: ACL Generator

```bash
python acl_generator.py
```

## Lab 5: Runbook Generator

```bash
python runbook_generator.py
```

## Files Included

- `Modelfile-neteng` - Custom Ollama model with Cisco IOS ACL constraints
- `acl_generator.py` - Lab 4 ACL configuration generator
- `runbook_generator.py` - Lab 5 automated runbook creation

## Requirements

- Python 3.8+
- Ollama installed and running (`ollama serve`)
- Models pulled: `ollama pull llama3.2`

## Links

- The Tech-E LLC: https://thetech-e.com
- Ollama: https://ollama.com
