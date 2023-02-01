import apiont as ont
import graphics as gr
from SPARQLWrapper import SPARQLWrapper, JSON


def queryDbpedia(ontpath):
    
    """
        intera funzione che si occupa di interrogare l'endpoin sparql di dbpedia
        
        Args:
            filepath dell'ontologia
    """
    ontology = ont.loadOntology(ontpath)
    classes = list(ontology.classes())
    classes = [x for x in classes if x.isDefinedBy]
    while True:
        print("\nScegli l'argomento su cui vuoi avere una descrizione\n")
        j=0
        
        for i in classes:
            if i.isDefinedBy:
                print("["+str(j)+"]"+str(i.label))
                print(i.isDefinedBy)
                print()
            j+=1
        choice = gr.numericInput(0,j-1)
        gr.printSeparator()                             
        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        iri = str(classes[choice].isDefinedBy)
        iri = iri.replace("page","resource")
        iri = iri.replace("[","")
        iri = iri.replace("]","")
        iri = iri.replace("'","")
        iri = "<"+iri+">"
        query = """
        SELECT ?abstract
        WHERE {
        %s dbo:abstract ?abstract .
        FILTER (lang(?abstract) = 'it')
        }
        """%iri
        sparql.setQuery(query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        for result in results["results"]["bindings"]:
            print(result["abstract"]["value"])
        print()
        print("\nVuoi avere altre informazioni ? \n")
        choice = gr.numericInput(1,2,"\n[1]Si\n[2]No\n")
        gr.printSeparator()
        if choice ==2:
            print("\nRitorno al menu' principale\n")
            break



