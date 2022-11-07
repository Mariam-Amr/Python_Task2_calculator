
'''
Claculator task , 2 operating modes scientific mode (addition, subtraction, devision,
multiplication) and binary mode(binary,hex,oct,dec)
'''

print("/"*40,"Welcome To Your Python Caculator","/"*40)   #welcome message
print("\n")


# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y
	
# This function give you the exponintial result of two numbers
def exponential(x, y):
    return x**y

#This function returns modolus of two numbers
def modolus (x, y):
    return(x & y)
	
#choose the operaition mode
print("."*15,"Select Operation Mode","."*15)
print("1 ------> Scientific Mode")
print("2 ------> Binary Mode")

op_choice = int(input())
#check the operation mode to choose either scientific or binary
if op_choice ==1:
 print("."*15,"a.Add","."*15)         #a for addition
 print("."*15,"s.Subtract","."*15)    #s for subtraction
 print("."*15,"m.Multiply","."*15)    #m for multiplication
 print("."*15,"d.Divide","."*15)      #d for division
 print("."*15,"e.Exponintial","."*15) #e for exponential
 print("."*15,"%.Modolus","."*15)     #% for modolus
 print("\n")
 choice = input("Enter choice(a/s/m/d/e): ")
    # check if choice is one of the four options
 if choice in ('a', 's', 'm', 'd','e'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 'a':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == 's':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == 'm':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == 'd':
            print(num1, "/", num2, "=", divide(num1, num2))   
			
        elif choice=='e':
            print(num1, "**", num2, "=", exponential(num1, num2))
         
        elif choice=='%':
            print(num1, "%", num2, "=", modolus(num1, num2))
					
 else:
     print("Please Enter a Valid Operation")
         		 
else:
  print("-"*5,"Enter your numbers either in decimal,binary,hex,or octal","-"*5)
  print("."*15,"a.Add","."*15)         #a for addition
  print("."*15,"s.Subtract","."*15)    #s for subtraction
  print("."*15,"m.Multiply","."*15)    #m for multiplication
  print("."*15,"d.Divide","."*15)      #d for division
  print("."*15,"&.AND","."*15)         #& AND operation
  print("."*15,"|.OR","."*15)          #| OR  operation
  print("."*15,"~.XOR","."*15)         #~ XOR operation
  choice_2 = input("Enter Your Operation")
  systems= input(" Choose to show your Result in DEC,BIN,HEX, or OCT ")

  print("."*15,"DEC","."*15) 
  print("."*15,"BIN","."*15)
  print("."*15,"HEX","."*15)
  print("."*15,"OCT","."*15) 
  num1=int(input("Enter frist number:"))
  num2=int(input("Enter second number:"))
  
if choice_2 =='a':					
		if systems == "BIN":
			print("result is:",bin(add(num1, num2)))
		elif systems == "HEX":
			print("result is:",hex(add(num1, num2)))
		elif systems == "DEC":
			print("result is:",dec(add(num1, num2)))
		elif systems == "OCT":
			print("result is:",oct(add(num1, num2)))
		else:
			print("please select DEC, BIN,HEX, or OCT  ")
elif choice_2 == 's':						
		if systems == "BIN":
			print("result is:",bin(subtract(num1, num2)))
		elif systems == "HEX":
			print("result is:",hex(subtract(num1, num2)))
		elif systems == "DEC":
			print("result is:",dec(subtract(num1, num2)))
		elif systems == "OCT":
			print("result is:",oct(subtract(num1, num2)))
		else:
			print("please select DEC, BIN,HEX, or OCT  ")

elif choice_2 == 'm':					
		if systems == "BIN":
			print("result is:",bin(multiply(num1, num2)))
		elif systems == "HEX":
			print("result is:",hex(multiply(num1, num2)))
		elif systems == "DEC":
			print("result is:",dec(multiply(num1, num2)))
		elif systems == "OCT":
			print("result is:",oct(multiply(num1, num2)))
		else:
			print("please select DEC, BIN,HEX, or OCT  ")		
elif choice_2 == 'd':					
			if systems == "BIN":
				print("result is:",bin(divide(num1, num2)))
			elif systems == "HEX":
				print("result is:",hex(divide(num1, num2)))
			elif systems == "DEC":
				print("result is:",dec(divide(num1, num2)))
			elif systems == "OCT":
				print("result is:",oct(divide(num1, num2)))
			else:
				print("please select DEC, BIN,HEX, or OCT  ")		
elif choice_2 == '%':						
			if systems == "BIN":
				print("result is:",bin(modolus(num1, num2)))
			elif systems == "HEX":
				print("result is:",hex(modolus(num1, num2)))
			elif systems == "DEC":
				print("result is:",dec(modolus(num1, num2)))
			elif systems == "OCT":
				print("result is:",oct(modolus(num1, num2)))
			else:
				print("please select DEC, BIN,HEX, or OCT  ")		
						
elif choice_2 == "**":					
		if systems == "BIN":
			print("result is:",bin(exponential(num1, num2)))
		elif systems == "HEX":
			print("result is:",hex(exponential(num1, num2)))
		elif systems == "DEC":
			print("result is:",dec(exponential(num1, num2)))
		elif systems == "OCT":
			print("result is:",oct(exponential(num1, num2)))
		else:
			print("please select DEC, BIN,HEX, or OCT  ")			
else :	
	print("Please inter a valid choice")	 


		
