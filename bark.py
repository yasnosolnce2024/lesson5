class bank():
    def init(self, id, balance=0):
        self.id = id
        self.balance = balance
    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f'Вы успешно пополнили счет на сумму {self.balance}')
    def withdraw(self, money):
        if money > self.balance:
            print('Не достаточно на счете средств!')
        else:
            self.balance -= money
            print(f'Снятие со счета {money}. Остаток {self.balance}')
    def all_balance(self):
        print(f'Текущий баланс {self.balance}')

man = bank('2233', 6000)
man.all_balance()
man.deposit(1000)
man.withdraw(500)
man.all_balance()


