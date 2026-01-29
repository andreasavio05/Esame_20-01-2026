from database.DB_connect import DBConnect
from model.artist import Artist

class DAO:

    @staticmethod
    def get_all_artists():

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT *
                FROM artist a
                """
        cursor.execute(query)
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'])
            result.append(artist)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_nodi(n_alb):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT ar.id, ar.name FROM artist ar, album al WHERE ar.id = al.artist_id GROUP BY ar.id, ar.name HAVING COUNT(*) >= %s """
        cursor.execute(query, (n_alb,))

        for row in cursor:
            result.append(Artist(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_archi():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT distinct a1.id as a1, a2.id as a2, COUNT(distinct t1.genre_id) as peso
                    FROM artist as a1, artist a2, track t1, track t2, album al1, album al2
                    WHERE a1.id != a2.id AND a1.id = al1.artist_id AND a2.id = al2.artist_id AND al1.id = t1.album_id AND al2.id = t2.album_id AND t1.genre_id = t2.genre_id
                    GROUP BY a1.id, a2.id """
        cursor.execute(query)
        for row in cursor:
            row.append((row['a1'], row['a2'], row['peso']))

        cursor.close()
        conn.close()
        return result
