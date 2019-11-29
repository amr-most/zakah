my_money = float(input('you have = '))
gold_cost = float(input('Gm gold = '))
if my_money >= 97.14*gold_cost:
    zakah = 0.025*my_money
    print('you should purchase',zakah)