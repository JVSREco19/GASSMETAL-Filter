import re
import os

def remove_repetidos(lista):
    l = []
    l.append(aux)
    removeCounter = 0;
    for i in lista:
      if i[0:len(i)-1] not in l and i!= aux:
        l.append(i[0:len(i)-1])
        linesToMantain.append(int(i[len(i)-1]))

      else:
        removeCounter+=1;
    
      l.sort()
    print(str(removeCounter)+ " Removed")
    return l

for filename in os.listdir(os.getcwd()):
  aux = ['template','ligations','counter']
  archiveName =  filename
  if archiveName[len(archiveName)-3:len(archiveName)] =='txt' and archiveName[0:7]!='treated':
    print("Opening {} file".format(archiveName))
    ficheiro = open(archiveName)
    text = ficheiro.readlines()
    linesToMantain = []
    repeatedLines = []
    if(archiveName[-3:]=='csv'):
      text = text[2:]

    activeSites = []
    counter = 0;
    textList =[]
    for linha in text:
      words = linha.split()
      textList.append(linha.split())
      stringWithSpaces= " ".join(words[3:])
      templateMatch = re.search(r'\b[a-zA-Z][a-zA-Z0-9]{3}\b|\b[a-zA-Z0-9][a-zA-Z][a-zA-Z0-9]{2}\b|\b[a-zA-Z0-9]{2}[a-zA-Z][a-zA-Z0-9]\b|\b[a-zA-Z0-9]{3}[a-zA-Z]\b',stringWithSpaces)

      if templateMatch != None:
        templatePos = templateMatch.start()
        templateCode = templateMatch.group()
        ligationsString = stringWithSpaces[:templatePos-1]
        finalArray= ligationsString.split(';')
        findHifen = re.search(r'-',''.join(finalArray))
        if findHifen!= None or templateCode =="NULL":
          activeSites.insert(counter,finalArray)
          activeSites[counter]= aux
        else:
          templateCode =stringWithSpaces[templatePos:len(stringWithSpaces)-1]
          finalArray.append(templateCode)
          activeSites.insert(counter,finalArray)
          activeSites[counter].sort()
          activeSites[counter].append(str(counter))
      else:
        activeSites.insert(counter,finalArray)
        activeSites[counter]= aux
      
      counter= counter +1;
    counter = 0;

    remove_repetidos(activeSites)
    
    treatedText = []

    for num in linesToMantain:
      if(counter==100):
        counter =0
      treatedLine = textList[num]
      treatedLine[1] = str(counter);
      counter += 1;
      treatedLineStr = ' '.join(treatedLine)
      treatedText.append(treatedLineStr)
      
      
    ficheiro.close()
    treatedFile = open("treated"+archiveName,"w")


    for member in treatedText:
      treatedFile.write(member+'\n')
    
    treatedFile.close()
    