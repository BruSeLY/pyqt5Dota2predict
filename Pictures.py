import pymysql
from PIL import Image


def get_photo(radiantThis, direThis):
    radiantThis = radiantThis.split()
    direThis = direThis.split()
    photoRadiant = Image.open("Background.jpg").resize((512 * 5, 1520))
    im1 = Image.open(f"IconHero\{radiantThis[0]}_icon.webp").convert("RGB").resize((512, 288))
    im2 = Image.open(f"IconHero\{radiantThis[1]}_icon.webp").convert("RGB").resize((512, 288))
    im3 = Image.open(f"IconHero\{radiantThis[2]}_icon.webp").convert("RGB").resize((512, 288))
    im4 = Image.open(f"IconHero\{radiantThis[3]}_icon.webp").convert("RGB").resize((512, 288))
    im5 = Image.open(f"IconHero\{radiantThis[4]}_icon.webp").convert("RGB").resize((512, 288))
    im6 = Image.open(f"IconHero\{direThis[0]}_icon.webp").convert("RGB").resize((512, 288))
    im7 = Image.open(f"IconHero\{direThis[1]}_icon.webp").convert("RGB").resize((512, 288))
    im8 = Image.open(f"IconHero\{direThis[2]}_icon.webp").convert("RGB").resize((512, 288))
    im9 = Image.open(f"IconHero\{direThis[3]}_icon.webp").convert("RGB").resize((512, 288))
    im10 = Image.open(f"IconHero\{direThis[4]}_icon.webp").convert("RGB").resize((512, 288))
    photoRadiant.paste(im1, (0, 0))
    photoRadiant.paste(im2, (512, 0))
    photoRadiant.paste(im3, (512*2, 0))
    photoRadiant.paste(im4, (512*3, 0))
    photoRadiant.paste(im5, (512*4, 0))
    photoRadiant.paste(im6, (0, 1230))
    photoRadiant.paste(im7, (512, 1230))
    photoRadiant.paste(im8, (512*2, 1230))
    photoRadiant.paste(im9, (512*3, 1230))
    photoRadiant.paste(im10, (512*4, 1230))
    photoRadiant.save("photo1.jpg")
    photoRadiant = Image.open("photo1.jpg").resize((531, 291))
    photoRadiant.save("photo.jpg")
    return photoRadiant