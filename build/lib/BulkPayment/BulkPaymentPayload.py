from typing import List


class BulkPaymentInfo:
    total_amount: float
    batch_ref: str
    debit_account: str
    narration: str
    bank_code: str
    request_id: str


    def __init__(self, total_amount: str, batch_ref: str, debit_account: str, narration: str, bank_code: str, request_id: str) -> None:
        self.total_amount = total_amount
        self.batch_ref = batch_ref
        self.debit_account = debit_account
        self.narration = narration
        self.bank_code = bank_code
        self.request_id = request_id


class PaymentDetail:
    trans_ref: str
    narration: str
    benficiary_email: str
    benficiary_bank_code: str
    benficiary_account_number: str
    amount: float

    def __init__(self, trans_ref: str, narration: str, benficiary_email: str, benficiary_bank_code: str, benficiary_account_number: str, amount: str) -> None:
        self.trans_ref = trans_ref
        self.narration = narration
        self.benficiary_email = benficiary_email
        self.benficiary_bank_code = benficiary_bank_code
        self.benficiary_account_number = benficiary_account_number
        self.amount = amount


class BulkPaymentPayload:
    bulk_payment_info: BulkPaymentInfo
    payment_details: List[PaymentDetail]

    def __init__(self, bulk_payment_info: BulkPaymentInfo, payment_details: List[PaymentDetail]) -> None:
        self.bulk_payment_info = bulk_payment_info
        self.payment_details = payment_details
