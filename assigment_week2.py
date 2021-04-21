category1 = "vegetables"
item1 = "Potatoes"
print(f"Enter below remaining amount of {item1}:")
remaining_p = input()
print(f"Enter needed amount of {item1}:")
needed_p = input()
buy_p = (int(needed_p) - int(remaining_p))
print(f"You should buy {buy_p} kg of {item1}.")

item2 = "Carrots"
print(f"\nEnter below remaining amount of {item2}:")
remaining_c = input()
print(f"Enter needed amount of {item2}:")
needed_c = input()
buy_c = (int(needed_c)-int(remaining_c))
print(f"You should buy {buy_c} kg of {item2}.")

item3 = "Onions"
print(f"\nEnter below remaining amount of {item3}:")
remaining_o = input()
print(f"Enter needed amount of {item3}:")
needed_o = input()
buy_o = (int(needed_o)-int(remaining_o))
print(f"You should buy {buy_o} kg of {item3}.")
print(f"\n All things to buy: \n \n{item1}, \n{item2}, \n{item3}.")
price_p = 5000
price_c = 3000
price_o = 1000
print(f"\n{item1}={buy_p}*{price_p}=",(buy_p)*(price_p))
print(f"{item2}={buy_c}*{price_c}=",(buy_c)*(price_c))
print(f"{item3}={buy_o}*{price_o}=",(buy_o)*(price_o))
print(f"Total:", ((buy_p)*(price_p))+((buy_c)*(price_c))+((buy_o)*(price_o)), "sums.")