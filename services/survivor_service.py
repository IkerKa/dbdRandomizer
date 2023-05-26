from .connection import conn

#Survivor service

class SurvivorService():

    def checkName(self, survivorName: str) -> bool:
        # Check if the name is in the database
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT survName
                FROM Survivors
                WHERE survName = %s
                """,
                (survivorName,)
            )

            # Get the result
            result = cursor.fetchone()

            # If there is no result, raise an exception
            if result is None:
                return False

            return True
    
    # Commands: survivor, survivor <name> at the moment
    def get_survivor(self, survivorName: str, specific : bool) -> tuple:

        # Check if it is a command or the other
        if specific == False:
            # Random survivor (just image and name)
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT *
                    FROM Survivors
                    ORDER BY RANDOM()
                    LIMIT 1
                    """
                )

                # Get the result
                result = cursor.fetchone()

                # If there is no result, raise an exception
                if result is None:
                    raise Exception("WHOOOOPSIES :o, there is no survivor")

                # Return the result
                return result
            
        else:

            # Capitalize the first letter of all the words
            # Lower case all the words
            survivorName = survivorName.lower()
            survivorName = survivorName.title()






            # Fetch the survivor with name
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT *
                    FROM Survivors
                    WHERE survName = %s
                    """,
                    (survivorName,)
                )

                # Get the result
                result = cursor.fetchone()

                # Return the result
                return result
            
    def get_survivor_perks(self, survivorName: str) -> tuple:
        # Get only the perks of the survivor with name "survivorName"

        # Just get the name of the perks and then goto perks table and get the name and icon
        with conn.cursor() as cursor:
            # perk_1s, perk_2s, perk_3s with 
            cursor.execute(
                """
                SELECT perk_1s, perk_2s, perk_3s
                FROM Survivors
                WHERE survName = %s
                """,
                (survivorName,)
            )

            # Get the result
            perks = cursor.fetchone()

            # If there is no result, raise an exception
            if perks is None:
                return None
            
            # Now lets take the icon of the 3 perks
            cursor.execute(
                """
                SELECT perkName, icon
                FROM Perks
                WHERE perkName = %s OR perkName = %s OR perkName = %s
                """,
                (perks[0], perks[1], perks[2])
            )

            # Get the result
            perks = cursor.fetchall()

            # If there is no result, raise an exception
            if perks is None:
                return None
            

            return perks


            