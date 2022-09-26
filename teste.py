import re

ficheiro = open('ActiveSitesFound.txt')
text = ficheiro.readlines()
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
  counter= counter +1;


print(activeSites)
  


