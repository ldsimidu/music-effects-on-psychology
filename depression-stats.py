import pandas as pd
from matplotlib.pyplot import plot
from flask import Flask, render_template

app = Flask(__name__)

depression_table = "https://raw.githubusercontent.com/ldsimidu/music-effects-on-psychology/refs/heads/main/spreadsheets/taxa-depressao-regiao.csv"

@app.route("/")
def show_total_table():
    df = pd.read_csv(depression_table)
    total_table = df[["Região","Total de Casos de Depressão","Percentual de Depressão","População Total (2019)"]].to_html(classes="table table-stripped")
    
    return render_template("index.html", tabela=total_table)


@app.route("/total_casos")
def show_total_cases():
    df = pd.read_csv(depression_table)
    total_cases = df[["Região","Total de Casos de Depressão", "População Total (2019)"]].to_html(classes="table table-stripped")

    return render_template("index.html", tabela=total_cases)


@app.route("/percentual_total")
def show_percent_table():
    df = pd.read_csv(depression_table)
    percent_table = df[["Região","Percentual de Depressão","População Total (2019)"]].to_html(classes="table table-stripped")
    
    return render_template("index.html", tabela=percent_table)

app.run(debug=True)
