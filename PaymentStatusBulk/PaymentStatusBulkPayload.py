class PaymentStatusBulkPayload:

    @property
    def request_id(self):
        return self.__request_id

    @request_id.setter
    def request_id(self, value):
        self.__request_id = value

    @property
    def batch_ref(self):
        return self.__batch_ref

    @batch_ref.setter
    def batch_ref(self, value):
        self.__batch_ref = value
