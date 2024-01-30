from pymongo import MongoClient
from pymongo.errors import CollectionInvalid
from collections import OrderedDict

class Schema:
    def __init__(self, database_url, database_name, schema,col_name):
        self.client = MongoClient(database_url)
        self.db = self.client[database_name]
        self.schema = schema
        self.col_name = col_name
        #self._create_collection()

    def _create_collection(self):
        validator = {'$jsonSchema': {'bsonType': 'object', 'properties': {}}}
        required = []

        for field_key in self.schema:
            field = self.schema[field_key]
            properties = {'bsonType': field['type']}
            minimum = field.get('minlength')

            if type(minimum) == int:
                properties['minimum'] = minimum

            if field.get('required') is True:
                required.append(field_key)

            validator['$jsonSchema']['properties'][field_key] = properties

        if len(required) > 0:
            validator['$jsonSchema']['required'] = required

        collection_name = self.col_name
        try:
            self.db.create_collection(collection_name)
        except CollectionInvalid:
            assert False, "Invalid Collection"
        query = [('collMod', collection_name),
         ('validator', validator)]
        command_result = self.db.command(OrderedDict(query))

    def close_connection(self):
        self.client.close()
