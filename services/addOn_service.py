from .connection import conn
import random

# SURVIVOR ITEMS ADD-ONS

class AddOnService():

    def check_name(self, addOnName: str) -> bool:
        # Check if the name is in the database
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT addonName
                FROM Item_Addons
                WHERE addonName = %s
                """,
                (addOnName,)
            )

            # Get the result
            result = cursor.fetchone()

            # If there is no result, raise an exception
            if result is None:
                return False

            return True

    def random_addOn(self) -> tuple:
        """
        # Get a random add-on from the database
        # Result: name,item,description,image
        """

        # Random number betwe1en 1 and 2
        random_number = random.randint(1, 2)


        if random_number == 1:

            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT *
                    FROM Item_Addons
                    ORDER BY RANDOM()
                    LIMIT 1
                    """
                )

                # Get the result
                result = cursor.fetchone()

                # If there is no result, raise an exception
                if result is None:
                    raise Exception("WHOOOOPSIES :o, there is no add-on")

                # Now lets take the icon of the item
                cursor.execute(
                    """
                    SELECT itemIcon
                    FROM Items
                    WHERE itemName = %s
                    """,
                    (result[1],)
                )

                # Get the result
                itemIcon = cursor.fetchone()

                # If there is no result, raise an exception
                if itemIcon is None:
                    itemIcon = "https://i.imgur.com/0QZS6ZV.png"

                # Return the result
                return result, itemIcon[0]
            
        else:
            # Random from killer Power_addons
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                    SELECT *
                    FROM Power_Addons
                    ORDER BY RANDOM()
                    LIMIT 1
                    """
                )

                # Get the result
                result = cursor.fetchone()

                # If there is no result, raise an exception
                if result is None:
                    raise Exception("WHOOOOPSIES :o, there is no add-on")

                # Now lets take the icon of the item
                cursor.execute(
                    """
                    SELECT image_k
                    FROM Killers
                    WHERE killerName = %s
                    """,
                    (result[1],)
                )

                # Get the result
                itemIcon = cursor.fetchone()

                # If there is no result, raise an exception
                if itemIcon is None:
                    itemIcon = "https://i.imgur.com/0QZS6ZV.png"

                # Return the result
                return result, itemIcon[0]



    def get_addOn(self, addOnName: str) -> tuple:
        # The embed:
        # From: general 
        # Title
        # Description
        # Image
        # Footer: list of all items that can use this add-on

        isPower = False

        # First take all the addon info
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT *
                FROM Item_Addons
                WHERE addonName = %s
                """,
                (addOnName,)
            )

            # Get the result
            result = cursor.fetchone()

            # If there is no result, raise an exception
            if result is None:
                # Check if is on Power Add-ons
                cursor.execute(
                    """
                    SELECT *
                    FROM Power_Addons
                    WHERE powerAddName = %s
                    """,
                    (addOnName,)
                )

                # Get the result
                result = cursor.fetchone()

                # If there is no result, raise an exception
                if result is None:
                    return None, None, None
                else:
                    isPower = True
            
            # Now lets take all the items that can use this add-on:
            # We will go to the add-on table and take all the items that have this add-on

            if not isPower:
                cursor.execute(
                    """
                    SELECT itemName
                    FROM Item_Addons
                    WHERE addonName = %s
                    """,
                    (addOnName,)
                )

                # Get the result
                items = cursor.fetchall()

                # Now lets take the general name of the item
                # If 2 or more items have the word "Flashlight" in their name, we will take the word "Flashlight"
                if items == None:
                    generalName = "No items can use this add-on"
                else:
                    # We take the last words of the item name
                    generalName = items[0][0].split(" ")[-1]
                    if generalName == "Kit":
                        generalName = "Med-Kit"
                    if generalName == "Tools":
                        generalName = "Toolbox"

                # Return the result
                return result, items, generalName, isPower

            else:
                # Get the killer name and the image
                cursor.execute(
                    """
                    SELECT killerName, image_k
                    FROM Killers
                    WHERE killerName = %s
                    """,
                    (result[1],)
                )

                # Get the result
                killer = cursor.fetchone()

                # If there is no result, raise an exception
                return result, killer, killer[0], isPower
                



                    

            


            


    
