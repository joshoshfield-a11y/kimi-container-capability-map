#!/usr/bin/env python3
"""
Kimi Session Loader — reconstructs knowledge base from GitHub at session start.
Usage: python3 session_loader.py
"""
import urllib.request, json

KB_URL = "https://raw.githubusercontent.com/joshoshfield-a11y/kimi-container-capability-map/main/findings/knowledge_base.json"

def load_kb():
    req = urllib.request.Request(KB_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=10) as resp:
        kb = json.loads(resp.read())
    print(f"Knowledge base loaded: {kb['meta']['version']}")
    print(f"  Created: {kb['meta']['created']}")
    print(f"  Categories: {list(kb.keys())}")
    return kb

def print_section(kb, section):
    if section in kb:
        print(f"\n=== {section.upper()} ===")
        print(json.dumps(kb[section], indent=2))
    else:
        print(f"Section '{section}' not found")

if __name__ == "__main__":
    kb = load_kb()
    # Print summary
    print(f"\nSummary:")
    print(f"  Python packages: {kb['capabilities']['python_packages']['count']}")
    print(f"  Widget features: {len(kb['capabilities']['widget_system']['features'])}")
    print(f"  Active ports: {len(kb['network']['port_map'])}")
    print(f"  API models: {', '.join(kb['api']['verified_endpoints']['models'])}")
