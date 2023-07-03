from flask import Flask, request, jsonify
from cur.models import *
from cur.views import *

app=Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@server/db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:Sonuaws1&&@database-teethi.ce3v5gwcmm1a.ap-southeast-2.rds.amazonaws.com/bank_flask'
db.init_app(app)

@app.route('/' , methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return "Hello World"
    else:
        data = request.get_json()
        return "Hello " + data['name'] 

@app.route('/create_tables')
def create_tables():
    db.create_all()
    return "Tables created"

@app.route('/add_user' , methods=['POST'])
def add_user():
    data = request.get_json()
    username = data['username']
    password = data['password']
    email = data['email']
    first_name = data['first_name']
    last_name = data['last_name']
    date_of_birth = data['date_of_birth']
    address = data['address']
    phone_number = data['phone_number']
    return views_add_user(
        username,
        password,
        email,
        first_name,
        last_name,
        date_of_birth,
        address,
        phone_number
    )

@app.route('/add_account' , methods=['GET','POST'])
def account():
    if request.method == 'POST':
        data = request.get_json()
        user_id = data['user_id']
        account_type = data['account_type']
        balance = 0
        return add_account(account_type,balance,user_id)

@app.route('/get_acc' , methods=['POST'])
def get_acc():
    data = request.get_json()
    account_id = data['account_id']
    return get_accounts(account_id)

@app.route('/deposit' , methods=['POST'])
def deposit():
    data = request.get_json()
    account_id = data['account_id']
    amount = data['amount']
    return deposit_amount(account_id,amount)

@app.route('/withdraw' , methods=['POST'])
def withdraw():
    data = request.get_json()
    account_id = data['account_id']
    amount = data['amount']
    return withdraw_amount(account_id,amount)

@app.route('/transfer' , methods=['POST'])
def transfer():
    data = request.get_json()
    from_acc = data['from_acc']
    to_acc = data['to_acc']
    amount = data['amount']
    return transfer_amount(from_acc,to_acc,amount)

if __name__ == '__main__':
    app.run(debug=True)
