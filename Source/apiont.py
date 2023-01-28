from owlready2 import *


def uploadInstance(maltype,sha,ontology):
    upmal = ontology.search_one(label = maltype)(sha)
    upmal.sha.append(sha)
    return True


# def exploreClass(classes):
#     j = 0
#     for i in classes:
#         print("["+str(j)+"]"+str(i.label))
#         j+=1

#     choice = int(input())
#     if choice < 0 or choice > len(classes)-1:
#         print("\nScelta non valida\n")
#         return
#     sublist = list(classes[choice].subclasses())
#     if len(sublist) == 0:
#         return classes[choice]    
#     else:
#         exploreClass(sublist)

def exploreClass(classes):
    sublist = list(classes[choice].subclasses())
    if len(sublist) == 0:
        return classes[choice]    

    j = 0
    for i in classes:
        print("["+str(j)+"]"+str(i.label))
        j+=1

    choice = int(input())
    if choice < 0 or choice > len(classes)-1:
        print("\nScelta non valida\n")
        return
    else:
        exploreClass(sublist)

def choosePropAndOb(ontology):
    list_prop = list(ontology.object_properties())
    j=0
    for i in list_prop:
        print("["+str(j)+"]"+str(i.label))
        j+=1
    choice = int(input())
    if choice < 0 or choice > len(list_prop)-1:
        print("\nScelta non valida\n")
        return
    prop = list_prop[choice]
    classes = prop.range
    classes = classes[0].subclasses()
    classes = list(classes)
    object=exploreClass(classes)
    return prop,object
