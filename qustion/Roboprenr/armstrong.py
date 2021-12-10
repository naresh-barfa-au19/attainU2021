# Assignment 1 - Check Armstrong 
# Write a Program to determine if the given number is Armstrong number or not. Print True if 
# number is Armstrong, otherwise print False.
# An Armstrong number is a number (with digits n) such that the sum of its digits raised to nth 
# power is equal to the number itself.
# For example,
# 371, as 3^3 + 7^3 + 1^3 = 371
# 1634, as 1^4 + 6^4 + 3^4 + 4^4 = 1634
# Sample Input 1:
# 1
# Sample Output 1:
# True
# Sample Input 2:
# 103
# Sample Output 2:
# False

def isArmstrongNumber(num):
    n = len(str(num))
    strNum = str(num)
    tempNum = 0
    for i in range(n):
        tempNum += int(strNum[i])**n

    if(tempNum == num):
        return True
    else:
        return False


number = 103
print("is ",number,"Armstrong Number : ",isArmstrongNumber(number))

