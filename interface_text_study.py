import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import PhotoImage



def afficher_options():
    options = [
        "Mettre tous les mots en minuscule",
        "Mettre tous les mots en majuscule",
        "Déterminer le nombre de mots",
        "Trouver le nombre précis d'un mot",
        "Trouver le mot le plus utilisé",
        "Remplacer une occurrence précise par une autre"
    ]
    return options


def mettre_en_minuscule(texte):
    return texte.lower()


def mettre_en_majuscule(texte):
    return texte.upper()


def compter_mots(texte):
    mots = texte.split()
    return len(mots)


def trouver_occurence(texte, mot):
    mots = texte.split()
    return mots.count(mot)


def mot_le_plus_utilise(texte):
    mots = texte.split()
    frequence = {}
    for mot in mots:
        if mot in frequence:
            frequence[mot] += 1
        else:
            frequence[mot] = 1
    mot_frequent = max(frequence, key=frequence.get)
    return mot_frequent


def remplacer_occurrence(texte, ancien_mot, nouveau_mot):
    return texte.replace(ancien_mot, nouveau_mot)


def afficher_resultat(result):
    result_window = tk.Toplevel()
    result_window.title("Résultat")
    result_label = tk.Label(result_window, text="Résultat de l'opération:")
    result_label.pack()
    result_text = tk.Text(result_window, height=10, width=50, wrap='word')
    result_text.insert(tk.END, result)
    result_text.pack()
    result_window.mainloop()


def traiter_option():
    texte = text_entry.get("1.0", tk.END).strip()
    if not texte:
        messagebox.showerror("Erreur", "Le texte ne doit pas être vide.")
        return

    option_choisi = option_var.get()
    if option_choisi == 0:
        result = mettre_en_minuscule(texte)
    elif option_choisi == 1:
        result = mettre_en_majuscule(texte)
    elif option_choisi == 2:
        result = compter_mots(texte)
    elif option_choisi == 3:
        mot = simpledialog.askstring("Entrer le mot", "Entrez le mot à rechercher:")
        if mot:
            result = trouver_occurence(texte, mot)
            result = f"Le mot '{mot}' apparaît {result} fois."
    elif option_choisi == 4:
        result = mot_le_plus_utilise(texte)
        result = f"Le mot le plus utilisé est: {result}"
    elif option_choisi == 5:
        ancien_mot = simpledialog.askstring("Ancien mot", "Entrez le mot à remplacer:")
        nouveau_mot = simpledialog.askstring("Nouveau mot", "Entrez le nouveau mot:")
        if ancien_mot and nouveau_mot:
            result = remplacer_occurrence(texte, ancien_mot, nouveau_mot)

    afficher_resultat(result if isinstance(result, str) else str(result))


def main():
    global text_entry, option_var

    root = tk.Tk()
    root.title("Wordi - Manipulation de texte")

    # Charger l'image
    background_image = PhotoImage(file="logo_wordi.png")

    # Créer une étiquette pour l'image
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)  # Étirer l'image pour remplir toute la fenêtre

    tk.Label(root, text="Saisissez le texte à étudier ici:", bg='white').pack()

    text_entry = tk.Text(root, height=10, width=50)
    text_entry.pack()

    options = afficher_options()
    option_var = tk.IntVar(value=0)

    for i, option in enumerate(options):
        tk.Radiobutton(root, text=option, variable=option_var, value=i).pack(anchor='w')

    tk.Button(root, text="Exécuter", command=traiter_option, bg='pink').pack()

    root.mainloop()


if __name__ == "__main__":
    main()
