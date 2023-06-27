from Person import Person
from User import User
from Bank import Bank


class Admin(Person):
    adminCount = 0  # Class attribute to track the number of admins

    def __init__(self, name, email, password, bankInstance):
        super().__init__(name, email, password)
        self.adminId = self.generateAdminId()
        self.bankInstance = bankInstance

    @classmethod
    def generateAdminId(cls):
        cls.adminCount += 1
        return f"A{cls.adminCount}"

    def create_account(self, user):
        if self.adminId in Bank.admins:
            self.bankInstance.addUser(user)
        else:
            return "Unauthorized"

    def checkBankBalance(self):
        if self.adminId in Bank.admins:
            return self.bankInstance.checkBankBalance(self.adminId)
        else:
            return "Unauthorized"

    def checkLoanAmount(self):
        if self.adminId in Bank.admins:
            return self.bankInstance.getLoanAmount(self.adminId)
        else:
            return "Unauthorized"

    def changeLoanFeature(self):
        if self.adminId in Bank.admins:
            return self.bankInstance.changeLoanFeature(self.adminId)
        else:
            return "Unauthorized"
