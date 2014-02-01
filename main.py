import sys
import os
import itertools

#g ya du shit dans le readme


# Faire un graph oriente avec un arc seulement si un mot a 1 seulemeent de difeerence
# Puis faire une recherche de plus court chemin dans le graphe

#g on ne peut passer que par les mots dans le dictionnaire pour faire les sauts
#g (ca m'a pris trop de temps pour compredre ca, dsl. Martin a code comme un malade et pas moi) 

# lengthword a laire de fonctioner
#g wat? mais ca marche...
def lengthWord(word1, word2, maximum=100000):
    """

    >>> lengthWord("cat","cot")
    1

    >>> lengthWord("penis","prots")
    3

    >>> lengthWord("asd","asd")
    0

    """
    if word1 == word2:
        return 0
    nombreDifference = 0
    
    #g Itertools.izip_longest dans la doc:
    #g Make an iterator that aggregates elements from each of the iterables. 
    #g If the iterables are of uneven length, missing values are filled-in with fillvalue.
    #g Iteration continues until the longest iterable is exhausted.
    for char1, char2 in itertools.izip_longest(word1, word2, fillvalue=' '):
        if char1 != char2:
            nombreDifference = nombreDifference + 1
            if nombreDifference == maximum:
                return maximum
    return nombreDifference



# make A*, lengthWord is the heuristic
#g (heuristic = a decouvrir)
def findDist(graph, word1, word2):
    s = {word1}

    #g pour x dans le graph, la entre x et word2
    distance_courante = {x: 1 + lengthWord(x, word2) for x in graph[word1]}
    print(distance_courante)
    # check list filter and stuff 
    #g (C'est a faire ou quoi xD  je crois que oui, fuu, je sais pas quoi faire ici... ca marche?)



if __name__ == "__main__":

    # sys.argv = ["", "cat", "dog"]  # Pour tester

    if len(sys.argv) < 3:
        print("Pas assez d'arguments")

    elif len(sys.argv) > 3:
        print("trop d'arguments")

    word1, word2 = sys.argv[1:3]

    if len(word1) != len(word2):
        print("Ne peut etre resolu")

    with open("dictionnaire.txt") as f:
        #g retrouve tous les mots du dictionnaire
        words = {x.strip().lower() for x in f}

        graph = {}
        i = len(word1)
        wordsOfLengthI = list(filter(lambda x: len(x) == i, words))
        print(i, len(wordsOfLengthI))
        for w1 in wordsOfLengthI:
            for w2 in wordsOfLengthI:
                if lengthWord(w1, w2, 2) == 1:
                    if w1 in graph:
                        graph[w1].append(w2)
                    else:
                        graph[w1] = [w2]

        # print(graph)
        findDist(graph, word1, word2)
        print("End")
