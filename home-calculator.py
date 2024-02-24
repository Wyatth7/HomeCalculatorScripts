import math
import locale

locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')


# Prints home calculation results
def print_results(result_dictionary, take_home):

    print()
    print('Welcome to the Mortgage & Home Payment Calculator!')
    print('We will calculate if you can afford a home and it\'s monthly operating cost.')
    print()
    print('Your total take home pay for this month is: ', get_currency(take_home))
    print()

    print('--------------------------------------------------')
    print('|               Payment Breakdown                |')
    for key, value in result_dictionary.items():
        print('--------------------------------------------------')

        # table width is 50, but we insert a : , so use 49 in calculation characters
        spaces = create_spaces(49 - (key.__len__() + value.__len__()))

        print(key + ':' + spaces + value)

    print('--------------------------------------------------')


# Creates spaces for table output
def create_spaces(count):
    space_string = ''
    for space in range(0, count):
        space_string += ' '

    return space_string


def get_currency(amount):
    return locale.currency(amount, grouping=True)


# Calculates monthly mortgage payment
def monthly_payment(principle, rate_decimal, years=30):
    months = years * 12
    formula_top = principle * (rate_decimal / 12)
    formula_bottom = (1 - math.pow(1 + (rate_decimal / 12), -months))

    return formula_top / formula_bottom


# Checks if payment is affordable for take home pay
def affordable(take_home, payment):
    highest_payment = take_home * .3
    return payment <= (highest_payment + 150)


def entry():
    monthly_take_home = 5598
    down_payment = 50000
    mortgage = 300000
    rate = .03
    power = 200
    water = 40
    insurance = 200
    total_operations_cost = power + water + insurance

    payment = monthly_payment(mortgage - down_payment, rate)
    is_affordable = 'Affordable' if affordable(monthly_take_home, payment + total_operations_cost) else 'Not Affordable'

    result_dictionary = {
        'Monthly Payment': get_currency(payment + total_operations_cost) + '; ' + is_affordable,
        'Monthly Take Home': get_currency(monthly_take_home),
        'Mortgage': get_currency(mortgage),
        'Mortgage Payment': get_currency(payment),
        'Operations': get_currency(total_operations_cost),
    }

    print_results(result_dictionary, monthly_take_home)


if __name__ == '__main__':
    entry()
