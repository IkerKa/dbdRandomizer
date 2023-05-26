from .connection import conn

# Offering service

class OfferingService():
    
    def randomOffering(self, fromSurvivor : int, fromKiller : int):
        # After that, get the owner
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT *
                FROM Offerings
                where fromSurvivor = %s AND fromKiller = %s
                ORDER BY RANDOM()
                LIMIT 1
                """,

                (fromSurvivor, fromKiller)
            )

            offering = cursor.fetchone()

            return offering[0], offering[1], offering[2]