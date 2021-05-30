# OC-QL-P4-Chess
***

# 1.Presentation
***
Ce programme permet de gérer un tournoi d'échecs de 8 joueurs avec la création de tournois, sauvegarde, chargement et génération de rapports pour les joueurs, tournois, rounds et  matchs.

# 2.Pre-requits
***
* Python 3
* tinydb
* flake8

# 3.Installation
***
Pour installer le programme via un terminal :  

Sous Windows :  

$ git clone https://github.com/quentin8469/OC-QL-P4-Chess.git    
$ python3 -m venv env  
$ env/scripts/activate  
$ pip3 install -r requirements.txt   
$ python app.py

Sous linux/Mac :      

$ git clone https://github.com/quentin8469/OC-QL-P4-Chess.git    
$ python3 -m venv env    
$ source env/bin/activate    
$ pip3 install -r requirements.txt    
$ python app.py    

Créer un rapport flake8 :  

`flake8 --exclude=env,venv --format=html --htmldir=flake8_report --max-line-lengt=119`
