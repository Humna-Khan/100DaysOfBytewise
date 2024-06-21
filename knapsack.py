def knapsack(weight, val, cap):
    numItems = len(weight)
    dyanamicProg = [0] * (cap + 1)
    for i in range(numItems):
        for w in range(cap, weight[i] - 1, -1):
            dyanamicProg[w] = max(dyanamicProg[w], dyanamicProg[w - weight[i]] + values[i])
    return dyanamicProg[cap]

weight = [1, 3, 4, 5]
values = [1, 4, 5, 7]
cap = 7
maxValue = knapsack(weight, values, cap)
print("The maximum value that can be obtained is:", maxValue)