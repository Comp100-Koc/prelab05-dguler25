def bin_to_int(string):

    total, power = 0, 0
    for onero in string[::-1]:
    
        if onero == "1":
            total += 2**power
        
        power += 1 
    return total

def int_to_bin(n):
    
    if n == 0:
        return "0b0"
    
    oneros = ""
    while n > 0:
        remainder = n % 2
        oneros = str(remainder) + oneros
        n //= 2
    return  "0b" + oneros

def add_binary(a, b):
    integer_a = a[2:]
    integer_b = b[2:]

    sum_a = bin_to_int(integer_a)
    sum_b = bin_to_int(integer_b)
    total = sum_a + sum_b
    
    return int_to_bin(total)