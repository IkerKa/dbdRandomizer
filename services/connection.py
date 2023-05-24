import psycopg2
import os
# env file module
from dotenv import load_dotenv

# Poniendo __conn quiere decir que es una variable privada: no se puede acceder desde fuera

#--->load env file from the project
load_dotenv()

# Se crea la conexión a la base de datos
# Imprimimos las variables del fichero .env del proyecto


conn = psycopg2.connect(
    dbname   = os.getenv('POSTGRES_DB'),
    user     = os.getenv('POSTGRES_USER'),
    password = os.getenv('POSTGRES_PASSWORD'),
    host     = os.getenv('POSTGRES_HOST'),
    port     = os.getenv('POSTGRES_PORT')
)

# Si no se conecta, se lanza una excepción
if conn is None:
    raise Exception("Couldn't connect!") 