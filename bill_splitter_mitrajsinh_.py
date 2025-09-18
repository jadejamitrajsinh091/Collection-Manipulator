print("welcome to bill splitter app")

while True:

    amount=float(input("enter the bill amount:\n"))

    people=int(input("enter number of people:\n"))

    percent=int(input("enter tip percentage(0/5/10/15/20):\n"))

    if people <=0:
        print("ERROR!,please eneter the number of people")


    tipamount=(percent/100) * amount

    totalamount=amount+tipamount

    perperson=totalamount / people


    print(f"\ntip amount: ${amount}\n")

    print(f"total bill (with tip): ${totalamount}\n")

    print(f"each person should pay: ${perperson}\n")


    repeat=input("Would You Like To Calculate Another Bill? (yes/no):  ")

    if repeat != 'yes':
        print("Thank you for using the Bill Splitter App,VISIT AGAIN!")

        break



    








             
