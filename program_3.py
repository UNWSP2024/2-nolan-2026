    # By Nolan Nelsen
    # Written on 1/30/2026
    # Total Purchase

def calculate_total_purchase():
    # A customer in a store is purchasing five items.
    # Write a program that asks for each item,
    # then displays the subtotal of the sale,
    # the amount of sales tax, and the total.
    # Assume the sales tax is 7 percent.
    item1 = 25
    item2 = 40
    item3 = 5
    item4 = 15
    item5 = 25

    subtotal = item1 + item2 + item3 + item4 + item5
    sales_tax = 0.07
    total = subtotal * (1 + sales_tax)

    print('Subtotal = ' + str(subtotal))
    print('Sales tax = 7%')
    print('Total = ' + str(total))

calculate_total_purchase()
