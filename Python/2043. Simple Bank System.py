class Bank:

    def __init__(self, balance: List[int]):
        self.acc = balance

    def validateAccount(self, account: int) -> bool:
        if account <= len(self.acc):
            return True
        return False

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        #put money from account1 into account2
        #aAcc is the array account position
        aAcc1 = account1 - 1
        aAcc2 = account2 - 1

        #check both accounts exist
        if not (self.validateAccount(account1) and self.validateAccount(account2)):
            return False
        bal1 = self.acc[aAcc1]
        bal1 = self.acc[aAcc2]
        if self.withdraw(account1,money):
            self.deposit(account2,money)
        else:
            return False
        return True

    def deposit(self, account: int, money: int) -> bool:
        #aAcc is the array account position
        aAcc = account - 1
        if not (self.validateAccount(account)):
            return False
        self.acc[aAcc] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        #aAcc is the array account position
        aAcc = account - 1
        if not (self.validateAccount(account) and self.acc[aAcc]>= money):
            return False
        self.acc[aAcc] -= money
        return True

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
