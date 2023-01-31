import apiont as ont
import glob as gl
import re
ontology = ont.loadOntology(gl.ONTPATH)

listclass =list(ontology.classes())

for i in listclass:
    if i.isDefinedBy:
        i.isDefinedBy = str(i.isDefinedBy).replace("[","")
        i.isDefinedBy = str(i.isDefinedBy).replace("]","")
        i.isDefinedBy = str(i.isDefinedBy).replace("\'","")
        i.isDefinedBy = str(i.isDefinedBy).replace("\"","")

                
for i in listclass:
    if i.isDefinedBy:
        print(i.isDefinedBy)



ontology.save(gl.ONTPATH,format="rdfxml")