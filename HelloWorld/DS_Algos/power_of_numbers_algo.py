

def power_of_numbers(base_number, exponent):
    assert exponent >= 0 and int(exponent) == exponent, "exponent must be positive integer"
    if exponent == 0:
        return 1
    if  exponent == 1:
        return base_number
    else:
        return base_number * power_of_numbers(base_number, exponent -1)
    
print(power_of_numbers(2,9))