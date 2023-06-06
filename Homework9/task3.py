# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код

def three_most_expensive_purchases():
    global three_most_expensive_purchases
    product_costs_sum = 0
    purchases = []
    with open('test_file/task_3.txt', mode='r', encoding='utf-8') as file_start:
        for current_line in file_start:
            if current_line[0] == '\n':
                if len(purchases) == 3 and product_costs_sum > purchases[0]:
                    purchases[0] = product_costs_sum
                    purchases.sort()
                else:
                    if len(purchases) < 3:
                        purchases.append(product_costs_sum)
                        purchases.sort()
                product_costs_sum = 0
            else:
                product_costs_sum += int(current_line)
    three_most_expensive_purchases = sum(sorted(purchases)[-3:])


three_most_expensive_purchases()

assert three_most_expensive_purchases == 202346