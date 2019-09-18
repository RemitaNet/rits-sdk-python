from BulkPayment.BulkPayment import BulkPayment
from Credentials import Credentials
from EncryptionUtil import EncryptionConfig
from GetAccountEnquiry.AccountEnquiry import AccountEnquiry
from GetAccountEnquiry.AccountEnquiryPayload import AccountEnquiryPayload
from GetAddAccount.AddAccount import AddAccount
from GetAddAccount.AddAccountPayload import AddAccountPayload
from GetActiveBanks.GetActiveBanks import GetActiveBanks
from GetActiveBanks.GetActiveBanksPayload import GetActiveBanksPayload
from PaymentStatus.PaymentStatus import PaymentStatus
from PaymentStatus.PaymentStatusPayload import PaymentStatusPayload
from PaymentStatusBulk.PaymentStatusBulk import PaymentStatusBulk
from PaymentStatusBulk.PaymentStatusBulkPayload import PaymentStatusBulkPayload
from RemitaRITs import RemitaRITs
from SinglePayment.SinglePayment import SinglePayment
from SinglePayment.SinglePaymentPayload import SinglePaymentPayload
from ValidateAccountOTP.ValidateAccountOTP import ValidateAccountOTP
from ValidateAccountOTP.ValidateAccountOTPPayload import ValidateAccountOTPPayload
from BulkPayment.BulkPaymentPayload import BulkPaymentPayload, PaymentDetail
from BulkPayment.BulkPaymentPayload import BulkPaymentInfo


