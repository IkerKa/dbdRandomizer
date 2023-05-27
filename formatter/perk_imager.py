from PIL import Image, ImageDraw
from io import BytesIO
import math

#finds the straight-line distance between two points
def __distance(ax, ay, bx, by):
    return math.sqrt((by - ay)**2 + (bx - ax)**2)

#rotates point `A` about point `B` by `angle` radians clockwise.
def __rotated_about(ax, ay, bx, by, angle):
    radius = __distance(ax,ay,bx,by)
    angle += math.atan2(ay-by, ax-bx)
    return (
        round(bx + radius * math.cos(angle)),
        round(by + radius * math.sin(angle))
    )

def __draw_empty(img : Image, pos : tuple, size : tuple = (40, 40), fill_colour=(128, 128, 128)) -> None:
    draw = ImageDraw.Draw(img)

    vertices = (
        (pos[0] + size[0] / 2, pos[1] + size[1] / 2),
        (pos[0] + size[0] / 2, pos[1] - size[1] / 2),
        (pos[0] - size[0] / 2, pos[1] - size[1] / 2),
        (pos[0] - size[0] / 2, pos[1] + size[1] / 2)
    )

    rotated_vertices = [__rotated_about(x,y, pos[0], pos[1], math.radians(45)) for x,y in vertices]
    draw.polygon(rotated_vertices, fill=fill_colour)


def perk_display(up : Image, left : Image, right : Image, down : Image, size : tuple = (256, 256), empty_fill_col=(128, 128, 128), empty_size=(80, 80)) -> Image:
    """Generate a perk display image object, with up to 4 perks.

    If a perk slot image is set to None, that slot will show an empty placeholder.

    Args:
        up (Image): The perk on the upper slot, can be None
        left (Image): The perk on the left slot, can be None
        right (Image): The perk on the right slot, can be None
        down (Image): The perk on the lower slot, can be None
        size (tuple, optional): The width and height of the image. Defaults to (256, 256).
        empty_fill_col (tuple, optional): The fill colour when a perk slot is empty. Defaults to (128, 128, 128).
        empty_size (tuple, optional): The size of a perk slot when it's empty. Defaults to (80, 80).

    Returns:
        Image: The perk display image
    """
    img = Image.new("RGBA", size)

    if up is not None:
        uw, uh = up.width, up.height
        up_pos = (int(size[0] / 2 - uw / 2), int(size[1] / 4 - uh / 2))
        img.paste(up, up_pos, up)
    else:
        __draw_empty(img, (int(size[0] / 2), int(size[1] / 4)), empty_size, empty_fill_col)

    if left is not None:
        lw, lh = left.width, left.height
        left_pos = (int(size[0] / 4 - lw / 2), int(size[1] / 2 - lh / 2))
        img.paste(left, left_pos, left)
    else:
        __draw_empty(img, (int(size[0] / 4), int(size[1] / 2)), empty_size, empty_fill_col)

    if right is not None:
        rw, rh = right.width, right.height
        right_pos =  (int(3 * size[0] / 4 - rw / 2), int(size[1] / 2 - rh / 2))
        img.paste(right, right_pos, right)
    else:
        __draw_empty(img, (3 * int(size[0] / 4), int(size[1] / 2)), empty_size, empty_fill_col)

    if down is not None:
        dw, dh = down.width, down.height
        down_pos = (int(size[0] / 2 - dw / 2), int(3 * size[1] / 4 - dh / 2))
        img.paste(down, down_pos, down)
    else:
        __draw_empty(img, (int(size[0] / 2), int(3 * size[1] / 4)), empty_size, empty_fill_col)

    return img



def perk_display_url(up_url, left_url, right_url, down_url, size=(256, 256), empty_fill_col=(128, 128, 128), empty_size=(80, 80)):
    """Generate a perk display image object, with up to 4 perks.

    If a perk slot URL is set to None, that slot will show an empty placeholder.

    Args:
        up_url (str): The URL of the perk on the upper slot, can be None
        left_url (str): The URL of the perk on the left slot, can be None
        right_url (str): The URL of the perk on the right slot, can be None
        down_url (str): The URL of the perk on the lower slot, can be None
        size (tuple, optional): The width and height of the image. Defaults to (256, 256).
        empty_fill_col (tuple, optional): The fill colour when a perk slot is empty. Defaults to (128, 128, 128).
        empty_size (tuple, optional): The size of a perk slot when it's empty. Defaults to (80, 80).

    Returns:
        Image: The perk display image
    """
    img = Image.new("RGBA", size)

    def paste_image(url, position):
        response = requests.get(url)
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            img.paste(image, position)
        else:
            __draw_empty(img, position, empty_size, empty_fill_col)

    if up_url is not None:
        uw, uh = size[0] / 2, size[1] / 4
        up_pos = (int(size[0] / 2 - uw / 2), int(size[1] / 4 - uh / 2))
        paste_image(up_url, up_pos)
    else:
        __draw_empty(img, (int(size[0] / 2), int(size[1] / 4)), empty_size, empty_fill_col)

    if left_url is not None:
        lw, lh = size[0] / 4, size[1] / 2
        left_pos = (int(size[0] / 4 - lw / 2), int(size[1] / 2 - lh / 2))
        paste_image(left_url, left_pos)
    else:
        __draw_empty(img, (int(size[0] / 4), int(size[1] / 2)), empty_size, empty_fill_col)

    if right_url is not None:
        rw, rh = size[0] / 4, size[1] / 2
        right_pos = (int(3 * size[0] / 4 - rw / 2), int(size[1] / 2 - rh / 2))
        paste_image(right_url, right_pos)
    else:
        __draw_empty(img, (int(size[0] / 2), int(3 * size[1] / 4)), empty_size, empty_fill_col)

    if down_url is not None:
        dw, dh = size[0] / 2, size[1] / 4
        down_pos = (int(size[0] / 2 - dw / 2), int(3 * size[1] / 4 - dh / 2))
        paste_image(down_url, down_pos)
    else:
        __draw_empty(img, (int(size[0] / 2), int(3 * size[1] / 4)), empty_size, empty_fill_col)

    return img

def itemDisplay():
    raise "Not implemented"