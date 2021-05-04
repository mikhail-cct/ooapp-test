"""
    =========== Exercise 1 =============

    Take the current for loop below and add
    two conditions to the loop body:
        1. If 'Eggs' are the current element, then conitnue
        2. If 'Sausages' is the current element, stop iterating.
"""

shopping_list = ["Bread", "Bannanas", "Pineapples", "Eggs", "Oranges", "Milk", "Sausages"]

# for item in shopping_list: # Iterate over the items in the shopping list
#     # Do stuff
#    if item == "Eggs":
#         continue
#    elif item == "Sausages":
#         break    

"""
    =========== Exercise 2 =============

    Take the current existing shopping list
    and ask the user to add a number of items
    to the list.

    For example, if someone enters 3 then prompt
    them for input and append it to the list 3 times.
"""

amount_to_add = int(input("How many items do you want to add?"))

counter = 1 # A counter to keep track of the number of items that have been added

while counter <= amount_to_add:
    # Do stuff
    shopping_list += [input("Please enter the new list item: ")]
    counter += 1

print(shopping_list)