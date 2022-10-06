#======================================
#Nombre del estudiante: Paula Rodríguez
#Carnet: 20221110264
#======================================
digits=[]
is_repunit=True
number=input("Please enter an integer number greater than 0: ")
while not number.isnumeric() or int(number)<1:
    print("Invalid input.")
    number=input("Please enter an integer number greater than 0: ")
for x in number:
    x=int(x)
    digits.append(x)
for y in digits:
    if digits[0]!=y:
        is_repunit=False
        break
if is_repunit:
    print(f"The number {number} is repunit.")
else:
    print(f"The number {number} is not repunit.")