from flask import Flask, render_template, jsonify, request
from apipaypal import Paypal
import paypalrestsdk
import os

paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": os.environ['PAYPAL_CLIENT_ID'],
  "client_secret": os.environ['PAYPAL_SECRET'] })

app = Flask(__name__)
paypal = Paypal()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/payment', methods=['POST'])
def payment():

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"},
        "redirect_urls": {
            "return_url": "/payment/execute",
            "cancel_url": "/"},
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "Prova Teste",
                    "sku": "12345",
                    "price": "300.00",
                    "currency": "BRL",
                    "quantity": 1}]},
            "amount": {
                "total": "300.00",
                "currency": "BRL"},
            "description": "Pagamento da prova"}]})

    if payment.create():
        print('Successo!')
    else:
        print(payment.error)

    return jsonify({'paymentID' : payment.id})

@app.route('/execute', methods=['POST'])
def execute():
    success = False

    payment = paypalrestsdk.Payment.find(request.form['paymentID'])

    if payment.execute({'payer_id' : request.form['payerID']}):
        print('Successo!')
        success = True
    else:
        print(payment.error)

    return jsonify({'success' : success})