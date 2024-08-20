import re

output = []

with open("output.txt","a") as output_file:
    with open("1234.txt") as file1:
        for line in file1:
            
            if line == '\n':
                pass
            
            elif re.search(r"20[0-9][0-9].[0-1][0-9].[0-3][0-9] วัน",line):
                line_strip = str(line).rstrip('\n')
                output_file.write('\n\n'+line_strip)
            
            elif re.search(r"^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]", line):
                line_strip = str(line).rstrip('\n')
                output_file.write('\n' + line_strip)
            
            else:
                output_file.write(str(line).rstrip('\n'))
        
