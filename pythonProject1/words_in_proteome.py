
def read_words(f):
    l=[]
    for line in f:
        line = line.strip('\n').strip().upper()
        if len(line) > 2:
            l.append(line)
    f.seek(0)
    return l


def read_sequences(f):
   dic={}
   for line in f :
       if line.startswith(">") :
           y=""
           x=getcode(line)
       else :
           y=y+line.strip('\n')
       dic[x]=y

   return dic

def getcode(ch):
    indice = ch.find('|') + 1
    ch = ch[indice:]
    ch = ch[:ch.find('|')]
    return ch

def search_words_in_proteome(list ,dict):
    dict_result={}
    for i in list:
        nb = 0
        for j in dict.values():
            if i in j:
                nb = nb + 1
        dict_result[i]=nb
        print(i , 'found in ',nb ,' sequences')
    return dict_result




def find_most_frequent_word(dict):
    max=0
    indice = ''
    for i in dict:
        if dict[i] > max:
            max = dict[i]
            indice = i
    print( 'the most frequent word ==> ' , indice +' found in '+ str(max) +' sequences ')

    return max
