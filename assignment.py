#the variuble a is the users input number

def calculate_pi(iterations):
    return 4 * sum((-1)**a / (2*a + 1) for a in range(iterations))

if __name__ == "__main__":
    while True:
        a = input(" ")
        
        if not a.isdigit() or int(a) < 1:

            
            print("Error put in a positive number no negatives or decimals")  #This is the test case for positive numbers for this asignment
            continue

        iterations = int(a)
        pi = calculate_pi(iterations)


        print(f"{pi:.5f}")