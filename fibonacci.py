def generate_fibonacci_sequence(limit):
    (a, b) = 0, 1
    fibonacci_sequence = [a]
    while b <= limit:
        fibonacci_sequence.append(b)
        a, b = b, a + b
    return fibonacci_sequence

def get_limit_from_user():
    while True:
        try:
            limit = int(input("Ingrese el número límite para la secuencia de Fibonacci: "))
            return limit
        except ValueError:
            print("Por favor, ingrese un número válido.")

def print_sequence(sequence, limit):
    print(f"Secuencia de Fibonacci hasta el número {limit}:")
    print(sequence)

def main():
    limit = get_limit_from_user()
    result = generate_fibonacci_sequence(limit)
    print_sequence(result, limit)

if __name__ == "__main__":
    main()
