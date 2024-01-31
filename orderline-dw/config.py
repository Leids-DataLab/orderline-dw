import configparser

# Hier staan de config parameters. Ze worden gelezen uit config_{environment}.ini.
databases_connection_string_oltp = None
databases_connection_string_dw = None


def read_globals_from_config_file():
    """
    Lees config_dev.ini uit en zet alle variabelen in de config parameters van deze module.
    """
    config_file = f"config_dev.ini"
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)

    globals().update({f"{section}_{key}": value for section in config_parser.sections() for key, value in config_parser.items(section)})


read_globals_from_config_file()
