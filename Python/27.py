from collections import deque

bank = deque(["habib", "anis", "labib"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)

if not bank:
    print("No persion left")