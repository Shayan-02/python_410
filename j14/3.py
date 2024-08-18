class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # متغیر خصوصی با دو زیرخط

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount < (self.__balance + 1):
            self.__balance -= amount
            print(f"{amount} withdrawn. Remaining balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance


# ایجاد یک حساب بانکی
account = BankAccount("Alice", 1000)

# انجام عملیات
account.deposit(500)
account.withdraw(300)
print(f"Final balance: {account.get_balance()}")

# تلاش برای دسترسی مستقیم به متغیر خصوصی (ناموفق)
# print(account.__balance)  # باعث خطا می‌شود
