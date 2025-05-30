# --- Demo Code for BankAccount class ---
from bankaccount import BankAccount
# Create accounts
acc1 = BankAccount("Alice", 800.0)
acc2 = BankAccount("Bob", 1200.0)
acc3 = BankAccount("Alice", 800.0)
acc4 = BankAccount("Charlie", 300.0)

# Test __repr__ / __str__
print("Accounts:")
print(acc1)
print(acc2)
print(acc3)

# Test __eq__ (same owner and balance)
print("\nEquality:")
print("acc1 == acc3:", acc1 == acc3)  # True
print("acc1 == acc2:", acc1 == acc2)  # False
print("acc1 == 800:", acc1 == 800)    # True
print("acc1 == ('Alice', 800):", acc1 == ("Alice", 800))  # True

# Test __ne__
print("\nInequality:")
print("acc1 != acc2:", acc1 != acc2)  # True

# Test __gt__ (based on balance)
print("\nGreater Than:")
print("acc2 > acc1:", acc2 > acc1)  # True
print("acc4 > acc1:", acc4 > acc1)  # False

# Test __lt__, __ge__, __le__
print("\nOther comparisons:")
print("acc1 < acc2:", acc1 < acc2)  # True
print("acc2 >= acc1:", acc2 >= acc1)  # True
print("acc4 <= acc1:", acc4 <= acc1)  # True

# Test __add__ (same owner)
print("\nAdd:")
acc5 = acc1 + acc3
print("acc5 (Alice + Alice):", acc5)

# Test __add__ (different owners)
acc6 = acc1 + acc2
print("acc6 (Alice + Bob):", acc6)

# Test __add__ with number
acc7 = acc1 + 200
print("acc1 + 200:", acc7)

# Test __sub__ with another account
acc8 = acc2 - acc1
print("acc2 - acc1:", acc8)

# Test __sub__ with number
acc9 = acc2 - 500
print("acc2 - 500:", acc9)

# Test __getitem__
print("\nGet item:")
print("acc1['owner']:", acc1['owner'])
print("acc1[1]:", acc1[1])  # balance

# Test __iter__
print("\nIterating acc1:")
for info in acc1:
    print(info)

# Test __len__
print("\nLength of acc1:", len(acc1))

# Test class method
print("\nBank address:", BankAccount.get_bank_address())

# Test static method
print("\nHighest balance:", BankAccount.highest_balance(acc1, acc2, acc4))
