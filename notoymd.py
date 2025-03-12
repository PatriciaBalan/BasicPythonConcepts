# given a no of days-> transform it in year, date, month


def birthday(n):
    years = n // 365

    months = (n - years *365) // 30
    month = (n % 365) // 30

    days = (n - years * 365 - months * 30)
    day = (n % 365) % 30

    print("Years = ", years)
    print("Months = ", months, month)
    print("Days = ", days, day)

birthday(3000)

#given no of minutes -> hours and minutes
m = 350
def hour(m):
    hour = m // 60
    min = (m % 60)

    print("hours = ", hour)
    print("minutes = ", min)

hour(376)