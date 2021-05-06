# -*- coding: utf-8 -*-
"""
Created on Mon May  3 00:17:59 2021

@author: micha
"""
import json

    #file=input("enter file")
def readfile():
    file=open('whatsapp.txt',encoding="utf8")
    dict1(file)
    



def dict1(file) :
    # file=open('whatsapp.txt',encoding="utf8")
    dict_id=dict()
    message=dict()
    metadata=dict()
    AllDict=dict()
    Teams=list()
    count=1
    firstRow=file.readline()
    for line in file:
        index1 = line.find('-')
        if(line[1] == "." or line[2] == "."):
            result = line[index1+1::] 
                # print(result)
            index3 = result.find(':')
            if(index3>0):
                result2 = result[0:index3]
                    # print(result2)
                if not dict_id.get(result2):   #אם אין ערך של ריזולט 2 במילון שלי אז תיתן לו count
                    dict_id[result2]=count
                    count=count+1
                message['datetime']=line[0:index1-1]
                message['id']=dict_id[result2]
                message['text']=result[index3+1::].strip() 
                Teams.append(message.copy())
        else:
            Teams.pop()
            message["text"]=(message["text"]+ " " + line).strip()
            Teams.append(message.copy())
        IndexGroup=line.find('קבוצה')
        IndexStop=line.find('נוצרה')
        if(IndexGroup>0):
            NameOfGroup=line[IndexGroup+7:IndexStop-2]
            metadata['chat_name']= NameOfGroup
            metadata['creator']=(line[IndexStop+13::]).strip()
    metadata['creation_date'] = firstRow[0:index1-1] 
    metadata['num_of_participants']=len(dict_id)
    AllDict['messages']=Teams
    AllDict['metadata']=metadata
    
    file_json=NameOfGroup+".txt"
    with open(file_json,'w',encoding='utf8') as file_json:
        json.dump(AllDict,file_json,ensure_ascii=False,indent=4)    
        

# dict1()
readfile()










