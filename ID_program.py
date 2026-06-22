import uuid

class IDCard:
    def __init__(self, name, role):
        self.id_number = str(uuid.uuid4())[:8].upper()
        self.name = name
        self.role = role

    def show(self):
        print(f"\n--- ID CARD ---")
        print(f"ID:   {self.id_number}")
        print(f"NAME: {self.name}")
        print(f"ROLE: {self.role}")
        print(f"---------------\n")

def run_program():
    ids = []

    while True:
        print("1.Create a neew ID")
        print("2.View All IDs")
        print("3.Exit")

        choice = input("Select an option (1-3): ")

        if choice == '1':
            name = input("Enter Name: ")
            role = input("Enter Role: ")
            new_card = IDCard(name, role)
            ids.append(new_card)
            print(f"ID created for {name}!")

        elif choice == '2':
            if not ids:
                print("\nNo IDs found.\n")
            for card in ids:
                card.show()

        elif choice == '3':
            print("Exit")
            break

        else:
            print("Invalid choice, try again!")


run_program()

