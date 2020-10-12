from datetime import datetime

import requests
from requests import ConnectTimeout, ReadTimeout

from RemitaInterbankService.BaseResponse import BaseResponse
from RemitaInterbankService.EncryptionUtil import EncryptionConfig
from RemitaInterbankService.EnvironmentConfig import EnvironmentConfig
from RemitaInterbankService.SdkResponseCode import SdkResponseCode
from RemitaInterbankService.Timestamp import Timestamp


class ValidateAccountOTP(object):

    def validate_account_otp(self, validate_account_otp_payload, credentials):

        try:
            get_response = EnvironmentConfig()
            if not get_response.credential_available(credentials):
                return get_response.throw_exception(status=get_response.empty_credential_code,
                                                    data=get_response.empty_credential_msg)
            else:
                rpg_environment = EnvironmentConfig.set_rpg_environment(credentials)
                headers = self.set_header(validate_account_otp_payload, credentials)
                url = rpg_environment['VALIDATE_ACC_OTP__URL']
                if not credentials.connection_timeout:
                    credentials.connection_timeout = 30000
                config = EncryptionConfig()
                validate_account_otp_payload_list = validate_account_otp_payload.auth_params
                validate_account_otp_payload_otp_value = config.AES128(credentials.enc_key, validate_account_otp_payload_list["OTP"], credentials.enc_vector)
                validate_account_otp_payload_card_value = config.AES128(credentials.enc_key, validate_account_otp_payload_list["Card"], credentials.enc_vector)

                get_otp = {
                    "param1":"OTP",
                    "value": validate_account_otp_payload_otp_value
                }

                get_card = {
                    "param2":"CARD",
                    "value": validate_account_otp_payload_card_value
                }

                get_authParams = [get_otp, get_card]

                payload = {
                    'remitaTransRef': config.AES128(credentials.enc_key, validate_account_otp_payload.remita_trans_ref,credentials.enc_vector),
                    'authParams': get_authParams
                }
                try:
                    response = requests.post(url, headers=headers, json=payload)
                    validate_account_otp_response = BaseResponse(response.content)

                except ConnectTimeout:
                    return get_response.throw_exception(status=SdkResponseCode.CONNECTION_TIMEOUT_CODE,
                                                        data=SdkResponseCode.CONNECTION_TIMEOUT)
                except ValueError:
                    return get_response.throw_exception(status=SdkResponseCode.ERROR_IN_VALUE_CODE,
                                                        data=SdkResponseCode.ERROR_IN_VALUE)
                except ReadTimeout:
                    return get_response.throw_exception(status=SdkResponseCode.CONNECTION_TIMEOUT_CODE,
                                                        data=SdkResponseCode.CONNECTION_TIMEOUT)
                except ConnectionError as e:  # This is the correct syntax
                    return get_response.throw_exception(status=SdkResponseCode.ERROR_WHILE_CONNECTING_CODE,
                                                        data=SdkResponseCode.ERROR_WHILE_CONNECTING)

            return validate_account_otp_response

        except Exception:
            return get_response.throw_exception(status=SdkResponseCode.ERROR_PROCESSING_REQUEST_CODE,
                                            data=SdkResponseCode.ERROR_PROCESSING_REQUEST)



    def set_header(self, validate_account_otp_payload, credentials):

        hash_string = credentials.api_key + validate_account_otp_payload.request_id + credentials.api_token

        txn_hash = EncryptionConfig.sha512(hash_string)
        time_stamp = Timestamp()

        headers = {'Content-Type': 'application/json', 'MERCHANT_ID':credentials.merchant_id, 'API_KEY':credentials.api_key,
                   'REQUEST_ID':validate_account_otp_payload.request_id, 'REQUEST_TS':time_stamp.dateTimeObj(dateTimeObj=datetime.now()),
                   'API_DETAILS_HASH': txn_hash}

        return headers



