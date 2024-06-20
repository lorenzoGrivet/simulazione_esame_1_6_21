from database.DB_connect import DBConnect



class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllTeams():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct teamCode , name 
                    from lahmansbaseballdb.teams 
                    order by name"""

        cursor.execute(query, ())

        for row in cursor:
            result.append((row['teamCode'], row["name"]))

        cursor.close()
        conn.close()
        return result

