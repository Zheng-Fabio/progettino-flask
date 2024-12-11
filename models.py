from flask_sqlalchemy import SQLAlchemy #qui importiamo la classe SQLAlchemy
db = SQLAlchemy() #Creiamo un oggetto di tipo SQLAlchemy
class ListaSpesa(db.Model):
    # Tabella per gestire gli elementi della lista
    id = db.Column(db.Integer, primary_key=True)  # Identificativo unico
    elemento = db.Column(db.String(100), nullable=False)  # Nome dell'elemento, campo obbligatorio
