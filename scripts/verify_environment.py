#!/usr/bin/env python3
"""Verify current session matches documented baselines."""

import sys
import os

PERSISTENT_DIR = "/mnt/agents/output/custom_python_env"
if PERSISTENT_DIR not in sys.path:
    sys.path.insert(0, PERSISTENT_DIR)

CHECKS = {
    'base': ['numpy', 'pandas', 'torch', 'scipy', 'matplotlib', 'sklearn'],
    'persistent': ['flask', 'sqlalchemy', 'faiss', 'redis', 'pytest', 'h5py'],
    'system': ['cv2', 'PIL', 'playwright'],
}

def verify():
    print("=" * 50)
    print("ENVIRONMENT VERIFICATION")
    print("=" * 50)
    
    for category, modules in CHECKS.items():
        print(f"\n--- {category.upper()} ---")
        for mod in modules:
            try:
                m = __import__(mod)
                ver = getattr(m, '__version__', 'unknown')
                print(f"  ✓ {mod}: {ver}")
            except ImportError:
                print(f"  ✗ {mod}: MISSING")
    
    print(f"\nPersistent dir mounted: {os.path.exists(PERSISTENT_DIR)}")
    print(f"Python: {sys.version}")
    print("=" * 50)

if __name__ == "__main__":
    verify()
