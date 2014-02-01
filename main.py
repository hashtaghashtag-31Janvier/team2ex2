import sys
import os
import itertools


#Faire un graph oriente avec un arc seulement si un mot a 1 seulemeent de difeerence
#Puis faire une recherche de plus court chemin dans le graphe

def lengthWord(word1, word2, maximum=100000):
    """

    >>> lengthWord("cat","cot")
    1

    """
    if word1 == word2: return 0
    nombreDifference = 0
    for char1,char2 in itertools.zip_longest(word1,word2, fillvalue=' '):
        if char1 != char2:
            nombreDifference = nombreDifference + 1
            if nombreDifference == maximum:
                return maximum
    return nombreDifference


#make A*, lengthWord is the heuristic
def findDist(graph, word1, word2):
    s = {word1}

    distcourante = { x:1 + lengthWord(x,word2)  for x in graph[word1]}
    print(distcourante)
    #check list filter and stuff 
    
    
    
    

if __name__=="__main__":

    sys.argv = ["","cat","dog"] #Pour tester 
    
    if len(sys.argv) < 3:
        print("Pas assez d'argument")

    word1,word2 = sys.argv[1:3]

    if len(word1) != len(word2):
        print("Ne peut etre resolu")
    
    with open("dictionnaire.txt") as f:
        words = {x.strip().lower() for x in f}

        graph = {}
        i=len(word1)
        wordsOfLengthI = list(filter(lambda x: len(x) == i, words))
        print(i, len(wordsOfLengthI))
        for w1 in wordsOfLengthI:
            for w2 in wordsOfLengthI:
                if lengthWord(w1,w2,2)==1:
                    if w1 in graph:
                        graph[w1].append(w2)
                    else:
                        graph[w1] = [w2]
            
                        

        #print(graph)
        findDist(graph,word1,word2)
        print("End")
        
        
