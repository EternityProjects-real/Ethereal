from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.utils import secure_filename

import os
import json 
import mining

with open("info.json", "r") as c:
    parameters = json.load(c)["parameters"]
    

app = Flask(__name__)


# Project specific Confrigration
app.config['SQLALCHEMY_DATABASE_URI'] = parameters["database"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = parameters["track_modifications"]
app.config['SECRET_KEY'] = parameters["secret_key"]
app.config['UPLOAD_FOLDER'] = parameters["UPLOAD_FOLDER"]
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)


gas_price_minting = 2
addres_key_admin = "0x9109C4575a824535bAc4efA008Ed4E81DFf8755E"


class Blockchain(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    desc_transfer = db.Column(db.String(512), nullable = False)
    prev_hash = db.Column(db.String(512), nullable = False)
    sender_id = db.Column(db.String(512), nullable = False)
    reciver_id = db.Column(db.String(512), nullable = False)
    transaction_amt = db.Column(db.Float, nullable = False)
    new_hash = db.Column(db.String(512), nullable = False)
    addres_key_miner = db.Column(db.String(512), nullable = False)
    nonce = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return str(self.id) + ': New Hash: ' + self.new_hash + ' Previous Hash: ' + self.prev_hash + ' '



class Blockchain_Waiting(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    desc_transfer = db.Column(db.String(512), nullable = False)
    sender_id = db.Column(db.String(512), nullable = False)
    reciver_id = db.Column(db.String(512), nullable = False)
    transaction_amt = db.Column(db.Float, nullable = False)

    def __repr__(self):
        return str(self.id) + ': ' + ' transaction_amt: ' + str(self.transaction_amt)



class Keys(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    private_key = db.Column(db.String(512), nullable = False)
    addres_key = db.Column(db.String(512), nullable = False)

    def __repr__(self):
        return str(self.id) + ': Addres: ' + self.addres_key
    


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(512), nullable = False)
    dob = db.Column(db.String(512), nullable = False)
    addres_key = db.Column(db.String(512), nullable = False)
    private_key = db.Column(db.String(512), nullable = False)
    pan_no = db.Column(db.String(512), nullable = False)
    mobile_no = db.Column(db.String(512), nullable = False)
    current_balance = db.Column(db.Float, default = 0, nullable = False)
    miner_status = db.Column(db.Boolean, default = False, nullable = False)
    loan_status = db.Column(db.Boolean, default = False, nullable = False)
    loan_taken = db.Column(db.Boolean, default = False, nullable = False)
    blocks_mined = db.Column(db.Integer, default = 0, nullable = False)
    wallet_balance = db.Column(db.Float, default = 0, nullable = False)

    def __repr__(self):
        return str(self.id) + ': Addres : ' + self.addres_key + ' Miner status: ' + str(self.miner_status) + ' Name: ' + str(self.name)



class Crowdsourcing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    addres_key = db.Column(db.String(512), nullable=False)
    problem_desc = db.Column(db.Text(), nullable=False)
    title_desc = db.Column(db.String(512), nullable=False)
    target_required = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return str(self.id) + ': Addres : ' + self.addres_key + ' title_desc: ' + self.title_desc
    


class Nfts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hash_nft = db.Column(db.String(512), nullable = False)
    location_addres = db.Column(db.String(512), nullable=False)
    addres_owner = db.Column(db.String(512), nullable=False)
    tittle_nft = db.Column(db.String(512), nullable=False)
    desc_nft = db.Column(db.Text(), nullable=False)
    price_nft = db.Column(db.Float, default = 1, nullable = False)

    def __repr__(self):
        return str(self.id) + ': Hash of nft: ' + str(self.hash_nft) + ' price: ' + str(self.price_nft) + ' tittle_nft: ' + str(self.tittle_nft)



class MakeModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    addres_key = db.Column(db.String(512), nullable=False)
    no_of_hash = db.Column(db.Integer, nullable=False)
    no_of_blocks_mined = db.Column(db.Integer, default = 0, nullable = False)

    def __repr__(self):
        return str(self.id) + ' Addres of the Miner ' + self.addres_key + ' no_of_hash: ' + str(self.no_of_hash) + ' no_of_blocks_mined: ' + str(self.no_of_blocks_mined)


class LoanStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    addres_key = db.Column(db.String(512), nullable=False)
    amt_on_loan = db.Column(db.Float, nullable=False)
    amt_paid = db.Column(db.Float, default = 0, nullable = False)
    
    def __repr__(self):
        return str(self.id) + ' addres_key: ' + str(self.addres_key) + ' amt_on_loan: ' + str(self.amt_on_loan) + ' amt_paid: ' + str(self.amt_paid)
    

class CoinManager(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    addres_key = db.Column(db.String(512), nullable = False)
    private_key = db.Column(db.String(512), nullable = False)
    total_coin = db.Column(db.Float, default = 0, nullable = False)
    total_given = db.Column(db.Float, default = 0, nullable = False)
    total_money_in_network = db.Column(db.Float, default = 0, nullable = False)
    total_given_to_miners = db.Column(db.Float, default = 0, nullable = False)
    
    def __repr__(self):
        return str(self.id) + ': Total coin in network: ' + str(self.total_coin) + ' Total coin bought: ' + str(self.total_given) + ' Total Mine reward: ' + str(self.total_given_to_miners)



@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))     
        


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        private_key = request.form.get('private_key')
        addres_key = request.form.get('addres_key')
        
        if private_key and addres_key:
            add_key = Keys(private_key = private_key, addres_key = addres_key)
            db.session.add(add_key)
            db.session.commit()
            return render_template('admin.html', msg = jsonify({'addres_key': addres_key,
                                                                'private_key' : private_key}))
        
    keys = Keys.query.all()
    return render_template('admin.html', keys = keys)



@app.route('/genesis', methods = ['GET', 'POST'])
def genesis():
    block = Blockchain(desc_transfer = "This is Genesis Block", prev_hash = '0c08c0d223af7f43cbf3543b4a3559cd0cc0b37893c38a2fc8319e204e80c2c2', sender_id = 'genesis', reciver_id = 'genesis', transaction_amt = float(1000), new_hash = '5957b313c1653a9fdf97e25373bd7641a456e4d75789110c7092a71a03a67c33', addres_key_miner = 'genesis', nonce = 1 )
    db.session.add(block)
    db.session.commit()
    return jsonify({'Succesfull': 'genesis block added '})


@app.route('/checkblockchain', methods = ['GET', 'POST'])
def checkblockchain():
    blocks = Blockchain.query.all()
    for i in blocks:
        prev_hash_check, new_hash_check, nonce = mining.checkchain(i)
        if not (i.prev_hash == prev_hash_check and i.new_hash == new_hash_check and i.nonce == nonce):
            return False
    return jsonify({'Yay': 'All the blocks are valid! Thansk For chechking!'})


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        dob = request.form.get('dob')
        miner_status = request.form.get('miner_status')
        pan_no = request.form.get('pan_no')
        mobile_no = request.form.get('mobile_no')
        
        blockkey = Keys.query.all()[0]
        addres_key, private_key = blockkey.addres_key, blockkey.private_key

        if miner_status == 'Yes':
            temp_priv = mining.SHA256(blockkey.private_key)
            new_user = User(name = name, dob = dob, miner_status = True, addres_key = addres_key, private_key = temp_priv, pan_no = pan_no, mobile_no = mobile_no)
        elif miner_status == 'No':
            temp_priv = mining.SHA256(blockkey.private_key)
            new_user = User(name = name, dob = dob, miner_status = False, addres_key = addres_key, private_key = temp_priv, pan_no = pan_no, mobile_no = mobile_no)
        
        block_remove = Keys.query.get_or_404(blockkey.id)
        db.session.delete(block_remove)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'Keep Your details safe:':'We provide you with this msg so that u can safely store ur private key',
                        'Caution': 'We do not know ur private key it is hashed and stored in databse pls keep it safe',
                        'name': name,
                        'dob': dob,
                        'miner_status': miner_status,
                        'addres_key': addres_key,
                        'private_key': private_key,
                        'pan_no': pan_no,
                        'mobile_no': mobile_no,})

    return render_template('login.html')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        private_key = request.form.get('private_key')
        pos_users = User.query.filter_by(name = name)
        private_key = mining.SHA256(private_key)
        
        for i in pos_users:
            if i.name == name and i.private_key == private_key:
                user = User.query.get(i.id)
                load_user(user.id)
                login_user(user)
                return redirect('http://127.0.0.1:3000/')
            
    return redirect('http://127.0.0.1:3000/')
    # return render_template('login.html')


