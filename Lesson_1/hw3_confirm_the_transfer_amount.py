"""
轉帳金額確認
題目敘述
在兩個戶頭之間轉帳，是非常普通的一個金融交易。假設我們現在有兩個帳戶，戶頭金額各為 x1和 x2，
而我們想要從第一個戶頭轉 y 元到第二個戶頭，則一般情況下兩個戶頭的金額各會變成 x1 - y 和 x2 + y。
但如果第一個戶頭錢不夠的話，我們就把第一個戶頭的錢扣到變成 0，然後把第二個戶頭的錢變成 x2 + x1。
舉例來說，如果原本兩個戶頭各有 1000 和 2000 元，而我們要轉 500 元，那就會變成 500 和 2500，
但如果要轉 1200 元，就會變成 0 和 3000。

請寫一個程式，讀入 x1、x2和 y 之後，判斷兩個戶頭各應該變成多少錢。
"""

account_1 = int(input())
account_2 = int(input())
transfer = int(input())

if transfer > account_1:
    account_2 += account_1
    account_1 = 0
else:
    account_2 += transfer
    account_1 -= transfer

print(account_1, account_2)
