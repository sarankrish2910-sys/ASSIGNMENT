import yaml
import os


def get_config():
    """
    Reads config.yaml file and returns configuration dictionary.
    """

    config_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "config",
        "config.yaml"
    )

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    return config
