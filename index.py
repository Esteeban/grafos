from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/grafos')
def grafos1():
    return render_template("grafos.html")    

@app.route('/Sobre_Nosotros')
def nosotros():
    return render_template("grafos2.html")

if __name__ == '__main__':
    app.run(debug=True)       