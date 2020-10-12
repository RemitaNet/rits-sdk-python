from typing import Optional, List


class AuthParam:
    param1: Optional[str]
    value: str
    param2: Optional[str]

    def __init__(self, param1: Optional[str], value: str, param2: Optional[str]) -> None:
        self.param1 = param1
        self.value = value
        self.param2 = param2


class ValidateAccountOTPPayload:
    remita_trans_ref: str
    auth_params: List[AuthParam]
    request_id: str

    def __init__(self, remita_trans_ref: str, auth_params: List[AuthParam], request_id) -> None:
        self.request_id = request_id
        self.remita_trans_ref = remita_trans_ref
        self.auth_params = auth_params
