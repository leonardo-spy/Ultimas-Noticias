from dotenv import load_dotenv, dotenv_values


def initialize():
    config = {}
    load_dotenv()
    config = dotenv_values(".env")
    return config
