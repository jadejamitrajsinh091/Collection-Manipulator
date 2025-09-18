items = []

categories = []

quantities = []

while True:

    product= input("Enter item name: ")

    pcategory = input("Enter category: ")

    pquantity = int(input("Enter quantity: "))

    items.append(product)

    categories.append(pcategory.lower())

    quantities.append(pquantity)

    choose = input("Do you want to add more items? (yes/no): ")

    if choose.lower() != "yes":

        break


print("\n============== INVENTORY SUMMARY ==============")

#different items:

totalItems = len(items)

print("Total Different Items:", totalItems)

print("Explanation: You entered", totalItems, "different items:", ", ".join(items) + ".")

#quantity in stock:

totalQuantity = sum(quantities)

print("\nTotal Quantity in Stock:", totalQuantity)

print("Explanation: Sum of all quantities:", " + ".join(map(str, quantities)), "=", totalQuantity)

# Average quantity:

averageQuantity_ = totalQuantity / totalItems

print("\nAverage Quantity per Item:", averageQuantity_)

print("Explanation: Average =", totalQuantity, "total /", totalItems, "items")

# Most stocked item:

maxQuantity = max(quantities)

max_item = items[quantities.index(maxQuantity)]

print("\nMost Stocked Item:", max_item, "(", maxQuantity, "units )")

print("Explanation:", max_item, "has the highest quantity among all items.")

# Least stocked item:

minQuantity = min(quantities)

minItem = items[quantities.index(minQuantity)]

print("\nLeast Stocked Item:", minItem, "(", minQuantity, "units )")

print("Explanation:", minItem, "has the lowest quantity.")

# Unique categories:

uniqueCategories = set(categories)

print("\n===================================================")

print("Unique Categories in Inventory:", uniqueCategories)

print("Explanation: Categories are taken from user input and converted to lowercase.")

print("No duplicates are shown here.")

# Items sorted by quantity:

print("\n======================================================")

print(" Items Sorted by Quantity (High to Low):")

sorted_items = sorted(zip(quantities, items), reverse=True)

for idx, (qty, item) in enumerate(sorted_items, start=1):

    print(f"{idx}. {item} - {qty} units")

print("Explanation: Items Are Sorted Using The Quantity Field From highest to lowest.")

# Categories in alphabetical order:

print("\n======================================================")

print(" Categories In Alphabetical Order:")

sorted_categories = sorted(uniqueCategories)

for idx, cat in enumerate(sorted_categories, start=1):

    print(f"{idx}. {cat}")

print("Explanation: The Set Of Unique Categories Was Sorted Alphabetically For Display.")




print("\n========================= END OF REPORT =========================")

     


