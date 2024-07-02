def main():

    numbers = []
    for i in range(5):
        num = int(input("Input a number: "))
        numbers.append(num)
        
    minval = numbers[0]
    maxval = numbers[0]
    
    for num in numbers:
        if num < minval:
            minval = num
        elif num > maxval:
            maxval = num
    """
    ########################################
    Code Your Program here
    ########################################
    """

    print(*numbers)
    print(maxval, minval)
    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, maxval, minval


if __name__ == '__main__':
    main()
