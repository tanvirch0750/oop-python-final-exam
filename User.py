from Person import Person
from Bank import Bank
import random


class User(Person):
    userCount = 0

    def __init__(self, name, email, password) -> None:
        super().__init__(name, email, password)
        self.accountNumber = self.generateAccountNumber()
        self.balance = 0
        self.loanAmount = 0
        self.transactionHistory = []

    @classmethod
    def generateAccountNumber(self):
        self.userCount += 1
        return f"U{self.userCount}{random.randint(1000, 9999)}"

    def deposit(self, amount):
        if self.accountNumber in Bank.users:
            self.balance += amount
            Bank.totalBalance += amount
            self.transactionHistory.append(f"Deposited: {amount}")
        else:
            return "No user found"

    def withdraw(self, amount):
        if self.accountNumber in Bank.users:
            if Bank.totalBalance >= amount:
                if self.balance >= amount:
                    self.balance -= amount
                    Bank.totalBalance -= amount
                    self.transactionHistory.append(f"Withdrawn: {amount}")
                else:
                    return "Not Enough funds. Unable to withdraw."
            else:
                return "Bank is bankrupt"
        else:
            return "No user found"

    def checkBalance(self):
        if self.accountNumber in Bank.users:
            return self.balance
        else:
            return "No user found"

    def transfer(self, amount, recipient):
        if self.accountNumber in Bank.users:
            if self.balance >= amount:
                self.balance -= amount
                recipient.balance += amount
                self.transactionHistory.append(
                    f"Transferred: {amount} to {recipient.name}"
                )
            else:
                return "Not enough funds. Unable to transfer."
        else:
            return "No user found"

    def checkTransactionHistory(self):
        if self.accountNumber in Bank.users:
            return self.transactionHistory
        else:
            return "No user found"

    def takeLoan(self):
        if self.accountNumber in Bank.users:
            if Bank.totalBalance >= self.balance * 2:
                if Bank.loanActive and self.loanAmount == 0:
                    loan_amount = self.balance * 2
                    self.balance += loan_amount
                    self.loanAmount = loan_amount
                    Bank.totalLoanAmount += loan_amount
                    self.transactionHistory.append(f"Loan taken: {loan_amount}")
                elif self.loanAmount > 0:
                    return "Loan already taken. Please repay the existing loan."
                else:
                    return "Loan feature is currently disabled."
            else:
                return "Bank is bankrupt"
        else:
            return "No user found"
