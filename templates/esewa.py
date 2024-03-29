
import json


import requests

__all__ = [
    'BasePaymentIntent',
    'BasePaymentClient',
    'PaymentClientError'
]

class BasePaymentClient(ABC):
    base_url: str
    merchant_id: str
    public_key: str
    secret_key: str
    sandbox: str

    def __init__(self, *args, **kwargs):
        """
        It accepts all the keys and values from keyword arguments and
        sets instance attributes to the instance.
        """
        self.session = requests.Session()

        for k, v in kwargs.items():
            # initializing initial values
            setattr(self, k, v)

    @abstractmethod
    def _get_request_headers(self) -> dict:
        """
        It returns the dictionary with all request headers if needed
        """
        pass

    @abstractmethod
    def _get_request_body(self) -> dict:
        """
        It returns the default payload data
        """
        pass

    @abstractmethod
    def create_intent(self, *args, **kwargs) -> BasePaymentIntent:
        """
        It creates the payment intent for specific payment gateway
        """
        pass

    @abstractmethod
    def complete_payment(self, *args, **kwargs):
        """
        It performs the payment transaction so that the amount is deducted from the client's account
        """
        pass

    @abstractmethod
    def verify_payment(self, *args, **kwargs):
        """
        It is used for verifying the transaction
        """
        pass

class EsewaClient(BasePaymentClient):
    username: str
    password: str
    success_url: str
    failure_url: str

    def _get_request_headers(self) -> dict:
        return {}

    def _get_request_body(self) -> dict:
        return {}

    def create_intent(self, *args, **kwargs):
        raise NotImplementedError()

    def complete_payment(self, *args, **kwargs):
        raise NotImplementedError()

    def verify_payment(self, *args, **kwargs) -> dict:
        raise NotImplementedError()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.sandbox:
            self.base_url = 'https://uat.esewa.com.np'
        else:
            self.base_url = 'https://esewa.com.np'