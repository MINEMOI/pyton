i = 0
comas = 0
space = 0
points = 0
vocales = ["a", "e", "i", "o", "u",]
capital_letter = 0
used_vocals = []

user_input = input("cuentame tu vida")
for i in user_input:
   if i in vocales:
       used_vocals += [i]

print(format(used_vocals))

