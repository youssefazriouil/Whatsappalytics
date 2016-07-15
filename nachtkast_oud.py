#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,re,operator,json,os
#open het bestand die whatsapp geÃ«xporteerd heeft, die de naam 'Whatsapp chat_Nachtkast.txt' heeft
nk = open('Whatsapp chat_Nachtkast.txt')

#maak een vertaal-woordenboek voor tekentjes die je computer niet kan begrijpen (emoji e.d.)
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
#initialiseer de python-dictionaries
nachtkastleden = {}
lines = 0
woordenboek = {}
dates = {}
times = {'00':0,'01':0,'02':0,'03':0,'04':0,'05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0,'12':0,'13':0,'14':0,'15':0,'16':0,'17':0,'18':0,'19':0,'20':0,'21':0,'22':0,'23':0}
index = 1

#itereer over elke line in de file, en splits de delen van de line op in een lijst die elements heet
for line in nk:
    line = line.decode("utf-8-sig").encode("utf-8")
    elements = line.split(':')
    index+=1

    #weggelaten komt voor in posts waar een vide,foto, of voicenote is geplaatst, deze moet genegeerd worden
    if(len(elements) == 5 and not('weggelaten' in line)):
        print 'line ', index
        #sla de delen van de line op in respectievelijke variabelen, verwijder de leestekens uit het bericht
        author = elements[3][1:]
        date = elements[0].split()[0]
        time = elements[0].split()[1]
        cleanPost = re.sub("[\.\"'?!\t\,\:@;\(\)\.]", "", elements[4][1:-1], 0, 0).lower()
        cleanPostTokens = cleanPost.split()
        lines+=1
        #als we een auteur van een bericht nog niet eerder zijn tegengekomen, initialiseer zijn dictionaries
        if(not(elements[3][1:] in nachtkastleden)):
            nachtkastleden[author] = {'zinnen':1,
                                      'woorden':len(elements[4][:-1]),
                                      'woordenlijst': {},
                                      'tijden':{'00':0,'01':0,'02':0,'03':0,'04':0,'05':0,'06':0,'07':0,'08':0,'09':0,'10':0,'11':0,'12':0,'13':0,'14':0,'15':0,'16':0,'17':0,'18':0,'19':0,'20':0,'21':0,'22':0,'23':0}
                                     }            
        #als we een auteur al wel zijn tegengekomen, verhoog de waarden in zijn dictionaries
        else:
            nachtkastleden[author]['zinnen']+=1
            nachtkastleden[author]['woorden']+=len(elements[4][:-1])
        #houd per auteur bij op welk uur een bericht is geplaatst
        nachtkastleden[author]['tijden'][time]+=1
        #houd bij voor iedereen wat de dag is met de meeste berichten en op welk uur er het meest gepost werd
        if(not(date in dates)):
            dates[date]=1
        else:
            dates[date]+=1
        times[time]+=1

        #houd per auteur bij hoevaak hij een woord heeft gebruikt    
        for word in cleanPostTokens:
            if(not(word in nachtkastleden[author]['woordenlijst'])):
                nachtkastleden[author]['woordenlijst'][word] = 1
            else:
                nachtkastleden[author]['woordenlijst'][word] += 1
            #houd bij voor iedereen wat de meest populaire woorden zijn
            if(not(word in woordenboek)):
                woordenboek[word] = 1;
            else:
                woordenboek[word]+=1

#sorteer de woorden-frequentielijst, (optioneel datum en tijdenfrequentielijst) op basis van frequentie met de meest frequente woorden als eerst (reverse=True)
woordenboek = sorted(woordenboek.items(), key=operator.itemgetter(1),reverse=True)
#dates = sorted(dates.items(), key=operator.itemgetter(1),reverse=True)
#times = sorted(times.items(), key=operator.itemgetter(1),reverse=True)

#maak (als ie nog niet bestaat) de map 'leden' aan
dir = 'leden/'
if not os.path.exists(dir):
    os.makedirs(dir)
#maak voor elke lid een nieuw txt bestand aan met de gegevens erin
for lid in nachtkastleden:
    file = open(dir+str(lid)+".txt",'a')
    nachtkastleden[lid]['percentage zinnen van het totaal'] = round((nachtkastleden[lid]['zinnen']/lines)*100,2)
    nachtkastleden[lid]['aantal woorden per zin'] = round(nachtkastleden[lid]['woorden']/nachtkastleden[lid]['zinnen'],2)
    nachtkastleden[lid]['woordenlijst'] = sorted(nachtkastleden[lid]['woordenlijst'].items(), key=operator.itemgetter(1),reverse=True)
    #nachtkastleden[lid]['tijden'] = sorted(nachtkastleden[lid]['tijden'].items(), key=operator.itemgetter(1),reverse=True)
    file.write('zinnen: ')
    json.dump(nachtkastleden[lid]['zinnen'],file)
    file.write('\n')
    file.write('percentage zinnen van het totaal: ')
    json.dump(nachtkastleden[lid]['percentage zinnen van het totaal'],file)
    file.write('\n')
    file.write('frequenties/tijd: ')
    json.dump(nachtkastleden[lid]['tijden'],file)
    file.write('\n')
    file.write('woorden: ')
    json.dump(nachtkastleden[lid]['woorden'],file)
    file.write('\n')
    file.write('aantal woorden per zin: ')
    json.dump(nachtkastleden[lid]['aantal woorden per zin'],file)
    file.write('\n')
    file.write('woordenlijst: ')
    file.write('\n')
    for woord in nachtkastleden[lid]['woordenlijst']:
        json.dump(woord,file)
        file.write('\n')
#maak ook een bestand 'woordenlijst aan, die de algemene statistieken bevat'
file = open(dir+'woordenlijst.txt','w+')
file.write('datums: ')
json.dump(dates,file)
file.write('\n')
file.write('tijden: ')
json.dump(times,file)
file.write('\n')
file.write('woordenboek: ')
file.write('\n')
for woord in woordenboek:
        json.dump(woord,file)
        file.write('\n')
print('Done')
    
   


