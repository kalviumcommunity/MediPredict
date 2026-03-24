# FOR LOOP EXAMPLE
print("---- FOR LOOP ----")

patients = ["John", "Alice", "Bob", "Emma"]

for patient in patients:
    print("Patient:", patient)


# WHILE LOOP EXAMPLE
print("\n---- WHILE LOOP ----")

count = 1

while count <= 5:
    print("Count:", count)
    count += 1   # important to avoid infinite loop


# BREAK EXAMPLE
print("\n---- BREAK ----")

for num in range(1, 10):
    if num == 5:
        print("Stopping at", num)
        break
    print(num)


# CONTINUE EXAMPLE
print("\n---- CONTINUE ----")

for num in range(1, 6):
    if num == 3:
        continue   # skip 3
    print(num)