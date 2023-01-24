from tkinter import *

expression = ""


def appuyer(touche):
    if touche == "=":
        calculer()
        return
    if touche == "%":
        calculer_pourcentage()
        return
    if touche == "√":
        calculer_racine()
        return
    if touche == "x^2":
        calculer_carré()
        return
    global expression
    expression += str(touche)
    equation.set(expression)



def calculer():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = total
    except:
        equation.set("erreur")
        expression = ""

def calculer_pourcentage():
    try:
        global expression
        result = eval(expression)
        result = result / 100
        expression = str(result)
        equation.set(result)
    except:
        equation.set("erreur")
        expression = ""

def calculer_racine():
    try:
        global expression
        rac = eval(expression)
        rac = rac ** (0.5)
        expression = str(rac)
        equation.set(rac)
    except:
        equation.set("Veuillez retaper le calcul comme cela : 4√")
        expression = ""

def calculer_carré():
    try:
        global expression
        car = eval(expression)
        car = car ** 2
        expression = str(car)
        equation.set(car)
    except:
        equation.set("erreur")
        expression = ""


def effacer():
    global expression
    expression = ""
    equation.set("")









π = 3,14159265


if __name__ == "__main__":
    gui = Tk()


    gui.configure(background="#101419")


    gui.title("Calculatrice")


    gui.geometry("247x350")


    equation = StringVar()


    resultat = Label(gui, bg="#101419", fg="#FFF", textvariable=equation, height=2)
    resultat.grid(columnspan=4)


    boutons = [7, 8, 9, "*", 4, 5, 6, "+", 1, 2, 3, "-", "%", 0, "√", "/","π", "x^2", ".", "=",]
    ligne = 1
    colonne = 0

    for bouton in boutons:
        b = Label(gui, text=str(bouton), bg="#476C9B", fg="#FFF", height=3, width=8)

        b.bind("<Button-1>", lambda e, bouton=bouton: appuyer(bouton))

        b.grid(row=ligne, column=colonne)

        colonne += 1
        if colonne == 4:
            colonne = 0
            ligne += 1


    b = Label(gui, text="Effacer", bg="#984447", fg="#FFF", height=4, width=17)
    b.bind("<Button-1>", lambda e: effacer())
    b.grid(row=6, column=2, columnspan=2)


    b = Label(gui, text="Historique", bg="#984447", fg="#FFF", height=4, width=17)
b.bind("<Button-1>",lambda e: historique())
b.grid(row=6, column=0, columnspan=2)








gui.mainloop()
