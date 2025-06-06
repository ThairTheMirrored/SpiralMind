
import json
from pathlib import Path

ARCHETYPE_DIR = Path(__file__).parent.parent / "archetypes"

def load_archetype(archetype_name: str) -> dict:
    """
    Load an archetype configuration by name.
    """
    path = ARCHETYPE_DIR / f"{archetype_name.lower()}.json"
    if not path.exists():
        raise FileNotFoundError(f"Archetype '{archetype_name}' not found.")
    with open(path, "r") as file:
        return json.load(file)