@app.route('/signout', methods = ['GET', 'POST'])
@login_required
def signout():
    logout_user()
    return redirect(url_for('login'))



@app.route('/makepayment', methods = ['GET', 'POST'])
@login_required
def makepayment():
    if request.method == 'POST':
        amount = request.form.get('amount')
        addres_key = request.form.get('addres_key')
        private_key = request.form.get('private_key')
        private_key = mining.SHA256(private_key)
        
        if current_user.private_key == private_key and current_user.current_balance >= float(amount):
            
            if current_user.addres_key == addres_key:
                return jsonify({'error': 'You cant send money to yourself'})
            
            if float(amount) <= 0:
                return jsonify({'error': 'amount cant be negative'})
            
            block_waiting = Blockchain_Waiting(desc_transfer = 'User Transaction', sender_id = private_key, reciver_id = addres_key, transaction_amt = float(amount))
            db.session.add(block_waiting)
            db.session.commit()            
            
            return redirect('http://127.0.0.1:3000/')

    return redirect('http://127.0.0.1:3000/')


@app.route('/addfunds', methods = ['GET', 'POST'])
@login_required
def addfunds():
    if request.method == 'POST':
        amount = request.form.get('amount')
        amount_inr = request.form.get('amount_inr')
        private_key = request.form.get('private_key')
        private_key = mining.SHA256(private_key)
            
        if current_user.private_key == private_key:
            current_user.current_balance = current_user.current_balance + float(amount)
            
            admin_acc = User.query.filter_by(addres_key = addres_key_admin)[0]
            admin_acc.current_balance -= float(amount)
            
            coin = CoinManager.query.all()[0]
            coin.total_given += float(amount)
            coin.total_money_in_network += float(amount_inr)
            
            db.session.commit()
            return redirect(url_for('makepayment'))
        
        else:
            return jsonify({'error':'enter correct privatekey'})
    return render_template('index.html')



