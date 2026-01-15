recharges = []

def recharge_airtime():
    phone = input("Enter phone number: ")
    amount = input("Enter recharge amount: ")
    recharges.append({"phone": phone, "amount": amount})
    print("Airtime recharged successfully")

def view_recharges():
    if not recharges:
        print("No recharge records found")
    else:
        for recharge in recharges:
            print("Phone:", recharge["phone"], "- Amount:", recharge["amount"])

def main():
    while True:
        print("1. Recharge Airtime")
        print("2. View Recharges")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            recharge_airtime()
        elif choice == "2":
            view_recharges()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
