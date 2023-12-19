print("                                                                                                   ")
print("                                                                                        #           ")
print("                                                                                        #          ")
print("                                                                                      #####         ")
print("                                                                                      #   #         ")
print("                                                                                      #####      ")
print(
    "#########  ##     ##  ########  ########    ########   ########  ########          ####   ####                                                                                        ")
print(
    "#          ##     ##  ##    ##     ##       ##    ##   ##    ##     ##         ######        #####                                                                                                                    ")
print(
    "#          #########  ########     ##       #########  ##    ##     ##      ####                 ####                                                                                                                                                               ")
print(
    "#          ##     ##  ##    ##     ##       ##     ##  ##    ##     ##      ##                     ##                                                                                                                  ")
print(
    "#          ##     ##  ##    ##     ##       ##     ##  ##    ##     ##      #                       #                                                                                                                 ")
print(
    "#########  ##     ##  ##    ##     ##       ########   ########     ##      #                       #                                                                                                                ")
print(
    "                                                                            #########################                        ")
print(
    "                                                                            #   #   #   #   #   #   #                                                                                         ")
print(
    "                                                                            #   #   #   #   #   #   #                                            ")
print(
    "                                                                        ################################                                                 ")
print(
    "                                                                        #    #    #           #    #   #                                          ")
print(
    "                                                                        #    #    #           #    #   #             ")
print(
    "                                                                        #    #    #     #     #    #   #                                          ")
print(
    "                                                                        #    #    # #       # #    #   #                                          ")
print(
    "                                                                        #    #   #             #   #   #                                            ")
print(
    "                                                                        #    ##                   #    #                                     ")
print(
    "                                                                        #  #                         # #                                  ")
print("                                                                        #                               #  ")
print(
    "                                                                     #                                     #             ")

import os
import string
import collections
import shutil





def extract_prenom(file):
    nom = ''
    if file[-5] == '1' or file[-5] == '2':
        nom = file[11:-5]
    else:
        nom = file[11:-4]
    return nom


def associate_nom_prenom(liste1, liste2):
    for i in range(len(liste1)):
        liste2.append('')
        nom = extract_prenom(liste1[i])
        prenom = dico[nom]
        nom_prenom = nom + ' ' + prenom
        liste2[i] = nom_prenom
    return liste2


def nettoyer_texte(texte):
    text_sans_ponctuation = texte.translate(str.maketrans(",", string.punctuation.replace("'", " ").replace("-", " ")))
    texte_nettoye = " ".join([mot.strip(string.punctuation) for mot in text_sans_ponctuation.split()])
    return texte_nettoye

def Clean_Text(texte):
    NewText = texte.strip()
    cleaned_txt = NewText.translate(str.maketrans("'-","  "))
    return cleaned_txt




def transpose(matrix):
    transposed = []
    for i in range(len(matrix[0])):
        transposed_row = []
        for row in matrix:
            transposed_row.append(row[i])
        transposed.append(transposed_row)
    return transposed


def calculate_tfidf(directory):
    documents = []
    for filename in os.list(dictionary):
        with open(os.join(directory, nabil), 'r') as f:
            documents.append(f.read())
        vectorizer = tfidfVectorizer.fit_transform(documents)
        return vectorizer


def find_least_important_words(directory):
    words, tfidf_matrix = calculate_tfidf(directory)
    tfidf_matrix_matrix = transpose(tfidf_matrix)
    least_important_words = []
    for i, word in enumerate(words):
        if all(score == 0 for score in tfidf_matrix[i]):
            least_important_words.append(word)
    return least_important_words


def split_question(question):
    return question.split()


def common_terms(question, corpus):
    corpus_content = [extract(file) for file in corpus]
    question_terms = set(question.lower().split())
    corpus_terms = set(' '.join(corpus_content).lower().split())
    # Find and return the common terms
    common = question_terms.intersection(corpus_terms)
    return common


def compute_tf(question, corpus):
    words = question.split()
    tf_scores = {words}
    tf_victor = {}
    for words in corpus:
        tf_vector[word] = tf_scores.get(word, 0)
    return tf_vector


L = ("Nomination_Chirac1.txt", "Nomination_Chirac2.txt", "Nomination_Giscard dEstaing.txt", "Nomination_Hollande.txt",
     "Nomination_Macron.txt", "Nomination_Mitterand1.txt", "Nomination_Mitterand2.txt", "Nomination_Sarkozy.txt")

dico = {'Chirac': 'Jacques', 'Giscard dEstaing': 'Valérie', 'Hollande': 'François', 'Macron': 'Emmanuel',
        'Mitterand': 'François', 'Sarkozy': 'Nicolas'}

newlist = []
Liste_presidents = associate_nom_prenom(L, newlist)
NewListe_presidents = []
for i in range(len(Liste_presidents)):
    if Liste_presidents[i] not in NewListe_presidents:
        NewListe_presidents.append(Liste_presidents[i])
print(NewListe_presidents)

with open(":/../Speeches/Nomination_Chirac1.txt", "r") as f1, open(":/../Speeches/Nomination_Chirac2.txt", "r") as f2, open(":/../Speeches/Nomination_Giscard dEstaing.txt", "r") as f3, open(":/../Speeches/Nomination_Sarkozy.txt", "r") as f4, open(":/../Speeches/Nomination_Mitterrand1.txt","r") as f5, open(":/../Speeches/Nomination_Mitterrand2.txt","r") as f6, open(":/../Speeches/Nomination_Hollande.txt", "r") as f7, open(":/../Speeches/Nomination_Macron.txt", "r") as f8 :
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    lines3 = f3.readlines()
    lines4 = f4.readlines()
    lines5 = f5.readlines()
    lines6 = f6.readlines()
    lines7 = f7.readlines()
    lines8 = f8.readlines()
