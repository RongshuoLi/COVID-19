fileobj = open("test.csv","r")
datalist = fileobj.readlines()
fileobj.close()
#print(datalist)
for country is datalist:
    #print(country)
    templist = country.split(",")
    pname = templist[2]
    cname = templist[3]
    lat = templist[5]
    lon = templist[6]
    conf = templist[7]
    #print(pname + cname + lat + lon + conf)
    conflist.append({"panme":pname,"canme":cname,"lat":lat,"lon":lon,"conf":conf})

#prist(conflist)
conflist.sort(key=lambda s:s["conf"],reverse=True)
fileout = open("test.js","w")
fileout.write("data = " + str(conflist))
fileout.close()
    
