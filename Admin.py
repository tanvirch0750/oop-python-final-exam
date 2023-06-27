from Person import Person
from User import User
from Bank import Bank


class Admin(Person):
    adminCount = 0  # Class attribute to track the number of admins

    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.adminId = self.generateAdminId()
        # Rest of the admin-specific code...

    @classmethod
    def generateAdminId(cls):
        cls.adminCount += 1
        return f"A{cls.adminCount}"

    def create_account(self, name, email, password):
        user = User(name, email, password)
        Bank.addUser(user)
        return user

    def checkBankBalance(self):
        return Bank.checkBankBalance(self.adminId)

    def checkLoanAmount(self):
        return Bank.changeLoanFeature(self.adminId)

    def changeLoanFeature(self):
        return Bank.changeLoanFeature(self.adminId)
