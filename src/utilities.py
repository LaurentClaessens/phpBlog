"""Some utilities."""

from pathlib import Path
import json


def read_json_file(json_path, default=None):
    """
    Return the given json file as dictionary.

    @param {string} `json_path`
    @return {dictionary}
    """
    json_path = Path(json_path)
    if not json_path.is_file():
        if default is None:
            raise ValueError(f"You try to read {json_path}. "
                             f"The file does not exist and you "
                             f"furnished no default.")
        return default
    with open(json_path, 'r') as json_data:
        try:
            answer = json.load(json_data)
        except json.decoder.JSONDecodeError as err:
            print("JSONDecodeError:", err)
            message = f"Json error in {json_path}:\n {err}"
            raise ValueError(message) from err
    return answer


def json_serial(obj):
    """Serialize the datetime."""
    if isinstance(obj, datetime.datetime):
        timestamp = obj.timestamp()
        return human_timestamp(timestamp)
    return str(obj)


def write_json_file(json_dict,
                    filename,
                    pretty=False,
                    default=None):
    """Write the dictionary in the given file."""
    if default is None:
        default = json_serial
    if pretty:
        str_json = json.dumps(json_dict,
                              sort_keys=True,
                              indent=4,
                              default=default)
    else:
        str_json = json.dumps(json_dict, default=default)
    with open(filename, 'w') as json_file:
        json_file.write(str_json)
