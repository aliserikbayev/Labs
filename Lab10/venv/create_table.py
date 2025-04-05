import psycopg2

from config import load_config

def create_table():
    commands = (
        """

        """
        ,
        """

        """
        ,
        """

        """
        ,
    )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                