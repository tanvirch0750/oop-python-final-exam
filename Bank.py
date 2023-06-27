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

    def checkBankBalance(self, admin):
        if admin.adminId in self.admins:
            return Bank.totalBalance
        else:
            return "Only admins can check the bank balance."

    def getLoanAmount(self, admin):
        if admin.adminId in self.admins:
            return Bank.totalLoanAmount
        else:
            return "Only admins can check the total loan amount."

    def changeLoanFeature(self, admin):
        if admin.adminId in self.admins:
            Bank.loanActive = not Bank.loanActive
            return f"Loan feature is {'active' if Bank.loanActive else 'disabled'}."
        else:
            return "Only admins can change the loan feature."
        
    def __repr__(self) -> str:
        print(f"*********{self.name}*********")