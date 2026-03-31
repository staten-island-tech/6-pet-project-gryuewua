sushi_orders = [
    {"name": "California Roll", "price": 8},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8},
    {"name": "Dragon Roll", "price": 12},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Miso Soup", "price": 4},
    {"name": "Edamame", "price": 5},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8}
]

def reciept(orders):
    reciept={}
    for order in orders:
        if order['name'] in reciept:
            reciept[order['name']]['quantity'] += 1
        else:
            reciept[order['name']] = {
                'price': order['price'],
                'quantity': 1
            }
    for order, value in reciept.items():
        price = value['price'] * value['quantity']
        print(order,value['quantity'],price)

reciept(sushi_orders)