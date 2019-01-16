i = 0
comas = 0
space = 0
points = 0
mayusculas = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Ñ", "Z", "X", "C", "V", "B", "N", "M", ]
capital_letter = 0

user_input = input("cuentame tu vida")
for i in user_input:
   if i in mayusculas:
       capital_letter += 1

print(f"Mayusculas: {capital_letter}")

