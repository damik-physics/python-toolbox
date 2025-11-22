import json
from pathlib import Path

CARDS_FILE = Path(__file__).parent / "cards.json"

    
def load_cards() -> dict[str, str]:
    """
    Load cards from the cards.json file.
    Returns an empty dict if the file is missing or invalid JSON.
    """
    try:
        with CARDS_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                return {str(k): str(v) for k, v in data.items()}
            else:
                print("Card file is not a dictionary. Starting fresh.")
                return {}
    except FileNotFoundError:
        print("Card file not found. Creating a new one.")
        return {}
    except json.JSONDecodeError:
        print("Card file is corrupted. Starting with an empty set.")
        return {}
    except ValueError:
        print("Invalid data encountered. Resetting card file.")
        return {}


def save_cards(cards: dict[str, str]) -> None:
    """
    Write input card dictionary to JSON file.
    Create file if not existent. 
    """
    with CARDS_FILE.open("w") as f:
        return json.dump({k: v for k, v in cards.items()}, f, indent = 2)