"""Python Programmme to make a Calculator using functions
Author = Jayesh
Date Modified = 20th June 2019"""

from __future__ import print_function

x = input(str('Please input your name: '))
print('Hi There,')
print(x)


print('This is a calculator made using python programming language(3.7.2) and Sublime Text 3\n ')

print(f"{x},"'What type of calculation do you want to perform??\n')

print('NOTE:This calculator takes input and performs operations for integers only.(The output may be in float form )\n')
choice = 'Yes'
while choice == 'Yes' :
    print('1.Arithmetic')
    print('2.Trigonometric')
    print('3.Logarithms')
    print('4.Other')

    choice = input('Enter Choice(1/2/3/4)): ') 
# Python is the worst programming language I have ever seen
    #The below program is for Arithmetical Operations

    if choice == '1': 

        print('There are 7 operations available')

        print('a.Addition')
        print('b.Subtraction')
        print('c.Multiplication')
        print('d.Division')
        print('e.Exponents') 
        print('f.Remainder for division of two numbers')
        print('g.Non-Float Division')

        choice = input('Enter Choice(a/b/c/d/e/f/g): ')

        num1 = int(input('Enter First Number: '))
        num2 = int(input('Enter Second Number: '))

        if choice == 'a':
            sum = int(num1)+int(num2)
            print(sum)
        elif choice == 'b':
            sum = (int(num1)-int(num2))
            print(sum)
        elif choice == 'c':
            sum = (int(num1)*int(num2))
            print(sum)
        elif choice == 'd':
            sum = (int(num1)/int(num2))
            print(sum)
        elif choice == 'e':
            sum = (int(num1)**int(num2))
            print(sum)
        elif choice == 'f':
            sum = (int(num1)%int(num2))
            print(sum)
        elif choice == 'g':
            sum = (int(num1)//int(num2))
            print(sum)
        else: 
            print('Invalid Input')
            
        print('Your Calculation is over')
        print('Thank You')

    #The Below Program is for Trigonometric Operations     

    elif choice == '2':

        print('There are 5 operations available')

        print('a.Cosine to X radians')
        print('b.Sine to x radians')
        print('c.Tangent to x radians')
        print('d.Radians to degrees')
        print('e.Degrees to Radians')
        

        choice = input('Enter Choice(a/b/c/d/e): ')

        num1 = int(input('Enter the Number: '))
        
        if choice == 'a':
            import math
            sum = math.cos(num1)
            print(sum) 
        elif choice == 'b':
            import math
            sum = math.sin(num1)
            print(sum)
        elif choice == 'c':
            import math
            sum = math.tan(num1)
            print(sum)
        elif choice == 'd':
            import math
            sum = math.degree(num1)
            print(sum)
        elif choice == 'e':
            import math
            sum = math.radians(num1)
            print(sum) 
        else: 
            print('Invalid Input')

        print('Your calculation is over')
        print('Thank You')

    #The below program is for Log Operations

    elif choice == '3':

        print('There are 3 operations available')

        print('a.Log to base 2')
        print('b.Log to base 10')
        print('c.Log to base e')
        

        choice = input('Enter Choice(a/b/c): ')

        num1 = int(input('Enter the Number: '))

        if choice == 'a':
            import math
            sum = math.log2(num1)
            print(sum)
        elif choice == 'b':
            import math#Python se acha Java Hai
            sum = math.log2(num1)
            print(sum)
        elif choice == 'c':
            import math
            sum = math.loge(num1)
            print(sum)
        else: 
            print('Invalid Input')

        print('Your calculation is over')
        print('Thank You')

        #The below program is for Other than the above 3 Operations

    elif choice == '4': 

        print('There are 2 operations available')

        print('For factorial, you will be provided with an option for 2nd Number. Please ignore it')

        print('a.Factorial')
        print('b.HCF/GCD')

        choice = input('Enter Choice(a/b): ')

        num1 = int(input('Enter First Number: '))#JavaSript is better than Python
        num2 = int(input('Enter Second Number: '))

        if choice == 'a':
            import math
            sum = math.factorial(num1)
            print(sum)
        elif choice == 'b':
            import math    
            sum = math.gcd(num1,num2)
            print(sum)
        else:
            print('Invalid Input')
    print(f"{x},"'Do you want to continue??')
    print('NOTE:Except "Yes", if any other input is given,')
    print('The loop will break and as a result you will exit the calculator' )
    choice = input('Yes/No: ')
    if choice == 'No':
        print('Thanks'  f"{x}")





