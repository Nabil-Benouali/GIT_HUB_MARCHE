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


def extract(txt):
    if txt[-5] == '1' or txt[-5] == '2':
        nom = txt[11:-5]
    else:
        nom = txt[11:-4]
    return nom


nom = ''
prenom = ''
L = ("Nomination_Chirac1.txt", "Nomination_Chirac2.txt", "Nomination_Giscard dEstaing.txt", "Nomination_Hollande.txt",
     "Nomination_Macron.txt", "Nomination_Mitterand1.txt", "Nomination_Mitterand2.txt", "Nomination_Sarkozy.txt")
extract("Nomination_Chirac1.txt")
extract("Nomination_Chirac2.txt")
extract("Nomination_Giscard dEstaing.txt")
extract("Nomination_Hollande.txt")
extract("Nomination_Macron.txt")
extract("Nomination_Mitterand1.txt")
extract("Nomination_Mitterand2.txt")
extract("Nomination_Sarkozy.txt")

dico = {'Chirac': 'Jacques', 'Giscard dEstaing': 'Valérie', 'Hollande': 'François', 'Macron': 'Emmanuel',
        'Mitterand': 'François', 'Sarkozy': 'Nicolas'}

newlist = []


def associate(liste1, liste2):
    for i in range(len(liste1)):
        liste2.append('')
        m = extract(liste1[i])
        prenom = dico[m]
        np = m + ' ' + prenom
        liste2[i] = np
    return liste2


Liste_presidents = associate(L, newlist)
NewListe_presidents = []
for i in range(len(Liste_presidents)):
    if Liste_presidents[i] not in NewListe_presidents:
        NewListe_presidents.append(Liste_presidents[i])
print(NewListe_presidents)

import os
import string


def nettoyer_texte(texte):
    # Je supprime ici toute les fonctuation sauf l'apostrophe et les trait d'unions
    text_sans_ponctuation = texte.translate(str.maketrans(", ", string.punctuation.replace("'", "").replace("-", "")))
    # On gere les appostrophe et le tiret pour eviter la concaténation des mots
    texte_nettoye = " ".join([mot.strip(string.punctuation) for mot in texte_sans_pontuation.split()])

    return texte_nettoye


# Liste des chemins des fichiers
chemins_fichiers = [
    '/Users/nabil/Desktop/ChatBot-2023/SPeeches/Nomination_Chirac1.txt',
    '/Users/nabil/Desktop/ChatBot-2023/SPeeches/Nomination_Chirac2.txt',
    '/Users/nabil/Desktop/ChatBot-2023/SPeeches/Nomination_Giscard_dEstaing.txt',
    '/Users/nabil/Desktop/ChatBot-2023/SPeeches/Nomination_Hollande.txt',
    '/Users/nabil/Desktop/ChatBot-2023/SPeeches/Nomination_Macron.txt',
    '/Users/nabil/Desktop/ChatBot-2023/SPeeches/Nomination_Mitterrand1.txt',
    '/Users/nabil/Desktop/ChatBot-2023/SPeeches/Nomination_Mitterrand2.txt',
    '/Users/nabil/Desktop/ChatBot-2023/SPeeches/Nomination_Sarkozy.txt'
]

# Créer le dossier "cleaned" s'il n'existe pas
dossier_cleaned = '/users/nabil/Desktop/SPeeches/cleaned'
if not os.path.exists(dossier_cleaned):
    os.makedirs(dossier_cleaned)

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

# PARTIE DE MARIEM ///////////////////////////////////////////////////////////////////////////////////////////////////

import os


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
        with open(os.join(dierctory, nabil), 'r') as f:
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


directory = "nabil"
print("least important words:", find_least_important_words(directory))

max_scores = df.max()
highest_tfidf_words = max_scores[max_scores.max()]
print(f"the words with the highest tf_idf score are {highest_tfidf_words} with a score of {max_scores.max()}.")

import os
import string
import collections


def nettoyer_texte(texte):
    text_sans_ponctuation = texte.translate(str.maketrans(", ", string.punctuation.replace("'", "").replace("-", "")))
    texte_nettoye = " ".join([mot.strip(string.punctuation) for mot in text_sans_ponctuation.split()])
    return texte_nettoye


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









#travail mariem #17/12/2023
#1
def split_question(what_is_the_earth_made_of):
    return question.split()
question = "What is the Earth made of?"
words = split_question(question)
print(words)
#2
def common_terms(question, corpus):
    corpus_content = [extract(file) for file in corpus]
    question_terms = set(question.lower().split())
    corpus_terms = set(' '.join(corpus_content).lower().split())
    # Find and return the common terms
    common = question_terms.intersection(corpus_terms)
    return common

question = "terms that form the intersection between the set of words in the corpus and the set of words in the question ?"
corpus = ("Nomination_Chirac1.txt", "Nomination_Chirac2.txt", "Nomination_Giscard dEstaing.txt", "Nomination_Hollande.txt",
"Nomination_Macron.txt", "Nomination_Mitterand1.txt", "Nomination_Mitterand2.txt", "Nomination_Sarkozy.txt")

print(common_terms(question, corpus))
#3
question = "the TF-IDF matrix of the corpus must have N rows and M columns, where N = 8 and M =1681 "
corpus = ("Nomination_Chirac1.txt", "Nomination_Chirac2.txt", "Nomination_Giscard dEstaing.txt", "Nomination_Hollande.txt",
"Nomination_Macron.txt", "Nomination_Mitterand1.txt", "Nomination_Mitterand2.txt", "Nomination_Sarkozy.txt")
def compute_tf(question, corpus):
    words = question.split()
    tf_scores = {words}
    tf_victor = {}

    for words in corpus :
        tf_vector[word] = tf_scores.get(word, 0)
    return tf_vector




