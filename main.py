import psycopg2
from vacina import vacina2anos
from lista import lista
try:
   for i in lista():
       vacina2anos(i["codibge"], i["dbname"])
   #vacina2anos()
except psycopg2.Error as e:
    print(f"Error: {e}")
## valmir é o nome do banco de dados