import os
import json


def load_json_schema(filename: str):
    schema_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                               'schemas', filename)
    with open(schema_path) as schema:
        return json.loads(schema.read())
