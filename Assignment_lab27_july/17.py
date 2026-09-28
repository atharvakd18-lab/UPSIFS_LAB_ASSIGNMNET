#   write a program that calculate the in hand salary after deducing
#           HRA(10%),DA(5%),PF(3%),and tax based on th following
#           a. salary between 5-10 lakh: 10% taxs
#           b. salary between 11-20 lakh: 20% tax
#           c. salary above 20 lakh: 30% tax
#           d. salary between 0-1 lakh: print 'k'


salary = float(input("Enter your annual salary (in lakhs): "))

if 0 <= salary <= 1:
    print("k")
else:

    hra = 0.10 * salary   # 10% HRA
    da  = 0.05 * salary   # 5% DA
    pf  = 0.03 * salary   # 3% PF

    if 5 <= salary <= 10:
        tax = 0.10 * salary
    elif 11 <= salary <= 20:
        tax = 0.20 * salary
    elif salary > 20:
        tax = 0.30 * salary
    else:
        tax = 0  

    in_hand = salary - (hra + da + pf + tax)

    print(f"In-hand salary after deductions: {in_hand:.2f} lakhs")
