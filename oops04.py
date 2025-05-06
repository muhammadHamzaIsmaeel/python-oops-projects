class Bank():
    bank_name = "HBL"

    def change_bank_name(cls, name):
        cls.bank_name = name

bank1 = Bank()
bank1.change_bank_name("UBL")

print(bank1.bank_name)