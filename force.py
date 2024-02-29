print("Newton's second law of motion.")

#Determine the missing value
print("Select the missing value:")
print("1.Mass (m)")
print("2.Acceleration (a)")
print("3.Force (F)")
missing_value_choice = input("Enter the option number for the missing value:")

#prompt the user to enter the other two values
if missing_value_choice == "1":
    a = float(input("enter acceleration (a): "))
    F = float(input("enter force(F): "))
    m = F / a
    print(f"Mass (m) = {m} Kg")

elif missing_value_choice == "2":
    m = float(input("enter mass (m): "))
    F = float(input("enter force(F): "))
    a = F / m
    print(f"Acceleration (a) = {a} m/s**2")

elif missing_value_choice == "3":
    m = float(input("enter mass (m): "))
    a = float(input("enter acceleration (a): "))
    F = m * a
    print(f"Force (f) = {F} N")

else:
    print("Sorry!! Invalid option selected for the missing value choice.Try again")
    