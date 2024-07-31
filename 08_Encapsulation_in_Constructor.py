# Without Encapsulation
class BankAccount:
    pass

# Object creation
account = BankAccount()
account.account_number = "123456789"
account.balance = 1000

# Directly modifying the balance
account.balance += 500
print(f"Balance after deposit: {account.balance}")

account.balance -= 200
print(f"Balance after withdrawal: {account.balance}")


