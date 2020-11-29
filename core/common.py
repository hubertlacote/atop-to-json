import json
import logging


def configure(logging_level):

    logging.basicConfig(
        format='%(asctime)s %(filename)s:%(lineno)d:'
        ' %(levelname)s: %(message)s', level=logging_level)

    logging.getLogger().setLevel(logging_level)


def prettify(decoded_json, indent=4):
    return json.dumps(decoded_json, indent=indent)
