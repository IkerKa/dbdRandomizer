from .connection import conn


class AuthorService():

    def author_setup(self, authorName) -> tuple:
        # ...Juan (if u need parameters, dont forget to add them)

        print("Author name: " + authorName)

        # Parse the name
        authorName = authorName.lower()
        authorName = authorName.title()

        perks = []


        survivor_name = ""

        mapa_name = ""

        if authorName == "Juan":
            survivor_name="Leon Scott Kennedy"
            mapa_name="Coldwind Farm"
            perks.append("Flashbang")
            perks.append("Spine Chill")
            perks.append("Bond")
            perks.append("Windows of Opportunity")


        elif authorName == "Iker":
            survivor_name="Jill Valentine"
            mapa_name="Hawkins National Laboratory/Haddonfield"
            perks.append("Lithe")
            perks.append("Adrenaline")
            perks.append("Off the Record")
            perks.append("Inner Healing")

        elif authorName == "Dario":
            survivor_name="Jake Park"
            mapa_name="The Game"
            perks.append("Dance With Me")
            perks.append("Iron Will")
            perks.append("Saboteur")
            perks.append("Calm Spirit")

        else:
            return None, None, None, None


        with conn.cursor() as cursor:
            cursor.execute(
                """
                    SELECT *
                    FROM Survivors 
                    WHERE survName = %s
                """,
                (survivor_name,)
            )

            resultado = cursor.fetchone()

        # Get perks images
        # Search them in the database
        perks_images = []

        for perk in perks:
            print("PERK: ", perk)
            with conn.cursor() as cursor:
                cursor.execute(
                    """
                        SELECT icon
                        FROM Perks
                        WHERE perkName = %s
                    """,
                    (perk,)
                )

                res = cursor.fetchone()
                perks_images.append(res[0])

        # Get map image
        # Coming soon




        # Nombre survivor , Foto , perk 1, perk 2, perk 3, perk 4 y mapa
        return resultado[0],resultado[-1], perks, perks_images, mapa_name







    def get_author_suggestions() -> tuple:
        pass
