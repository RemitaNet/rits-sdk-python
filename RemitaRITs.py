from BulkPayment.BulkPayment import BulkPayment
from Credentials import Credentials
from GetAccountEnquiry.AccountEnquiry import AccountEnquiry
from GetActiveBanks.GetActiveBanks import GetActiveBanks
from GetAddAccount.AddAccount import AddAccount
from PaymentStatus.PaymentStatus import PaymentStatus
from PaymentStatusBulk.PaymentStatusBulk import PaymentStatusBulk
from SinglePayment.SinglePayment import SinglePayment
from ValidateAccountOTP.ValidateAccountOTP import ValidateAccountOTP


class RemitaRITs:

    credentials: Credentials

    def __init__(self, credentials: Credentials):
        self.credentials = credentials

    def account_enquiry(self, payload):
        account_enquiry = AccountEnquiry()
        return account_enquiry.account_enquiry(payload, self.credentials)

    def get_active_banks(self, payload):
        get_active_banks = GetActiveBanks()
        return get_active_banks.get_active_banks(payload, self.credentials)

    def add_account(self, payload):
        add_account = AddAccount()
        return add_account.add_account(payload, self.credentials)

    def payment_status(self, payload):
        payment_status = PaymentStatus()
        return payment_status.payment_status(payload, self.credentials)

    def payment_status_bulk(self, payload):
        payment_status_bulk = PaymentStatusBulk()
        return payment_status_bulk.payment_status_bulk(payload, self.credentials)

    def single_payment(self, payload):
        single_payment = SinglePayment()
        return single_payment.single_payment(payload, self.credentials)

    def validate_account_otp(self, payload):
        validate_account_otp = ValidateAccountOTP()
        return validate_account_otp.validate_account_otp(payload, self.credentials)

    def bulk_payment(self, payload):
        bulk_payment = BulkPayment()
        return bulk_payment.bulk_payment(payload, self.credentials)