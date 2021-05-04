import re

# Find words that start with cat and end with one of these options: 'fish','nap', or 'claw'
text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

print(re.search(r'cat(fish|nap|claw)',text))

print(re.search(r'cat(fish|nap|claw)',texttwo))

# None returned
print(re.search(r'cat(fish|nap|claw)',textthree))