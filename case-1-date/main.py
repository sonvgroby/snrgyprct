from datetime import date
import calendar

DIGITS = {
    "0": [" *** ", "*   *", "*   *", "*   *", " *** "],
    "1": ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
    "2": [" *** ", "    *", " *** ", "*    ", "*****"],
    "3": [" *** ", "    *", " *** ", "    *", " *** "],
    "4": ["*   *", "*   *", "*****", "    *", "    *"],
    "5": ["*****", "*    ", "**** ", "    *", "**** "],
    "6": [" *** ", "*    ", "**** ", "*   *", " *** "],
    "7": ["*****", "    *", "   * ", "  *  ", " *   "],
    "8": [" *** ", "*   *", " *** ", "*   *", " *** "],
    "9": [" *** ", "*   *", " ****", "    *", " *** "],
}


def get_weekday(day: int, month: int, year: int) -> str:
    weekday_index = date(year, month, day).weekday()
    weekdays = [
        "понедельник",
        "вторник",
        "среда",
        "четверг",
        "пятница",
        "суббота",
        "воскресенье",
    ]
    return weekdays[weekday_index]


def is_leap_year(year: int) -> bool:
    return calendar.isleap(year)


def get_age(day: int, month: int, year: int) -> int:
    today = date.today()
    age = today.year - year

    if (today.month, today.day) < (month, day):
        age -= 1

    return age


def print_styled_date(day: int, month: int, year: int) -> None:
    date_string = f"{day:02d}{month:02d}{year:04d}"

    for row in range(5):
        line = []
        for char in date_string:
            line.append(DIGITS[char][row])
        print("  ".join(line))


def main():
    try:
        day = int(input("Введите день рождения: "))
        month = int(input("Введите месяц рождения: "))
        year = int(input("Введите год рождения: "))

        birth_date = date(year, month, day)

        print("\nДата рождения:", birth_date.strftime("%d.%m.%Y"))
        print("День недели:", get_weekday(day, month, year))
        print("Високосный год:", "да" if is_leap_year(year) else "нет")
        print("Возраст:", get_age(day, month, year), "лет")

        print("\nДата рождения звездочками:")
        print_styled_date(day, month, year)

    except ValueError:
        print("Ошибка: введена некорректная дата или нечисловое значение.")


if __name__ == "__main__":
    main()
