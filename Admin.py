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
        self.bankInstance.addUser(user)
        # return user1

    def checkBankBalance(self):
        return self.bankInstance.checkBankBalance(self.adminId)

    def checkLoanAmount(self):
        return self.bankInstance.getLoanAmount(self.adminId)

    def changeLoanFeature(self):
        return self.bankInstance.changeLoanFeature(self.adminId)
