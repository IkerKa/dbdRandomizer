from .connection import conn

# Killer service

class KillerService():

    def __parseKillerName(self, kName):
        # if there are 2 words...
        if len(kName.split(" ")) == 2:
            # Check if the first word is "The"
            if kName.split(" ")[0].lower() == "the":
                # If it is, remove it
                kName = kName.split(" ")[1]

        # Check if the name is onryo
        if kName.lower() == "onryo":
            kName = "onryō"

        # then capitalize the first letter of the word
        # First lower case all the letters
        return kName.lower().capitalize()

    # The checkName is on survivor_service.py

    # Commands: killer, killer <name> at the moment
    def get_killer(self, kName: str, specific : bool) -> tuple:
        # Check if it is a command or the other
        if specific == False:
            # Random survivor (just image and name)
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT *
                    FROM Killers
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

            # if there are 2 words...
            kName = self.__parseKillerName(kName)

            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT *
                    FROM Killers
                    """
                )

                # Get the result
                result = cursor.fetchall()

                # If there is no result, raise an exception
                if result is None:
                    raise Exception("WHOOOOPSIES :o, there is no killer")
                
                # Iterate over the result
                for killer in result:
                    # Split the string between ( ) and get the "The Trapper" part
                    # The pseudoname is the second part of the string
                    pseudoname = killer[0].split("(")[1].split(")")[0]
                    # Remove the "The " part of the string if the kname has not
                    # Example: The Trapper and Trapper
                    pseudoname = pseudoname.replace("The  ","")
                    # Compare the pseudoname with the killerName parameter
                    # print(pseudoname)
                    if pseudoname == kName:
                        # If they are equal, return the killer
                        return killer
                    
                # If there is no killer with that name, return None
                return None

    def get_killer_perks(self, kName: str) -> tuple:
        # Get only the perks of the survivor with name "survivorName"
        # Just get the name of the perks and then goto perks table and get the name and icon
        with conn.cursor() as cursor:
            # perk_1s, perk_2s, perk_3s with 
            cursor.execute(
                """
                SELECT perk_1k, perk_2k, perk_3k
                FROM Killers
                WHERE killerName = %s
                """,
                (kName,)
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

    # Power addons
    def get_killer_addons(self, kName: str) -> tuple:
        # Get the killer
        killer = self.get_killer(kName, True)

        # Get the killer addons
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT *
                FROM Power_Addons
                WHERE killerName = %s
                """,
                (killer[0],)
            )

            # Get the result
            result = cursor.fetchall()

            # If there is no result, raise an exception
            if result is None:
                raise Exception("WHOOOOPSIES :o, there is no killer")

            # Return the result
            return result

