import yaml
from housing.Exception import housingException


def read_yaml_file(file_path : str)-> dict:
    """
    Reads a Yaml file and returns the contents as dictionary.
    file_path: str
    """
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise housingException(e,sys) from e