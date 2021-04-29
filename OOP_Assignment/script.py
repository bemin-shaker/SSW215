class duckBankAccount:
    name_of_scrooge = 'Scrooge McDuck'
    ducks = []
    percentage_max_withdraw = 0.1
    penalty = 5

    def __init__(self, name, accNum, balance):
        self.numWithdrawals = 0
        self.numDeposits = 0
        self.numPenalties = 0
        self.name = name
        self.accNum = accNum
        self.balance = balance
        self.maxWithdraw = self.balance * self.percentage_max_withdraw
        self.ducks.append(self)

    def deposit(self, amount):
        self.balance += amount
        self.numDeposits += 1

    def withdraw(self, amount):
        if(amount > self.maxWithdraw):
            self.numPenalties += 1
            self.balance -= self.penalty
            self.updateMaxWithdrawAmount()
            self.depositInScrooge(self.penalty)
            self.printAccounts()
        else:
            self.balance -= amount
            self.numWithdrawals += 1
            self.depositInOtherDucks(self.accNum, amount)
            self.printAccounts()

    def depositInOtherDucks(self, accNum, amount):
        for duck in self.ducks:
            if(duck.accNum != accNum):
                duck.deposit(amount)
                self.withDrawFromScrooge(amount)
        self.printAccounts()

    def depositInScrooge(self, amount):
        for duck in self.ducks:
            if duck.name == self.name_of_scrooge:
                duck.balance += amount

    def withDrawFromScrooge(self, amount):
        for duck in self.ducks:
            if duck.name == self.name_of_scrooge:
                duck.balance -= amount

    def updateMaxWithdrawAmount(self):
        self.maxWithdraw = self.balance * self.percentage_max_withdraw

    def printAccounts(self):
        for duck in self.ducks:
            print(duck.name + ' has $' + str(duck.balance) +
                  ' in account')
        print()


dewey = duckBankAccount('Dewey Duck', 800008, 350)
huey = duckBankAccount('Huey Duck', 700007, 150)
louie = duckBankAccount('Louie Duck', 900009, 25)
scrooge = duckBankAccount('Scrooge McDuck', 100001, 1000000)

louie.withdraw(2)
dewey.withdraw(20)
huey.withdraw(20)
louie.withdraw(10)
dewey.withdraw(20)
huey.withdraw(30)
louie.withdraw(40)
