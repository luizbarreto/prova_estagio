def is_fibonacci(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    if b == num or num == 0:
        return True
    return False

# Número a ser verificado
num = int(input("Informe um número: "))

if is_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
