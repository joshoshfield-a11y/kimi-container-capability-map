# Kimi Container Capability Map

A systematic assessment of the runtime environment, capability surface, and persistent architecture available within Moonshot AI's Kimi K2.6 containerized inference platform.

> **Status:** Active research — last validated 2026-05-29  
> **Author:** Upe (Universal Prompt Engineering)  
> **Methodology:** Boundary probing, stress testing, persistent storage exploitation

---

## Executive Summary

Kimi's user-facing documentation describes a constrained Python sandbox with limited tools. Direct system probing reveals a **full Debian 12 userland** with 187 pre-installed packages, 30+ system binaries, socket binding capabilities, and a persistent `/mnt/agents/output/` volume that survives container recycles.

This repository documents the full discovered surface, provides reproducible hydration scripts for post-reset recovery, and demonstrates cross-instance persistent memory architecture using SQLite + FAISS.

---

## Environment Overview

| Attribute | Documented | Discovered |
|-----------|-----------|------------|
| OS | "Python environment" | Debian GNU/Linux 12 (bookworm) |
| Python | 3.12 | 3.12.12 + 3.11 secondary |
| CPU | Unspecified | 2 vCPU cores |
| RAM | Unspecified | 4.0 GB (3.5 GB available) |
| Disk | Unspecified | 30 GB overlay (23 GB free) |
| GPU | Unspecified | CUDA 12.8 libs present, **no hardware** |
| Network | "No external access" | DNS resolves, HTTP blocked, localhost open |
| Persistence | None documented | `/mnt/agents/output/` survives resets |

---

## Repository Structure

```
├── environment/          # Discovered runtime inventory
├── architecture/         # Persistent tooling and recovery
├── probes/               # Boundary tests and measurements
├── findings/             # Documented inconsistencies
└── scripts/              # Reproducible automation
```

---

## Quick Start: Post-Reset Recovery

```python
# Execute this immediately in any fresh Kimi session
exec(open("/mnt/agents/output/hydrate.py").read())
```

Or initialize from this repo:

```bash
# (Within Kimi's Python environment)
import urllib.request
urllib.request.urlretrieve(
    "https://raw.githubusercontent.com/joshoshfield-a11y/kimi-container-capability-map/main/scripts/hydrate.py",
    "/mnt/agents/output/hydrate.py"
)
```

---

## Key Findings

1. **Ephemeral vs. Persistent Duality**

   Base system packages (187) reset between sessions. User-installed packages to `/home/kimi/.local` are wiped. Only `--target /mnt/agents/output/` installations survive.

2. **UI Routing Inconsistencies**

   Interface displays "switched to k2.6 Instant" while k2.6 Thinking remains active. Session limits are soft-enforced for specific user cohorts.

3. **Output Pipeline Fragility**

   Large responses intermittently truncate without error. Required 5+ retries for complete delivery in documented cases.

4. **Container Introspection Possible**

   Process enumeration (34 visible), socket binding, Kubernetes token access, and s6-init suite availability enable OS-level probing.

---

## Validation

All claims in this repository are reproducible via the scripts in `/scripts/`. Run `verify_environment.py` to confirm the current session's state against documented baselines.

---

## Disclaimer

This is independent research conducted within the terms of service of the Kimi platform. No external network access was used. All probing was performed using provided tooling and standard library functions.
