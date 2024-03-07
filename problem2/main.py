def maximum_buy_product(money, product_price):
    product_price.sort() 

    n = len(product_price)
    indeks = set()
    count = 0

    for x in range(n):
        if x not in indeks and money >= product_price[x]:
            money -= product_price[x]
            count += 1
            indeks.add(x)

    return count

if __name__ == "__main__":
    print(maximum_buy_product(50000, [25000, 25000, 10000, 14000]))      # 3
    print(maximum_buy_product(30000, [15000, 10000, 12000, 5000, 3000])) # 4
    print(maximum_buy_product(10000, [2000, 3000, 1000, 2000, 10000]))   # 4
    print(maximum_buy_product(4000, [7500, 3000, 2500, 2000]))           # 1
    print(maximum_buy_product(0, [10000, 30000]))                        # 0