"""
該怎麼找錢（進階版）
本題是第二週作業「該怎麼找錢」的進階版，輸入格式與演算規則完全相同，只有輸出格式不同。
"""
customer_pay = int(input())
give_change = 1000 - customer_pay

coin_500 = give_change // 500
give_change %= 500
coin_100 = give_change // 100
give_change %= 100
coin_50 = give_change // 50
give_change %= 50
coin_10 = give_change // 10
give_change %= 10
coin_5 = give_change // 5
give_change %= 5
coin_1 = give_change // 1
give_change %= 1

ans = ""
if coin_500 != 0:
    ans = "500, "+str(coin_500)
if coin_100 != 0:
    ans = ("100, "+str(coin_100)) if ans == "" else ans + \
        "; 100, " + str(coin_100)
if coin_50 != 0:
    ans = ("50, "+str(coin_50)) if ans == "" else ans + "; 50, " + str(coin_50)
if coin_10 != 0:
    ans = ("10, "+str(coin_10)) if ans == "" else ans + "; 10, " + str(coin_10)
if coin_5 != 0:
    ans = ("5, "+str(coin_5)) if ans == "" else ans + "; 5, " + str(coin_5)
if coin_1 != 0:
    ans = ("1, "+str(coin_1)) if ans == "" else ans + "; 1, " + str(coin_1)

print(ans)
