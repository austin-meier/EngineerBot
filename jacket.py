import os
import io
from PIL import Image, ImageDraw

path = os.path.realpath(os.path.dirname(__file__)) + os.path.sep
jacket_image = path + "jacket.png"
jacket_text = path + "jacket_text.png"

gold_color = (255, 215, 0, 100)
white_color = (255, 255, 255, 100)

jacket_pieces = [
    ((150, 50), ["SAP"]),
    ((300, 50), ["DOP"]),
    ((70, 150), ["DBS"]),
    ((150, 150), ["ANS", "NETWORKING"]),
    ((300, 150), ["SCS"]),
    ((380, 150), ["DAS"]),
    ((150, 250), ["DVA"]),
    ((300, 250), ["SOA"]),
    ((30, 350), ["MLS"]),
    ((150, 350), ["CLF", "CCP"]),
    ((300, 350), ["SAA"]),
    ((415, 350), ["PAS"])
]

# ["ANS", "SOA"]
def create_jacket(certs: list[str]):
  certs = [cert.upper() for cert in certs]
  jacket = Image.open(jacket_image)
  for piece in jacket_pieces:
    location, names = piece

    color = white_color

    if any(map(lambda name: name in certs, names)):
      color = gold_color

    ImageDraw.floodfill(
          image=jacket,
          xy=location,
          value=color
    )

  # We need to overlay the text on the image
  text_layer = Image.open(jacket_text)
  jacket.paste(text_layer, (0, 0), text_layer)

  image_byte_array = io.BytesIO()
  jacket.convert("RGB").save(image_byte_array, format="jpeg")
  image_byte_array.seek(0)
  return image_byte_array
