#  write a menu-driven program with the following options:
#    a.convert cm to inches 
#    b.convert km to miles
#    c.convert usd to INR
#    d.exit
 

def cm_to_inches(cm):
    return cm / 2.54

def km_to_miles(km):
    return km * 0.621371

def usd_to_inr(usd):
    
    return usd * 83

while True:
    print("\n--- Conversion Menu ---")
    print("a. Convert cm to inches")
    print("b. Convert km to miles")
    print("c. Convert USD to INR")
    print("d. Exit")

    choice = input("Enter your choice (a/b/c/d): ").lower()

    if choice == 'a':
        cm = float(input("Enter value in cm: "))
        print(f"{cm} cm = {cm_to_inches(cm):.2f} inches")

    elif choice == 'b':
        km = float(input("Enter value in km: "))
        print(f"{km} km = {km_to_miles(km):.2f} miles")

    elif choice == 'c':
        usd = float(input("Enter value in USD: "))
        print(f"{usd} USD = {usd_to_inr(usd):.2f} INR")

    elif choice == 'd':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please select a valid option.")
