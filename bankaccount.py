from typing import override


class BankAccount:
    __bank_address: str = "1 Allenby street, Tel Aviv"
# 1. Constructor
    def __init__(self,owner: str,balance: float ):
        self.__owner = owner
        self.__balance = balance

# 4. Properties (Getters and Setters)
    @ property
    def owner(self):
        return self.__owner

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.balance = value

# 2. Class Variable and Class Method
    @classmethod
    def get_bank_address(cls) -> str:
        return cls.__bank_address

# 3. Static Method
    @staticmethod
    def highest_balance(acc1: "BankAccount", acc2: "BankAccount", acc3: "BankAccount") -> float:
        return max(acc1.balance, acc2.balance, acc3.balance)

# 5. Methods
    def deposit(self, amount: float) -> None:
        if amount >= 0:
            self.balance += amount
        else:
            print("You can't deposit a negative sum of money")

    def withdraw(self, amount: float) -> None:
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            print("You can't withdraw a negative sum of money")

    def is_rich(self) -> bool:
        return self.balance > 1000000

# 6. Operator Overloading
    def __add__(self, other: ("BankAccount",int, float)):
        if isinstance(other, BankAccount):
            if self.owner != other.owner:
                return f"joint: {self.owner} & {other.owner}"
            else:
                return BankAccount(self.owner, self.balance + other.balance)
        elif isinstance(other, (int, float)):
            return BankAccount(self.owner, self.balance + other)
        else:
            raise ValueError("You can't add none numeric value")

    def __sub__(self, other: ("BankAccount", int, float)):
        if isinstance(other, BankAccount):
            return BankAccount(self.owner, self.balance - other.balance)
        elif isinstance(other, (int, float)):
            return BankAccount(self.owner, self.balance - other)
        else:
            raise ValueError("You can't subtract none numeric value")

    @override
    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.owner == other.owner and self.balance == other.balance
        elif isinstance(other, (int, float)):
            return self.balance == other
        elif isinstance(other, tuple):
            return self.owner == other[0] and self.balance == other[1]
        else:
            raise ValueError("You can't compare none numeric values")

    @override
    def __ne__(self, other):
        if isinstance(other, BankAccount):
            return not self.balance == other.balance
        else:
            raise ValueError("You can only compare accounts' balances")

    def __gt__(self, other):
        if isinstance(other, BankAccount):
            return self.balance > other.balance
        else:
            raise ValueError("You can only compare accounts' balances")

    def __ge__(self, other):
        if isinstance(other, BankAccount):
            return self.balance >= other.balance
        else:
            raise ValueError("You can only compare accounts' balances")

    def __lt__(self, other):
        if isinstance(other, BankAccount):
            return self.balance < other.balance
        else:
            raise ValueError("You can only compare accounts' balances")

    def __le__(self, other):
        if isinstance(other, BankAccount):
            return self.balance <= other.balance
        else:
            raise ValueError("You can only compare accounts' balances")

    @override
    def __repr__(self):
        return f"BankAccount(owner={self.owner}, balance={self.balance})"

    @override
    def __str__(self):
        return f"{self.owner}'s account: {self.balance}"

    def __len__(self):
        return round(self.balance)

    def __getitem__(self, key):
        if key == 'owner' or key == 0:
            return self.owner
        elif key == 'balance' or key == 1:
            return self.balance
        else:
            raise KeyError (f"the key: {key} is invalid")

    def __iter__(self):
        yield self.owner
        yield self.balance