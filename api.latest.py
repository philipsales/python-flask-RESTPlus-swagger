from flask import Flask, make_response, abort, request, jsonify, json
from flask_restplus import Api, Resource, fields, reqparse
import re
from marshmallow import Schema, fields, pprint

app = Flask(__name__)
api = Api(app, 
    version='1.0.0', 
    title='OpenRefine Reconciliation API',
    description='OpenRefine Reconciliation API',
)

class QuerySchema(Schema):
    query = fields.Str()

class QueryItemSchema(Schema):
    q0 = fields.Nested(QuerySchema())

query = dict(query='Barrack')
q0 = dict(q0=query)

schema = QueryItemSchema()
result = schema.dump(q0)
pprint(type(result))
pprint(result, indent=2)

metadatas = {
    "name" : "2020 ICD-10-CM",
    "identifierSpace" : "http://www.wikidata.org/entity/",
    "schemaSpace" : "http://www.wikidata.org/prop/direct/",
    "defaultTypes": [
        { "id": "/2020icd10cm/diagnosis_name", "name": "Diagnosis Name" },
        { "id": "/2020icd10cm/diagnosis_code", "name": "Diagnosis Code" }
        ]
    }

# The data we'll match against.
presidents = [
    "George Washington", "John Adams", "Thomas Jefferson", "James Madison",
    "James Monroe", "John Quincy Adams", "Andrew Jackson", "Martin Van Buren",
    "William Henry Harrison", "John Tyler", "James K. Polk", "Zachary Taylor",
    "Millard  Fillmore", "Franklin Pierce", "James Buchanan",
    "Abraham Lincoln", "Andrew Jackson", "Ulysses S. Grant",
    "Rutherford B. Hayes", "James A. Garfield", "Chester A. Arthur",
    "Grover Cleveland", "Benjamin Harrison", "William McKinley",
    "Theodore Roosevelt", "William Howard Taft", "Woodrow Wilson",
    "Warren G. Harding", "Calvin Coolidge", "Herbert Hoover",
    "Franklin D. Roosevelt", "Harry S. Truman", "Dwight D. Eisenhower",
    "John F. Kennedy", "Lyndon B. Johnson", "Richard Nixon", "Gerald Ford",
    "Jimmy Carter", "Ronald Reagan", "George H. W. Bush", "Bill Clinton",
    "George W. Bush", "Barack Obama",
    ]

def search(query):
    """
    Do a simple fuzzy match of US presidents, returning results in
    Refine reconciliation API format.
    """
    pattern = re.compile(query, re.IGNORECASE)
    matches = []

    for (id, name) in zip(range(0, len(presidents)), presidents):
        if pattern.search(name):
            # If the name matches the query exactly then it's a
            # (near-)certain match, otherwise it could be ambiguous.
            if name == query:
                match = True
            else:
                match = False

            matches.append({
                "id": id,
                "name": name,
                "score": 100,
                "match": match,
                "type": [
                    {"id": "/people/presidents",
                     "name": "US President"}]})

    return matches

def jsonpify(obj):
    """
    Like jsonify but wraps result in a JSONP callback if a 'callback'
    query param is supplied.
    """
    try:
        callback = request.args['callback']
        response = app.make_response("%s(%s)" % (callback, json.dumps(obj)))
        response.mimetype = "text/javascript"
        return response
    except KeyError:
        return jsonify(obj)

#@api.route('/reconcile/diagnosis/<queries>', methods=['POST', 'GET'])
@api.route('/reconcile/diagnosis/<queries>')
@api.doc(params={ 'queries': { 'description': 'queries' , 'type': 'object' } })
class Diagnosis(Resource):

    def get(self,queries):
        pprint('GET----')
        # empty queries for initialization only
        if not bool(json.loads(queries)):
            return jsonpify(metadatas)

    def post(self,queries):
        queries = request.form.get('queries')
        pprint('POST----')
        pprint(queries)

        if queries:
            queries = json.loads(queries)
            results = {}
            for (key, query) in queries.items():
                results[key] = {"result": search(query['query'])}
            return jsonpify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
    app.run(debug=True)