#AFVINKOPDRACHT 2 - OPDRACHT 4
#Morgan Atmodimedjo BIN1a

b = 1
bedrag = 0
while b < 6:
    print("product nummer ", b)
    product = float(input("voer de prijs van uw product in "))
    prod = product * 1.07
    bedrag = bedrag + prod
    b = b + 1
print(bedrag)
