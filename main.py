import utils
import tools


print("Welcome to the PyPassword Generator!")
nr_total= int(input("How many characters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

while (nr_symbols + nr_numbers) > nr_total:
    print('Total length can not be larger than number of symbols and numbers! \n')
    nr_total = int(input("How many characters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

print(tools.gen_password(nr_total, nr_symbols, nr_numbers))
