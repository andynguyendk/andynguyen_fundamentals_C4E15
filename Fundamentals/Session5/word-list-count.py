import re
para = ("""Whether you are a student, a scholar, looking to meet fellow Alice in Wonderland fans, or throwing a theme party, here you can find everything you always wanted to know about Lewis Carroll’s books “Alice’s Adventures in Wonderland” and “Through the Looking Glass and what Alice found there”, as well as Disney’s Alice in Wonderland cartoon movie.
Enjoy your stay in Wonderland!""")
delimiters = ['\n', ' ', ',', '.', '?', '!', ':', 'and_what_else_you_need']
parastring = re.split('|'.join(delimiters), para)
#print(parastring)
wordlist = {}
for index, word in enumerate(parastring):
    if word in wordlist:
        wordlist[word] += 1
    else:
        wordlist[word] = 1
print(wordlist)
