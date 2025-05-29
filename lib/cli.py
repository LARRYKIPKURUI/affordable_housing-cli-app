from helpers import (
    add_agent, list_agents, delete_agent,
    add_client, list_clients, delete_client,
    add_house, list_houses,
    assign
)
from debug import Session, init_db

def run_cli():
    init_db()  # Ensure tables are created

    with Session() as session:  # Using session for entire CLI process
        while True:
            print("\n->> AFFORDABLE HOUSING <<-")
            print("1. Add Agent")
            print("2. List Agents")
            print("3. Delete Agent")
            print("4. Add Client")
            print("5. List Clients")
            print("6. Delete Client")
            print("7. Add House")
            print("8. List Houses")
            print("9. Assign Agent to Client for House")
            print("10. Exit")

            choice = input("Choose option: ")

            if choice == "1":
                name = input("Agent name: ")
                add_agent(session, name)
            elif choice == "2":
                list_agents(session)
            elif choice == "3":
                agent_id = int(input("Agent ID to delete: "))
                delete_agent(session, agent_id)
            elif choice == "4":
                name = input("Client name: ")
                phone = input("Phone: ")
                email = input("Email: ")
                add_client(session, name, phone, email)
            elif choice == "5":
                list_clients(session)
            elif choice == "6":
                client_id = int(input("Client ID to delete: "))
                delete_client(session, client_id)
            elif choice == "7":
                location = input("Location: ")
                rooms = int(input("No. of rooms: "))
                amount = int(input("Amount: "))
                add_house(session, location, rooms, amount)
            elif choice == "8":
                list_houses(session)
            elif choice == "9":
                agent_id = int(input("Agent ID: "))
                client_id = int(input("Client ID: "))
                house_id = int(input("House ID: "))
                assign(session, agent_id, client_id, house_id)
            elif choice == "10":
                print("Goodbye")
                break
            else:
                print("Invalid option.")

if __name__ == "__main__":
    run_cli()