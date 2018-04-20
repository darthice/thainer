import codecs
import pandas as pd
import ngram

def token(text):
    sens = []
    sens = ngram.run(text)
    run(sens)
def run(sens):
    word = []
    tag = []
    with codecs.open('dict.txt','r',encoding='utf-8') as f:
        dicts = [line.rstrip() for line in f]
    dicts[0] = dicts[0].replace('\ufeff','')
    test = []
    for i in range(len(dicts)):
        test.append(dicts[i].split('-'))
    for i in range(len(sens)):
        for k in range(len(test)):
            if sens[i] == test[k][0]:
                word.append(sens[i])
                tag.append(test[k][1])
    for i in range(len(word)):
        print(word[i], '-',tag[i])
def test():
    while True:
        sen = input('Input: ')
        if sen == 'exit':
            break
        token(sen)
