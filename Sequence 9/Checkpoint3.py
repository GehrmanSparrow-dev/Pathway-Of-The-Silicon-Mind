for i in range(50):
    n = int(input("Enter a number: "))
    if n<2:
        print("Number is not prime")
    else:
        for j in range(2, int(n**0.5) + 1):
            if n % j == 0:
                print("Number is not prime")
                break
        else:
            print("Number is prime")