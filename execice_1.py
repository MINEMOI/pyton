i = 0
comas = 0
space = 0
points = 0

user_input = input("cuentame tu vida")
for i in user_input:
    if i == (","):
        comas += 1
    if i == (" "):
        space += 1
    if i == ("."):
        points += 1

print(f"las comas fueron: {comas}")
print()
print(f"los espacios fueron: {space}")
print()
print(f"los puntos fueron: {points}")