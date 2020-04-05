import os
import math
from PIL import Image
from PIL import ImageColor
dir = "disease"
list  = os.listdir(dir)

def create():
    im = Image.new('RGB',(200,200))
    for x in range(200):
        for y in range(200):
            im.putpixel((x,y),ImageColor.getcolor('black','RGBA'))
    return im
def charged(aminoacid_name):
    if aminoacid_name == 'ARG'or aminoacid_name == 'LYS'or aminoacid_name == 'ASP'or aminoacid_name == 'GLU':
        return 1
    else:
        return 0

def polar(aminoacid_name):
    if aminoacid_name == 'GLN'or aminoacid_name == 'ASN'or aminoacid_name == 'HIS'or aminoacid_name == 'SER'or aminoacid_name == 'THR'or aminoacid_name == 'TYR'or aminoacid_name == 'CYS'or aminoacid_name == 'MET'or aminoacid_name == 'TRP':
        return 1
    else:
        return 0

def aromatic(aminoacid_name):
    if aminoacid_name == 'TYR'or aminoacid_name == 'TRP'or aminoacid_name == 'PHE':
        return 1
    else:
        return 0

def aliphatic(aminoacid_name):
    if aminoacid_name == 'ALA'or aminoacid_name == 'ILE'or aminoacid_name == 'LEU'or aminoacid_name == 'VAL':
        return 1
    else:
        return 0

def acidic(aminoacid_name):
    if aminoacid_name == 'ASP'or aminoacid_name == 'GLU':
        return 1
    else:
        return 0


def basic(aminoacid_name):
    if aminoacid_name == 'ARG'or aminoacid_name == 'LYS'or aminoacid_name == 'HIS':
        return 1
    else:
        return 0

def neutral(aminoacid_name):
    if aminoacid_name == 'ARG'or aminoacid_name == 'LYS'or aminoacid_name == 'ASP'or aminoacid_name == 'GLU'or aminoacid_name == 'HIS':
        return 0
    else:
        return 1

