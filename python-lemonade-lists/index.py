sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]

extra_day = input('How many extra were sold on day 2?')
sales_w2.append(int(extra_day))
sales = sales_w1 + sales_w2
minsales = min(sales) * 1.5
maxsales = max(sales) * 1.5
print(f'The best day we earned {maxsales} and the worst day we earned {minsales}.')