#base = int(input("Enter the base of the triangle: "))

#height = int(input("Enter the height of the triangle: "))

#area = (base * height) / 2

#print(area)

#a = int(input('Enter the side a: '))

#b = int(input('Enter the side b: '))

#c = int(input('Enter the side c: '))

#perimeter = a + b + c

#print('Perimeter is:', perimeter)

float_number = float(input("Enter a floating number: "))
integer = int(input('Enter an integer: '))

print(f'Are the types of {float_number} and {integer} equal?' ) 

if type(float_number) == type(integer):
    print('True')
else:
    print('False')