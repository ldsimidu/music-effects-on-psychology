import pandas as pd
from matplotlib.pyplot import plt
from flask import Flask, render_template

app = Flask(__name__)

depression_table = "spreadsheets/taxa-depressao-regiao.csv"

@app.route("/")
def show_table():
    df = pd.read_csv(depression_table)
    total_table = df[["Times","TOTAL"]].to_html(classes="table table-stripped")
    
    return render_template("index.html", tabela=total_table)


