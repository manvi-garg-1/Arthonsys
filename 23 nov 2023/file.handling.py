'''2. File I/O:
   - Understanding file handling in Python.
   - Reading, writing, and appending data to text files.
   - Handling different file formats like CSV, JSON.'''

#file create through file handling
#text file
#write
f=open('myfile.txt','w')
f.write('hello my name is manvi garg\n')
f.write('i am a student\n')
f.close()

#read
f=open('myfile.txt','r')
print(f.read())
f.close()

#append
f=open('myfile.txt','a')
f.write('hello manvi')
f.close()


#csv file
#write
import csv
data=[["SNo", "Name", "Age"],
           [1, "manvi", "23"],
           [2, "neha", "22"],
          [3, "dipti", "20"]]
with open('file.csv', 'w', newline='') as file:
    w1 = csv.writer(file)
    w1.writerows(data)

#read
with open('file.csv','r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        print(lines[1])
  #print(file.readlines())
file.close()

#append
with open('file.csv','a') as file:
    writer=csv.writer(file)
    writer.writerow([4,'nidhi',25])
    file.close()


#json file
#write
import json
list1=['manvi','nidhi','deeksha','preeti','neha']
with open('json_demo.json','w') as f:
  json.dump(list1,f)


#read
with open('json_demo.json','r') as f:
  d=json.load(f)
  print(d)
f.close()


#append
with open('json_demo.json','a') as f:
  json.dump([1,2,3,4], f)
f.close()
