"""
    Name: Patricia Gariando
    Student ID: 991 446 494
    Summary: Assignment 2
    Date: Oct. 29 2023 
"""
# HEADERS 
menuTitle = """
=================================================================
=           S A L E S P E R S O N     H I S T O R Y             =
================================================================="""

salesTitle = """
=================================================================
=                   S A L E S     T A B L E                     =
================================================================="""

commsTitle = """
=================================================================
=             C O M M I S S I O N S     T A B L E               =
================================================================="""

# Lists
salespersonId = ["ID", "Tables", "Desks", "Chairs"]
salespersonComm = ["ID", "Tables", "Desks", "Chairs"] 

# Counters
totalTableSales = totalDeskSales = totalChairSales = totalTableComm = totalDeskComm = totalChairComm = 0

# Display Title and prompt the user 
print(menuTitle)
id = int(input("Enter salesperson ID or -1 to end: "))

while id != -1:
    if id > 0: 
        salespersonId.append(id)
        salespersonComm.append(id)
        # prompt the user for table sales 
        tables = int(input("Enter table sales: "))
        while tables < 0: tables = int(input("Invalid: Enter valid table sales: "))
        else:
            salespersonId.append(tables)
            totalTableSales += tables
            # determine how much a commission was made 
            if tables < 500:
                salespersonComm.append(10)
                totalTableComm += 10
            elif tables < 1000:
                salespersonComm.append(20)
                totalTableComm += 20
            elif tables < 1500:
                salespersonComm.append(30)
                totalTableComm += 30
            else:
                salespersonComm.append(40)
                totalTableComm += 40
        # prompt the user for desk sales
        desks = int(input("Enter desk sales: "))
        while desks < 0: desks = int(input("Invalid: Enter valid desk sales: "))
        else: 
            salespersonId.append(desks)
            totalDeskSales += desks
            # determine how much a commission was made
            if desks < 500:
                salespersonComm.append(20)
                totalDeskComm += 20
            elif desks < 1000:
                salespersonComm.append(30)
                totalDeskComm += 30
            elif desks < 1500:
                salespersonComm.append(40)
                totalDeskComm += 40
            else:
                salespersonComm.append(50)
                totalDeskComm += 50
        # prompt the user for chair sales
        chairs = int(input("Enter chair sales: "))
        while chairs < 0: chairs = int(input("Invalid: Enter valid chair sales: "))
        else:
            salespersonId.append(chairs)
            totalChairSales += chairs
            # determine how much a commission was made
            if chairs < 500:
                salespersonComm.append(30)
                totalChairComm += 30
            elif chairs < 1000:
                salespersonComm.append(40)
                totalChairComm += 40
            elif chairs < 1500:
                salespersonComm.append(50)
                totalChairComm += 50
            else:
                salespersonComm.append(60)
                totalChairComm += 60 
    id = int(input("\nEnter salesperson ID or -1 to end: "))

salespersonId.append("Total")
salespersonId.append(totalTableSales)
salespersonId.append(totalDeskSales)
salespersonId.append(totalChairSales)

salespersonComm.append("Total")
salespersonComm.append(totalTableComm)
salespersonComm.append(totalDeskComm)
salespersonComm.append(totalChairComm)

print(salesTitle) # Sales Table 
count = 0
for row in range(0, len(salespersonId)):
    print("|".ljust(5), salespersonId[row], end="\t")
    count += 1
    if count%4 == 0: print("|")

print(commsTitle) # Commissions Table
count = 0
for row in range(0, len(salespersonComm)):
    print("|".ljust(5), salespersonComm[row], end="\t")
    count += 1
    if count%4 == 0: print("|")

# always show name and ID  
print("\nPatricia Gariando: 991 446 494\n")