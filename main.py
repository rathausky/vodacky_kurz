import re
from flask import Flask, redirect
from flask import request, render_template

import json
class Student:
    def __init__(self, nick, jmeno, prijmeni, trida, tridni, je_plavec, kanoe_kamarad):
        """

        :param nick: nick uzivatele
        :param jmeno: jmeno uzivatele
        :param prijmeni: prijmeni uzivatele
        :param trida: trida uzivatele
        :param tridni: tridni uzivatele
        :param je_plavec: atribut zda je plavec
        :param kanoe_kamarad: kamarad na kanoe uzivatele
        """
        self.nick = nick
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.trida = trida
        self.tridni = tridni
        self.je_plavec = je_plavec
        self.kanoe_kamarad = kanoe_kamarad

studenti = []

app = Flask(__name__)
data = 0
@app.route('/')
def index():
    """

    :return: metoda vrací stránku index.html
    """
    return render_template("index.html")

@app.route('/registrace.html')
def moje_zkouska():
    """

    :return: metoda vrací stránku registrace.html
    """
    return render_template('registrace.html')

@app.route("/vypis.html", methods=["GET"])
def vypis():
    """

    :return: metoda vrací stránku vypis.html
    """
    return render_template('vypis.html', studenti = studenti)

@app.route("/registruj", methods=["POST"])
def registruj():

    try:
        nick = zkontroluj_neprazdnost(request.form["nick"])
        jmeno = zkontroluj_neprazdnost(request.form["jmeno"])
        prijmeni = zkontroluj_neprazdnost(request.form["prijmeni"])
        trida = zkontroluj_neprazdnost(request.form["trida"])
        tridni = zkontroluj_neprazdnost(request.form["tridni"])
        je_plavec = zkontroluj_neprazdnost(request.form["je_plavec"])
        kanoe_kamarad = zkontroluj_neprazdnost(request.form["kanoe_kamarad"])
        if ((je_plavec == "1") or (je_plavec == 1)):
            je_plavec = True
        else:
            je_plavec = False
        if je_plavec == False:
            return render_template("400.html")

        if not re.search("^[a-zA-Z0-9]{2,20}$", nick):
            return render_template("400.html")
        if ((kanoe_kamarad == '') or not (re.search("^[a-zA-Z0-9]{2,20}$", kanoe_kamarad))):
            return render_template("400.html")
        if not re.search("^[a-zA-Z0-9]{2,20}$", jmeno):
            return render_template("400.html")
        if not re.search("^[a-zA-Z0-9]{2,20}$", prijmeni):
            return render_template("400.html")
        if not re.search("^[a-zA-Z0-9]{1,3}$", trida):
            return render_template("400.html")
        if not re.search("^[a-zA-Z0-9]{2,20}$", tridni):
            return render_template("400.html")

        student = Student(nick, jmeno, prijmeni, trida, tridni, je_plavec, kanoe_kamarad)
        studenti.append(student)
        return redirect("/vypis.html", code=301)
    except ValueError as e:
        return render_template('400.html')

def zkontroluj_neprazdnost(text):
    if (text == None) or (text == ''):
        raise ValueError(text)

    return text








#@app.route("/test.html", methods=["GET"])
#def test():
    #return "ahoj"

#@app.route('/restapi/v1/<nickname>', methods=["POST","GET"])
#def validace_duplicita(nickname):

    #for user in list_users:
        #if user["nick"] == nickname:
            #return render_template("400.html")

#@app.route('/restapi/v1/nacitani_souboru/<nickname>', methods=["POST","GET"])
#def nacitani_souboru(nick, jmeno, prijmenit, )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)