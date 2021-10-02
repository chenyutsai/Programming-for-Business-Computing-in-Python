purchase_cost = int(input())
unit_price = int(input())
order_amount = possible_requirements = int(input())
probabilities = []

for i in range(possible_requirements+1):
    probabilities.append(float(input()))

max_profit = 0
best_amount = 0

for amount in range(order_amount+1):
    expect_value = 0
    index = 0
    remain = 1
    while index < amount:
        expect_value += probabilities[index] * index * unit_price
        remain -= probabilities[index]
        index += 1
    expect_value += remain * amount * unit_price
    profit = expect_value - purchase_cost * amount
    if profit > max_profit:
        best_amount, max_profit = amount, profit

print(best_amount, int(max_profit))
