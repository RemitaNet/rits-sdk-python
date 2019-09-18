class Credentials:


    @property
    def api_key(self):
        return self.__api_key


    @api_key.setter
    def api_key(self, value):
        self.__api_key = value

    @property
    def merchant_id(self):
        return self.__merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self.__merchant_id = value

    @property
    def api_token(self):
        return self.__api_token

    @api_token.setter
    def api_token(self, value):
        self.__api_token = value

    @property
    def enc_key(self):
        return self.__enc_key

    @enc_key.setter
    def enc_key(self, value):
        self.__enc_key = value

    @property
    def enc_vector(self):
        return self.__enc_vector

    @enc_vector.setter
    def enc_vector(self, value):
        self.__enc_vector = value

    @property
    def environment(self):
        return self.__environment

    @environment.setter
    def environment(self, value):
        self.__environment = value


    @property
    def read_timeout(self):
        return self.__read_timeout


    @read_timeout.setter
    def read_timeout(self, value):
        self.__read_timeout = value


    @property
    def connection_timeout(self):
        return self.__connection_timeout


    @connection_timeout.setter
    def connection_timeout(self, value):
        self.__connection_timeout = value