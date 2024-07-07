def LoadObj(fileName):
    data = open(fileName, "r", encoding="utf-8")
    
    dataDict = {"Vertices":[], "Vertex Textures":[], "Vertex Normals":[], "Faces":[]}

    while 1:
        read = data.readline()
        readlen = len(read)
        prefix = read[0:2]
        partlist = []
        
        for i in range(readlen):
            if read[i] == ' ' or read[i] == '/':
                partlist.append(i)
        
        if prefix == 'v ':
            vertex = []
            
            vertex.append(float(read[partlist[0]+1:partlist[1]]))
            vertex.append(float(read[partlist[1]+1:partlist[2]]))
            vertex.append(float(read[partlist[2]+1:-1]))
            
            dataDict["Vertices"].append(vertex)
            
        elif prefix == 'vt':
            vertexTexture = []
            
            vertexTexture.append(float(read[partlist[0]+1:partlist[1]]))
            vertexTexture.append(float(read[partlist[1]+1:-1]))
            
            dataDict["Vertex Textures"].append(vertexTexture)
            
            
        elif prefix == 'vn':
            vertexNormal = []
            
            vertexNormal.append(float(read[partlist[0]:partlist[1]]))
            vertexNormal.append(float(read[partlist[1]+1:partlist[2]]))
            vertexNormal.append(float(read[partlist[2]+1:-1]))
            
            dataDict["Vertex Normals"].append(vertexNormal)


        elif prefix == 'f ':
            facevals = []
            partlist.append(-1)
            for p in range(4):
                facevallist = []
                for n in range(3):
                    facevallist.append(int(read[partlist[p*3+n]+1:partlist[p*3+n+1]]))
                facevals.append(facevallist)
            
            dataDict["Faces"].append(facevals)
            

        elif prefix == "":
            return dataDict
