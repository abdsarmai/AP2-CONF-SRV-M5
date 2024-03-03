#!/bin/bash
#Installation de python3 et python3-pip
apt-get update && apt-get install python3 python3-pip
#Installation du Framework et Service web qui est lié avec
pip3 install flask Werkzeug
#Activation du module WSGI apache2
a2enmod wsgi
