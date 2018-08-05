#! usr/bin/env python    
# coding:utf-8    
import string    
    

def de_rot13(oristr):
    upperdict = {}    
    lowerdict = {}    
    upperletters =string.ascii_uppercase  
    lowerletters =string.ascii_lowercase 
    dststr = []    

    for i in range(0,len(lowerletters)):                        
        if i<13:    
            lowerdict[lowerletters[i]] = lowerletters[i+13]    
        else:    
            lowerdict[lowerletters[i]] = lowerletters[i-13]    
        
    for i in range(0,len(upperletters)):                           
        if i<13:    
            lowerdict[upperletters[i]] = upperletters[i+13]    
        else:    
            lowerdict[upperletters[i]] = upperletters[i-13]    
        
    for ch in oristr:    
        if ch in lowerdict:    
            dststr.append(lowerdict[ch])    
        elif ch in upperdict:    
            dststr.append(upperdict[ch])    
        else:    
            dststr.append(ch)    
    dststr = ''.join(dststr)    

    return dststr