# Question
#
# In this programming assignment you will implement one or more of the integer multiplication algorithms described in
# lecture.
# To get the most out of this assignment, your program should restrict itself to multiplying only pairs of single-digit
# numbers.  You can implement the grade-school algorithm if you want, but to get the most out of the assignment you'll
# want to implement recursive integer multiplication and/or Karatsuba's algorithm.
#
# So: what's the product of the following two 64-digit numbers?
#
# 3141592653589793238462643383279502884197169399375105820974944592
#
# 2718281828459045235360287471352662497757247093699959574966967627
#
#
# [Food for thought: the number of digits in each input number is a power of 2.  Does this make your life easier?
# Does it depend on which algorithm you're implementing?]
# Expected output:
# 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184


def append_zeros(num, num_zeros):
    if num_zeros == 0:
        return num
    else:
        return int(str(append_zeros(num, num_zeros - 1)) + '0')


def nearest_even_int(num):
    return num if num % 2 == 0 else num + 1


def multiply(num1, num2):
    num_digits_1 = len(str(num1))
    num_digits_2 = len(str(num2))

    if num_digits_1 == 1 and num_digits_2 == 1:
        num_digits = 1
    elif num_digits_1 >= num_digits_2:
        num_digits = nearest_even_int(num_digits_1)
    else:
        num_digits = nearest_even_int(num_digits_2)

    num1_padded = num1.zfill(num_digits)
    num2_padded = num2.zfill(num_digits)

    if num_digits == 1:
        return int(num1) * int(num2)
    else:
        a = int(num1_padded[:num_digits / 2])
        b = int(num1_padded[num_digits / 2:])
        c = int(num2_padded[:num_digits / 2])
        d = int(num2_padded[num_digits / 2:])
        ac = multiply(str(a), str(c))
        bd = multiply(str(b), str(d))
        ab_cd = multiply(str(a + b), str(c + d))
        ad_plus_bc = ab_cd - ac - bd
        val = append_zeros(ac, num_digits) + append_zeros(ad_plus_bc, num_digits / 2) + bd
        return int(val)


if __name__ == '__main__':
    print multiply('3141592653589793238462643383279502884197169399375105820974944592',
                   '2718281828459045235360287471352662497757247093699959574966967627')
