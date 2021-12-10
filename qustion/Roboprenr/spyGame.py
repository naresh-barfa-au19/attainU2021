# Assignment 2 - Spy Game
# Your program will be provided a variable data1 that will contain a list of integers.
# Write a program that prints True if the list contains 007 in order else print False.
# Sample Input 1:
# data1 = [1,2,4,0,0,7,5]
# Sample Output 2:
# True
# Sample Input 2:
# data1 = [1,0,2,4,0,5,7]
# Sample Output 2:
# True
# Sample Input 3:
# data1 = [1,7,2,0,4,5,0]
# Sample Output 3
# False

def spyGame(arr):
    tempStr = ""
    num = "007"
    for n in arr:
        if(n == 0 or n == 7):
            tempStr += str(n)
        if(len(tempStr)>2 and tempStr[len(tempStr)-3:] == num):
            return True

    return False
data1 = [1,2,4,0,0,7,5]
print(spyGame(data1))