class TestRPG(object):
    credentials = Credentials()
    credentials.api_key = "S1VESTEyMzR8S1VESQ=="
    credentials.api_token = "dWFBTVVGTGZRUEZaemRvVC8wYVNuRkVTc2REVi9GWGdCMHRvWHNXTnovaz0="
    credentials.merchant_id = "KUDI1234"
    credentials.enc_key= "cymsrniuxqtgfzva"
    credentials.enc_vector= "czidrfwqugpaxvkj"
    credentials.environment = "TEST"
    # Optional Credentials
    credentials.read_timeout = 30000
    credentials.connection_timeout = 30000

    payload = PaymentStatusBulkPayload()
    payload.request_id = "1567529455332544004653454505"
    payload.batch_ref = "418087"

    remita_rits_service = RemitaRITs(credentials=credentials)
    payment_status_bulk_response = remita_rits_service.payment_status_bulk(payload=payload)

    print (payment_status_bulk_response.data)



    # request_id = "156755354325527448866505"
    # auth_params = {"OTP": "1234", "Card": "0441234567890" }
    # remita_trans_ref = "MTU2NzcwNjAzNDAwOQ=="
    # payload = ValidateAccountOTPPayload(remita_trans_ref=remita_trans_ref, auth_params=auth_params, request_id=request_id)
    #
    # remita_rits_service = RemitaRITs(credentials=credentials)
    # validate_account_otp_response = remita_rits_service.validate_account_otp(payload=payload)
    # print (validate_account_otp_response.data)

    # payload= AddAccountPayload()
    # payload.request_id= "156752945496045566769090807860"
    # payload.account_number= "044222222"
    # payload.bank_code= "044"
    # remita_rits_service = RemitaRITs(credentials=credentials)
    # add_account_response = remita_rits_service.add_account(payload=payload)
    #
    # print (add_account_response.data)

    # payload= AccountEnquiryPayload()
    # payload.request_id= "156752903373566787764674989"
    # payload.account_number= "044222222"
    # payload.bank_code= "044"
    #
    # remita_rits_service = RemitaRITs(credentials=credentials)
    # account_enquiry_response = remita_rits_service.account_enquiry(payload=payload)
    # # account_enquiry_response = account_enquiry.account_enquiry(payload, credentials)
    #
    # print (account_enquiry_response.data)


    # payload= GetActiveBanksPayload()
    # payload.request_id= "156237566529477765505"
    #
    # # get_active_banks = GetActiveBanks()
    # # get_active_banks_response = get_active_banks.get_active_banks(payload, credentials)
    # remita_rits_service = RemitaRITs(credentials=credentials)
    # get_active_banks_response = remita_rits_service.get_active_banks(payload=payload)
    #
    # print (get_active_banks_response.data)


    # payload = PaymentStatusPayload()
    # payload.request_id = "15675546294777655544435564505"
    # payload.trans_ref = "418073388"
    #
    # # payment_status = PaymentStatus()
    # # payment_status_response = payment_status.payment_status(payload, credentials)
    # remita_rits_service = RemitaRITs(credentials=credentials)
    # payment_status_response = remita_rits_service.payment_status(payload=payload)
    #
    # print (payment_status_response.data)

    # payload = PaymentStatusBulkPayload()
    # payload.request_id = "15675294555444653454505"
    # payload.trans_ref = "418087"
    #
    # # payment_status_bulk = PaymentStatusBulk()
    # # payment_status_bulk_response = payment_status_bulk.payment_status_bulk(payload, credentials)
    # remita_rits_service = RemitaRITs(credentials=credentials)
    # payment_status_bulk_response = remita_rits_service.payment_status_bulk(payload=payload)
    #
    # print (payment_status_bulk_response.data)


    # payload = SinglePaymentPayload()
    # payload.request_id = "15675294789539842245099505"
    # payload.trans_ref = "418083388"
    # payload.to_bank = "058"
    # payload.credit_account = "0582915208017"
    # payload.narration = "Regular Payment"
    # payload.amount = "5000"
    # payload.from_bank = "044"
    # payload.debit_account = "1234565678"
    # payload.beneficiary_email = "qa@test.com"
    #
    # # single_payment = SinglePayment()
    # # single_payment_response = single_payment.single_payment(payload, credentials)
    # remita_rits_service = RemitaRITs(credentials=credentials)
    # single_payment_response = remita_rits_service.single_payment(payload=payload)
    #
    # print(single_payment_response.data)



    # request_id = "156755354325527448866505"
    # auth_params = {"OTP": "1234", "Card": "0441234567890" }
    # remita_trans_ref = "MTU2NzcwNjAzNDAwOQ=="
    # payload = ValidateAccountOTPPayload(remita_trans_ref=remita_trans_ref, auth_params=auth_params, request_id=request_id)
    #
    # # validate_account_otp = ValidateAccountOTP()
    # # validate_account_otp_response = validate_account_otp.validate_account_otp(payload, credentials)
    # remita_rits_service = RemitaRITs(credentials=credentials)
    # validate_account_otp_response = remita_rits_service.validate_account_otp(payload=payload)
    #
    # print (validate_account_otp_response.data)
    # #
    # totalAmount = "10000"
    # batchRef= "23262367734"
    # debitAccount= "1234565678"
    # narration= "test payment"
    # bankCode= "044"
    # request_id= "3566745353478825334324867789043222"
    # bulk_payment_info_payload = BulkPaymentInfo(total_amount=totalAmount, batch_ref=batchRef, debit_account=debitAccount, narration=narration, bank_code=bankCode, request_id=request_id)
    #
    # payment_detail_list = []
    # payment_detail1 =PaymentDetail(trans_ref="43qqrf72645686769i76896578456u476856i9768dqq243221111432245321", narration="Regular Payment", benficiary_email="qa@test.com", benficiary_account_number="0582915208017", benficiary_bank_code="058", amount="2000" )
    # payment_detail2 =PaymentDetail(trans_ref="432qqqt34356345y5u45784i4j65i56374562342531243e43221143224324422", narration="Regular Payment", benficiary_email="qa@test.com", benficiary_account_number="0582915208099", benficiary_bank_code="058", amount="3000" )
    # payment_detail3 =PaymentDetail(trans_ref="432432q53146345yy4y3g345gg43g4g45yw4yw45g453g3weee11143224323453", narration="Regular Payment", benficiary_email="qa@test.com", benficiary_account_number="04499999999", benficiary_bank_code="044", amount="5000" )
    #
    # payment_detail_list.append(payment_detail1)
    # payment_detail_list.append(payment_detail2)
    # payment_detail_list.append(payment_detail3)
    #
    #
    # bulk_payload = BulkPaymentPayload(bulk_payment_info=bulk_payment_info_payload, payment_details=payment_detail_list)
    # # print(bulk_payload.bulk_payment_info.__dict__)
    # # print(bulk_payload.payment_details)
    # # bulk_payment = BulkPayment()
    # # bulk_payment_response = bulk_payment.bulk_payment(bulk_payload, credentials)
    # remita_rits_service = RemitaRITs(credentials=credentials)
    # bulk_payment_response = remita_rits_service.bulk_payment(payload=bulk_payload)
    #
    # print (bulk_payment_response.data)