import re

def f_get_model(l):

    if re.search(r'[pP][aA][sS][sS][bB][oO][oO][kK]',l) or re.search(r'[cC][oO][mM][pP][uU]-?[pU][rRtT][iI][nN][tT]',l) or re.search(r'[sS][pP]40',l) or re.search(r'RHS-S[0-9][0-9]-[0-9]{6}',l):
        model_output = 'PASSBOOK'
                        
    elif re.search(r'[nN][eE][wW][tT][oO][nN]-? ?[3]',l) or re.search(r'[nN][tT]-?3',l):
        model_output = 'NT3'

    elif re.search(r'[pP][a-zA-Z][0-9][0-9][0-9][0-9]',l) or re.search(r'[nN][eE][wW][tT][oO][nN] ?-?\+?[vV]',l) or re.search(r'นิวตั้นวี',l):
        model_output = 'NTV'
        
    elif re.search(r'[nN][eE][wW][tT][oO][nN]-? ?[aA]',l):
        model_output = 'NTA'
        
    elif re.search(r'[kK]303',l) or re.search(r'[kK][uU][pP][pP][uU]',l):
        model_output = 'KUPPU'

    elif re.search(r'[kK]2',l):
        model_output = 'K2'
        
    elif re.search(r'[cC][sS]-?610',l):
        model_output = 'CS610'
        
    elif re.search(r'[jJ][bB]-?3008[fF]+',l) or re.search(r' 161[0-9]{5} ',l):
        model_output = 'JB-3008F+'
            
    elif re.search(r'[jJ][bB]-?3008[fF]',l) or re.search(r' 881[0-9]{5} ',l):
        model_output = 'JB3008F'
        
    elif re.search(r'[jJ][bB]-?3008',l):
        model_output = 'jb3008'
        
    elif re.search(r'[jJ][bB]4001',l) or re.search(r'1809[0-9]{4} ',l):
        model_output = 'JB4001'

    elif re.search(r'CM-?5500S',l):
        model_output = 'CM-5500S'
    
    elif re.search(r'[aA][kK][eE][bB][oO][nN][oO]',l) or re.search(r'[sS][pP]-?757',l):
        model_output = 'AKEBONO'
    
    elif re.search(r'[cC]?[mM]?-? ?800[hH]\(?[uU][vV]\)?',l):
        model_output = 'CM800HUV'
    
    elif re.search(r'323[0-9]{5}',l):
        model_output = 'CM800H-DC'
        
    elif re.search(r'324[0-9]{5}',l):
        model_output = 'CM800H-DC-2microswitch'
        
    elif re.search(r'[cC]?[mM]?-? ?800[hH]',l) or re.search(r'31[7-9][0-9]{5}',l):
        model_output = 'CM800H'
    
    elif re.search(r'[nN]-? ?120',l):
        model_output = 'N-120'
    
    elif re.search(r'[nN]-? ?132[aA]',l):
        model_output = 'N-132A'
    
    # 132 == 132a ???
    elif re.search(r'[nN]-? ?132',l):
        model_output = 'N-132'
    
    elif re.search(r'[sS][cC][rR]-? ?3310',l):
        model_output = 'SCR'
    
    elif re.search(r'S?m?a?r?t? ?C?ard Reader',l):
        model_output = 'Card Reader'
    
    elif re.search(r'S6 Lite',l):
        model_output = 'S6 Lite'
        
    elif re.search(r'[mM][aA][gG][nN][eE][tT][iI][cC][sS][tT][rR][iI][pP][eE]',l) or re.search(r'[sS][cC]-? ?206',l):
        model_output = 'SC206'
    
    
    else:
        model_output = ''
    
    return model_output



