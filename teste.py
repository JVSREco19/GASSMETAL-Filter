import re

def remove_repetidos(lista):
    l = []
    removeCounter = 0;
    for i in lista:
      if i[0:len(i)-1] not in l:
        l.append(i[0:len(i)-1])
        linesToMantain.append(int(i[len(i)-1]))
      else:
        removeCounter+=1;
      l.sort()
    print(removeCounter)
    return l


archiveName = 'ActiveSitesFound (3).txt'
ficheiro = open(archiveName)
text = ficheiro.readlines()
linesToMantain = []

if(archiveName[-3:]=='csv'):
  text = text[2:]


activeSites = []
counter = 0;
textList =[]
for linha in text:
  words = linha.split()
  textList.append(linha.split("\t"))
  stringWithSpaces= " ".join(words[3:])
  templateMatch = re.search(r'[a-zA-Z]{4}|[0-9]{3}[a-zA-Z]|[a-zA-Z][0-9]{3}|[a-zA-Z]{3}[0-9]|[0-9][a-zA-Z]{3}|[0-9]{2}[a-zA-Z][0-9]|[0-9][a-zA-Z][0-9]{2}|[a-zA-Z][0-9]{2}[a-zA-Z]|[0-9][a-zA-Z]{2}[0-9]|[0-9]{2}[a-zA-Z]{2}|[a-zA-Z]{2}[0-9]{2}|[a-zA-Z][0-9][a-zA-Z][0-9]|[0-9][a-zA-Z][0-9][a-zA-Z]',stringWithSpaces)
  templatePos = templateMatch.start()
  templateCode = templateMatch.group()
  ligationsString = stringWithSpaces[:templatePos-1]
  finalArray= ligationsString.split(';')
  finalArray.append(templateCode)
  activeSites.insert(counter,finalArray)
  activeSites[counter].sort()
  activeSites[counter].append(str(counter))
  counter= counter +1;
counter = 0;
activeSites= remove_repetidos(activeSites)
activeSites.sort()
for line in activeSites:
  print(line)
treatedText = []
for num in linesToMantain:
  if(counter==100):
    counter =0
  treatedLine = textList[num]
  treatedLine[1] = str(counter);
  counter += 1;
  treatedText.append(' '.join(treatedLine))
ficheiro.close()
treatedFile = open("treated"+archiveName,"w")

for member in treatedText:
  treatedFile.write(member)


treatedFile.close()