from perk_imager import perk_display
from PIL import Image

def main():

    # Load perk test images (can be None, the slot will be empty)
    p1 = Image.open("assets/i1.png")
    p2 = Image.open("assets/i2.png")
    p3 = Image.open("assets/i3.png")
    p4 = None

    # Create a perk display object
    # 4 arguments passed as 
    pdisp = perk_display(
        up=p1, 
        left=p2, 
        right=p3, 
        down=p4, 
        size=(512, 512)
    )

    #show image
    pdisp.show()

    # Create another perk display
    # custom empty perk size and bg colour
    pdisp2 = perk_display(
        up=p3, 
        left=p4, 
        right=p1, 
        down=p2, 
        size=(512, 512),
        empty_fill_col=(56, 78, 10),
        empty_size=(100, 100)
    )

    #show image
    pdisp2.show()

if __name__ == "__main__":
    main()