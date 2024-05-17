EGY = 1
USD = 47
EUR = 50
GBP = 59
AED = 13

From = input("exchange currency( EGY,USD,EUR,GBP,AED)\n").upper()
amount = int(input("how much of currency\n"))
to = input("the new currency(EGY,USD,EUR,GBP,AED)\n").upper()

if From == "USD" and to == "EGY" :
    amountchanged = amount * USD
    print (amountchanged)
elif From == "EGY"and to == "USD" :
    amountchanged = amount / USD
    print (amountchanged)
elif From == "EUR" and to =="EGY" :
     amountchanged = amount * EUR
     print(amountchanged)
elif From == "GBP" and to ==  "EGY" :
     amountchanged = amount * GBP
     print(amountchanged)
elif From == "EGY" and to == "GBP" :
     amountchanged = amount / GBP.2f
     print (amountchanged)
elif From == "AED" and to == "EGY":
     amountchanged = amount * AED
     print (amountchanged)

else :
     print ("tray again")     

    