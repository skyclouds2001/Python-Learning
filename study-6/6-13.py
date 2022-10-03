def print_month(year, month):
    print_month_title(year, month)
    print_month_body(year, month)


def print_month_title(year, month):
    print("           ", get_month_name(month), "  ", year)
    print("-----------------------------------")
    print(" Sun  Mon  Tue  Wed  Thu  Fri  Sat")


def print_month_body(year, month):
    start_day = get_start_day(year, month)
    numbers_of_days_in_month = get_number_of_days_in_month(year, month)

    for i in range(0, start_day):
        print("    ", end=" ")

    for i in range(1, numbers_of_days_in_month + 1):
        print(format(i, "4d"), end=" ")

        if (i + start_day) % 7 == 0:
            print()


def get_month_name(month):
    list0 = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

    return list0[month - 1]


def get_number_of_days_in_month(year, month):
    list1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return list1[month - 1]


def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def get_start_day(year, month):
    START_DAY_FOR_JAN_1_1800 = 3

    total_numbers_of_days = get_total_numbers_of_days(year, month)
    return (total_numbers_of_days + START_DAY_FOR_JAN_1_1800) % 7


def get_total_numbers_of_days(year, month):
    total = 0

    for i in range(1800, year):
        total += 366 if is_leap_year(i) else 365

    for i in range(1, month):
        total += get_number_of_days_in_month(year, i)

    return total


def main():
    year = eval(input("Enter full year : "))
    month = eval(input("Enter full month : "))
    print_month(year, month)


main()
