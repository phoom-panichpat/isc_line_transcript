import re 
import csv

output = []
        
with open("output.csv","w") as output_file:
    fieldnames = ['date','line_id','items','assign_no', 'detail']
    writer = csv.DictWriter(output_file,fieldnames=fieldnames)
    
    
    
    with open("output.txt") as file1:
        line_dict = {'date': '','line_id':'','items':'','assign_no':'', 'detail':''}
    
        for f in file1:
            line = f.replace('\t',' ')
            
            
            
            if line == '\n' or re.search('รูป', line):
                pass
            
            elif re.search(r"20[0-9][0-9].[0-1][0-9].[0-3][0-9] วัน",line):
                line_dict['date'] = line.strip('\n')
            
            elif re.search(r"^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]", line):
                line_list = line.split(' ')
                line_dict['line_id'] = line_list[1]
                
                for i,l in enumerate(line_list):
                    if re.search(r"[1-9][0-9][0-9][0-9a-zA-Z][0-9]{6}",l):
                        line_dict['assign_no'] = re.search(r"[1-9][0-9][0-9][0-9a-zA-Z][0-9]{6}",l).group()
                        
                    if re.search(r'เบิก',l):
                        line_dict['items'] = ' '.join(line_list[i:len(line_list)]).replace('\n','')
                        print(line_dict['items'])
                        
                    line_dict['detail'] = ' '.join(line_list).replace(',',' ').replace('\n','')
                        
         
            else:
                pass
                
            if line_dict['assign_no'] != '': 
                writer.writerow(line_dict)
            else:
                pass
            
            print(line_dict)
            line_dict['line_id'] = ''
            line_dict['assign_no'] = ''
            line_dict['detail'] = ''
            line_dict['items'] = ''
