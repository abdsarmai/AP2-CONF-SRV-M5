#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import *
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    try:
        connexionBD = mysql.connector.connect(
            host='IP-serveur-BDD',
            user='adminresanet',
            password='azerty2022',
            database='resanet'
        )
        curseur = connexionBD.cursor()
        requete = 'select id, libelle from service'
        curseur.execute(requete, ())
        lst = curseur.fetchall()
        services = '<html><body><ul>'
        for e in lst:
            services += '<li>' + str(e[0]) + ' ' + str(e[1]) + '</li>'
        curseur.close()
        services += '</ul></body></html>'
        reponse = make_response(services)
        return reponse
    except Exception as e:
        print(e)  # Afficher l'erreur pour le débogage
        reponse = make_response('<html><body><h1>Nok</h1></body></html>')
        return reponse

#if __name__ == '__main__':
#    app.run(debug=True, host='0.0.0.0', port=5000)
# serveur de test en cas de debug, ne pas utiliser en dehors du développement
