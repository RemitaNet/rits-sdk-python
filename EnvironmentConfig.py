from BaseResponse import BaseResponse
from Credentials import Credentials

class EnvironmentConfig:

    def set_rpg_environment(Credentials):
        trim_environment = Credentials.environment.strip()
        environment_to_upper = trim_environment.upper()

        if environment_to_upper == "TEST":
            test_url = "https://remitademo.net/remita/exapp/api/v1/send/api/rpgsvc/rpg/api/v2/"
            rpg_environment = {'API_KEY': Credentials.api_key,
                                   'API_TOKEN': Credentials.api_token,
                                   'MERCHANT_ID': Credentials.merchant_id,
                                   'KEY': Credentials.enc_key,
                                   'IV': Credentials.enc_vector,
                                   'ENVIRONMENT': Credentials.environment,
                                   'READ_TIMEOUT': Credentials.read_timeout,
                                   'CONNECTION_TIMEOUT': Credentials.connection_timeout,
                                   'ACCOUNT_ENQUIRY_URL': test_url + "merc/fi/account/lookup",
                                   'GET_ACTIVE_BANKS_URL': test_url + "fi/banks",
                                   'SINGLE_PAYMENT_URL': test_url + "merc/payment/singlePayment.json",
                                   'SINGLE_PAYMENT_STATUS_URL': test_url + "merc/payment/status",
                                   'BULK_PAYMENT_STATUS_URL': test_url + "merc/bulk/payment/status",
                                   'BULK_PAYMENT_URL': test_url + "merc/bulk/payment/send",
                                   'ADD_ACCOUNT_URL': test_url + "merc/account/token/init",
                                   'VALIDATE_ACC_OTP__URL': test_url + "merc/account/token/validate"
                                   }
            return rpg_environment
        elif environment_to_upper == "LIVE":
            live_url = "https://login.remita.net/remita/exapp/api/v1/send/api/rpgsvc/rpg/api/v2/"
            rpg_environment = {'PUBLIC_KEY': Credentials.public_key,
                                   'SECRET_KEY': Credentials.secret_key,
                                   'ENVIRONMENT': Credentials.environment,
                                   'READ_TIMEOUT': Credentials.read_timeout,
                                   'CONNECTION_TIMEOUT': Credentials.connection_timeout,
                                   'ACCOUNT_ENQUIRY_URL': live_url + "merc/fi/account/lookup",
                                   'GET_ACTIVE_BANKS_URL': live_url + "fi/banks",
                                   'SINGLE_PAYMENT_URL': live_url + "merc/payment/singlePayment.json",
                                   'SINGLE_PAYMENT_STATUS_URL': live_url + "merc/payment/status",
                                   'BULK_PAYMENT_STATUS_URL': live_url + "merc/bulk/payment/status",
                                   'BULK_PAYMENT_URL': live_url + "merc/bulk/payment/send",
                                   'ADD_ACCOUNT_URL': live_url + "merc/account/token/init",
                                   'VALIDATE_ACC_OTP__URL': live_url + "merc/account/token/validate"
                                   }
            return rpg_environment

    def credential_available(self, credentials):

        if not credentials.merchant_id:
            self.empty_credential_msg = "Merchant ID cannot be empty"
            self.empty_credential_data = "No available data"
            self.empty_credential_code = "011"
            return False

        elif not credentials.api_key:
            self.empty_credential_msg = "API key cannot be empty"
            self.empty_credential_data = "No available data"
            self.empty_credential_code = "012"
            return False

        elif not credentials.api_token:
            self.empty_credential_msg = "API Token cannot be empty"
            self.empty_credential_data = "No available data"
            self.empty_credential_code = "013"
            return False

        elif not credentials.enc_vector:
            self.empty_credential_msg = "ENC Vector cannot be empty"
            self.empty_credential_data = "No available data"
            self.empty_credential_code = "014"
            return False

        elif not credentials.enc_key:
            self.empty_credential_msg = "ENC key cannot be empty"
            self.empty_credential_data = "No available data"
            self.empty_credential_code = "015"
            return False

        elif not credentials.environment:
            credentials.environment = "TEST"
            return True
        else:
            return True


    def throw_exception(self, status, data):

        response = '{"status": "' + status + \
                   '", "data": "' + str(data) + \
                   '"}'
        base_response = \
            BaseResponse(response)
        return base_response



