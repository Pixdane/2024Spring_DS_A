from statistics import median

n = int(input())
distances = [sum(eval(i)) for i in input().split()]
prices = [int(i) for i in input().split()]
effs = list(map(lambda x: x[0] / x[1], zip(distances, prices)))

houses = list(zip(prices, effs))
median_prices = median(prices)
median_eff = median(effs)

print(len(list(filter(lambda x: x[0] < median_prices and x[1] > median_eff, houses))))
