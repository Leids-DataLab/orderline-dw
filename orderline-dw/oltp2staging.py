import pandas as pd
import sqlalchemy as sa

import config

SCHEMA_OLTP = "oltp"
SCHEMA_DW = "staging"
TABLES = ["klant", "productcategorie", "productsubcategorie", "product", "bestelling", "bestellingregel"]


def copy_tables(engine_oltp, engine_dw):
    global SCHEMA_OLTP, TABLES

    for table in TABLES:
        print(f"Lees de tabel {table} uit oltp.")
        df = pd.read_sql_table(schema=SCHEMA_OLTP, table_name=table, con=engine_oltp)
        print(f"Schrijf de tabel {table} naar staging in het data warehouse.")
        df.to_sql(schema=SCHEMA_DW, name=table, if_exists='replace', index=False, con=engine_dw)


if __name__ == "__main__":
    engine_oltp = sa.create_engine(config.databases_connection_string_oltp)
    engine_dw = sa.create_engine(config.databases_connection_string_dw, fast_executemany=True)
    try:
        copy_tables(engine_oltp=engine_oltp, engine_dw=engine_dw)
    finally:
        engine_oltp.dispose()
        engine_dw.dispose()
