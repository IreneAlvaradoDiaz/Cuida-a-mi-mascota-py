import matplotlib.pyplot as plt
from flask import Flask, make_response
from flask_cors import CORS
import pandas as pd
import io
import base64

satisfecho=["satisfecho", 48]
insatisfecho=["insatisfecho", 22]

app = Flask(__name__)
CORS(app, resources={r"/*":{"origin":"http://localhost"}})

@app.route("/")
def encuesta():
    lista_usado = [satisfecho, insatisfecho]
    df_lista_usado = pd.DataFrame(lista_usado, columns = ["usabilidad", "porciento"])
    plt.bar(df_lista_usado["usabilidad"], df_lista_usado["porciento"])
    img = io.BytesIO()
    plt.savefig(img, facecolor='none')
    plt.close()
    response = make_response(img.getvalue())
    response.headers.set('Content-Type', 'image/png')
    return response