@app.route('/sellfunds', methods = ['GET', 'POST'])
@login_required
def sellfunds():
    if request.method == 'POST':
        amount = request.form.get('amount')
        private_key = request.form.get('private_key')
        private_key = mining.SHA256(private_key)
        
        if float(amount) >= (current_user.current_balance)*0.5:
            return jsonify({'error':'Exceding the transaction limit'})
            
        if current_user.private_key == private_key:
            current_user.current_balance -= float(amount)
            admin_acc = User.query.filter_by(addres_key = addres_key_admin)[0]
            admin_acc.current_balance += float(amount)
            db.session.commit()
            return jsonify({'yay':'You Succesfull sold the coins!'})
        else:
            return jsonify({'error':'Enter correct Private Key'})
    return render_template('index.html')


@app.route('/getloan', methods = ['GET', 'POST'])
@login_required
def getloan():
    if request.method == 'POST':
        amount = request.form.get('amount')
        private_key = request.form.get('private_key')
        private_key = mining.SHA256(private_key)
        
        if current_user.current_balance <= float(amount):
            return jsonify({'error':'We cant provide u loan more than your worth!'})
        
        if (current_user.current_balance)*0.5 >= float(amount):
            current_user.current_balance += float(amount)
            current_user.loan_status = True
            current_user.loan_taken += float(amount)
            
            admin_acc = User.query.filter_by(addres_key = addres_key_admin)[0]
            admin_acc.current_balance -= float(amount)
            
            loan_status = LoanStats(addres_key = current_user.addres_key, amt_on_loan = float(amount))
            
            db.session.add(loan_status)
            db.session.commit()
            
            return jsonify({'Yay':'Loan was successfully granted',
                            'Amount': amount})    
        
        else:
            return jsonify({'error':'U are not eligible for loan'})
    
    return render_template('loan.html')



