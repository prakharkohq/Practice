"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
"""

"""
Using a dictionary or Ordinal to get ascii value Minus the ascii value of zero will give us exact representation 
"""

def solution(num1, num2):
    keymap = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5,
                  '6' : 6, '7' : 7, '8' : 8, '9' : 9}

    def num_to_int(num):
        raw_number = 0
        # we need to find number integer eq and multiply ordinal with the value
        for item in num:
            raw_number = raw_number * 10 + keymap.get(item)
        return raw_number

    return int( num_to_int(num1) + num_to_int(num2) )


def solution_2(num1, num2):
    def num_to_int(num):
        output = 0
        for item in num:
            output = output * 10 + ord(item) - ord('0')
        return output
    print( num_to_int(num1))
    return ( num_to_int(num1) + num_to_int(num2) )

if __name__ == "__main__":
    num1 = "34"
    num2 = "123"
    print(solution_2(num1, num2))