'''
總共多少錢
題目敘述
你手上有面額 50、10、5、1 元的銅板各 w、x、y、z 個，請計算你一共有多少錢。
'''
# coin 50
w = int(input())
coin_50 = w * 50
# coin 10
x = int(input())
coin_10 = x * 10
# coin 5
y = int(input())
coin_5 = y * 5
# coin 1
z = int(input())
coin_1 = z * 1

print(coin_50 + coin_10 + coin_5 + coin_1)
