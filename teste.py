import re

archiveName = 'ActiveSitesFound.txt'
ficheiro = open(archiveName)
text = ficheiro.readlines()

if(archiveName[-3:]=='csv'):
  text = text[2:]


activeSites = []
counter = 0;
for linha in text:
  words = linha.split()
  stringWithSpaces= " ".join(words[3:])
  templateMatch = re.search(r'[a-zA-Z0-9]{4}',stringWithSpaces)
  templatePos = templateMatch.start()
  templateCode = templateMatch.group()
  ligationsString = stringWithSpaces[:templatePos-1]
  finalArray = []
  finalArray= ligationsString.split(';')
  finalArray.append(templateCode)
  activeSites.insert(counter,finalArray)
  activeSites[counter].sort()
  activeSites[counter].append(str(counter))
  counter= counter +1;

print(activeSites)