for filename in list:
    print(filename)
    f = open('disease/'+ filename,"r")
    line = f.readline()
    span = line.split()
    data = []
    x1 = []
    y1 = []
    z1 = []
    r1 = []
    theta1 = []
    fai1 = []
    known = []
    aminoacid = []

    while 'ATOM'not in span[0]:
        line = f.readline()
        span = line.split()
    span = line.split()
    if 'CA'== span[2]:#1号如果是CA
        x = eval(line[30:38])
        y = eval(line[38:46])
        z = eval(line[46:54])
        index = span[1]
        aminoacid.append(span[3])
        r = (x*x+y*y+z*z)**0.5
        theta = math.acos(z/r)/math.pi*180
        if x>0 and y>0:
            fai = math.atan(y/x)/math.pi*180
        elif x>0 and y<0:
            fai = 360 + math.atan(y/x)/math.pi*180
        else:
            fai = 180 + math.atan(y/x)/math.pi*180
        theta = int(theta)
        fai = int(fai)
        #ca.write(index+' '+str(x)+' '+str(y)+' '+str(z)+' '+str(r)+' '+str(theta)+' '+str(fai)+'\n')
        data.append(index)
        known.append(1)
        x1.append(x)
        y1.append(y)
        z1.append(z)
        theta1.append(theta)
        r1.append(r)
        fai1.append(fai)



    while 'CONECT'not in span[0] and 'MASTER'not in span[0]:
        line = f.readline()
        span = line.split()
        if 'ATOM'==span[0] and 'CA'== span[2]:
            x = eval(line[30:38])
            y = eval(line[38:46])
            z = eval(line[46:54])
            index = span[1]
            aminoacid.append(span[3])
            r = (x*x+y*y+z*z)**0.5
            theta = math.acos(z/r)/math.pi*180
            if x>0 and y>0:
                fai = math.atan(y/x)/math.pi*180
            elif x>0 and y<0:
                fai = 360 + math.atan(y/x)/math.pi*180
            elif x<0:
               fai = 180 + math.atan(y/x)/math.pi*180
            theta = int(theta)
            fai = int(fai)
            #ca.write(index+' '+str(x)+' '+str(y)+' '+str(z)+' '+str(r)+' '+str(theta)+' '+str(fai)+'\n')
            data.append(index)
            known.append(1)
            x1.append(x)
            y1.append(y)
            z1.append(z)
            theta1.append(theta)
            r1.append(r)
            fai1.append(fai)
    minx = min(x1)
    miny = min(y1)
    minz = min(z1)
    maxx = max(x1)
    maxy = max(y1)
    maxz = max(z1)
    for i in range(len(x1)):
       x1[i] = (x1[i]-minx)/(maxx-minx)*195
       y1[i] = (y1[i]-miny)/(maxy-miny)*195
       z1[i] = (z1[i]-minz)/(maxz-minz)*195

    for i in range(0,len(data)):
        for j in range(i+1,len(data)):
            if(theta1[i]==theta1[j]and fai1[i]==fai1[j]):
                if(r1[i]<r1[j]):
                    known[i] = 0
                else:
                    known[j] = 0

    '''ca1 = create()
    for i in range(0,len(known)):
        if known[i]==1:
            ca1.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(255,255,255))
    ca1.save('CA.png')'''

    ca1 = create()
    ca2 = create()
    ca3 = create()

    ca4 = create()
    ca5 = create()
    ca6 = create()

    ca7 = create()
    ca8 = create()
    ca9 = create()
    '''for i in range(0,10):
        if known[i]==1 and charged(aminoacid[i])==1:
            ca2.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(255,255,255))
    #ca2.save(filename[0:4]+'charged.png')

    #ca3 = create()
    for i in range(0,len(known)):
        if known[i]==1 and polar(aminoacid[i])==1:
            ca3.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(255,255,255))
    #ca3.save(filename[0:4]+'polar.png')

    #ca4 = create()
    for i in range(0,len(known)):
        if known[i]==1 and aromatic(aminoacid[i])==1:
            ca4.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(255,255,255))
    #ca4.save(filename[0:4]+'aromatic.png')

    #ca5 = create()
    for i in range(0,len(known)):
        if known[i]==1 and aliphatic(aminoacid[i])==1:
            ca5.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(255,255,255))
    #ca5.save(filename[0:4]+'aliphatic.png')

    #ca6 = create()
    for i in range(0,len(known)):
        if known[i]==1 and acidic(aminoacid[i])==1:
            ca6.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(255,255,255))
    #ca6.save(filename[0:4]+'acidic.png')

    #ca7 = create()
    for i in range(0,len(known)):
        if known[i]==1 and basic(aminoacid[i])==1:
            ca7.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(255,255,255))'''
    #ca7.save(filename[0:4]+'basic.png')

    #ca8 = create()
    for i in range(0,len(known)):
        if known[i]==1:
            if acidic(aminoacid[i])==1:
                ca1.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(255,255,255))#负电用白色,xy投影
                ca4.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(255,255,255))
                ca7.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(255,255,255))
                '''ca1.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)+200),(255,255,255))#xz
                ca1.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)+400),(255,255,255))#yz'''
            elif basic(aminoacid[i])==1:
                ca1.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(170,170,170))#正电用灰色
                ca4.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(170,170,170))
                ca7.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(170,170,170))
                '''ca1.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)+200),(170,170,170))#xz
                ca1.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)+400),(170,170,170))#yz'''
            else:
                ca1.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(85,85,85))#中性用灰色
                ca4.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(85,85,85))
                ca7.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(85,85,85))
                '''ca1.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)+200),(85,85,85))#xz
                ca1.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)+400),(85,85,85))#yz'''
 
    for i in range(0,len(known)):
        if known[i]==1:
            if aromatic(aminoacid[i])==1:
                ca2.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(255,255,255))#芳香
                ca5.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(255,255,255))
                ca8.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(255,255,255))
                '''ca1.putpixel((int(x1[i]+0.5)+200,int(z1[i]+0.5)+200),(255,255,255))#xz
                ca1.putpixel((int(y1[i]+0.5)+200,int(z1[i]+0.5)+400),(255,255,255))#yz'''
            if aliphatic(aminoacid[i])==1:
                ca2.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(85,85,85))#脂肪
                ca5.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(85,85,85))
                ca8.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(85,85,85))
                '''ca1.putpixel((int(x1[i]+0.5)+200,int(z1[i]+0.5)+200),(85,85,85))#xz
                ca1.putpixel((int(y1[i]+0.5)+200,int(z1[i]+0.5)+400),(85,85,85))#yz'''

    #ca9 = create()
    #ca10 = create()
    for i in range(0,len(known)):
        if known[i]==1:
            if aminoacid[i]=='ALA':
                '''ca1.putpixel((int(x1[i]+0.5)+400,int(y1[i]+0.5)),(205,205,205))
                ca1.putpixel((int(x1[i]+0.5)+400,int(z1[i]+0.5)+200),(205,205,205))
                ca1.putpixel((int(y1[i]+0.5)+400,int(z1[i]+0.5)+400),(205,205,205))'''
                ca3.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(116,116,116))
                ca6.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(116,116,116))
                ca9.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(116,116,116))
            if aminoacid[i]=='CYS':
                '''ca1.putpixel((int(x1[i]+0.5)+400,int(y1[i]+0.5)),(184,184,184))
                ca1.putpixel((int(x1[i]+0.5)+400,int(z1[i]+0.5)+200),(184,184,184))
                ca1.putpixel((int(y1[i]+0.5)+400,int(z1[i]+0.5)+400),(184,184,184))'''
                ca3.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(96,96,96))
                ca6.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(96,96,96))
                ca9.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(96,96,96))
            if aminoacid[i]=='ASP':
                '''ca1.putpixel((int(x1[i]+0.5)+400,int(y1[i]+0.5)),(106,106,106))
                ca1.putpixel((int(x1[i]+0.5)+400,int(z1[i]+0.5)+200),(205,205,205))
                ca1.putpixel((int(y1[i]+0.5)+400,int(z1[i]+0.5)+400),(205,205,205))'''
                ca3.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(255,255,255))
                ca6.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(255,255,255))
                ca9.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(255,255,255))
            if aminoacid[i]=='GLU':
                '''ca1.putpixel((int(x1[i]+0.5)+400,int(y1[i]+0.5)),(117,117,117))
                ca1.putpixel((int(x1[i]+0.5)+400,int(z1[i]+0.5)+200),(117,117,117))
                ca1.putpixel((int(y1[i]+0.5)+400,int(z1[i]+0.5)+400),(117,117,117))'''
                ca3.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(255,255,255))
                ca6.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(255,255,255))
                ca9.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(255,255,255))
            if aminoacid[i]=='PHE':
                '''ca1.putpixel((int(x1[i]+0.5)+400,int(y1[i]+0.5)),(243,243,243))
                ca1.putpixel((int(x1[i]+0.5)+400,int(z1[i]+0.5)+200),(243,243,243))
                ca1.putpixel((int(y1[i]+0.5)+400,int(z1[i]+0.5)+400),(243,243,243))'''
                ca3.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(36,36,36))
                ca6.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(36,36,36))
                ca9.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(36,36,36))
            if aminoacid[i]=='GLY':
                '''ca1.putpixel((int(x1[i]+0.5)+400,int(y1[i]+0.5)),(196,196,196))
                ca1.putpixel((int(x1[i]+0.5)+400,int(z1[i]+0.5)+200),(196,196,196))
                ca1.putpixel((int(y1[i]+0.5)+400,int(z1[i]+0.5)+400),(196,196,196))'''
                ca3.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(135,135,135))
                ca6.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(135,135,135))
                ca9.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(135,135,135))
            if aminoacid[i]=='HIS':
                '''ca1.putpixel((int(x1[i]+0.5)+400,int(y1[i]+0.5)),(139,139,139))
                ca1.putpixel((int(x1[i]+0.5)+400,int(z1[i]+0.5)+200),(139,139,139))
                ca1.putpixel((int(y1[i]+0.5)+400,int(z1[i]+0.5)+400),(139,139,139))'''
                ca3.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(116,116,116))
                ca6.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(116,116,116))
                ca9.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(116,116,116))
            if aminoacid[i]=='ILE':
                '''ca1.putpixel((int(x1[i]+0.5)+400,int(y1[i]+0.5)),(255,255,255))
                ca1.putpixel((int(x1[i]+0.5)+400,int(z1[i]+0.5)+200),(255,255,255))
                ca1.putpixel((int(y1[i]+0.5)+400,int(z1[i]+0.5)+400),(255,255,255))'''
                ca3.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(64,64,64))
                ca6.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(64,64,64))
                ca9.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(64,64,64))
            if aminoacid[i]=='LYS':
                '''ca1.putpixel((int(x1[i]+0.5)+400,int(y1[i]+0.5)),(67,67,67))
                ca1.putpixel((int(x1[i]+0.5)+400,int(z1[i]+0.5)+200),(67,67,67))
                ca1.putpixel((int(y1[i]+0.5)+400,int(z1[i]+0.5)+400),(67,67,67))'''
                ca3.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(255,255,255))
                ca6.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(255,255,255))
                ca9.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(255,255,255))
            if aminoacid[i]=='LEU':
                '''ca1.putpixel((int(x1[i]+0.5)+400,int(y1[i]+0.5)),(234,234,234))
                ca1.putpixel((int(x1[i]+0.5)+400,int(z1[i]+0.5)+200),(234,234,234))
                ca1.putpixel((int(y1[i]+0.5)+400,int(z1[i]+0.5)+400),(234,234,234))'''
                ca3.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(64,64,64))
                ca6.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(64,64,64))
                ca9.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(64,64,64))
            if aminoacid[i]=='MET':
                '''ca1.putpixel((int(x1[i]+0.5)+400,int(y1[i]+0.5)),(207,207,207))
                ca1.putpixel((int(x1[i]+0.5)+400,int(z1[i]+0.5)+200),(207,207,207))
                ca1.putpixel((int(y1[i]+0.5)+400,int(z1[i]+0.5)+400),(207,207,207))'''
                ca3.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(84,84,84))
                ca6.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(84,84,84))
                ca9.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(84,84,84))
            if aminoacid[i]=='ASN':
                '''ca1.putpixel((int(x1[i]+0.5)+400,int(y1[i]+0.5)),(114,114,114))
                ca1.putpixel((int(x1[i]+0.5)+400,int(z1[i]+0.5)+200),(114,114,114))
                ca1.putpixel((int(y1[i]+0.5)+400,int(z1[i]+0.5)+400),(114,114,114))'''
                ca3.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(215,215,215))
                ca6.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(215,215,215))
                ca9.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(215,215,215))
            if aminoacid[i]=='PRO':
                '''ca1.putpixel((int(x1[i]+0.5)+400,int(y1[i]+0.5)),(173,173,173))
                ca1.putpixel((int(x1[i]+0.5)+400,int(z1[i]+0.5)+200),(173,173,173))
                ca1.putpixel((int(y1[i]+0.5)+400,int(z1[i]+0.5)+400),(173,173,173))'''
                ca3.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(135,135,135))
                ca6.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(135,135,135))
                ca9.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(135,135,135))
            if aminoacid[i]=='GLN':
                '''ca1.putpixel((int(x1[i]+0.5)+400,int(y1[i]+0.5)),(110,110,110))
                ca1.putpixel((int(x1[i]+0.5)+400,int(z1[i]+0.5)+200),(110,110,110))
                ca1.putpixel((int(y1[i]+0.5)+400,int(z1[i]+0.5)+400),(110,110,110))'''
                ca3.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(143,143,143))
                ca6.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(143,143,143))
                ca9.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(143,143,143))
            if aminoacid[i]=='ARG':
                '''ca1.putpixel((int(x1[i]+0.5)+400,int(y1[i]+0.5)),(0,0,0))
                ca1.putpixel((int(x1[i]+0.5)+400,int(z1[i]+0.5)+200),(0,0,0))
                ca1.putpixel((int(y1[i]+0.5)+400,int(z1[i]+0.5)+400),(0,0,0))'''
                ca3.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(255,255,255))
                ca6.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(255,255,255))
                ca9.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(255,255,255))
            if aminoacid[i]=='SER':
                '''ca1.putpixel((int(x1[i]+0.5)+400,int(y1[i]+0.5)),(153,153,153))
                ca1.putpixel((int(x1[i]+0.5)+400,int(z1[i]+0.5)+200),(153,153,153))
                ca1.putpixel((int(y1[i]+0.5)+400,int(z1[i]+0.5)+400),(153,153,153))'''
                ca3.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(147,147,147))
                ca6.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(147,147,147))
                ca9.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(147,147,147))
            if aminoacid[i]=='THR':
                '''ca1.putpixel((int(x1[i]+0.5)+400,int(y1[i]+0.5)),(162,162,162))
                ca1.putpixel((int(x1[i]+0.5)+400,int(z1[i]+0.5)+200),(162,162,162))
                ca1.putpixel((int(y1[i]+0.5)+400,int(z1[i]+0.5)+400),(162,162,162))'''
                ca3.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(120,120,120))
                ca6.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(120,120,120))
                ca9.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(120,120,120))
            if aminoacid[i]=='VAL':
                '''ca1.putpixel((int(x1[i]+0.5)+400,int(y1[i]+0.5)),(235,235,235))
                ca1.putpixel((int(x1[i]+0.5)+400,int(z1[i]+0.5)+200),(235,235,235))
                ca1.putpixel((int(y1[i]+0.5)+400,int(z1[i]+0.5)+400),(235,235,235))'''
                ca3.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(76,76,76))
                ca6.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(76,76,76))
                ca9.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(76,76,76))
            if aminoacid[i]=='TRP':
                '''ca1.putpixel((int(x1[i]+0.5)+400,int(y1[i]+0.5)),(218,218,218))
                ca1.putpixel((int(x1[i]+0.5)+400,int(z1[i]+0.5)+200),(218,218,218))
                ca1.putpixel((int(y1[i]+0.5)+400,int(z1[i]+0.5)+400),(218,218,218))'''
                ca3.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(0,0,0))
                ca6.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(0,0,0))
                ca9.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(0,0,0))
            if aminoacid[i]=='TYR':
                '''ca1.putpixel((int(x1[i]+0.5)+400,int(y1[i]+0.5)),(182,182,182))
                ca1.putpixel((int(x1[i]+0.5)+400,int(z1[i]+0.5)+200),(182,182,182))
                ca1.putpixel((int(y1[i]+0.5)+400,int(z1[i]+0.5)+400),(182,182,182))'''
                ca3.putpixel((int(x1[i]+0.5),int(z1[i]+0.5)),(44,44,44))
                ca6.putpixel((int(x1[i]+0.5),int(y1[i]+0.5)),(44,44,44))
                ca9.putpixel((int(y1[i]+0.5),int(z1[i]+0.5)),(44,44,44))
    #ca9.save(filename[0:4]+'hydrophobic.png')
    #ca10.save(filename[0:4]+'hydrophillic.png')
    r1 = ca1.split()[0]
    g1= ca2.split()[0]
    b1 = ca3.split()[0]
    ca = Image.merge("RGB",(r1,g1,b1))
    
    r2 = ca4.split()[0]
    g2= ca5.split()[0]
    b2 = ca6.split()[0]
    cb = Image.merge("RGB",(r2,g2,b2))

    r3 = ca7.split()[0]
    g3= ca8.split()[0]
    b3 = ca9.split()[0]
    cc = Image.merge("RGB",(r3,g3,b3))
    
    ca.save("../training/dataset/CNNxz/disease_featurexz/"+filename[0:4]+'xz.jpg')
    cb.save("../training/dataset/CNNxy/disease_featurexy/"+filename[0:4]+'xy.jpg')
    cc.save("../training/dataset/CNNyz/disease_featureyz/"+filename[0:4]+'yz.jpg')
    

