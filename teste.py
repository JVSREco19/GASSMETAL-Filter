import re

def remove_repetidos(lista):
    l = []
    for i in lista:
      if i[0:len(i)-1] not in l:
          l.append(i[0:len(i)-1])
          linesToMantain.append(int(i[len(i)-1]))
      l.sort()
    return l


archiveName = 'ActiveSitesFound.txt'
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
  textList.append(words)
  stringWithSpaces= " ".join(words[3:])
  templateMatch = re.search(r'[a-zA-Z0-9]{4}',stringWithSpaces)
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

print(linesToMantain)
treatedText = []
for num in linesToMantain:
  treatedLine = textList[num]
  treatedLine[1] = str(counter);
  counter += 1;
  treatedText.append(' '.join(treatedLine))

for member in treatedText:
  print(member)
