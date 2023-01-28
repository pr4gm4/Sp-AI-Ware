import apiont as ont
import glob as gl
import random




ontology = ont.get_ontology("/home/manuel/Scrivania/Workspace/Sp-AI-Ware/Ontologies/Sp-AI-Ware-OWL.owl").load()

list_prop = list(ontology.object_properties())

mal = ontology.Wannacry

j = 0
for i in list_prop:
    print("["+str(j)+"]"+str(i.label))
    j+=1

choice = int(input())
if choice < 0 or choice > len(list_prop)-1:
    print("\nScelta non valida\n")
    # return TODO
list_obj = list_prop[choice].range
list_obj = list(list_obj[0].subclasses())
objclass = ont.exploreClass(list_obj)
objind = objclass(str(objclass.name)+str(random.randint(0,999)))

if choice == 0:
    mal.attack_type.append(objind)
elif choice == 1:
    mal.attacks.append(objind)
elif choice == 2:
    mal.attack_type.append(objind)
elif choice == 3:
    mal.attack_type.append(objind)
elif choice == 4:
    mal.attack_type.append(objind)
elif choice == 5:
    mal.host_program.append(objind)
elif choice == 6:
    mal.attack_type.append(objind)
elif choice == 7:
    mal.attack_type.append(objind)
elif choice == 8:
    mal.attack_type.append(objind)
elif choice == 9:
    mal.attack_type.append(objind)

ontology.save(file="/home/manuel/Scrivania/Workspace/Sp-AI-Ware/Ontologies/Sp-AI-Ware-OWL.owl",format="rdfxml")