from bank_account import Banck_Account

if __name__=='__main__':
    account = Banck_Account(10000)

    #Depositing
    account.depositing(350)
    print(f'Balance after depositing {account.balance}')

    #withdrawing
    account.withdrawing(350)
    print(f'Balance after withdrawing {account.balance}')

    