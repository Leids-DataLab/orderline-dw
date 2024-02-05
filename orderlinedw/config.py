"""
Gebruik
-------
Deze module bevat configuratieparameters. Je kunt ze bijvoorbeeld zo gebruiken:

import config

path = config.databases_connection_string_oltp

De parameters worden bij het importeren van deze module gelezen uit
-het config.ini bestand

Met de functie load(env) laad je de parameters opnieuw in. Met env geef je aan
voor welke environment je de variabelen inleest, bijvoorbeeld dev, test of prod.
Voor het config.ini bestand wordt het bestand config_{env}.ini gebruikt, bijvoorbeeld config_dev.ini.
De default environment is dev.

Configuratie/installatie
------------------------
In config_{env}.ini kun je de parameters instellen zoals je wilt. In config.ini staan de parameters die
deze module verwacht.

Parameters toevoegen aan config.ini
-----------------------------------

Als je parameters toevoegt aan config.ini worden ze automatisch ingelezen. Maar het
is handig/gewenst ze hier ook expliciet toe te voegen. Dat werkt fijn in de IDE en vermijdt tikfouten.
Je moet dan de volgende naamgevingsconventie hanteren. Stel je hebt in config.ini

[databases]
connection_string_oltp = mssql+pyodbc://username:password@server/database_oltp?driver=ODBC+Driver+17+for+SQL+Server

Voeg dan toe:

databases_connection_string_oltp = None
"""
import configparser

# Hier staan de config parameters. Ze worden gelezen uit config_{environment}.ini.
databases_connection_string_oltp = None
databases_connection_string_dw = None


def _read_globals_from_config_file(env):
    """
    Leest config.ini in en zet de waarden in globale variabelen met de naam {section}_{key}, bijvoorbeeld
    [dir]
    input_telbestanden = C:\Data\TB\dev_duck
    Komt in de variabele dir_input_telbestanden

    :param env: De environment waarvoor de parameters worden ingelezen.
    :return: Niks.
    """
    config_file = f"config_{env}.ini"
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)

    globals().update({f"{section}_{key}": value for section in config_parser.sections() for key, value in config_parser.items(section)})


def load(env_to_load="dev"):
    """
    Laadt de parameters uit de configuratie bestanden.
    :param env_to_load: De environment waarvoor de parameters worden geladen.
    :return:
    """
    global env
    env = env_to_load
    _read_globals_from_config_file(env)


# Dit zorgt ervoor dat de parameters worden geladen bij het importeren van deze module.
load()
