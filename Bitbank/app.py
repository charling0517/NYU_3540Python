from flask import flask, request, session, render_template, jsonify
from coinbase.wallet.client import Client
from blockchain import statistics
import requests
from tinydb import TinyDB, Query
import mysql.connector as mc
from mysql.connector.conversion import MySQLConverter
from mysql.connector.cursor import MySQLCursor

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('main.html')

@app.route('/login', methods=['GET', 'POST'])

def login():
    connection = get_connection()
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)
   
    return render_template('login.html')
    connection.commit()
    connection.close()
    return render_template('login.html')

'''@app.route('/currency',methods=['POST'])
def get_value():
  
    ticker = exchangerates.get_ticker() '''
    

'''@app.route('/process',methods=['POST'])
def process_trade():
    connection = get_connection()
    ticker = exchangerates.get_ticker() '''
    
    
    
@app.route('/currency',methods=['POST'])    
def get_btc_buyprice():
    client = Client('apibuy', 'secretbuy')
    buy_btc = client.get_buy_price(currency_pair = 'BTC-USD')
    return buy_btc

@app.route('/buy', methods=['post'])
def buy_bitcoin():
    connection = get_connection()
    Trade_Qty = request.form['Qty']
    Symbol_Name =request. form['Symbol_Name']
    client = Client('apibuy', 'secretbuy')
    buy_btc = client.get_buy_price(currency_pair = 'BTC-USD')
    buy_price = float (buy_info['amount'])
    cmd = connection.cursor()
    cmd.execute("select Inventory from Trade where user_id = 1")
    remain = cmd.fetchmany(1)
    remain = float(remain[0][0])
    qty_float = float(qty)
    total_price = qty_float * buy_price
    if total_price<=remain:
        buy_price = str(buy_price)
        sql=("select sum(quantity) from trade_record where item_id = 1")
        result = connection.cmd_query(sql)
        sum_quatity = int(sum_quantity[0][0][0])+qty
        sum_quantity = str(sum_quantity)
      
    sql = 'insert into trade (Trade_Qty, Symbol_Name, Time DATETIME, Inventory, Cash, Side_Side_Index, Symbol_Symbol_ID, Symbol_Name) values (+qty+','+price+','+time+','+inventory+','+cash+','+side_index+','+id+','+symbol_name+')'
    result = connection.cmd_query(sql)
    connection.commit()
    connection.close()
    return "Trade processed" 

@app.route('/sell', methods=['post'])
def sell_bitcoin():
    Qty = request.form['Qty']
    Symbol_name = request.form['Symbol_Name']
    client = Client('apibuy', 'secretbuy')
    buy_price = client.get_buy_price(currency_pair = 'BTC-USD')
    connection = get_connection()
    #sql = 'insert into trade (Trade_Qty, Price, Time DATETIME, Inventory, Cash, Side_Side_Index, Symbol_Symbol_ID, Symbol_Name) values (+qty+','+price+','+time+','+inventory+','+cash+','+side_index+','+id+','+symbol_name+')
    result = connection.cmd_query(sql)
    connection.commit()
    connection.close()
    return "Trade processed" 
    

@app.route('/TradesPortfolio')
def TradesPortfolio():
    connection = get_connection()
    
    sql = "select pl_ID, VWAP, UPL, RPL from PL, Symbol, Trade, Side where Trade.Sylmbol_Sylmbol_ID = Symbol.Symbol_ID and Trade.Site_Site_Index = Side.Side_Index and Symbol.Symbol_ID = PL.Symbol_ID" 
    result = connection.cmd_query(sql)
    rows = connection.get_rows()
    connection.close()
    return render_template('portfolio.html', rows = [1])





def get_connection():
    return mc.connect(user='root',
    password='jamiel',
    host='127.0.0.1',
    database='candystore',
    auth_plugin='mysql_native_password')

   

if __name__ == '__main__':
    app.run()#(debug=True)
