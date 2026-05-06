from data import MENU, resources

def format_report_resource(resource):
    water = resource['water']
    milk = resource['milk']
    coffee = resource['coffee']

    return f'Water: {water} ml\nMilk: {milk}ml\nCoffee: {coffee}g'

