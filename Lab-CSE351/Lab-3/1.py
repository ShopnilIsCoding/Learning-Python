def sumSeries(n):
    return sum(i * (i + 1) // 2 for i in range(1, n + 1))

print(sumSeries(3))