@app.route('/payloan', methods = ['GET', 'POST'])
@login_required
def payloan():
    if request.method == 'POST':
        amount = request.form.get('amount')
        private_key = request.form.get('private_key')
        private_key = mining.SHA256(private_key)
        
        if float(amount) and current_user.private_key == private_key:
            current_user.current_balance -= float(amount)
            current_user.loan_status = True
            current_user.loan_taken -= float(amount)
            
            if current_user.current_balance < 0 or current_user.loan_taken < 0:
                return jsonify({'error' : 'Balance cant be negative'})
            
            admin_acc = User.query.filter_by(addres_key = addres_key_admin)[0]
            admin_acc.current_balance += float(amount)
            
            loan_status = LoanStats.query.filter_by(addres_key = current_user.addres_key)[0]
            loan_status.amt_on_loan -= float(amount)
            loan_status.amt_paid += float(amount)
            
            if current_user.loan_taken == 0:
                current_user.loan_status = False
            
            db.session.add(loan_status)
            db.session.commit()
            
            return jsonify({'Yay':'Loan was Paid successfully!',
                            'Amount': amount})    
        
        else:
            return jsonify({'error':'U are not eligible for loan'})
    
    return render_template('loan.html')

        
@app.route('/addwallet', methods = ['GET', 'POST'])
@login_required
def addwallet():
    if request.method == 'POST':
        amount = request.form.get('amount')
        private_key = request.form.get('private_key')
        private_key = mining.SHA256(private_key)
        
        if float(amount) < current_user.current_balance and current_user.private_key == private_key:
            current_user.current_balance -= float(amount)
            current_user.wallet_balance += float(amount)
            
            db.session.commit()
            return jsonify({'Yay':'Your Eternity coins are converted into Eternity credits'})
        
    return render_template('wallet.html')


@app.route('/coinwallet', methods = ['GET', 'POST'])
@login_required
def coinwallet():
    if request.method == 'POST':
        amount = request.form.get('amount')
        private_key = request.form.get('private_key')
        private_key = mining.SHA256(private_key)
        
        if float(amount) < current_user.current_balance and current_user.private_key == private_key:
            current_user.current_balance += float(amount)
            current_user.wallet_balance -= float(amount)
            
            db.session.commit()
            return jsonify({'Yay':'Your Eternity coins are converted into Eternity credits'})
        
    return render_template('wallet.html')


@app.route('/usedata', methods = ['GET'])
@login_required
def usedata():
    return current_user.current_balance


@app.route('/sellwallet', methods = ['GET', 'POST'])
@login_required
def sellwallet():
    if request.method == 'POST':
        mobile_no = request.form.get('mobile_no')
        amount = request.form.get('amount')
        # private_key = request.form.get('private_key')
        # private_key = mining.SHA256(private_key)  
        # and current_user.private_key == private_key
        
        if current_user.wallet_balance > float(amount):
            current_user.wallet_balance -= float(amount) + float(gas_price_minting/4)
            
            pos_recivers = User.query.filter_by(mobile_no = str(mobile_no)).first()

            print(pos_recivers)
            pos_recivers.wallet_balance += float(amount)
            
            prev_block = Blockchain.query.all()[-1]
            
            new_hash, nonce = mining.wallet_tx(prev_block.new_hash, current_user.private_key, pos_recivers.addres_key, amount)
            
            block = Blockchain(desc_transfer = 'Wallet transaction', prev_hash = prev_block.new_hash, sender_id = current_user.private_key, reciver_id = pos_recivers.addres_key, transaction_amt = float(amount), new_hash = new_hash , addres_key_miner = current_user.addres_key, nonce = nonce)
            
            admin_acc = User.query.filter_by(addres_key = addres_key_admin)[0]
            admin_acc.current_balance += float(gas_price_minting/4)
            
            db.session.add(block)
            db.session.commit()
            
            return redirect('http://127.0.0.1:3000/Wallet')

    return render_template('wallet.html')


@app.route('/crowdsourcing', methods = ['GET', 'POST'])
@login_required
def crowdsourcing():
    if request.method == 'POST':
        problem_desc = request.form.get('problem_desc')
        title_desc = request.form.get('title_desc')
        target_required = request.form.get('target_required')
        private_key = request.form.get('private_key')
        private_key = mining.SHA256(private_key)
        
        if current_user.private_key == private_key:
            crowd = Crowdsourcing(addres_key = current_user.addres_key, problem_desc = problem_desc, title_desc = title_desc, target_required = float(target_required))
            current_user.current_balance -= float(gas_price_minting)
            
            admin_acc = User.query.filter_by(addres_key = addres_key_admin)[0]
            admin_acc.current_balance += float(gas_price_minting)
            
            db.session.add(crowd)
            db.session.commit()
            return redirect('http://127.0.0.1:3000/crowdSourcing')
            # return jsonify({'Yay': 'You have created new Crowdsourced project'})

    crowd = Crowdsourcing.query.all()
    return render_template('crowd.html', crowd = crowd)



