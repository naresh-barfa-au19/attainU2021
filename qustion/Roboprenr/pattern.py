# Assignment 3 - Zeros and Stars Pattern 
# Print the following pattern
# Pattern for N = 4
# *000*000*
# 0*00*00*0
# 00*0*0*00
# 000***000
# Input Format :
# N (Total no. of rows)
# Output Format :
# Pattern in N lines
# Sample Input 1:
# 3
# Sample Output 1:
# *00*00*
# 0*0*0*0
# 00***00
# Sample Input 2:
# 5
# Sample Output 2:
# *0000*0000*
# 0*000*000*0
# 00*00*00*00
# 000*0*0*000
# 0000***0000

def zeroStarPattern(num):
    total = 2*(num-1)+3
    for i in range(num):
        temp =""
        for j in range(total):
            if(i == j or j== total//2 or j ==total-1-i):
                temp += "*"
            else:
                temp += "0"
        print(temp,end="\n")


zeroStarPattern(10)