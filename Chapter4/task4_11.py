import task4_1

friend_pizzas = task4_1.pizzas[:]
task4_1.pizzas.append('pizza4')
friend_pizzas.append('pizza5')
print('My favorite pizzas are:')
print(task4_1.pizzas)
print("My friend's favorite pizzas are:")
print(friend_pizzas)