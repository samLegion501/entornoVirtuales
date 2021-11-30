


from colorama import Fore, Back, Style
from art import *

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')

print(Style.RESET_ALL)
print('back to normal now')

art_1=art("coffee") # return art as str in normal mode

print(art_1)
print(art("random"))

print(art("random"))
print(art("random"))
