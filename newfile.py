#maximum of 3 numbers
def max(x,y,z):
	if x>y and x>z:
		print("maximum is :",x)
	elif y>x and y>z:
		print("maximum is :",y)
	else:
		print("maximum is :",z)
max(2,7,6)

#to reverse a string
x=str(input("Enter a string:"))
print("Reverse of the string is:")
print(x[::-1])

# prime or not
num=int(input("enter a number:"))
for i in range(2,num):
	if num %i ==0:
		print(num,"is not a prime number")
		break
	else:
		print(num,"is a prime number")
		
#palindrome or not
try:
	num=int(input("Enter a number:"))
	except Exception as ValueError:
		print('Invalid input enter a integer')	
		else:
			temp=num
			rev=0
			while(num>0):
				dig=num%10
				rev=rev*10+dig
				num=num//10
				if(temp==rev):
					print(' The number is palindrome')
			else:	
			print('Not a palindrome')
			finally:
				print('program executed')
				
#sum of squares of n natural numbers
def squaresum(n):
				return(n*(n+1)*(2*n+1))//6
n= int(input('Enter the number:'))
print(squaresum(n))
				
				