#Pfund practice questions   SEC(A)-044
con=eval(input("press 1 for Marksheet\npress 2 for odd or even identifier\npress 3 for vowel identifier\npress 4 for Area of circle calculater\npress 5 for Calculator\n"))
if con==1:
    s1=eval(input("Enter the marks of subject 1:\n"))
    s2=eval(input("Enter the marks of subject 2:\n"))
    s3=eval(input("Enter the marks of subject 3:\n"))
    s4=eval(input("Enter the marks of subject 4:\n"))
    s5=eval(input("Enter the marks of subject 5:\n"))
    tot= s1+s2+s3+s4+s5
    per= tot/500 * 100
#this is the subject grading
    if s1>=50 and s1<101:
        print({s1},"pass in English")
    else:
        print({s1},"fail in English")
    if s2>=50 and s2<101:
        print({s2},"pass in Maths")
    else:
        print({s2},"fail in Maths")
    if s3 >= 50 and s3<101:
        print({s3}, "pass in History")
    else:
        print({s3}, "fail in History")
    if s4>=50 and s4<101:
        print({s4},"pass in Science")
    else:
        print({s4},"fail in Science")
    if s5>=50 and s5<101:
        print({s5},"pass in Islamiat")
    else:
        print({s5},"fail in Islamiat")
#This is percentage based grading
    print("you scored ",tot,"out  of 500")
    if per>=85 and per<=100:
        print("Outstanding\nYou got A+ grade with",{per},"\b%")
    elif per>=70 and per<=101:
        print("Excellent\nYou got A grade with",{per},"\b%")
    elif per>=60 and per<=101:
        print("Good\nYou got B grade with",{per},"\b%")
    elif per>=50 and per<=101:
        print("You got C grade with",{per},"\b%")
    else:
        print("You Failed with",{per},"\b%")
elif con==2:
    CH=eval(input("Enter a No: "))
    if CH%2==0:
        print("No is  Even")
    else:
        print("No is odd")
elif con==3:
    CH=input("Enter an alphabet").upper()
    if CH=="A" or CH=="E" or CH=="I" or CH=="O" or CH=="U":
        print("Character is a Vowel")
    else:
        print("Character is a Consonant")
elif con==4:
    PI  = 3.14
    rad=eval(input("Enter the radius of your circle\n"))
    if rad>=0:
        tot= PI * pow(rad,2)
        print("The Area of your  circle is : ",{tot})
    else:
        print("Invalid Radius")
elif con==5:
    x,y=eval(input("Enter value for X\n")),eval(input("Enter value for Y\n"))
    opp=eval(input("Press 1 for Addition\nPress 2 for Subtraction\nPress 3 for Multiplication\nPress 4 for Division\nPress 5 for Exponent\n"))
    if opp==1:
        z=x+y
        print({x}," + ",{y}," = ",{z})
    elif opp==2:
        z=x-y
        print({x}," - ",{y}," = ",{z})
    elif opp==3:
        z=x*y
        print({x}," * ",{y}," = ",{z})
    elif opp==4:
        z=x/y
        print(f'{x}," / ",{y}," = ",{z:.2f}')
    elif opp==5:
        z=x**y
        print({x}," ** ",{y}," = ",{z})
    else:
        print("Invalid Input")
else:
    print("Invalid input")