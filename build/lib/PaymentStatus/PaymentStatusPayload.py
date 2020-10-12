class PaymentStatusPayload:

    @property
    def request_id(self):
        return self.__request_id

    @request_id.setter
    def request_id(self, value):
        self.__request_id = value

    @property
    def trans_ref(self):
        return self.__trans_ref

    @trans_ref.setter
    def trans_ref(self, value):
        self.__trans_ref = value
