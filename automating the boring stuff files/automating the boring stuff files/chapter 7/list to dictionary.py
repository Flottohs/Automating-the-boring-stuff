listz = ['train','crain','brain','train']
dictionaryz = {}




def listtodict():
    for _ in range(len(listz)):
        
        jistvalue = listz[_]
        if jistvalue in dictionaryz:
            
            dictionaryz[jistvalue] += 1
        else:
            dictionaryz[jistvalue] = 1
    print( dictionaryz)
            
    
    
    
    
    
    
    
    
    
    
    
listtodict()