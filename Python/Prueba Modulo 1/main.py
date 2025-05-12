inventory: dict = {
'vegetable oil':[12000, 5],
'bread flour':[4000,9],
'apple':[1500, 22],
'milk':[4100, 32],
'egg': [800, 5]
}
"""Function to add products to inventory with name, price, and amount attributes
"""
def add_product(product:str, price: float, amount: int ) -> None:
    if product not in inventory:
        inventory[product] = [price, amount]
        print('\n***********************************************')
        print(f'The product ({product}) was successfully added to inventory.')
        print(f'With the price of ${price:.2f} and the amount of {amount}')
        print('***********************************************\n')
    else:
        print('\n***********************************************')
        print(f'The product "{product}" already exists in the inventory.')
        print('***********************************************\n')

"""Function to search for products by name in the inventory
"""
def search_product(product: str) -> None:
    if product in inventory:
        price: float = inventory[product][0] 
        amount: int = inventory[product][1]
        print('\n***********************************************')
        print(f'Product: {product}')
        print(f'Price: ${price:.2f}')
        print(f'Amount: {amount}')
        print('***********************************************\n')
    else:
        print('\n***********************************************')
        print(f'The product "{product}" does not exist in the inventory.')
        print('***********************************************\n')
"""function to update the price of an existing product
"""
def update_product_price(product:str, price: float) -> None:
    if product in inventory:
        amount: int = inventory[product][1]
        inventory[product] = [price, amount]
        print('\n***********************************************')
        print(f'The product "{product}" with price "${price:.2f}" was successfully updated.\n')
        print('***********************************************\n')
    else:
        print(f'\nThe product "{product}" is not in stock. Please go to "Add Product.\n"')
"""function to delete an existing product in the inventory
"""
def delete_product(product: str) -> None:
    if product in inventory:
        delete_validation = input(f'Are you sure that you want to delete {product} from the inventory? Enter "Yes" or "No": ').strip().lower()
        if delete_validation == 'yes':
            del inventory[product]
            print('\n*********************************')
            print(f'The product {product} was deleted successfully')
            print('*********************************\n')

    else: 
        print(f'We cannot delete the product "{product}" because it does not exist in the inventory.\n')
"""function to calculate the total value of the inventory
"""
def calculate_total_inventory() -> None:
    calculate_total_value = lambda price, amount: price * amount
    total: float = 0
    for value in inventory.values():
        total += calculate_total_value(value[0], value[1])
    print('\n***********************************************')
    print(f'The total value of the inventory is ${total:.2f}')
    print('***********************************************')
"""Function to receive data entered by the user, evaluate whether it is a number and is positive.
 If so, it returns that value."""
def positive_number_val(message: str) -> float:
    while True:
        try:
            number:float = float(input(message))
            if number > 0:
                return number
            else:
                print('The number must be greater than 0\n')
        except ValueError:
            print('The data entered must be a number\n') 

def menu() -> None:
    print('\n************************')
    print('Inventory management')
    print('************************\n')
    print('1. Add product')
    print('2. Search product')
    print('3. Update product')
    print('4. Delete product')
    print('5. Calculate the total value of the inventory')
    print('6. Quit\n')

while True:
    menu()
    try:
        option: int = int(input('Select option: '))
        if option > 6 or option < 1:
            print('\nYou must select a number between 1 and 6')
            continue
        elif option == 1:
            print('\n**************')
            print('Add product')
            print('**************\n')
            product: str = input('Enter the product name: ').strip().lower()
            price: float = positive_number_val('Enter the price of the product: ')
            amount:int = int(positive_number_val('Enter the amount of the product: '))
            add_product(product, price, amount)
        elif option == 2:
            print('\n**************')
            print('Search product')
            print('**************\n')
            product: str = input('Enter the product name: ').strip().lower()
            search_product(product)
        elif option == 3:
            print('\n**************')
            print('Update product')
            print('**************\n')
            product: str = input('Enter the product name: ').strip().lower()
            price: float = positive_number_val('Enter the new price of the product: ')
            update_product_price(product, price)
        elif option == 4:
            print('\n**************')
            print('Delete product')
            print('**************\n')
            product: str = input('Enter the product name: ').strip().lower()
            delete_product(product)
        elif option == 5:
            calculate_total_inventory()
        elif option == 6:
            break
    except ValueError:
        print('You must select a number between 1 and 6')