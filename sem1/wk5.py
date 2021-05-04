# name = "Mike T"

# greeting = f"Welcome, {name}!"

# print(greeting) # Prints: Welcome John Doe!

# import datetime

# current_datetime = datetime.date.today() # Returns datetime object of todays date

# print(current_datetime)

# class Animal:
#   counter = 0 # Initialize counter to 0
#   # This ^^ is a class variable since it is outside of __init__ and has no self. in front
#   def __init__(self, species_name, regions, common_name):
#     """A class to represent a generic animal

#    Attributes
#     ----------
#     species_name : (str) 
#         The technical species name of the animal
#     regions : (list[str]) 
#         A list of regions the animal is endemic to
#     common_name : (str) 
#         The colloquial name of the animal
#     """
#     self.species_name = species_name
#     self.regions = regions
#     self.common_name = common_name
#     Animal.counter += 1 # Accessing and incrementing the class counter by 1 on each instantiation of an Animal

#   def print_info(self):
#     """Prints information about animal instance"""
#     print(f"\nCommon Name: {self.common_name}\nSpecies: {self.species_name}\nRegions: {self.regions}")

# leopard_gecko = Animal("Eublepharis macularius", ["Afghanistan","Pakistan","India", "Iran"],"Common Leopard Gecko")

# leopard_gecko.print_info()

# class CookieBaker:
#   def __init__(self, number_of_cookies):
#     """ Example class that is used to show off the __init__ method.
#     The __init__ method calls the bake_cookie() method as many times as there are number_of_cookies.

#     Attributes
#     ----------
#     number_of_cookies(int): How many cookies to bake
#     """
#     print(f"__init__ method called, creating {number_of_cookies} cookie(s):")
#     self.number_of_cookies = number_of_cookies
#     for cookie in range(number_of_cookies):
#       self.bake_cookie()

#   def bake_cookie(self):
#     """Print's 'Cookie Baked!'."""
#     print("Cookie Baked!")

# cookies = CookieBaker(10)

# cookies.bake_cookie()

import datetime
class user:
  def __init__(self, name, age, sign_up_date, birthday, premium_member):
    """A class to represent a generic animal

    Attributes
    ----------
    name(str): The technical species name of the animal
    age(str): A list of regions the animal is endemic to
    sign_up_date(datetime.datetime): A datetime object of the day the user signed up
    birthday(datetime.datetime): A datetime object of the users birthday
    premium_member(bool): Whether the user is on premium or free subscription
    """
    self.name = name
    self.age = age
    self.sign_up_date = sign_up_date
    self.birthday = birthday
    self.premium_member = premium_member

from dataclasses import dataclass

@dataclass
class user:
    """A class to represent a generic animal

    Attributes
    ----------
    name(str): The technical species name of the animal
    age(str): A list of regions the animal is endemic to
    sign_up_date(datetime.datetime): A datetime object of the day the user signed up
    birthday(datetime.datetime): A datetime object of the users birthday
    premium_member(bool): Whether the user is on premium or free subscription
    """
    name:str
    age:str
    sign_up_date:datetime.datetime
    birthday:datetime.datetime
    premium_member:bool