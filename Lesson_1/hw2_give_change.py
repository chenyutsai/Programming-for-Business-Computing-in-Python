'''
該怎麼找錢
題目敘述
如果你在一家零售店幫消費的客人結帳，你可能需要快速地挑出合適且數量正確的鈔票與零錢。
假設客人的消費金額 aa 一定是 1 到 1000 之間的整數，而你有無限量的 500、100、50、10、5、1 這些面額的鈔票和零錢，
我們希望你能依照下面的規則找錢：

你找的錢的總額要是 1000 - a。

與其給客人五張 100 元，不如給他一張 500 元；與其給客人兩個 50 元，不如給他一張 100 元……依此類推。
'''
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

print(coin_500, coin_100, coin_50, coin_10, coin_5, coin_1)
