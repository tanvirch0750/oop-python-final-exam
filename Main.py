from Bank import Bank
from Admin import Admin
from User import User


def main():
    bank = Bank("Bank Tanvir", "Dhaka Bangladesh")

    # create admin
    admin1 = Admin("Israk Chowdhury", "israk@email.com", "1234", bank)
    admin2 = Admin("Tanvir Chowdhury", "tanvir@email.com", "1234", bank)

    bank.addAdmin(admin1)
    bank.addAdmin(admin2)

    # create user
    userHasan = User("Hasan Mahmud", "hasan@email.com", "1234")
    userJubaer = User("Jubaer Ahmed", "jubaer@email.com", "1234")

    # add user to bank
    admin1.create_account(userHasan)
    admin1.create_account(userJubaer)

    # deposit
    userHasan.deposit(50000)
    userJubaer.deposit(10000)

    # withdraw
    withd = userJubaer.withdraw(1000)
    print(withd)

    # check Balance
    print(f"Balance: {userJubaer.checkBalance()}")

    # transfer money
    tfm = userJubaer.transfer(1000, userHasan)
    print(tfm)

    # check transaction history
    print(userJubaer.checkTransactionHistory())

    # take loan
    loan = userJubaer.takeLoan()
    print(loan)

    userHasan.withdraw(1000)

    # admin check balance
    total_balance = admin2.checkBankBalance()
    print(f"Total Balance: {total_balance}")

    # admin check balance
    total_balance = admin1.checkBankBalance()
    print(f"Total Balance: {total_balance}")

    # admin check loan amount
    total_loan = admin1.checkLoanAmount()
    print(f"Total Loan: {total_loan}")

    # admin can off loan feature
    admin1.changeLoanFeature()

    print(bank)


if __name__ == "__main__":
    main()
