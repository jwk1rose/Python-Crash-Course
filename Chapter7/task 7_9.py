sandwich_orders = ['BBQ sandwich', 'fruit sandwich', 'beef sandwich', "pastrami", "pastrami", "pastrami"]
print("pastrami has been sale over!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print('remove success')
    print(sandwich_orders)
print('no pastrami in sandwich_orders')