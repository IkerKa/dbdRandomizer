from .connection import conn

class PerkService():

    def random_perk(self, survivor : int, killer : int) -> tuple:
        """
        Get a random perk from the database with all its info.
        Note: both flags can't be false, that is, `survivor or killer = True`
        
        Args:
            survivor(bool) : True if the perks come from survivors
            killer(bool) : True if the perks come from killers
            
        Returns:
            tuple : A tuple with the perk info
        """
        
        # If both flags are false, raise an exception
        if not survivor and not killer:
            raise Exception("Both flags can't be false")
        
        # Get a random perk from the database
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT *
                FROM Perks
                WHERE fromSurvivor = %s OR fromKiller = %s
                ORDER BY RANDOM()
                LIMIT 1
                """,
                (survivor, killer)
            )

            # Get the result
            result = cursor.fetchone()

            # If there is no result, raise an exception
            if result is None:
                raise Exception("WHOOOOPSIES :o, there is no perk with those flags")
            
            # Return the result
            return result

    def random_perks(self, number : int) -> list:
        """

        """
        pass
    
    def random_combo(self):
        pass