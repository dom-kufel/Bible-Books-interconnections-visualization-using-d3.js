import csv
import collections

lista2=[]
lista1=[]
lista=[lista1,lista2]
csv_reader = csv.reader(open("bible.csv"), delimiter=" ")
f=open("new.txt", 'w')
for row in csv_reader:
    for foo in row:
            comma=foo.split(".")
            
            comment=comma[2].split(",")
            #print comma[0],comment[1]
            f.write(comma[0])
            f.write(",")
            f.write(comment[1])
            f.write("\n")
            lista1.append(comma[0])
            lista2.append(comment[1])
print lista1[0]
print lista2[0]            
f.close()
if len(lista1)!=len(lista2):
    print "WARNING"
liscior=[]
for i in lista1:
    if i not in liscior:
        liscior.append(i)
print liscior


Gen=[]
listalist=[ [] for it in xrange(len(liscior)+1) ]
j=0
licznik=0
#stad numeracja ksiag w j od 1
for i in range(len(lista1)):
    if lista1[i]!=lista1[i-1]:
        j+=1
        licznik=0
    listalist[j].append(lista2[i])
    licznik+=1    
#print listalist[1]
filer=open("newest.json",'w')
filer.write("{")
filer.write("\n")
filer.write('"nodes"')
filer.write(":[")
filer.write("\n")
fread=list(csv.reader(open("dane.csv"),delimiter=","))
gread=list(csv.reader(open("linki.csv"),delimiter=","))
for j in range(0,len(listalist)-1):
    
    filer.write("{")
    filer.write('"name"')
    filer.write(":")
    filer.write('"')
    filer.write(liscior[j])
    filer.write('"')
    filer.write(",")
    filer.write('"group"')
    filer.write(":")
    filer.write(str(j))
    filer.write(",")
    filer.write('"size"')
    filer.write(":")
    filer.write(str(fread[j][0]))
    filer.write(",")
    filer.write('"wiki"')
    filer.write(":")
    filer.write('"')
    filer.write(str(gread[j][0]))
    filer.write('"')    
    filer.write("},")
    filer.write("\n")
    #print liscior[j]
    
filer.write("],")
filer.write("\n")
filer.write('"links"')
filer.write(":[")
filer.write("\n")

#dopisac funkcje ktora bedzie przerzucala na nody
for j in range(0,len(listalist)-1):
    cnt=collections.Counter()
    for word in listalist[j]:
        cnt[word] +=1
    level=list(cnt.items())
    #try:    
    poziom=15
    if len(level)-1<poziom:
        wartosc=len(level)-1
    else:
        wartosc=poziom
    for i in range(wartosc):
        #print level,level[1][0]
        filer.write("{")
        filer.write('"source"')
        filer.write(":")
        filer.write(str(j))
        filer.write(",")
        filer.write('"target"')
        filer.write(":")
        filer.write(str(liscior.index(level[i][0])))
        filer.write(",")
        filer.write('"value"')
        filer.write(":")
        filer.write(str(level[i][1]))
        print liscior.index(level[i][0]),level[i][1]
        filer.write(",")        
        filer.write('"group"')
        filer.write(":")
        filer.write("1")
        filer.write("},")
        filer.write("\n")
        
        #print cnt
    print "\n" 
    #except:
    #    pass

filer.write("\n")
filer.write("]")
filer.write("\n")
filer.write("}")

#chronologiczna koljenosc, to rozny kolor,
#albo rozdziel na kolory NT i ST ^ da sie polaczyc
#im wiecej polaczen miedzy soba tym wieksze
#dobrac sily
#skierowany graf
#albo dlugosc ksiazki jako wielkosc
