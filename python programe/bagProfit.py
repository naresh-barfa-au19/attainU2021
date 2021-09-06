def bagProfit(capacity, wt, val, n):
    if capacity == 0 or n == 0:
        return 0
    #if 60 > capacity = 50 we dont require wt [20,10,30]
    if wt[n-1] > capacity:
        return bagProfit(capacity, wt , val,n-1)
    else:
        return max(
            val[n-1] + bagProfit(
                capacity-wt[n-1], wt, val, n-1),
            bagProfit(capacity, wt, val, n-1))

def bagProfitMatrix(capacity, wt, val, n):
    matrix = [[0 for _ in range(capacity+1)] for _ in range(n+1)]

    #build the matrix from bottom up approach 
    for i in range(n+1):
        for w in range(capacity+1):
            if i == 0 or w ==0:
                matrix[i][w] = 0
            elif wt[i-1] <= w:
                matrix[i][w] = max(val[i-1]+ matrix[i-1][w-wt[i-1]],matrix[i-1][w])
            else:
                matrix[i][w] = matrix[i-1][w]
    return matrix[n][capacity]

if __name__ == '__main__':
    wt = [10,20,30]
    val = [60,100,120]
    capacity = 50
    print(bagProfit(capacity, wt,val,len(val)))
    # print(bagP)