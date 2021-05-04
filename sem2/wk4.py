# def func_one(n):
#     '''
#     Given a number n, returns a list of string integers
#     ['0','1','2',...'n]
#     '''
#     return [str(num) for num in range(n)]

# func_one(10)

# def func_two(n):
#     '''
#     Given a number n, returns a list of string integers
#     ['0','1','2',...'n]
#     '''
#     return list(map(str,range(n)))

# func_two(10)

# # import time

# # # STEP 1: Get start time
# # start_time = time.time()
# # # Step 2: Run your code you want to time
# # result = func_one(1000000)
# # # Step 3: Calculate total time elapsed
# # end_time = time.time() - start_time

# # print(end_time)

# # # STEP 1: Get start time
# # start_time = time.time()
# # # Step 2: Run your code you want to time
# # result = func_two(1000000)
# # # Step 3: Calculate total time elapsed
# # end_time = time.time() - start_time

# # print(end_time)

# import timeit

# setup = '''
# def func_one(n):
#     return [str(num) for num in range(n)]
# '''

# stmt = 'func_one(100)'

# print(timeit.timeit(stmt,setup,number=1000000))

# setup2 = '''
# def func_two(n):
#     return list(map(str,range(n)))
# '''

# stmt2 = 'func_two(100)'

# print(timeit.timeit(stmt2,setup2,number=1000000))

# import zipfile

# comp_file = zipfile.ZipFile('comp_file.zip','w')

# comp_file.write("new_file.txt",compress_type=zipfile.ZIP_DEFLATED)

# comp_file.write('new_file2.txt',compress_type=zipfile.ZIP_DEFLATED)

# comp_file.close()

# zip_obj = zipfile.ZipFile('comp_file.zip','r')

# zip_obj.extractall("extracted_content")

# import shutil

# directory_to_zip='/workspace/ooapp-test'

# # Creating a zip archive
# output_filename = 'example'
# # Just fill in the output_filename and the directory to zip
# # Note this won't run as is because the variable are undefined
# shutil.make_archive(output_filename,'zip',directory_to_zip)

# Extracting a zip archive
# Notice how the parameter/argument order is slightly different here
# shutil.unpack_archive("example.zip","test",'zip')

# import requests

# res = requests.get("http://www.example.com")

# print(type(res))

# # print(res.text)

# import bs4

# soup = bs4.BeautifulSoup(res.text,"lxml")

# # print(soup)

# # print(soup.select('title'))

# title_tag = soup.select('title')

# print(title_tag[0])

# print(type(title_tag[0]))

# print(title_tag[0].getText())

# import requests

# # First get the request
# res = requests.get('https://en.wikipedia.org/wiki/Yuri_Gagarin')

# import bs4

# # Create a soup from request
# soup = bs4.BeautifulSoup(res.text,"lxml")

# print(soup.select('title')[0].getText())

# soup.select(".mw-headline")

# for item in soup.select(".mw-headline"):
#     print(item.text)

# import requests
# import bs4

# res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")

# soup = bs4.BeautifulSoup(res.text,'lxml')

# image_info = soup.select('.thumbimage')

# print(image_info)

# print(len(image_info))

# computer = image_info[0]

# print(type(computer))

# print(computer['src'])

# image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg')

# # The raw content (its a binary file, meaning we will need to use binary read/write methods for saving it)
# image_link.content

# f = open('my_new_file_name.jpg','wb')

# f.write(image_link.content)

# f.close()

import requests
import bs4

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

two_star_titles = []

for n in range(1,51):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text,"lxml")
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            two_star_titles.append(book.select('a')[1]['title'])

print(two_star_titles)