with open(":/../cleaned/Nomination_Chirac1_cleaned.txt", "w") as F1, open(":/../cleaned/Nomination_Chirac2_cleaned.txt", "w") as F2, open(":/../cleaned/Nomination_Giscard dEstaing_cleaned.txt", "w") as F3, open(":/../cleaned/Nomination_Sarkozy_cleaned.txt", "w") as F4, open(":/../cleaned/Nomination_Mitterrand1_cleaned.txt", "w") as F5, open(":/../cleaned/Nomination_Mitterrand2_cleaned.txt", "w") as F6, open(":/../cleaned/Nomination_Hollande_cleaned.txt","w") as F7, open(":/../cleaned/Nomination_Macron_cleaned.txt", "w") as F8:
    for Line1 in lines1 :
        print(Clean_Text(Line1))
    for Line2 in lines2 :
        F2 = Clean_Text(Line2)
    for Line3 in lines3 :
        F3 = Clean_Text(Line3)
    for Line4 in lines4 :
        F4 = Clean_Text(Line4)
    for Line5 in lines5 :
        F5 = Clean_Text(Line5)
    for Line6 in lines6 :
        F6 = Clean_Text(Line6)
    for Line7 in lines7 :
        F7 = Clean_Text(Line7)
    for Line8 in lines8 :
        F8 = Clean_Text(Line8)



# Liste des chemins des fichiers

chemins_fichiers = [
    ':/../Speeches/Nomination_Chirac1.txt',
    ':/../Speeches/Nomination_Chirac2.txt',
    ':/../Speeches/Nomination_Giscard_dEstaing.txt',
    ':/../Speeches/Nomination_Hollande.txt',
    ':/../Speeches/Nomination_Macron.txt',
    ':/../Speeches/Nomination_Mitterrand1.txt',
    ':/../Speeches/Nomination_Mitterrand2.txt',
    ':/../Speeches/Nomination_Sarkozy.txt'
]


# Pour parcourir la liste des chemins des fichiers :
for chemin_fichier in chemins_fichiers:
    try:
        with open(chemin_fichier, 'r') as fichier:
            contenu = fichier.read()

            # Convertir le contenu en minuscules
            contenu_en_minuscules = contenu.lower()

            # Créer le chemin de sortie dans le dossier cleaned
            chemin_fichier_sortie = os.path.join(dossier_cleaned, os.path.basename(chemin_fichier))

            # Écrire le contenu converti en minuscules dans le fichier de sortie
            with open(chemin_fichier_sortie, 'w') as fichier_sortie:
                fichier_sortie.write(contenu_en_minuscules)

            # Afficher un message de confirmation
            print(
                f"Le fichier {chemin_fichier} a été converti en minuscules et enregistré dans {chemin_fichier_sortie}")

    except FileNotFoundError:
        print(f"Le fichier {chemin_fichier} n'a pas été trouvé.")

    except Exception as e:
        print(f"Une erreur s'est produite lors de la conversion du fichier {chemin_fichier}: {e}")




directory = "nabil"
print("least important words:", find_least_important_words(directory))

max_scores = df.max()
highest_tfidf_words = max_scores[max_scores.max()]
print(f"the words with the highest tf_idf score are {highest_tfidf_words} with a score of {max_scores.max()}.")

chemins_fichiers = []

dossier_cleaned = '/users/nabil/Desktop/SPeeches/cleaned'
if not os.path.exists(dossier_cleaned):
    os.makedirs(dossier_cleaned)

word_counts = collections.Counter()

for chemin_fichier in chemins_fichiers:
    try:
        with open(chemin_fichier, 'r') as fichier:
            contenu = fichier.read()
            contenu_en_minuscules = contenu.lower()
            contenu_nettoye = nettoyer_texte(contenu_en_minuscules)
            word_counts.update(contenu_nettoye.split())

            chemin_fichier_sortie = os.path.join(dossier_cleaned, os.path.basename(chemin_fichier))
            with open(chemin_fichier_sortie, 'w') as fichier_sortie:
                fichier_sortie.write(contenu_en_minuscules)
            print(
                f"Le fichier {chemin_fichier} a été converti en minuscules et enregistré dans {chemin_fichier_sortie}")
    except FileNotFoundError:
        print(f"Le fichier {chemin_fichier} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la conversion du fichier {chemin_fichier}: {e}")

print("Most common words:")
for word, count in word_counts.most_common(10):
    print(f"{word}: {count}")






question = "What is the Earth made of?"
words = split_question(question)
print(words)


question = "terms that form the intersection between the set of words in the corpus and the set of words in the question ?"
corpus = (
"Nomination_Chirac1.txt", "Nomination_Chirac2.txt", "Nomination_Giscard dEstaing.txt", "Nomination_Hollande.txt",
"Nomination_Macron.txt", "Nomination_Mitterand1.txt", "Nomination_Mitterand2.txt", "Nomination_Sarkozy.txt")

print(common_terms(question, corpus))
# 3
question = "the TF-IDF matrix of the corpus must have N rows and M columns, where N = 8 and M =1681 "
corpus = (
"Nomination_Chirac1.txt", "Nomination_Chirac2.txt", "Nomination_Giscard dEstaing.txt", "Nomination_Hollande.txt",
"Nomination_Macron.txt", "Nomination_Mitterand1.txt", "Nomination_Mitterand2.txt", "Nomination_Sarkozy.txt")





