import json
import WordnikBase

class DisceResults():

    data = [ { 'Hola' : 'Hello', 'Hoi' : 'Hello', 'noun' : 'hello' } ]

    json_encoded = json.dumps(data)

    encoded_data = json.loads(json_encoded)

    print encoded_data