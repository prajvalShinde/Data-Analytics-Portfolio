accounts = {}

def get_account():
    number = input("Account number: ").strip()
    return number, accounts.get(number)

def create():
    number = input("New account number: ").strip()
    if not number or number in accounts: print("Invalid or existing account"); return
    name = input("Account holder: ").strip()
    accounts[number] = {"name": name, "balance": 0.0}
    print("Account created")

def display():
    for number, account in accounts.items(): print(number, account)
    if not accounts: print("No accounts found")

def search():
    number, account = get_account()
    print(account if account is not None else "Account not found")

def deposit():
    number, account = get_account()
    if account is None: print("Account not found"); return
    amount = float(input("Deposit amount: "))
    if amount <= 0: print("Amount must be positive"); return
    account["balance"] += amount
    print("Balance:", round(account["balance"], 2))

def withdraw():
    number, account = get_account()
    if account is None: print("Account not found"); return
    amount = float(input("Withdrawal amount: "))
    if amount <= 0 or amount > account["balance"]: print("Invalid amount or insufficient balance"); return
    account["balance"] -= amount
    print("Balance:", round(account["balance"], 2))

def balance():
    _, account = get_account()
    print("Balance:", account["balance"] if account is not None else "Account not found")

def transfer():
    sender = input("From account: ").strip()
    recipient = input("To account: ").strip()
    if sender not in accounts or recipient not in accounts or sender == recipient: print("Invalid accounts"); return
    amount = float(input("Transfer amount: "))
    if amount <= 0 or amount > accounts[sender]["balance"]: print("Invalid amount or insufficient balance"); return
    accounts[sender]["balance"] -= amount
    accounts[recipient]["balance"] += amount
    print("Transfer successful")

def update():
    _, account = get_account()
    if account is None: print("Account not found"); return
    account["name"] = input("New holder name: ").strip()
    print("Updated")

def delete():
    number, account = get_account()
    if account is None: print("Account not found"); return
    if account["balance"] != 0: print("Account must have zero balance"); return
    del accounts[number]
    print("Deleted")

def total(): print("Total bank balance:", round(sum(a["balance"] for a in accounts.values()),2))

def main():
    actions = {1:create,2:display,3:search,4:deposit,5:withdraw,6:balance,7:transfer,8:update,9:delete,10:total}
    while True:
        print("\n1.Create 2.Display 3.Search 4.Deposit 5.Withdraw 6.Balance 7.Transfer 8.Update 9.Delete 10.Total 11.Exit")
        try:
            choice = int(input("Choice: "))
            if choice == 11: break
            if choice in actions: actions[choice]()
            else: print("Invalid choice")
        except ValueError: print("Enter valid numeric input")

if __name__ == "__main__": main()
