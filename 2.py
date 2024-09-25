def is_fibonacci(n):
    def is_perfect_square(x):
        return int(x**0.5)**2 == x

    def is_fibonacci_number(n):
        return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

    if is_fibonacci_number(n):
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."

# Teste
numero = 34  # Altere o número conforme necessário
print(is_fibonacci(numero))
