import os
from flask import Flask, render_template,request,redirect,flash, session, url_for
from flask_security import Security, current_user, auth_required, hash_password, \
     SQLAlchemySessionUserDatastore
from database import db_session, init_db
from flask_login import login_required, logout_user, LoginManager
from models import User, Role
import json
import sqlite3 as sq
import pandas as pd
import plotly

import helpers.plotly_layouts as plt 


# Create app
app = Flask(__name__)
app.config['DEBUG'] = True

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Generate a secret key
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", 'pddfgfhghgf--ghb3Ag-ghgjwwss1234')
# Bcrypt is set as default SECURITY_PASSWORD_HASH, which requires a salt
# Generate a good salt using: secrets.SystemRandom().getrandbits(128)
app.config['SECURITY_PASSWORD_SALT'] = os.environ.get("SECURITY_PASSWORD_SALT", '182837584038784930239485749030293857390')

# Setup Flask-Security
user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
security = Security(app, user_datastore)

## Database for stocks
table_name = "stock_database" # table and file name
conn = sq.connect('{}.sqlite'.format(table_name))
df = pd.read_sql('select * from {}'.format(table_name), conn)

# Create a user to test with
@app.before_first_request
def create_user():
    init_db()
    if not user_datastore.find_user(email="test@me.com"):
        user_datastore.create_user(email="test@me.com", password=hash_password("password"))
    db_session.commit()

# Views
@app.route("/",  methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        
        greetings = f'Hello {current_user.email} !'

    else:
        greetings = 'Hello, please login'

    return render_template("landing.html", greetings=greetings)

@app.route("/login", methods=['GET', 'POST'])
@auth_required()
def home():
    if current_user.is_authenticated:
        
        greetings = f'Hello {current_user.email} !'
        return render_template("home.html", greetings=greetings)
    
    else:
        return redirect("/", code=302)


@app.route('/logout', methods=['GET', 'POST'])
@auth_required()
def logout():
    logout_user()
    
    return redirect("/", code=302)


@app.route("/Example1")
@auth_required()
def example():
    textout = "This is an example"
    return render_template("example1.html", textout=textout)

@app.route("/stocks/<ticker>", methods=['POST','GET'])
@auth_required()
def stocks(ticker):
    

    df_tickers = df["Ticker"].unique()

    if ticker is None or ticker not in df_tickers:
        ticker = "AAN"

    data = df[df["Ticker"]==ticker]
    
    plot = plt.create_plotly(data)
    #plot.show()
    #print(plot)
    plotly_plot = json.dumps(plot, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("stocks.html", plotly_plot= plotly_plot, ticker = ticker,
                          df_tickers = df_tickers)

@app.route("/stocks")
@auth_required()
def stocks_redirect():
    df_tickers = df["Ticker"].unique()
    return render_template("stocks.html", df_tickers= df_tickers)



@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.directory='./'
    app.run(host='127.0.0.1', port=5000)