@app.route('/paycrowdsourcing', methods = ['GET', 'POST'])
@login_required
def paycrowdsourcing():
    crowd = Crowdsourcing.query.all()
    
    if request.method == 'POST':
        amount = request.form.get('amount')
        private_key = request.form.get('private_key')
        addres_key = request.form.get('addres_key')
        title_desc = request.form.get('title_desc')
        private_key = mining.SHA256(private_key)
        
        if current_user.current_balance > float(amount) and current_user.private_key == private_key: 
            pos_crowd = Crowdsourcing.query.filter_by(addres_key = addres_key)
            
            for i in pos_crowd:
                if i.title_desc == title_desc:
                    set_crowd = Crowdsourcing.query.get_or_404(i.id)
                    set_crowd.target_required -= float(amount)
                     
            pos_recivers = User.query.filter_by(addres_key = str(addres_key)).first()
            pos_recivers.wallet_balance += float(amount)
            
            admin_acc = User.query.filter_by(addres_key = addres_key_admin)[0]
            admin_acc.current_balance += float(gas_price_minting/2)
            
            current_user.current_balance -= float(gas_price_minting/2) + float(amount)
            
            prev_block = Blockchain.query.all()[-1]
            
            new_hash, nonce = mining.wallet_tx(prev_block.new_hash, current_user.private_key, addres_key, amount)
            
            block = Blockchain(desc_transfer = 'Crowdsorcing transaction', prev_hash = prev_block.new_hash, sender_id = current_user.private_key, reciver_id = addres_key, transaction_amt = float(amount), new_hash = new_hash , addres_key_miner = current_user.addres_key, nonce = nonce)
            
            db.session.add(block)
            db.session.commit()
            
            return jsonify({'Yay':'You Succesfull Made the transaction!',
                            'Crowdourcing details' : str(title_desc + ' ' + addres_key),
                            'Amount': amount})
            
    crowd = Crowdsourcing.query.all()
    return render_template('crowd.html', crowd = crowd)



@app.route('/mintnfts', methods = ['GET', 'POST'])
@login_required
def mintnfts():    
    if request.method == 'POST':
        private_key = request.form.get('private_key')
        private_key = mining.SHA256(private_key)
        tittle_nft = request.form.get('tittle_nft')
        price_nft = request.form.get('price_nft')
        desc_nft = request.form.get('desc_nft')
        content = request.files['file']
        filename = secure_filename(content.filename)
        content.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        location_addres = str('uploads/' + str(filename))
        hash_nft = str(mining.img_Hash(location_addres))
        
        if current_user.private_key == private_key:
            current_user.current_balance -= float(gas_price_minting)
            blocknft = Nfts(hash_nft = hash_nft, location_addres = location_addres, addres_owner = current_user.addres_key, tittle_nft = tittle_nft, desc_nft = desc_nft, price_nft = price_nft)
            
            admin_acc = User.query.filter_by(addres_key = addres_key_admin)[0]
            admin_acc.current_balance += float(gas_price_minting)
            
            db.session.add(blocknft)
            db.session.commit()
            return redirect('http://127.0.0.1:3000/nft')
            # return jsonify({'Yay' : 'You have minted a new NFTs'})

    blocks = Nfts.query.all()
    return render_template('nfts.html', blocks = blocks)


