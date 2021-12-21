from words_in_proteome import *

f = open("english-common-words.txt", "r")
fasta = open ("human-proteome.fasta","r")

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('le nombre de mots sélectionnés :', len(read_words(f)))

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
dict = read_sequences(fasta)
print('le nombre de séquences lues : ' ,len(dict))
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print( 'la séquence associée à la protéine O95139  : ',dict['O95139'] )

print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

list = read_words(f)
fasta.seek(0)
dictionnaire = read_sequences(fasta)
dict_f = search_words_in_proteome(list , dictionnaire)
print('the pourcentage : ',str((find_most_frequent_word(dict_f)*100/len(dict))))
