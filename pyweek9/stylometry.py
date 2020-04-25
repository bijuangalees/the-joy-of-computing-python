# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 16:31:52 2020

@author: bijuangalees
"""

papers={'Madison':[10,14,37,38,39,40,41,42,43,44,45,45,47,48],
        'Hamilton':[1,6,7,8,9,11,12,13,15,16,17,21,22,23,24,25,26,27,28,29,
                    30,31,32,33,34,35,36,59,60,78,79,80,81,82,83,84,85],
        'jay':[2,3,4,5],
        'shared':[18,19,20],
        'Disputed':[49,50,51,52,53,54,55,56,57,58,62,63]
}

if read_files(filename):
    string=[]
    for file in filename:
        with open(f'federalist_{file}.txt')as f:
            string.append(f.read())
    return('/n'.join(strings))
    
federalist_byauthor={}
for author, files in papers.items():
    e=federalist_by_author[author]=read_files(files)

authors=('Hamilton','Madison','Disputed','Jay','Shared')
author_tokens={}
length_distribution={}

for author in authors:
    tokens=nltk.word_tokenize(federalist_by_author[author])
    
    author_tokens[author]=([token for tokens in token if any(c.aplha() for c in token)])
    token_lenghts=[len(token) for token in author_token[author]]
    length_distributions[authors]=nltk.FreqDist(token_lengths)
    length_distributions[author].plot(15,title=author)
