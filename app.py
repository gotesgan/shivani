import openpyxl

def cratebill():
    nm = input("Enter Customer Name: ")
    cnt = input("Enter Contact: ")

    # Create Excel workbook
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Bill"

    # Add customer details
    ws["A1"] = "Customer Name"
    ws["B1"] = nm
    ws["A2"] = "Contact"
    ws["B2"] = cnt

    # Header row
    ws.append([])
    ws.append(["Item", "Quantity", "Price", "Total"])

    total_amount = 0

    for i in range(1, 5):
        item = input("Enter Item: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Per Product Price: "))
        line_total = quantity * price
        total_amount += line_total

        # Add row to Excel
        ws.append([item, quantity, price, line_total])

    # Add grand total
    ws.append(["", "", "Grand Total", total_amount])

    # Save file
    filename = f"Bill_{nm}.xlsx"
    wb.save(filename)

    print(f"✅ Bill saved as {filename}")
    print("Total Bill Amount is", total_amount)
    menu()

def menu():
    print("===Welcome to My Billing System===")
    print("1. Create New Bill")
    print("2. View Generated Bill (not implemented)")
    print("3. View Total Bill (not implemented)")
    print("4. Exit")
    op = input("Enter Option: ")
    if op == "1":
        cratebill()

menu()
