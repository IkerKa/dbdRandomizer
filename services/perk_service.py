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

            # Get perk owner: access to the survivor or killer table and check the name

            # First check, if the perk is from a survivor
            cursor.execute(
                """
                SELECT *
                FROM Survivors
                WHERE perk_1s = %s OR perk_2s = %s OR perk_3s = %s;
                """,

                (result[0], result[0], result[0])
            )

            owner_survivor = cursor.fetchone()

            # Second check, if the perk is from a killer
            cursor.execute(
                """
                SELECT *
                FROM Killers
                WHERE perk_1k = %s OR perk_2k = %s OR perk_3k = %s;
                """,

                (result[0], result[0], result[0])
            )

            owner_killer = cursor.fetchone()
            
            # Union the results and take the first one of the tuple (deberia haber uno)
            if owner_killer is None:
                owner = owner_survivor
            else:
                owner = owner_killer
            # Return the result
            return result, owner

    def perk_info(self, perk_name : str) -> tuple:
        # The same as random_perk, but with a perk name, so first, we need to get the perk and check if it exists
        with conn.cursor() as cursor:

            cursor.execute(
                """
                SELECT *
                FROM Perks
                WHERE perkName = %s
                """,
                (perk_name,)
            )

            # Get the result
            result = cursor.fetchone()

            # Check if it has returned something
            if result is None:
                return None, None
            
            # After that, get the owner
            cursor.execute(
                """
                SELECT *
                FROM Survivors
                WHERE perk_1s = %s OR perk_2s = %s OR perk_3s = %s;
                """,

                (result[0], result[0], result[0])
            )

            owner_survivor = cursor.fetchone()

            # Second check, if the perk is from a killer
            cursor.execute(
                """
                SELECT *
                FROM Killers
                WHERE perk_1k = %s OR perk_2k = %s OR perk_3k = %s;
                """,

                (result[0], result[0], result[0])
            )

            owner_killer = cursor.fetchone()
            
            # Union the results and take the first one of the tuple (deberia haber uno)
            if owner_killer is None:
                owner = owner_survivor
            else:
                owner = owner_killer
            # Return the result
            return result, owner
        

            

    
    def random_combo(self):
        pass