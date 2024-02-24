import math
import locale


def monthly_payment(principle, rate_decimal, years=30):
    months = years * 12
    formula_top = principle * (rate_decimal / 12)
    formula_bottom = (1 - math.pow(1 + (rate_decimal / 12), -months))

    return formula_top / formula_bottom


def affordable(take_home, payment):
    highest_payment = take_home * .3
    return payment <= (highest_payment + 150)


def print_results(result_dictionary):

    for key, value in result_dictionary.items():
        print('--------------------------------------')
        print(key + ': ' + value)

    print('--------------------------------------')


def get_currency(amount):
    locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')
    return locale.currency(amount, grouping=True)


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

    print_results(result_dictionary)


if __name__ == '__main__':
    entry()
