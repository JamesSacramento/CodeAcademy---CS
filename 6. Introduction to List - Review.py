# Your code below: 

first_names = [ "Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]
preferred_size.append("Medium")
print(preferred_size)

customer_data = [
  [first_names[0],preferred_size[0], True],
  [first_names[1],preferred_size[1], False],
  [first_names[2],preferred_size[2], True],
  [first_names[3],preferred_size[3], False]]

customer_data[2][2] = False
customer_data[1].remove(False)

customer_data_final = [
  ["Amit", "Large", True], 
  ["Karim", "X-Large", False]]
customer_data_final = customer_data + customer_data_final

print(customer_data)
print(customer_data_final)
