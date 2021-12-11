inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory [2:6]
first_3 = inventory [:3]
twin_beds = inventory.count("twin bed")
removed_item = inventory.pop(4)
inventory.insert(10, "19th Century Bed Frame")
inventory_list = sorted(inventory)


print("This is the inventory length:" , inventory_len)
print("This is the first entry:", first)
print("This is the last entry: ", last)
print("These are the two to five: ", inventory_2_6)
print("These are the first three: ", first_3)
print("These are how many twin beds:", twin_beds)
print("This is a removed item:" , removed_item)
print("This is sorted using list = sort:" , inventory_list)
inventory.sort()
print("This is sorted using sort:" , inventory)
inventory.sort(reverse=True)
print("This is sorted using sort reverse:" , inventory)
