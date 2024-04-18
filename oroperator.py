salary=int(input("salry="))
age=int(input("age="))
if(salary>=20000 or age<=25):
    loan=int(input("loan amount="))
    if(loan>50000):
        print("maximum 50000")
    else:
        print("you are eligible")
else:
    print("you are not eligible")
 
