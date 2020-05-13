import requests
import os

class Paypal:
    def __init__(self):
        self.account = os.environ['PAYPAL_SANDBOX_ACCOUNT']
        self.client = os.environ['PAYPAL_CLIENT_ID']
        self.secret = os.environ['PAYPAL_SECRET']
