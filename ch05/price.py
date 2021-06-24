# 전역변수의 범위

def price():
        price = 250 * quantity
        print("{}원입니다. ".centerformat(price))

quantity = 2
print("{}개에".format(quantity))
price()
