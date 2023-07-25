import os
import io
from PIL import Image, ImageDraw

path = os.path.realpath(os.path.dirname(__file__)) + os.path.sep
jacket_background = path + "jacket.png"
jacket_text = path + "jacket_text.png"


background_image = Image.open(jacket_background).copy()
foreground_image = Image.open(jacket_text).copy().convert("RGBA")

gold_fill_color = (255, 215, 0, 100)
white_fill_color = (255, 255, 255, 100)

jacket_locations = {
    1:  (150, 50),
    2:  (300, 50),
    3:  (70, 150),
    4:  (150, 150),
    5:  (300, 150),
    6:  (380, 150),
    7:  (150, 250),
    8:  (300, 250),
    9:  (30, 350),
    10: (150, 350),
    11: (300, 350),
    12: (415, 350)
}

cert_locations = {
    1:  ["SAP"],
    2:  ["DOP"],
    3:  ["DBS"],
    4:  ["ANS"],
    5:  ["SCS"],
    6:  ["DAS"],
    7:  ["DVA"],
    8:  ["SOA"],
    9:  ["MLS"],
    10: ["CLF", "CCP"],
    11: ["SAA"],
    12: ["PAS"]
}

def get_cert_index(cert_name: str) -> int:
    cert_name = cert_name.upper()
    for index, cert_names in cert_locations.items():
        if cert_name in cert_names: return index
    return 0



def create_jacket(certs: list[str]) -> str:
    background_image = Image.open(jacket_background).copy()
    foreground_image = Image.open(jacket_text).copy().convert("RGBA")

    certs = list(certs)

    gold_pieces = [x for x in map(get_cert_index, certs) if x != 0]

    for piece, pixel_location in jacket_locations.items():
        color = white_fill_color
        if piece in gold_pieces: color = gold_fill_color
        ImageDraw.floodfill(background_image, pixel_location, color, thresh=100.0)

    background_image.paste(foreground_image, (0, 0), foreground_image)
    image_byte_array = io.BytesIO()
    background_image.convert("RGB").save(image_byte_array, format="jpeg")
    image_byte_array.seek(0)
    return image_byte_array
