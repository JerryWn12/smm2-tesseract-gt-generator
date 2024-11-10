import os

from PIL import Image, ImageDraw, ImageFont
from random import random

MODEL_NAME = "eng-smm2-hori"
FONT_FILENAME = "smm2.ttf"


def generate(name, text):

    font = ImageFont.truetype(f"fonts/{FONT_FILENAME}", size=64)
    length = font.getlength(text)

    image = Image.new("RGB", (int(length), 48), "white")

    draw = ImageDraw.Draw(image, "RGB")
    draw.text((0, -10), text, (0, 0, 0), font)

    image.save(f"gt/{MODEL_NAME}-{name}.png")

    try:
        with open(f"gt/{MODEL_NAME}-{name}.gt.txt", mode="x") as file:
            file.write(text)
    except OSError as err:
        print(f"error: {str(err)}, skip")


def generate_course_id(count):

    # smm2 course id do not contain I,O,Z
    chars = "1234567890ABCDEFGHJKLMNPQRSTUVWXY"
    length = len(chars)

    for _ in range(count):
        id = ""
        for _ in range(9):
            index = int(random() * length)
            char = chars[index]
            id = id + char
            if len(id) in (3, 7):
                id = id + "-"
        generate(f"{id[:3]}{id[-3:]}", id)


def generate_score(count):

    for _ in range(count):
        # smm2 have a maxinum score of 8000
        score = str(int(random() * 8000))
        generate(score, score)


if not os.path.exists("gt"):
    os.mkdir("gt")

generate_course_id(10)
generate_score(20)
