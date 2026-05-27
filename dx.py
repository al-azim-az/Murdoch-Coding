def collatz(num):
    if num <= 0:
        print("Collatz Sequence is only generated for the numbers greater than zero.")
        return

    print("Collatz Sequence:")
    
    while num != 1:
        print(num)
        
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1

    print(1)