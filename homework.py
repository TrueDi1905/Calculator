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
        num = 0
        moment = dt.datetime.now().date()
        for i in self.records:
            if i.date == moment:
                num += i.amount
        return num

    def get_week_stats(self):
        number = 0
        for i in self.records:
            today = dt.datetime.now().date()
            week = today - dt.timedelta(days=7)
            if week <= i.date <= today:
                number += i.amount
        return number


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        s = self.get_today_stats()
        if s < self.limit:
            other = self.limit - s
            return ('Сегодня можно съесть что-нибудь ещё, '
                    f'но с общей калорийностью не более {round(other, 2)} кКал')
        elif s >= self.limit:
            return ('Хватит есть!')


class CashCalculator(Calculator):
    USD_RATE = 75.12
    EURO_RATE = 85.31
    def get_today_cash_remained(self, currency):
        today_stats = self.get_today_stats()
        other_limit = self.limit - today_stats
        if currency == 'usd':
            rate = other_limit / self.USD_RATE
            forex = 'USD'
        elif currency == 'eur':
            rate = other_limit / self.EURO_RATE
            forex = 'Euro'
        elif currency == 'rub':
            rate = other_limit
            forex = 'руб'
        else:
            return ('не найдено')
        if today_stats < self.limit:
            return (f'На сегодня осталось {round(rate, 2)} {forex}')
        elif today_stats == self.limit:
            return ('Денег нет, держись')
        else:
            q = abs(rate)
            return (f'Денег нет, держись: твой долг - {round(q, 2)} {forex}')


cash_calculator = CashCalculator(1000)

cash_calculator.add_record(Record(amount=145, comment="кофе"))
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
print(cash_calculator.get_today_cash_remained("rub"))
r1 = Record(amount=145, comment="Безудержный шопинг", date="08.03.2019")
r2 = Record(amount=1568, comment="Наполнение потребительской корзины", date="09.03.2019")
r3 = Record(amount=691, comment="Катание на такси")
print(r1.date)
print(r2.date)
print(r3.date)