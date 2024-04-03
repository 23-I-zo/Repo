def sum_of_digits(n):  #"n" is the parameter
    if n < 10 :        # Base case: if n is a single digit number, return n or in the base case the function terminates
        return n
    else:       #Recursive case: 
        last_digit = n % 10     #get the last digit of n
        remaining_digits = n // 10  #Get the remaining digit by integer division by 10

        return last_digit + sum_of_digits(remaining_digits)     #Recursively call the function with the remaining digits
                                                                #and Add the last digit to the result

print(sum_of_digits(123))
