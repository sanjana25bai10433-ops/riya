a = int(input("Entered your age:"))

if(a>18):
    print("you are above the age of consent")
    print("good for you")

elif(a<0):
    print("you are entering a invalid age")

elif(a==0):
    print("you are entering 0 which is not a valid age")

else:
    print("you are below the age of consent")
    print("end of program")