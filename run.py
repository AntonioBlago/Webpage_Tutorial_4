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
import helpers.stocks as stocks


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

conn = sq.connect('helpers/{}.sqlite'.format("database"),check_same_thread=False)
df = pd.read_sql('select * from {}'.format("stock_database"), conn)
stock_infos = pd.read_sql("select * from {}".format("stock_infos"), conn)
return_and_volatility = pd.read_sql("select * from {}".format("performance_and_vola"), conn)


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
        login = True
        period = request.args.get("period")

        if period is None:
            period = "3y"


        
        greetings = f'Hello {current_user.email} !'

        period_tickers = ["1d","7d", "1m","3m","6m","1y","2y","3y","5y"]
        df = pd.merge(return_and_volatility, stock_infos[["Ticker", "Name", "Sector"]], on="Ticker", how="right")
        df["link"] =  df["Ticker"].apply(
            lambda
                x: '<a href="/stocks/{0}">{0}</a>'.format(
                x))

        plot = plt.create_plotly_xy(df, period)
        plotly_plot = json.dumps(plot, cls=plotly.utils.PlotlyJSONEncoder)

        return render_template("home.html", greetings=greetings, plotly_plot=plotly_plot,
                               period_tickers = period_tickers, login = login)

    else:
        greetings = 'Hello, please login'
        login = False

        return render_template("home.html", greetings=greetings,login = login)

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


@app.route("/stocks/<ticker>", methods=['POST','GET'])
@auth_required()
def stocks(ticker):

    df_tickers = df["Ticker"].unique()

    if ticker is None or ticker not in df_tickers:
        ticker = "AAN"

    data = df[df["Ticker"]==ticker]
    plot = plt.create_plotly(data)

    ## Stock info
    ticker_info = stock_infos[stock_infos["Ticker"]==ticker]
    ticker_info = ticker_info.transpose()
    ticker_info.columns = ["Ticker Information"]
    df1 = ticker_info.iloc[:round(len(ticker_info)/2)-1, :]
    df2 = ticker_info.iloc[(round(len(ticker_info)/2)):, :]

    df1 = df1.to_html()
    df2 = df2.to_html()

    plotly_plot = json.dumps(plot, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("stocks.html", plotly_plot= plotly_plot, ticker = ticker,
                          df_tickers = df_tickers, ticker_info = [df1,df2])

@app.route("/stocks")
@auth_required()
def stocks_redirect():
    df_tickers = df["Ticker"].unique()
    return render_template("stocks.html", df_tickers= df_tickers, ticker_info=None)



@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.directory='./'
    app.run(host='127.0.0.1', port=5000)
