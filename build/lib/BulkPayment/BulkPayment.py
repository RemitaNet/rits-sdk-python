from datetime import datetime

import requests
from requests import ReadTimeout, ConnectTimeout

from RemitaInterbankService.BaseResponse import BaseResponse
from RemitaInterbankService.EncryptionUtil import EncryptionConfig
from RemitaInterbankService.EnvironmentConfig import EnvironmentConfig
from RemitaInterbankService.SdkResponseCode import SdkResponseCode
from RemitaInterbankService.Timestamp import Timestamp


class BulkPayment(object):

    def bulk_payment(self, bulk_payment_payload, credentials):



        try:
            get_response = EnvironmentConfig()
            if not get_response.credential_available(credentials):
                return get_response.throw_exception(status=get_response.empty_credential_code,
                                                    data=get_response.empty_credential_msg)
            else:

                rpg_environment = EnvironmentConfig.set_rpg_environment(credentials)
                headers = self.set_header(bulk_payment_payload, credentials)
                url = rpg_environment['BULK_PAYMENT_URL']
                config = EncryptionConfig()
                encrypted_payment_detail_list = []
                encrypted_bulk_payment_info = {
                    'narration': config.AES128(credentials.enc_key, bulk_payment_payload.bulk_payment_info.narration, credentials.enc_vector),
                    'totalAmount': config.AES128(credentials.enc_key, bulk_payment_payload.bulk_payment_info.total_amount, credentials.enc_vector),
                    'batchRef': config.AES128(credentials.enc_key, bulk_payment_payload.bulk_payment_info.batch_ref, credentials.enc_vector),
                    'debitAccount': config.AES128(credentials.enc_key, bulk_payment_payload.bulk_payment_info.debit_account, credentials.enc_vector),
                    'bankCode': config.AES128(credentials.enc_key, bulk_payment_payload.bulk_payment_info.bank_code, credentials.enc_vector)}

                for payment_detail_values in bulk_payment_payload.payment_details:
                    encrypted_payment_details = {}
                    encrypted_payment_details.update({
                        'transRef': config.AES128(credentials.enc_key, payment_detail_values.trans_ref, credentials.enc_vector),
                        'narration': config.AES128(credentials.enc_key, payment_detail_values.narration, credentials.enc_vector),
                        'benficiaryEmail': config.AES128(credentials.enc_key, payment_detail_values.benficiary_email, credentials.enc_vector),
                        'benficiaryBankCode': config.AES128(credentials.enc_key, payment_detail_values.benficiary_bank_code, credentials.enc_vector),
                        'benficiaryAccountNumber': config.AES128(credentials.enc_key, payment_detail_values.benficiary_account_number,
                                                      credentials.enc_vector),
                        'amount': config.AES128(credentials.enc_key, str(payment_detail_values.amount), credentials.enc_vector)})
                    encrypted_payment_detail_list.append(encrypted_payment_details)

                bulk_payment_payload.bulk_payment_info = encrypted_bulk_payment_info
                bulk_payment_payload.payment_details = encrypted_payment_detail_list


                payload = {'bulkPaymentInfo':encrypted_bulk_payment_info, 'paymentDetails':encrypted_payment_detail_list}

                try:

                    response = requests.post(url, headers=headers, json=payload, timeout=credentials.connection_timeout)
                    bulk_payment_response = BaseResponse(response.content)

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

            return bulk_payment_response

        except Exception:
            return get_response.throw_exception(status=SdkResponseCode.ERROR_PROCESSING_REQUEST_CODE,
                                                data=SdkResponseCode.ERROR_PROCESSING_REQUEST)




    def set_header(self, bulk_payment_payload, credentials):

        hash_string = credentials.api_key + bulk_payment_payload.bulk_payment_info.request_id + credentials.api_token

        txn_hash = EncryptionConfig.sha512(hash_string)

        time_stamp = Timestamp()

        headers = {'Content-Type': 'application/json', 'MERCHANT_ID':credentials.merchant_id, 'API_KEY':credentials.api_key,
                   'REQUEST_ID':bulk_payment_payload.bulk_payment_info.request_id, 'REQUEST_TS': time_stamp.dateTimeObj(dateTimeObj=datetime.now()),
                   'API_DETAILS_HASH': txn_hash}
        return headers



