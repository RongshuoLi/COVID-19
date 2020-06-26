  
fileobj = open("06-15-2020.csv","r") # r,w or a are the options
delfirst = fileobj.readline()
datalist = fileobj.readlines()
fileobj.close()
#print(datalist)

conflist = []
for country in datalist:
    #print(country)
    templist = country.split(",")
    pname = templist[2]
    cname = templist[3]
    lat = templist[5]
    lon = templist[6]
    conf = int(templist[7])
    #print(pname + cname + lat + lon + conf)
    conflist.append({"pname":pname,"cname":cname,"lat":lat,"lon":lon,"conf":conf})

#print(conflist)
conflist.sort(key=lambda s: s['conf'], reverse=True)
fileout = open("06-15-2020.js","w")
fileout.write("data = " + str(conflist))
fileout.close()
