# app.py:

from flask import Flask, request, jsonify, render_template
from rdflib import Graph
from rdflib.namespace import RDFS

# app = Flask(__name__, static_url_path='', static_folder='static')
app = Flask(__name__)

# Load the RDF graph
# You may need to adjust the path to LMSS.owl based on its location relative to app.py
g = Graph()
g.parse("LMSS.owl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/get_node_info", methods=["POST"])
def get_node_info():
    data = request.json
    node_label = data["label"]

    # Perform SPARQL query
    query = f"""
        SELECT ?super ?label ?definition
        WHERE {{
            ?law rdfs:label ?label .
            ?law skos:definition ?definition .
            ?law rdfs:subClassOf ?supe .
            ?supe rdfs:label ?super .
            FILTER(?label = "{node_label}")
        }}
    """
    res = g.query(query)

    # Convert the results to JSON
    result_tuples = [
        {"label": str(row.label), "definition": str(row.definition), "superclass": str(row.super)}
        for row in res
    ]

    return jsonify(result_tuples)

if __name__ == "__main__":
    app.run(debug=True)
