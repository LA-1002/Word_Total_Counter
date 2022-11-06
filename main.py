import json
wordList = []

def WordCounter():
    with open('INPUT.txt','r',encoding='utf-8') as lines:
        for line in lines:
            spl = line.replace('\n','').split(' ');
            for w in spl:
                found = False;
                w =  w.upper().replace('.','').replace('?','').replace('!','').replace(',','')
                for i in range(len(wordList)):
                    if wordList[i]['Word'] == w.upper():
                        wordList[i]['Count'] = wordList[i]['Count']+1
                        found = True
                if found == False:
                    wordList.append({
                        'Word':w.upper(),
                        'Count':1
                    });
        for i in range(len(wordList)):
            if wordList[i]['Word'] == "":
                wordList.pop(i)
                break
        sortList = sorted(wordList,key=sort_key)
        sortList.reverse();

        
        with open('Output.json','w') as out:
            json.dump(sortList,out);

def sort_key(list):
    return list['Count']



if __name__ == '__main__':
    WordCounter();
