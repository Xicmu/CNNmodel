f1 = open('xy.txt',"r")
f2 = open('xz.txt',"r")
f3 = open('yz.txt',"r")
dict={}
count1 = 0
count2 = 0
count3 = 0
while 1:
        line = f1.readline()
        if not line:
                break
        else:
                name,status = line.split()
                dict[name[0:4]] = 0
                if status=="disease":
                        dict[name[0:4]] = dict[name[0:4]]+1
                        count1 = count1+1
while 1:
        line = f2.readline()
        if not line:
                break
        else:
                name,status = line.split()
                if status=="disease":
                       dict[name[0:4]] = dict[name[0:4]]+1
                       count2 = count2+1
while 1:
        line = f3.readline()
        if not line:
                break
        else:
                name,status = line.split()
                if status=="disease":
                        dict[name[0:4]] = dict[name[0:4]]+1
                        count3 = count3+1

count_disease = 0
count_healthy = 0
for (name,value) in dict.items():
        if value==2 or value==3:
                count_disease = count_disease+1
                print(name+':disease'+'  ' +str(value))
        else:
                count_healthy = count_healthy+1
                print(name+':healthy'+'  ' +str(value))

print('disease count:')
print(count_disease)
print('healthy count:')
print(count_healthy)
f1.close()
f2.close()
f3.close()
