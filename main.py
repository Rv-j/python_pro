
import product
import customer
import order
if __name__ == '__main__':
    x = product.Product('Realme 6 Pro 8/128GB Red', 'Width 75.8 mm, Height 163.8 mm, Depth 8.9 mm', 5000)
    y = product.Product('Samsung Galaxy M31 6/128GB Black', 'Width 75.1 mm, Height 159.2 mm, Depth 8.9 mm', 5500)
    z = product.Product('Motorola G9 Play 4/64GB Blue', 'Width 75.73 mm, Height 165.21 mm, Depth 9.18 mm', 4500)
    print(x, y, z, sep='; \n')

    a = customer.Customer('Shevchenko', 'Valerii', 'Ivanovich', '+380634833222')
    b = customer.Customer('Silko', 'Andrii', 'Vasilievich', '+380687841276')
    c = customer.Customer('Zubov', 'Sergii', 'Aleksandrovich', '+380976548723')
    print(a, b, c, sep='; \n')

    order_1 = order.Order(a)
    order_2 = order.Order(b)
    order_3 = order.Order(c)

    order_1.products.append(x)
    order_1.products.append(y)
    order_2.products.append(y)
    order_2.products.append(z)
    order_3.products.append(z)
    order_3.products.append(x)
    order_1.products.append(x)

    print(order_1)
    print(order_2)
    print(order_3)

    print(order.Order.get_orders_count())
