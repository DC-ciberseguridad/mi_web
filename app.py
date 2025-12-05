from flask import Flask, render_template # type: ignore

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html") #Flask trae esta función lista para usar. 
                                         #render_template() siempre busca los archivos dentro de: /templates

if __name__ == "__main__":
    app.run(debug=True)
