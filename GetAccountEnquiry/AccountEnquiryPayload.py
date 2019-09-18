class AccountEnquiryPayload:


    @property
    def account_number(self):
        return self.__account_number


    @account_number.setter
    def account_number(self, value):
        self.__account_number = value

    @property
    def bank_code(self):
        return self.__bank_code

    @bank_code.setter
    def bank_code(self, value):
        self.__bank_code = value

    @property
    def request_id(self):
        return self.__request_id

    @request_id.setter
    def request_id(self, value):
        self.__request_id = value
