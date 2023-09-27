import pyodbc
from pytests.support.hooks import *

class SqlServeService:

    def connection_sql(params):
        driver = '{ODBC Driver 18 for SQL Server}'
        try:
            connection = pyodbc.connect(
            f'SERVER={server};DATABASE={database};UID={username};PWD={password};DRIVER={driver}'
            )

            # Crie um cursor para executar consultas
            cursor = connection.cursor()
        except pyodbc.Error as e:
            LOG.log_error(f"Erro na conexão: {str(e)}")
        return cursor
    
    def run_query_sql(cursor, query):
        try:
            cursor.execute(query)
        except pyodbc.Error as e:
            LOG.log_error(f"Erro na query: {str(e)}")