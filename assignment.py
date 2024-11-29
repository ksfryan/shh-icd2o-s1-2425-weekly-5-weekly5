def calculate_pi(iterations):
    return 4 * sum((-1)**i / (2*i + 1) for i in range(iterations))

if __name__ == "__main__":
    

    while True:
        a = input(" ")
        if a.lower() == 'exit':
            
            break

        

        iterations = int(a)
        pi = calculate_pi(iterations)
        print(f"{iterations} iterations:{pi:.10f}")