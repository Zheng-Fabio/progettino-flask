from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import ListaSpesa, db
#apertura l'app Flask
app = Flask(__name__)
#strada principale
lista_spesa=[]

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    lista_spesa = ListaSpesa.query.all() #richiesta da parte della lista classeper i dati e salvarli
    return render_template('index.html', lista=lista_spesa)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        nuovo_elemento = ListaSpesa(elemento=elemento) #Qui stiamo creando un nuovo elemento passando tra 2-app.py 1-models.py
        db.session.add(nuovo_elemento) #aggiunge alla sessione
        db.session.commit() # commit applicando tutte le modifiche dalla sessione al database
    return redirect(url_for('home'))

@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    elemento = ListaSpesa.query.get_or_404(indice) #usiamoil get in questo modo passiamo indice ad elemento ma se è vuoto restituisce l'errore 404
    db.session.delete(elemento) #eliminazione della sessione 
    db.session.commit() #commit applicando la rimozione dell'elemento dalla sessione al database
    return redirect(url_for('home'))

@app.route('/svuota', methods=['POST'])
def svuota():
    ListaSpesa.query.delete() #metodo di Sqlachemy che elimina tutti gli elementi corrispondeti alla query quindi tutti
    db.session.commit() #Commit applicando le modifiche su tutti gli elementi al database
    return redirect(url_for('home'))

#avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)