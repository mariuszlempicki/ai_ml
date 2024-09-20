my_money = 10
beer_price = 5


def is_underage(age):
    return age < 18


def calculate_total_price(number, unit_price):
    return number * unit_price


def get_positive_integer(message):
    value = input(message)
    try:
        value = int(value)
    except ValueError:
        return False

    if value > 0:
        return value
    else:
        return False


def insist_for_positive_number(integer_name):
    message = f"Podaj {integer_name}: "
    output_value = get_positive_integer(message)
    if not output_value:
        insist_for_positive_number(integer_name)
    return output_value


print(f"Dzień dobry, chciałbym kupić piwo.\n")

age = insist_for_positive_number("wiek")

if is_underage(age):
    print("Nieletnim nie sprzedajemy alkoholu, do widzenia!")
else:
    while True:
        n_of_beers = insist_for_positive_number("liczba piw")
        total_price = calculate_total_price(n_of_beers, beer_price)

        print(f"\nPiwo kosztuje {beer_price}zł. To będzie razem {total_price}zł\n")
        print(f"Mam {my_money}zł\n")

        if n_of_beers == 0:
            print(f"Zapraszamy innym razem. Do widzenia!")
            break
        elif my_money == total_price:
            print(f"Proszę, oto piwa, sztuk - {n_of_beers}")
            break
        elif my_money > total_price:
            print(f"Proszę, oto piwa, sztuk - {n_of_beers} oraz reszta: {my_money - total_price}zł")
            break
        else:
            print(f"To za mało, brakuje {total_price - my_money}zł")
