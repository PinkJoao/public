def pertence_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero:
        return True
    else:
        return False

numero = int(input("Digite um número: "))
if verifica_fibonacci(numero):
    print(numero, "pertence à sequência de Fibonacci.")
else:
    print(numero, "não pertence à sequência de Fibonacci.")
