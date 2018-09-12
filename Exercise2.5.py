subtotal = eval(input("Subtotal: "))
gratuityRate = eval(input("Gratuity Rate (In Decimal): "))
# Could use subtotal, gratuityRate = eval(input("Please enter the subtotal and gratuity rate. "))
gratuityAmount = subtotal * gratuityRate
total = subtotal + gratuityAmount

print("The gratuity amounts to", gratuityAmount, "and the total will be", total)