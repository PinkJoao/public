def inverter(string):
    invertida = ""
    for i in range(len(string) - 1, -1, -1):
        invertida += string[i]
    return invertida

print("String invertida:", inverter(input("Digite uma string: ")))
