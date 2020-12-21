import datetime as dt


class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        self.date = date
        if date is None:
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(self.date, "%d.%m.%Y").date()


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, Record):
        self.records.append(Record)

    def get_today_stats(self):
        moment = dt.datetime.now().date()
        num = sum(i.amount for i in self.records if i.date == moment)
        return num

    def get_week_stats(self):
        today = dt.datetime.now().date()
        week = today - dt.timedelta(days=7)
        number = sum([i.amount for i in self.records if week <= i.date <= today])
        return number


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        number = self.get_today_stats()
        if number < self.limit:
            other = self.limit - number
            return ('Сегодня можно съесть что-нибудь ещё, '
                    f'но с общей калорийностью не более {round(other, 2)} кКал')
        else:
            return ('Хватит есть!')


class CashCalculator(Calculator):
    USD_RATE = 73.12
    EURO_RATE = 85.12

    def get_today_cash_remained(self, currency):
        today_stats = self.get_today_stats()
        other_limit = self.limit - today_stats
        currencies = {
             'usd': (self.USD_RATE, 'USD'),
             'eur': (self.EURO_RATE, 'Euro'),
             'rub': (1, 'руб')
        }

        if currency in currencies:
            currency_number = currencies[currency][0]
            currency_name = currencies[currency][1]
        else:
            return ('Валюта не найдена')
        if today_stats < self.limit:
            return ('На сегодня осталось '
                    f'{round(other_limit / currency_number, 2)} {currency_name}')
        elif today_stats == self.limit:
            return ('Денег нет, держись')
        elif today_stats > self.limit:
            debt = abs(other_limit)
            return ('Денег нет, держись: твой долг - '
                    f'{round(debt / currency_number, 2)} {currency_name}')


if __name__ == '__main__':
    cash_calculator = CashCalculator(1000)


    cash_calculator.add_record(Record(amount=145, comment="кофе"))
    cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
    cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
    print(cash_calculator.get_today_cash_remained("usd"))
