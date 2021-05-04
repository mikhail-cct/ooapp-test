# x = 0 # Setup a variable to use for the conditional

# while x <= 10: # Continue looping until x is greater than 10
#     print(x) # Print the current itterations value of x
#     x += 1 # Inrement x by 1 (add 1 to the current value of x)

# print("loop Finished") # This will execute after the loop since it's at a lower indentation level

# shopping_list = ["Eggs", "Ham", "Milk"]

# for item in shopping_list: # Iterate through the shopping list
#     print(item) # Print the item at the current iteration

# greeting = "Hello-World" # Setting up a string to iterate through

# for character in greeting: # Iterate over the string one letter at a time
#     if "-" in character: # if the current character is a hyphen
#         print("Hyphen detected, ending loop!")
#         break # End the loop
#     else:
#         print(character) # Print the current character

while True: # This is an infinite loop
  number = int(input("Please type a number between 1 and 10: ")) # Take user input

  if number < 1: # Number is too small
    print("Number provided is less than 1")

  elif number > 10: # Number is too large
    print("Number provided is greater than 10")

  else: # If the input is in a valid range
    print("Number provided is between 1 and 10")
    break # End the loop