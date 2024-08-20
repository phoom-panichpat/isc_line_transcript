import re
import csv
from get_model import f_get_model

output = []


def remove_emojis(data):

    emoj = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese char
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
                    "]+", re.UNICODE)
    return re.sub(emoj, '', data)

with open("output.txt","w") as output_file:
    with open("line.txt") as file1:
        for line in file1:
            print(line)
            if line == '\n':
                pass
            
            elif re.search(r"20[0-9][0-9].[0-1][0-9].[0-3][0-9] วัน",line):
                line_strip = str(line).replace('\n',' ')
                output_file.write('\n\n'+line_strip)
            
            elif re.search(r"^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]", line):
                line_strip = str(line).replace('\n',' ')
                output_file.write('\n' + line_strip)
            
            else:
                output_file.write(str(line).replace('\n',' '))



with open("output.csv","w") as output_file:
    fieldnames = ['date','line_id','items','model','destination','assign_no', 'detail']
    writer = csv.DictWriter(output_file,fieldnames=fieldnames)
    writer.writeheader()
    
    
    with open("output.txt") as file1:
        line_dict = {'date': '','line_id':'','items':'','model':'','destination':'','assign_no':'', 'detail':''}
    
        
        for f in file1:        
            line = f.replace('\t',' ').replace('=',' ').replace('เบิก',' เบิก').replace('ส่ง',' ส่ง').replace('ฝาก',' ฝาก').replace('ลง',' ลง').replace('รับเอง',' รับเอง')
            print(line)
            
            if re.search('[\U0001F6A9]',f):
                pass
            else:
                line = remove_emojis(line)

            if re.search(r"20[0-9][0-9].[0-1][0-9].[0-3][0-9] วัน",line):
                line_dict['date'] = line.strip('\n')
            
            elif re.search(r"^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]", line):
               
                # get model
                a = f_get_model(line)
                line_dict['model'] = a
                
                line_list = line.replace('\t',' ').split(' ')
                line_list = [x.strip(' ') for x in line_list]
                line_list = list(filter(None,line_list))     
                
                line_dict['line_id'] = line_list[1]            
                
                b_counter = 0
                for i,l in enumerate(line_list):                
                    # get เบิก item
                    if re.search(r'เบิก',l) or re.search('[\U0001F6A9]',l):
                        
                        if b_counter == 0:
                            b_counter += 1
                            line_dict['items'] = ' '.join(line_list[i:len(line_list)]).replace('\n','')
                        else:
                            pass
                    
                        
                    # get destination
                    if re.search("ฝาก",l) or re.search("ส่ง",l) or re.search("ลง",l) or re.search("รับเอง",l) :
                        line_dict['destination'] = ' '.join(line_list[i:len(line_list)]).replace('\n','')
                        
                        
                    
                    # prevent part id as assign id
                    if re.search(r"[1-2][0-1][0-9][0-9a-zA-Z][2-9][0-9][0-3][0-9][0-9][0-9]",line_dict['items']):
                        line_dict['assign_no'] = re.search(r"[1-2][0-1][0-9][0-9a-zA-Z][2-9][0-9][0-3][0-9][0-9][0-9]",line_dict['items']).group() + ' sn?'
                    
                    # get assign id
                    elif re.search(r"[1-2][0-1][0-9][0-9a-zA-Z][2-9][0-9][0-3][0-9][0-9][0-9]",l):
                        line_dict['assign_no'] = re.search(r"[1-2][0-1][0-9][0-9a-zA-Z][2-9][0-9][0-3][0-9][0-9][0-9]",l).group()
                     
                        
                    line_dict['detail'] = ' '.join(line_list).replace(',',' ').replace('\n',' ')
                        
         
            else:
                pass
            
            if re.search(r'[Kk][bB][Aa][Nn][Kk]',line_dict['detail']) or re.search(r'หมายเลข Service Request',line_dict['detail']):
                
                del1 = re.sub(r'หมายเลข Service Request:.*สาขา/ส่วนงาน/ทีมงาน',' ',line_dict['detail'])
                if re.search(r'ความต้องการอื่นๆ',line_dict['detail']):
                    del2 = re.sub(r'ชั้น:.*ห้อง:.*ความต้องการอื่นๆ',' ',del1)
                
                else:
                    del2 = del1
                
                line_dict['detail'] = del2
                
            
            line_dict['items'] = re.sub(r'[0-9]?[0-9]/[0-9]?[0-9]/[0-9][0-9].*','', line_dict['items'])
            line_dict['items'] = re.sub(r'@.*','', line_dict['items'])
            line_dict['items'] = re.sub(r'[Kk][bB][Aa][Nn][Kk].*','', line_dict['items'])
            line_dict['items'] = re.sub(r'ฝาก.*','', line_dict['items'])
            # ระวังฝากลงโปรแกรม
            
            line_dict['destination'] =re.sub(r'@.*','', line_dict['destination'])
            
            if re.search(r'เครื่องนอกสัญญา',line_dict['detail']) or re.search(r'เสนอราคา',line_dict['detail']) or re.search(r'อนุมัติซ่อม',line_dict['detail']):
                line_dict['items'] = line_dict['items'] + ' [เสนอราคา ไม่ต้องตัด]'
           
            
            if line_dict['detail'] != '':
                writer.writerow(line_dict)
                # print(line_dict)
           
            
            line_dict['line_id'] = ''
            line_dict['assign_no'] = ''
            line_dict['detail'] = ''
            line_dict['items'] = ''
            line_dict['destination'] = ''
            line_dict['model'] = ''
