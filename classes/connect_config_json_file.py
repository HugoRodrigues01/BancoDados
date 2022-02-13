from jsonpickle import encode, decode

JSON_CONFIG_FILE: str = "configs/database_config.json"
CONFIG_DEFAULT: dict = {
    "Host": "localhost",
    "User": "root",
    "Password": "",
    "DataBaseName": "Animes_DB"
}

class ConfigJson:

    @staticmethod
    def read_json_config() -> dict:
        """
        This function returns a configuration dictionary in the json file configuration. 
        """

        with open(JSON_CONFIG_FILE, "r", encoding="UTF-8") as file_json_read:
            return decode(file_json_read.read())

    @staticmethod
    def update_json_config(json_config: dict) -> None:
        """
        This function will update the configs of file json.
        json_confi: Dictionary of configs 
        """

        with open(JSON_CONFIG_FILE, "w", encoding="UTF-8") as file_json_write:
            file_json_write.write(encode(json_config))
    
    @staticmethod
    def defualt_config() -> None:
        """
        This function returns the default config of file json.
        """

        with open(JSON_CONFIG_FILE, "w", encoding="UTF-8") as file_json_default:
            file_json_default.write(encode(CONFIG_DEFAULT))
