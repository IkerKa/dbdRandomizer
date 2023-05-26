from .connection import conn

# Killer service

class KillerService():

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
            if len(kName.split(" ")) == 2:
                # Check if the first word is "The"
                if kName.split(" ")[0].lower() == "the":
                    # If it is, remove it
                    kName = kName.split(" ")[1]

            # then capitalize the first letter of the word
            # First lower case all the letters
            kName = kName.lower()
            kName = kName.capitalize()

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
        pass
        


    # Power addons
    def get_killer_addons(self, kName: str) -> tuple:
        pass

