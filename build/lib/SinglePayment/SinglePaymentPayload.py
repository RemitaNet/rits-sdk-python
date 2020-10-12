class SinglePaymentPayload:


    @property
    def to_bank(self):
        return self.__to_bank


    @to_bank.setter
    def to_bank(self, value):
        self.__to_bank = value

    @property
    def credit_account(self):
        return self.__credit_account


    @credit_account.setter
    def credit_account(self, value):
        self.__credit_account = value

    @property
    def narration(self):
        return self.__narration


    @narration.setter
    def narration(self, value):
        self.__narration = value

    @property
    def amount(self):
        return self.__amount


    @amount.setter
    def amount(self, value):
        self.__amount = value

    @property
    def trans_ref(self):
        return self.__trans_ref


    @trans_ref.setter
    def trans_ref(self, value):
        self.__trans_ref = value

    @property
    def from_bank(self):
        return self.__from_bank


    @from_bank.setter
    def from_bank(self, value):
        self.__from_bank = value

    @property
    def debit_account(self):
        return self.__debit_account


    @debit_account.setter
    def debit_account(self, value):
        self.__debit_account = value

    @property
    def beneficiary_email(self):
        return self.__beneficiary_email


    @beneficiary_email.setter
    def beneficiary_email(self, value):
        self.__beneficiary_email = value

    @property
    def request_id(self):
        return self.__request_id

    @request_id.setter
    def request_id(self, value):
        self.__request_id = value
