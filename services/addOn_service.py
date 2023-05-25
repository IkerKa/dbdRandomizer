from .connection import conn

# SURVIVOR ITEMS ADD-ONS

class AddOnService():

    def random_addOn(self) -> tuple:
        """
        # Get a random add-on from the database
        # Result: name,item,description,image
        """
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



    def get_addOn(self, addOnName: str) -> tuple:
        # The embed:
        # From: general 
        # Title
        # Description
        # Image
        # Footer: list of all items that can use this add-on

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
                return None, None, None
            
            # Now lets take all the items that can use this add-on:
            # We will go to the add-on table and take all the items that have this add-on
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
            return result, items, generalName



            


    
