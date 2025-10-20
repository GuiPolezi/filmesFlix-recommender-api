from pathlib import Path

def ensure_dirs():
    # Garantindo que as pastas principais existem
    for path in ["data/raw", "data/processed"]:
        Path(path).mkdir(parents=True, exist_ok=True)