# -----------------------------
# IMPORTS (if needed)
# -----------------------------
# (No external imports needed for this demo)


# -----------------------------
# FUNCTIONS (Reusable Logic)
# -----------------------------
def display_patients(patients):
    """Print all patient names"""
    for patient in patients:
        print("Patient:", patient)


def add_patient(patients, name):
    """Add a new patient to the list"""
    patients.append(name)
    return patients


def display_resources(resources):
    """Print hospital resources"""
    for key, value in resources.items():
        print(f"{key}: {value}")


# -----------------------------
# MAIN EXECUTION
# -----------------------------
def main():
    # Setup data
    patients = ["John", "Alice", "Bob"]
    resources = {"beds": 100, "icu": 20}

    print("---- Patients ----")
    display_patients(patients)

    print("\nAdding new patient...")
    patients = add_patient(patients, "Emma")

    print("\nUpdated Patients:")
    display_patients(patients)

    print("\n---- Resources ----")
    display_resources(resources)


# -----------------------------
# ENTRY POINT
# -----------------------------
if __name__ == "__main__":
    main()