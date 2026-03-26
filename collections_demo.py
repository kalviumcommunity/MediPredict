# LIST EXAMPLE
print("---- LIST ----")
patients = ["John", "Alice", "Bob"]

# Access
print("First patient:", patients[0])

# Modify
patients.append("Emma")
patients[1] = "Alicia"

print("Updated list:", patients)


# TUPLE EXAMPLE
print("\n---- TUPLE ----")
hospital_info = ("City Hospital", "Vellore", 200)

# Access
print("Hospital Name:", hospital_info[0])
print("Location:", hospital_info[1])

# Immutability demonstration
try:
    hospital_info[0] = "New Hospital"
except TypeError as e:
    print("Error (Tuples are immutable):", e)


# DICTIONARY EXAMPLE
print("\n---- DICTIONARY ----")
resource_data = {
    "beds": 120,
    "icu": 30,
    "oxygen": 50
}

# Access
print("ICU beds:", resource_data["icu"])

# Modify
resource_data["beds"] = 150
resource_data["staff"] = 40

print("Updated dictionary:", resource_data)