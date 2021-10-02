purchase_cost = int(input())
unit_price = int(input())
possible_requirements = int(input())
order_amount = int(input())
probabilities = []

for i in range(possible_requirements+1):
    probabilities.append(float(input()))

expect_value = 0
for j in range(len(probabilities)):
    if j <= order_amount:
        expect_value += probabilities[j] * j * unit_price
    else:
        expect_value += probabilities[j] * order_amount * unit_price
profit = int(expect_value - purchase_cost * order_amount)

print(profit)
