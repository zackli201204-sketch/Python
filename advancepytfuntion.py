items=["pencil", "eraser", "notebook", "sharpener", "glue"]
stock_counts=[12, 0, 8, 5, 3]

inventory={item: count for item, count in zip(items, stock_counts)}
print("Full inventory:", inventory)

in_stock_items=[item for item in items if inventory[item]>0]
print("Items in stock:", in_stock_items)

chosen_item=input("Whcih item do you want to buy?")

if chosen_item not in inventory or inventory[chosen_item]==0:
    print(chosen_item, "is out of stock! Stopping the checker.")
    exit()

prices=[10,5,40,15,20]
markup=int(input("Enter the markup amount to add to every price:"))

marked_up_prices=list(map(lambda p: p+markup, prices))
print("Marked up prices:", marked_up_prices)

item_index=items.index(chosen_item)
chosen_price=marked_up_prices[item_index]
print("price of", chosen_item, "after mark up:", chosen_price)

inventory[chosen_item]=inventory[chosen_item]-1
print(chosen_item, "purchased! remaining stock:", inventory[chosen_item])

print("")
print("===== SCHOOL STORE INVENTORY CHECKER =====")
print("ITEM BOUGHT:", chosen_item)
print("PRICE PAID:", chosen_price)
print("uPDATED inVENTORY:", inventory)
print("=======================================")