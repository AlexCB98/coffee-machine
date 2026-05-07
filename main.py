from data import MENU, resources

def format_report_resource(resource):
    water = resource['water']
    milk = resource['milk']
    coffee = resource['coffee']
    money = resource['money']

    return f'Water: {water} ml\nMilk: {milk} ml\nCoffee: {coffee} g\nMoney: $ {money}'

def check_resources(resource, drink):
    r_water = resource['water']
    r_milk = resource['milk']
    r_coffee = resource['coffee']
    d_water = drink['water']
    d_milk = drink['milk']
    d_coffee = drink['coffee']

    if r_water >= d_water and r_milk >= d_milk and r_coffee >= d_coffee:
        return True
    elif r_water < d_water:
        print('There is not enough water.')
        return False
    elif r_milk < d_milk:
        print('There is not enough milk.')
        return False
    else:
        print('There is not enough coffee.')
        return False

def process_coins():
    quarters = int(input('How many quarters ( $ 0.25 ) ?: '))
    dimes =  int(input('How many dimes ( $ 0.10 ) ? : '))
    nickles = int(input('How many nickles ( $ 0.05 ) ? : '))
    pennies = int(input('How many pennies ( % 0.01 ) ? : '))

    m_quarters = quarters * 0.25
    m_dimes = dimes * 0.10
    m_nickles = nickles * 0.05
    m_pennies = pennies * 0.01

    return m_quarters + m_dimes + m_nickles + m_pennies



while True:
    prompt = input('What would you like? (espresso / latte / cappuccino ): ').lower()

    if prompt == 'report'.lower():
        print(format_report_resource(resources))





    if prompt == 'off'.lower():
        break