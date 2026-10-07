from UsersBase import users
from Electronics import Devices
from Repository import Repo

repo = Repo("mydb.txt")


def ask_email() -> str:
    email = input("Email: ").strip()
    while "@" not in email or "." not in email:
        print("Wrong email, it must contain @ and .")
        email = input("Email: ").strip()
    return email


def register():
    name = input("Name: ").strip()
    email = ask_email()
    phone = input("Phone: ").strip()
    device_type = input("Which device is it for repair (phone, tv, ...): ").strip()
    fault = input("What issue is it: ").strip()
    if not name or not phone or not device_type or not fault:
        print("All fields are required.")
        return
    device = Devices(device_type, fault, email)
    repo.create(users(name, email, phone, device))
    print(f"Saved. {device}")


def search():
    value = input("Enter name, email or phone: ").strip()
    if not value:
        print("Nothing to search.")
        return
    results = repo.search(value)
    if not results:
        print("No results found.")
        return
    for record in results:
        print(
            f"{record.get('name', '-')} | {record.get('email', '-')} | "
            f"{record.get('phone', '-')} | {record.get('id', '-')}"
        )
        device = record.get("device")
        if device:
            print(f"   {device.get('owner', '-')} brought this item for repair at {device.get('brought_at', '-')}")
            print(f"   Device: {device.get('type', '-')} - {device.get('fault', '-')}")


def menu():
    print("\n1) Register")
    print("2) Search")
    print("3) Exit")


def main():
    while True:
        menu()
        choice = input("Press 1, 2 or 3: ").strip()
        if choice == "1":
            register()
        elif choice == "2":
            search()
        elif choice == "3":
            print("Bye.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nBye.")
