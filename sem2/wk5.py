from PIL import Image
# mac = Image.open('example.jpg')
# # Note this is a specialized file type from PIL (pillow)
# print(type(mac))

# print(mac.size)
# print(mac.filename)
# print(mac.format_description)

# halfway = 1993/2

# x = halfway - 200
# w = halfway + 200
# y = 800
# h = 1257

# # computer = mac.crop((x,y,w,h))

# # mac.paste(im=computer,box=(0,0))

# # mac.paste(im=computer,box=(796,0))

# h,w = mac.size

# new_h = int(h/3)
# new_w = int(w/3)

# # Note this is not permanent change
# # for permanent change, do a reassignment
# # e.g. mac = mac.resize((100,100))
# # mac = mac.resize((3000,500))


# mac.save("mac_edited.jpg")

# pencils = Image.open("pencils.jpg")

# print(pencils.size)

# # # Start at top corner (0,0)
# # x = 0
# # y = 0
# # # Grab about 10% in y direction , and about 30% in x direction
# # w = 1950/3
# # h = 1300/10


# pencils_edited = pencils.rotate(120,expand=True)

# pencils_edited.save("pencils_croped.jpg")

blue = Image.open('blue_color.png')
red = Image.open('red_color.jpg')

red = red.convert('RGB')

blue.putalpha(128)
red.putalpha(128)
red.paste(blue,box=(0,0),mask=blue)

# Get back an image that is more red.
red.save("result2.png")