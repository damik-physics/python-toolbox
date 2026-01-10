#!/usr/bin/env python3
print(f"Importing {__name__}")
from .storage import load_cards, save_cards


def add_card() -> None:
    """
    Create new flashcard by prompting front and back description. 
    Saves updated card list.
    """
    cards = load_cards()
    front = input("Front side: ").strip()
    if not front:
        print("Front side cannot be empty.")
        return
        
    back = input("Back side: ").strip()
    if not back:
        print("Back side cannot be empty.")
        return
      
    cards[front] = back
    save_cards(cards)
    print("Card added.")
     


def remove_card() -> None:
    """
    Remove card by its numeric index and update JSON file.
    Error printing for invalid index.
    """
    cards = load_cards()
    if not cards: 
        print("No cards available.")
        return 

    keys = list(cards)
    for i, k in enumerate(keys, start=1): 
        print(f"{i}. {k}: {cards[k]}")

    try: 
        idx = int(input("Card index to remove: ").strip())
    except ValueError:
        print("Index must be a number.")
        return 
        
    if idx < 1 or idx > len(keys):
        print("Index out of range.") 
        return 
    
    removed_key = keys[idx - 1]
    removed_value = cards.pop(removed_key)
    save_cards(cards)
    print(f'Removed: "{removed_key}: {removed_value}"') 


def view_stack() -> None:
    """
    Display all cards with their numeric index.
    """
    cards = load_cards()
    if not cards:
        print("No cards stored.")
        return

    for i, (front, back) in enumerate(cards.items(), start=1):
        print(f"{i}. {front}: {back}")


def quiz_me() -> None:
    """
    Run an interactive quiz session over the stored cards.
    """
    cards = load_cards()
    if not cards:
        print("No cards to quiz.")
        return

    for front, back in cards.items():
        ans = input(f"{front}: ").strip()
        if ans.lower() == back.lower():
            print("Correct.")
        else:
            print(f"Wrong. Correct: {back}")


def main() -> None:
    """
    Main menu loop for the flashcard CLI application.
    """
    while True:
        print("\n1. Add card\n2. Remove card\n3. View cards\n4. Quiz\n5. Exit")
        choice = input("Choose: ").strip() or "1"

        if choice == "1":
            add_card()
        elif choice == "2":
            remove_card()
        elif choice == "3":
            view_stack()
        elif choice == "4":
            quiz_me()
        elif choice == "5" or choice.lower() == "q":
            break
        else:
            print("Invalid choice.")
