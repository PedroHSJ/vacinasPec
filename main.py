import psycopg2
from vacina import vacina2anos
from lista import lista
from enviarEmail import enviarEmail
try:
   for i in lista():
       vacina2anos(i["codibge"], i["dbname"])
   #vacina2anos()
except psycopg2.Error as e:
    print(f"Error: {e}")
    enviarEmail(e, 'POSTGRES')