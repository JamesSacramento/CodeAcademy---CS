toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)

pizza_and_prices = [
  [prices[0], toppings[0]],
  [prices[1], toppings[1],],
  [prices[2], toppings[2]],
  [prices[3], toppings[3]],
  [prices[4], toppings[4]],
  [prices[5], toppings[5]],
  [prices[6], toppings[6]],
]

print("These are the available toppings:" , *toppings, sep = "\n")
print("These are the number of $2 slices:" , num_two_dollar_slices)
print(f"We sell {num_pizzas} different kinds of pizza!")
print(*pizza_and_prices, sep = "\n")

pizza_and_prices.sort()
print(f"Pizza Prices sorted ascending: {pizza_and_prices}")

cheapest_pizza =  pizza_and_prices[0][0] , pizza_and_prices[0][1]
print(f"The cheapest pizza is {cheapest_pizza}", )

priciest_pizza =  pizza_and_prices[-1][0] , pizza_and_prices[-1][1]
print(f"The priciest pizza is {priciest_pizza}")

pizza_and_prices.pop(-1)
print(f"Pizza Prices updated, anchoves sold out: {pizza_and_prices}")

pizza_and_prices.insert(4, ([2.5, "peppers"]))
print(pizza_and_prices)

three_cheapest =  pizza_and_prices[:3]
print(f"The three cheapest pizza for the mice are {three_cheapest}")
