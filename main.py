from data import MENU, resources

def format_report_resource(resource):
    water = resource['water']
    milk = resource['milk']
    coffee = resource['coffee']
    money = resource['money']

    return f'Water: {water} ml\nMilk: {milk} ml\nCoffee: {coffee} g\nMoney: $ {money}'


def check_resources(resource, drink):

    for ingredients in drink:
        if resource[ingredients] < drink[ingredients]:
            print(f'There is not enough {ingredients}.')
            return False
    return True


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


def check_transaction(money_received, drink_cost):
    if drink_cost > money_received:
        print("That's not enough money. Money refunded")
        return False
    elif money_received > drink_cost:
        print(f'Here is $ {round(money_received - drink_cost,2)} in change.')
        return True
    else:
        return True


def make_coffee(resource, drink_resource):

    for ingredients in drink_resource:
        resource[ingredients] -= drink_resource[ingredients]

while True:

    try:
        prompt = input('What would you like? -> espresso / latte / cappuccino : ').lower()

        if prompt == 'off'.lower():
            break

        if prompt == 'report'.lower():
            print(format_report_resource(resources))
            continue

        if check_resources(resources, MENU[prompt]['ingredients']):
            if check_transaction(process_coins(), MENU[prompt]['cost']):
                make_coffee(resources, MENU[prompt]['ingredients'])
                resources['money'] += MENU[prompt]['cost']
                print(f'Here is your {prompt}.')

    except KeyError:
        print('Invalid. Try again.')