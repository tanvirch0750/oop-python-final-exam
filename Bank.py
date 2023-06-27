class Bank:
    totalBalance = 0
    totalLoanAmount = 0
    loanActive = True

    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.users = {}
        self.admins = {}

    def addUser(self, user):
        self.users[user.accountNumber] = user

    def addAdmin(self, admin):
        self.admins[admin.adminId] = admin

    def checkBankBalance(self, adminId):
        if adminId in self.admins:
            return Bank.totalBalance
        else:
            return "Only admins can check the bank balance."

    def getLoanAmount(self, adminId):
        if adminId in self.admins:
            return Bank.totalLoanAmount
        else:
            return "Only admins can check the total loan amount."

    def changeLoanFeature(self, adminId):
        if adminId in self.admins:
            Bank.loanActive = not Bank.loanActive
            return f"Loan feature is {'active' if Bank.loanActive else 'disabled'}."
        else:
            return "Only admins can change the loan feature."

    def __repr__(self) -> str:
        print(" ")
        print("******************************")
        print(f"*********{self.name}*********")
        print("******************************")
        print(" ")
        print(f"=========Bank Stats==========")
        print(" ")
        print(f"Bank Total Balance: {self.totalBalance}")
        print(f"Bank Total Loan: {self.totalLoanAmount}")
        print(f"Loan Status: {self.loanActive}")
        print(" ")
        print(f"==========Bank Admins=========")
        print(" ")
        print("--------------------")
        for key, admin in self.admins.items():
            print(f"Name: {admin.name}")
            print(f"Id: {key}")
            print(f"Email: {admin.email}")
            print("--------------------")
        print(" ")
        print(f"===========Bank Users==========")
        print(" ")
        print("--------------------")
        for key, user in self.users.items():
            print(f"Name: {user.name}")
            print(f"Account Number: {key}")
            print(f"Email: {user.email}")
            print(f"Balance: {user.balance}")
            print(f"Loan Amount: {user.loanAmount}")
            print(f"Transaction History: {user.transactionHistory}")
            print("--------------------")

        return ""
