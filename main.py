from data import MENU, resources

def format_report_resource(resource):
    water = resource['water']
    milk = resource['milk']
    coffee = resource['coffee']

    return f'Water: {water} ml\nMilk: {milk}ml\nCoffee: {coffee}g'

while True:
    prompt = input('What would you like? (expresso / latte / cappuccino ): ').lower()

    if prompt == 'report'.lower():
        print(format_report_resource(resources))





    if prompt == 'off'.lower():
        break