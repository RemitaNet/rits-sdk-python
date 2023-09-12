# Remita Interbank Transfer Service (RITs) Python SDK

---
- [Overview](#Overview)
- [Installation](#Installation)
- [Usage](#Usage)
- [Contributing](#Contributing)
- [License](License)

---

## Overview
Python SDK for Remita Interbank Transfer Service simple APIs.

---

## Installation
To install the remita-rits-sdk-python package, run the following command:

```
pip install remita-rits
```

### Requirements
- Python 3.4 or later

### Dependencies
- pycryptodome package
- requests package

### Prerequisites
The workflow to getting started on RITs is as follows:

**Register a profile on Remita**: You can visit Remita to sign-up if you are not already registered as a merchant/biller on the platform.

**Receive the Remita credentials that certify you as a Biller**: Remita will send you your merchant ID and an API Key necessary to secure your handshake to the Remita platform.

### Configuration
All merchant credentials needed to use RITs are being setup by instantiating the Credential Class and set the properties in this class accordingly. Properties such as MerchantId, ApiKey, ApiToken, Key, Iv and the Environment needs to be set.

**Note**: Environment can either be TEST or LIVE, each of this environment has it respective Credential. Ensure you set the right credentials. By default Environment is TEST

---

## Usage

### Adding Account(s) To Your Profile

Adding an account to your merchant profile on the RITs is a dual process.

The first step is to **AddAccount**, 

Fields required to add account includes the following;

- **accountNo**: This is the number of the bank account being linked to merchant profile
- **bankCode**: This is the CBN code of the bank in which the account is domiciled
- **transRef**: This uniquely identifies the transaction
- **requestId**: This uniquely identifies the request

```python
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
    payload= AddAccountPayload()

    payload.request_id= "156752945496045566769090807860"
    payload.account_number= "044222222"
    payload.bank_code= "044"
    remita_rits_service = RemitaRITs(credentials=credentials)
    add_account_response = remita_rits_service.add_account(payload=payload)
```

The second step validates the account holder via bank authentication on the account details. You will be required by your bank to validate the account details the AddAccount request is being issued for, required fields(Payloads) are as follows;

- **card**: This is the one of the authentication detail required by the bank from the account owner to validate AddAccount request
- **otp**: This is the another authentication detail required by the bank from the account owner to validate AddAccount request
- **remitaTransref**: This uniquely identifies the specific add account request the validation is being called for
- **requestId**: This uniquely identifies the request

```python
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

    request_id = "156755354325527448866505"
    auth_params = {"OTP": "1234", "Card": "0441234567890" }
    remita_trans_ref = "MTU2NzcwNjAzNDAwOQ=="
    payload = ValidateAccountOTPPayload(remita_trans_ref=remita_trans_ref, auth_params=auth_params, request_id=request_id)

    remita_rits_service = RemitaRITs(credentials=credentials)
    validate_account_otp_response = remita_rits_service.validate_account_otp(payload=payload)
```
Successful authentication through the bank links the designated account to the corresponding merchant profile on the RITs platform.

### Payments
Payments on the RITs platform can only be made from Remita-identifiable accounts. This means that before an account can be debited on the RITs, it must be linked to a profile. Merchants may process payments via the following SDK methods on the platform:

**Single Payment Request**: This charges/debits a merchant’s account with a specified amount to credit a designated beneficiary account. Fields(payload) to set include:

- **fromBank**: This is the CBN code of the funding bank
- **debitAccount**: This is the funding account number
- **toBank**: The CBN code of destination bank where account number to be credited is domiciled. (You can use the Banks Enquiry method to get the list of all supported Banks’ code).
- **creditAccount**: This is the account number to be credited in destination bank.
- **narration**: The narration of the payment. This will typically be visible both in the debit and credit account statement. Max length 30 characters
- **amount**: The amount to be debited from the debitAccountToken and credited to **creditAccount** in bank toBank. Format ##.##
- **beneficiaryEmail**: Email of the beneficiary (email of creditAccount holder)
- **transRef**: A unique reference that identifies a payment request. This reference can be used subsequently to retrieve the details/status of the payment request
- **requestId**: This uniquely identifies the request

```python
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

    payload = SinglePaymentPayload()
    payload.request_id = "15675294789539842245099505"
    payload.trans_ref = "418083388"
    payload.to_bank = "058"
    payload.credit_account = "0582915208017"
    payload.narration = "Regular Payment"
    payload.amount = "5000"
    payload.from_bank = "044"
    payload.debit_account = "1234565678"
    payload.beneficiary_email = "qa@test.com"

    remita_rits_service = RemitaRITs(credentials=credentials)
    single_payment_response = remita_rits_service.single_payment(payload=payload)
```
**Bulk Send Payment Request**: Here, a single amount is debited to credit multiple accounts across several banks. 

Fields(payload) to set include the **bulkPaymentInfo** Parameters and **paymentDetails** Parameters

**bulkPaymentInfo Payload**

- **batchRef**: A unique reference that identifies a bulk payment request.
- **debitAccount**: Funding account number
- **bankCode**: 3 digit code representing funding bank
- **creditAccount**: This is the account number to be credited in destination bank.
- **narration**: Description of the payment
- **requestId**: This uniquely identifies the request
- **paymentDetails** Payload
- **beneficiaryBankCode**: The CBN code of destination bank where account number to be credited is domiciled. (You can use the Banks Enquiry method to get the list of all supported Banks’ code)
- **beneficiaryAccountNumber**: This is the account number to be credited in destination bank.
- **narration**: The narration of the payment. This will typically be visible both in the debit and credit account statement. Max length 30 characters
- **amount**: The amount to be debited from the debitAccountToken and credited to **creditAccount** in bank toBank
- **beneficiaryEmail**: Email of the beneficiary
- **transRef**: A unique reference that identifies a payment request. This reference can be used subsequently to retrieve the details/status of the payment request

```python
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
    
    totalAmount = "10000"
    batchRef= "23262367734"
    debitAccount= "1234565678"
    narration= "test payment"
    bankCode= "044"
    request_id= "3566745353478825334324867789043222"
    bulk_payment_info_payload = BulkPaymentInfo(total_amount=totalAmount, batch_ref=batchRef, debit_account=debitAccount, narration=narration, bank_code=bankCode, request_id=request_id)

    payment_detail_list = []
    payment_detail1 =PaymentDetail(trans_ref="43qqrf72645686769i76896578456u476856i9768dqq243221111432245321", narration="Regular Payment", benficiary_email="qa@test.com", benficiary_account_number="0582915208017", benficiary_bank_code="058", amount="2000" )
    payment_detail2 =PaymentDetail(trans_ref="432qqqt34356345y5u45784i4j65i56374562342531243e43221143224324422", narration="Regular Payment", benficiary_email="qa@test.com", benficiary_account_number="0582915208099", benficiary_bank_code="058", amount="3000" )
    payment_detail3 =PaymentDetail(trans_ref="432432q53146345yy4y3g345gg43g4g45yw4yw45g453g3weee11143224323453", narration="Regular Payment", benficiary_email="qa@test.com", benficiary_account_number="04499999999", benficiary_bank_code="044", amount="5000" )

    payment_detail_list.append(payment_detail1)
    payment_detail_list.append(payment_detail2)
    payment_detail_list.append(payment_detail3)

    bulk_payload = BulkPaymentPayload(bulk_payment_info=bulk_payment_info_payload, payment_details=payment_detail_list)
    remita_rits_service = RemitaRITs(credentials=credentials)
    bulk_payment_response = remita_rits_service.bulk_payment(payload=bulk_payload)
```

### Payment Request Status
The payment request status method essentially retrieves the status of a previous payment request(Single payment and Bulk payment) using its transaction reference.

**Single Payment Request Status:**

- **transRef**: This should be the same transRef that was used for the single payment request
- **requestId**: This uniquely identifies the request

```python
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
    
    payload = PaymentStatusPayload()
    payload.request_id = "15675546294777655544435564505"
    payload.batch_ref = "418073388"

    remita_rits_service = RemitaRITs(credentials=credentials)
    payment_status_response = remita_rits_service.payment_status(payload=payload)
```

**Bulk Send Payment Request Status:**

- **batchRef**: This should be the same batchRef that was used for the bulk payment request
- **requestId**: This uniquely identifies the request

```python
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
    payload.request_id = "15675294555444653454505"
    payload.trans_ref = "418087"

    remita_rits_service = RemitaRITs(credentials=credentials)
    payment_status_bulk_response = remita_rits_service.payment_status_bulk(payload=payload)
```

### Account Enquiry

Account Enquiry Request finds all available information on a specific account. Required fields(Payloads) are as follows;

- **accountNo**: Account number of tokenized account to be looked up 
- **bankCode**: The bank code where the account is domiciled. Use the Banks Enquiry method 
- **requestId**: This uniquely identifies the request

```python
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

    payload= AccountEnquiryPayload()
    payload.request_id= "156752903373566787764674989"
    payload.account_number= "044222222"
    payload.bank_code= "044"

    remita_rits_service = RemitaRITs(credentials=credentials)
    account_enquiry_response = remita_rits_service.account_enquiry(payload=payload)
```

### Bank Enquiry
This method lists the banks that are active on the RITs platform. required fields(Payloads) are as follow; 

- **requestId**: This uniquely identifies the request 

```python
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

    payload= GetActiveBanksPayload()
    payload.request_id= "156237566529477765505"

    remita_rits_service = RemitaRITs(credentials=credentials)
    get_active_banks_response = remita_rits_service.get_active_banks(payload=payload)
```


### Useful links
Join our Slack Developer/Support channel on [slack.](http://bit.ly/RemitaDevSlack)
    
### Support
For all other support needs, support@remita.net

---

## Contributing
To contribute to this repo, follow these guidelines for creating issues, proposing new features, and submitting pull requests:

1. Fork the repository.
2. Create a new branch: `git checkout -b "feature-name"`
3. Make your changes and commit: `git commit -m "added some new features"`
4. Push your changes: `git push origin feature-name`
5. Submit a Pull Request (PR).

Thank you!

---

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
