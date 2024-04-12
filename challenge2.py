import json
from datetime import datetime

def convert_number(value):
    try:
        return float(value.strip())
    except ValueError:
        return None

def convert_string(value):
    clean_value = value.strip()
    try:
        dt = datetime.fromisoformat(clean_value.replace('Z', '+00:00'))
        return int(dt.timestamp())
    except ValueError:
        return clean_value

def convert_boolean(value):
    truthy = {"1", "t", "T", "TRUE", "true", "True"}
    falsey = {"0", "f", "F", "FALSE", "false", "False"}
    clean_value = value.strip()
    if clean_value in truthy:
        return True
    elif clean_value in falsey:
        return False
    return None  

def convert_null(value):
    truthy = {"1", "t", "T", "TRUE", "true", "True"}
    return None if value.strip() in truthy else value

def process_list(items):
    result = []
    for item in items:
        if 'N' in item:
            converted = convert_number(item['N'])
            if converted is not None:
                result.append(converted)
        elif 'BOOL' in item:
            converted = convert_boolean(item['BOOL'])
            if converted is not None:
                result.append(converted)
    return result

def transform_data(input_json):
    output = {
        "map_1": {
            "list_1": process_list(input_json['map_1']['M']['list_1']['L']),
            "null_1": convert_null(input_json['map_1']['M']['null_1']['NULL '])
        },
        "number_1": convert_number(input_json['number_1']['N']),
        "string_1": input_json['string_1']['S'].strip(),
        "string_2": convert_string(input_json['string_2']['S'])
    }
    return [output]

# Input JSON
input_json = {
  "number_1": {
    "N": "1.50"
  },
  "string_1": {
    "S": "784498 "
  },
  "string_2": {
    "S": "2014-07-16T20:55:46Z"
  },
  "map_1": {
    "M": {
      "bool_1": {
        "BOOL": "truthy"
      },
      "null_1": {
        "NULL ": "true"
      },
      "list_1": {
        "L": [
          {
            "S": ""
          },
          {
            "N": "011"
          },
          {
            "BOOL": "f"
          },
          {
            "NULL": "0"
          }
        ]
      }
    }
  }
}

# Transform and print the output
output = transform_data(input_json)
print(json.dumps(output, indent=4))
