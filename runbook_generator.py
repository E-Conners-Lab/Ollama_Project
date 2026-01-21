"""
Runbook Generator using Ollama
The Tech-E LLC - Ollama for Network Engineers Lab 5
"""

import ollama


def generate_runbook(scenario: dict) -> str:
    """Generate an operational runbook from a scenario dict."""
    prompt = f"""Create operational runbook for:
    Scenario: {scenario["title"]}
    Devices: {", ".join(scenario["devices"])}
    Trigger: {scenario["trigger"]}
    
    Include: Overview, Diagnostics, Remediation, Verification"""
    
    response = ollama.generate(
        model="llama3.2",
        prompt=prompt,
        options={"temperature": 0.4, "num_ctx": 8192}
    )
    return response["response"]


if __name__ == "__main__":
    scenario = {
        "title": "BGP Peer Flapping on WAN Edge",
        "devices": ["wan-rtr-atl-01", "carrier-pe-01"],
        "trigger": "BGP peer 198.51.100.1 flapping >3x/hour"
    }
    print(generate_runbook(scenario))
