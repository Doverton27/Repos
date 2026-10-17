"""Project Two: Haunted Mansion Adventure."""

# David Overton


def show_instructions():
    """Display the game instructions."""
    print("Welcome to Haunted Mansion Adventure!")
    print("Collect all six items before entering the Master Bedroom.")
    print("Avoid the Ghost until you have collected every item.")
    print("Move commands: go north, go south, go east, go west")
    print("To collect an item, type: get item name")
    print("Example: get book")


def show_status(current_room, inventory, rooms):
    """Display the player's current location and inventory."""
    print("\nYou are in the", current_room)
    print("Inventory:", inventory)

    if "item" in rooms[current_room]:
        print("You see a", rooms[current_room]["item"])

    print("------------------------------")


def main():
    """Run the main gameplay loop."""

    rooms = {
        "Foyer": {
            "north": "Study",
            "west": "Library",
            "east": "Kitchen",
            "south": "Ballroom",
        },
        "Library": {"east": "Foyer", "item": "Book"},
        "Study": {"south": "Foyer", "east": "Master Bedroom", "item": "Map"},
        "Kitchen": {"west": "Foyer", "south": "Dining Room", "item": "Key"},
        "Dining Room": {"north": "Kitchen", "item": "Candle"},
        "Ballroom": {"north": "Foyer", "south": "Basement", "item": "Crystal"},
        "Basement": {"north": "Ballroom", "item": "Lantern"},
        "Master Bedroom": {"west": "Study"},
    }

    current_room = "Foyer"
    inventory = []

    show_instructions()

    while True:
        # Check the win or loss condition.
        if current_room == "Master Bedroom":
            if len(inventory) == 6:
                print("\nYou collected all six items!")
                print("You defeated the Ghost. You win!")
            else:
                print("\nThe Ghost catches you!")
                print("You entered the Master Bedroom without all six items.")
                print("GAME OVER!")
            break

        show_status(current_room, inventory, rooms)

        command = input("Enter your move: ").lower().strip()

        if command.startswith("go "):
            direction = command[3:].strip()

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can't go that way!")

        elif command.startswith("get "):
            requested_item = command[4:].strip()

            if "item" in rooms[current_room]:
                room_item = rooms[current_room]["item"]

                if requested_item == room_item.lower():
                    inventory.append(room_item)
                    del rooms[current_room]["item"]
                    print("You collected the", room_item)
                else:
                    print("That item is not available in this room!")
            else:
                print("There is no item to collect in this room!")

        else:
            print("Invalid command. Use 'go direction' or 'get item name'.")

    print("\nThanks for playing Haunted Mansion Adventure!")


if __name__ == "__main__":
    main()
