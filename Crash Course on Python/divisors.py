def sum_divisors(n):
    sum = 0
    div = 1
    div_list = []
    # Return the sum of all divisors of n, not including n
    while n != 0 and div < n:
        if n % div == 0:
            sum += div
            div_list.append(div)
        else:
            sum +=0
        div += 1
    div_string = '+'.join(str(i) for i in div_list)
    #print(div_string)
    return 'The sum of divisors {} is : {}'.format(div_string, sum)



print(sum_divisors(0))
print(sum_divisors(3))  # Should sum of 1
# 1
print(sum_divisors(36))  # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102))  # Should be sum of 2+3+6+17+34+51
# 114
