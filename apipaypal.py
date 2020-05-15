from paypalpayoutssdk.core import PayPalHttpClient, SandboxEnvironment

import os

class Paypal:
    def __init__(self):
        self.account = os.environ['PAYPAL_SANDBOX_ACCOUNT']
        self.client_id = os.environ['PAYPAL_CLIENT_ID']
        self.secret = os.environ['PAYPAL_SECRET']
        environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.secret)
        self.client = PayPalHttpClient(environment)
