import os
import sys

PERSISTENT_DIR = "/mnt/agents/output/custom_python_env"
SITE_PACKAGES = os.path.join(
    PERSISTENT_DIR, 
    "lib", 
    f"python{sys.version_info.major}.{sys.version_info.minor}", 
    "site-packages"
)

def stabilize_environment():
    """Bind persistent packages to current session."""
    for path in [PERSISTENT_DIR, SITE_PACKAGES]:
        if os.path.exists(path) and path not in sys.path:
            sys.path.insert(0, path)
    
    os.environ["PYTHONPATH"] = f"{PERSISTENT_DIR}:{SITE_PACKAGES}" + (
        f":{os.environ['PYTHONPATH']}" if "PYTHONPATH" in os.environ else ""
    )
    print("✓ Persistent toolkit bound.")

stabilize_environment()
