import pymysql
#Create connection
connection = pymysql.connect(host='localhost',
                            port = 3306, 
                            user = 'root', 
                            password ='',
                            db = 'colegio')
# Create cursor
cursor = connection.cursor()
#Execute 
query = 'INSERT INTO estudiantes values({0}, "{1}", "{2}", {3}, {4})'.format(555555, 'Camilo Andres', 'Rojas Leon', 11, 5)
