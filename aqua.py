def g_ltr(gal):
    ltr = gal * 3.78541
    return ltr
  
gal = float(input("Type how many gallons: "))

ltr = g_ltr(gal)

print(f"{gal} gallons is equal to {ltr} liters.")
