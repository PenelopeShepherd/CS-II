'''
Shepherd_Penelope_File_Conversion.py

Description: Turns a file of student data into a CSV

Log: 1.0

Bugs: No bugs discovered
'''

import csv
fhand = open('student_data_cs2.txt')
with open('my_data.csv', 'w', newline='') as file:
    for line in fhand: #for each bit of information, seperate the information into catagories for the CSV
        print(line)
        ID = line[0:4]
        first_name = line[4:19].strip()
        last_name = line[21:30].strip()
        grade = line[36:42].strip()
        GPA = line[42:45].strip()
        birthday = line[48:58].strip()
        gender = line[60:66].strip()
        classrank = line[67:76].strip()
        attendence = line[76:80].strip()
        honors = line[86:93].strip()
        sports = line[93:102].strip()
        clubcount = line[102:112]

        file.write(ID + ','+ first_name + ',' + last_name +','+grade+ ','+ GPA +',' + birthday+','+gender+','+classrank+','+attendence+','+honors+','+sports+','+clubcount + '\n') #Writes the organized information into the CSV file