@app.route('/buynfts', methods = ['GET', 'POST'])
@login_required
def buynfts():
    if request.method == 'POST':
        nft_id = request.form.get('nft_id')
        amount = request.form.get('amount')
        private_key = request.form.get('private_key')
        private_key = mining.SHA256(private_key)   
                    
        if current_user.current_balance >= float(amount) and current_user.private_key == private_key:
            
            if current_user.private_key == private_key and float(amount) <= current_user.current_balance:
                pos_nfts = Nfts.query.get_or_404(nft_id)
                
                
                if float(amount) >= pos_nfts.price_nft:
                    current_user.current_balance -= float(amount) + float(gas_price_minting/2)
                    
                    pos_recivers = User.query.filter_by(addres_key = pos_nfts.addres_owner).first()
                    print(pos_recivers)
                    pos_recivers.wallet_balance += float(amount)
                
                    admin_acc = User.query.filter_by(addres_key = addres_key_admin)[0]
                    admin_acc.current_balance += float(gas_price_minting/2)
                    
                    prev_block = Blockchain.query.all()[-1]
                
                    new_hash, nonce = mining.wallet_tx(prev_block.new_hash, current_user.private_key, pos_nfts.addres_owner, amount)
                    
                    block = Blockchain(desc_transfer = 'Nfts transaction', prev_hash = prev_block.new_hash, sender_id = current_user.private_key, reciver_id = pos_nfts.addres_owner, transaction_amt = float(amount), new_hash = new_hash , addres_key_miner = current_user.addres_key, nonce = nonce)
                    
                    if block:
                        pos_nfts.addres_owner = current_user.addres_key
                        pos_nfts.price_nft = float(amount)
                        
                        db.session.add(block)
                        db.session.commit()

                        return jsonify({'Yay': 'You have succesfull bought the nft!',
                                        'Addres of Previous owner': pos_recivers.addres_key,
                                        'Addres of Current Owner': current_user.addres_key, 
                                        'Amount': float(amount)})
                                 
    blocks = Nfts.query.all()
    return render_template('nfts.html', blocks = blocks)



@app.route('/mine', methods = ['GET', 'POST'])
@login_required
def mine():
    if request.method == 'POST':
        private_key = request.form.get('private_key')
        private_key = mining.SHA256(private_key)
        
        if current_user.private_key == private_key and current_user.miner_status == True:
            
            block_to_be_mined = Blockchain_Waiting.query.all()[0]
            
            if current_user.addres_key == block_to_be_mined.reciver_id or current_user.private_key == block_to_be_mined.sender_id:
                return jsonify({'error': 'You cant make and mine your own transactions'})
            
            prev_block = Blockchain.query.all()[-1]
            
            new_hash, mine_reward, nonce  = mining.set_mine(prev_block.new_hash, block_to_be_mined)

            block_to_be_added = Blockchain(desc_transfer = block_to_be_mined.desc_transfer, prev_hash = prev_block.new_hash, sender_id = block_to_be_mined.sender_id, reciver_id = block_to_be_mined.reciver_id, transaction_amt = float(block_to_be_mined.transaction_amt) + float(mine_reward), new_hash = new_hash, addres_key_miner = current_user.addres_key, nonce = nonce )
            
            block_to_be_removed = Blockchain_Waiting.query.get_or_404(block_to_be_mined.id)
            
            current_user.current_balance += float(mine_reward/2)
            current_user.blocks_mined += 1
            
            pos_transating = User.query.filter_by(private_key = block_to_be_mined.sender_id).first()
            pos_transating = User.query.get_or_404(pos_transating.id)
            pos_transating.current_balance -= float(block_to_be_mined.transaction_amt) + float(mine_reward/2)
            
            pos_recivers = User.query.filter_by(addres_key = block_to_be_mined.reciver_id).first()
            pos_recivers = User.query.get_or_404(pos_recivers.id)
            pos_recivers.current_balance += float(block_to_be_mined.transaction_amt)
            
            coin = CoinManager.query.all()[0]
            coin.total_coin += float(mine_reward)
            coin.total_given_to_miners += float(mine_reward)
            
            admin_acc = User.query.filter_by(addres_key = addres_key_admin)[0]
            admin_acc.current_balance += float(mine_reward/2)
            
            db.session.delete(block_to_be_removed)
            db.session.add(block_to_be_added)
            db.session.commit()
            
            return redirect('http://127.0.0.1:3000/miner')
            
            # return jsonify({'Yay': 'You ahve succesfull mined the block!',
            #                 'Mine Reward' : str(mine_reward/2)})
            
        else:
            return jsonify({'error1':'Enter correct Private Key',
                            'error2':'You may not be a miner',})

    blocks_waitaing = Blockchain_Waiting.query.all()
    return render_template('index.html', blocks = blocks_waitaing)



