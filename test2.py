def Monthly__Payment(pricipal,annual_interst_rate,duration):
    pricipal = float(pricipal)
    annual_interst_rate = float(annual_interst_rate)
    duration = float(duration)
    number_Monthly_payment = duration*12
    if annual_interst_rate ==0:
        Monthly_payment = priciple/number-Monthly_payment
        print("Your Monthly Payment : ",Monthly_payment)
    else:
        Monthly_Rate = ((annual-interst_rate/100)/12)
        phase1 = 1+Monthly_Rate
        phase2 = phasel**number_Monthly_payment
        phase3 = Monthly_Rate*phase2
        phase4 = pricipal*phase3
        phase5 = phase2-1
        Monthly_Payment = phase4/phase5
        print("Your Monthly Paymrnt : ",Monthly_Payment)


 pricipal = input("Enter priciple : ")
 annual_interst_rate= input("Enter annual_interst_rate : ")
 duration = input("Enter duration :)
 Monthly__payment(pricipal,annual_interst_rate,duration)                 
