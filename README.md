def fibonacci_sequence(n):
    # Initialize the sequence with the first two terms
    sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to the nth term
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    
    return sequence

def main():
    # input the value of n
    n = int(input("Enter the number of terms for the Fibonacci sequence: "))
    
    # Generate the Fibonacci sequence
    fibonacci_seq = fibonacci_sequence(n)
    
    # Print the generated Fibonacci sequence
    print("Fibonacci sequence up to term", n, ":", fibonacci_seq)

if __name__ == "__main__":
    main()
