
str1=input("Enter the class name : ")
res = g.query(
    f"""
    SELECT ?label ?definition ?super (GROUP_CONCAT(?alt; separator=", ") AS ?altLabels)
    WHERE {{
        ?law rdfs:label "{str1}" .
        ?law rdfs:label ?label .
        ?law skos:definition ?definition .
        OPTIONAL {{?law skos:altLabel ?alt .}}
        OPTIONAL {{?law rdfs:subClassOf ?supe .}}
        OPTIONAL {{?supe rdfs:label ?super .}}
    }}
    GROUP BY ?label
    """
    # f"""
    # SELECT ?super ?label ?alt ?definition
    # WHERE {{
    #     ?law rdfs:label "{str1}" .
    #     ?law rdfs:label ?label .
    #     ?law skos:definition ?definition .
    #     ?law skos:altLabel ?alt
    #     OPTIONAL {{?law rdfs:subClassOf ?supe .}} .
    #     OPTIONAL {{?supe rdfs:label ?super.}} .
    # }}
    # """
)

# Convert the results to a list of tuples with plain Python data types

for row in res:

    list_alt=str(row.altLabels).split(", ")
    
    alt_string=""
    for s in list_alt:
        alt_string=alt_string+s+"\n"
result_tuples = [(str(row.label), str(row.definition),alt_string,str(row.super)) for row in res]
