class ConfigurationManager:
    _instance = None

    @staticmethod
    def get_instance():
        if ConfigurationManager._instance is None:
            ConfigurationManager._instance = ConfigurationManager()
        return ConfigurationManager._instance

    def __init__(self):
        if ConfigurationManager._instance is not None:
            raise Exception("This class is a singleton!")
        self.config = {}

    def get_config(self, key):
        return self.config.get(key)

    def set_config(self, key, value):
        self.config[key] = value
