# A dictionary linking rooms to connected rooms.

rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}

# Set the player's starting room.
current_room = "Great Hall"

# Continue until the player chooses to exit.
while current_room != "exit":
    # Display the player's current room.
    print("\nYou are in the", current_room)

    # Ask the player for a movement command or exit.
    command = (
        input("Enter your move (go North, go South, go East, go West, or exit): ")
        .lower()
        .strip()
    )

    # Exit the game.
    if command == "exit":
        current_room = "exit"
        print("Thanks for playing!")

    # Handle movement commands.
    elif command.startswith("go "):
        direction = command[3:].strip()

        # Move only if the direction is available in this room.
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
            print("You moved to the", current_room)
        else:
            print("You can't go that way!")

    # Handle invalid commands.
    else:
        print("Invalid command. Please try again.")
