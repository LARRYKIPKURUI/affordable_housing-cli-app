from helpers import (
    add_agent, list_agents, delete_agent,
    add_client, list_clients,
    add_house, list_houses,
    assign
)

def run_cli():
    while True:
        print("\n->> AFFORDABLE HOUSING <<-")
        print("1. Add Agent")
        print("2. List Agents")
        print("3. Delete Agent")
        print("4. Add Client")
        print("5. List Clients")
        print("6. Add House")
        print("7. List Houses")
        print("8. Assign Agent to Client for House")
        print("9. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            name = input("Agent name: ")
            add_agent(name)
        elif choice == "2":
            list_agents()
        elif choice == "3":
            agent_id = int(input("Agent ID to delete: "))
            delete_agent(agent_id)
        elif choice == "4":
            name = input("Client name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            add_client(name, phone, email)
        elif choice == "5":
            list_clients()
        elif choice == "6":
            location = input("Location: ")
            rooms = int(input("No. of rooms: "))
            amount = int(input("Amount: "))
            add_house(location, rooms, amount)
        elif choice == "7":
            list_houses()
        elif choice == "8":
            agent_id = int(input("Agent ID: "))
            client_id = int(input("Client ID: "))
            house_id = int(input("House ID: "))
            assign(agent_id, client_id, house_id)
        elif choice == "9":
            print("Goodbye")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_cli()
