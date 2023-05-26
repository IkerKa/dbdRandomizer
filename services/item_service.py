from .connection import conn


class ItemService():

    # Commands for items

    # item <itemName> (optional)
    # item addons <itemName> (mandatory)

    def get_item(self, itemName: str, specific: bool) -> tuple:
        """
        Get an item from the database (if specific is True, it will get the item with the name, if not, it will get a random item)
        """

        if specific == False:
            # Ramdom item (just image and name)
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                   SELECT *
                   FROM Items
                   ORDER BY RANDOM()
                   LIMIT 1
                   """
                )

                # Get the result
                result = cursor.fetchone()

                   # If there is no result, raise an exception
                if result is None:
                    raise Exception(
                        "WHOOOOPSIES :o, there is no item in the database")

                    # Return the result
                return result
            
        else:
                
                # Fetch the item with name
                with conn.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT *
                        FROM Items
                        WHERE itemName = %s
                        """,
                        (itemName,)
                    )
    
                    # Get the result
                    result = cursor.fetchone()
    
                    # If there is no result with name, it will be shown an error message
    
                    # Return the result
                    return result
                


    def get_addons(self, itemName: str) -> tuple:
        # First, take the image and the name of the item
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT *
                FROM Items
                WHERE itemName = %s
                """,
                (itemName,)
            )

            # Get the result
            item = cursor.fetchone()

            # If there is no result with name, it will be shown an error message
            if item is None:
                return None, None
            
            # Get the addons of the item
            cursor.execute(
                """
                SELECT *
                FROM Item_Addons
                WHERE itemName = %s
                """,
                (itemName,)
            )

            # Get the result
            addons = cursor.fetchall()

            # If there is no result with name, it will be shown an error message
            if addons is None:
                return None, None
            
            # Return the result
            return item, addons