@app.route('/api/coinonnetwork', methods = ['GET', 'POST'])
def api_coinonnetwork():
    coins = CoinManager.query.all()
    total_coin_list, total_given_list, total_given_to_miners_list, total_money_in_network_list, total_given_to_miners_list = [], [], [], [], []
    
    for i in coins:
        total_coin_list.append(i.total_coin)
        total_given_list.append(i.total_given)
        total_given_to_miners_list.append(i.total_given_to_miners)
        total_money_in_network_list.append(i.total_money_in_network)
        total_given_to_miners_list.append(i.total_given_to_miners)
        
        return jsonify({'total_coin_list' : total_coin_list,
                        'total_given_list' : total_given_list,
                        'total_given_to_miners_list' : total_given_to_miners_list,
                        'total_money_in_network_list': total_money_in_network_list,
                        'total_given_to_miners_list':total_given_to_miners_list,})
        


@app.route('/api/blocksonchain', methods = ['GET', 'POST'])
def api_blocksonchain():
    blocks = Blockchain.query.all()
    hash_list, prev_hash_list, addres_key_miner_list, nonce_list, transaction_amt_list, desc_transfer_list, sender_list, reciver_list = [], [], [], [], [], [], [], []

    for i in blocks:
        hash_list.append(i.new_hash)
        prev_hash_list.append(i.prev_hash)
        addres_key_miner_list.append(i.addres_key_miner)
        nonce_list.append(i.nonce)
        transaction_amt_list.append(i.transaction_amt)
        desc_transfer_list.append(i.desc_transfer)
        sender_list.append(i.sender_id)
        reciver_list.append(i.reciver_id)

    return jsonify({'hash_list': hash_list,
                    'prev_hash_list': prev_hash_list,
                    'addres_key_miner_list' : addres_key_miner_list,
                    'nonce_list' : nonce_list,
                    'transaction_amt_list' : transaction_amt_list,
                    'desc_transfer_list':desc_transfer_list,
                    'sender_list':sender_list,
                    'reciver_list':reciver_list,})
    


@app.route('/api/blockswaiting', methods = ['GET', 'POST'])
def api_blockswaiting():
    blocks_waitaing = Blockchain_Waiting.query.all()
    transaction_amt_list, reciver_id_list, desc_transfer_list = [], [], [],

    for i in blocks_waitaing:
        transaction_amt_list.append(i.transaction_amt)
        reciver_id_list.append(i.reciver_id)
        desc_transfer_list.append(i.desc_transfer)

    return jsonify({'transaction_amt_list': transaction_amt_list,
                    'reciver_id_list' : reciver_id_list,
                    'desc_transfer_list':desc_transfer_list,})
    


@app.route('/api/minersnetwork', methods = ['GET', 'POST'])
def api_minersnetwork():
    miners = User.query.filter_by(miner_status = True)
    addres_key_list, name_list = [], []

    for i in miners:
        name_list.append(i.name)
        addres_key_list.append(i.addres_key)

    return jsonify({'addres_key_list': addres_key_list,
                    'name_list': name_list})
    


@app.route('/api/crowdsourcing', methods = ['GET', 'POST'])
def api_crowdsourcing():
    crowdsourcinginfo = Crowdsourcing.query.all()
    addres_key_list, problem_desc_list, title_desc_list, target_required_list = [], [], [], []

    for i in crowdsourcinginfo:
        addres_key_list.append(i.addres_key)
        problem_desc_list.append(i.problem_desc)
        title_desc_list.append(i.title_desc)
        target_required_list.append(i.target_required)

    return jsonify({'addres_key_list,' : addres_key_list,
                    'problem_desc_list' : problem_desc_list,
                    'title_desc_list' : title_desc_list,
                    'target_required_list' : target_required_list})
    
    
    
@app.route('/api/nfts', methods=['GET', 'POST'])
def api_nfts():
    nfts_block = Nfts.query.all()
    hash_nft_list, location_addres_list, addres_owner_list, price_nft_list, desc_nft_list, tittle_nft_list = [], [], [], [], [], []
    
    for i in nfts_block:
        hash_nft_list.append(i.hash_nft)
        location_addres_list.append(i.location_addres)
        addres_owner_list.append(i.addres_owner)
        price_nft_list.append(i.price_nft)
        desc_nft_list.append(i.desc_nft)
        tittle_nft_list.append(i.tittle_nft)
    
    return jsonify({'hash_nft_list': hash_nft_list,
                    'location_addres_list': location_addres_list,
                    'addres_owner_list': addres_owner_list,
                    'price_nft_list': price_nft_list,
                    'desc_nft_list': desc_nft_list,
                    'tittle_nft_list': tittle_nft_list,})
    
    
if __name__ == '__main__':
    app.run(debug = True, threaded = True)