class BankAccount:                                                              # parent class BankAccount (useless)
    def __init__(self, client, balance, interest, acc_type="deposit"):          # class constructor
        self._client = client
        self._balance = balance
        self._interest = interest
        self._acc_type = acc_type

    def get_client(self):                                                       # client getter
        return self._client

    def get_balance(self):                                                      # balance getter
        return self._balance

    def get_interest(self):                                                     # interest getter
        return self._interest

    def get_acc_type(self):                                                     # acc type getter
        return self._acc_type


class Deposit(BankAccount):                                                     # subclass Deposit
    def __init__(self, client, balance, interest, acc_type="deposit"):          # using superclass constructor
        super().__init__(client, balance, interest, acc_type)


class Credit(BankAccount):                                                      # subclass Credit
    def __init__(self, client, balance, interest, acc_type="credit"):           # using superclass constructor
        super().__init__(client, balance, interest)
        self._acc_type = acc_type                                               # changing acc_type parameter


class Mortgage(BankAccount):                                                    # subclass Mortgage
    def __init__(self, client, balance, interest, acc_type="mortgage"):         # using superclass constructor
        super().__init__(client, balance, interest)
        self._acc_type = acc_type                                               # changing acc_type parameter
