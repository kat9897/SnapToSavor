import requests
from PIL import Image
import os
from pages.landing_page import *

def compress_img(input_img_path, output_img_path, quality=50):
    try:
        with Image.open(input_img_path) as img:
            img.save(output_img_path, quality=quality)
    except Exception as e:
        print(f"Error: {e}")

#saves a list of the different items!
# img format should be the file path of the image. Ex: /User
def get_ingredients(img):
    api_user_token = 'a4a1d50385dc3ab50a6088a414b031137c87308c'
    headers = {'Authorization': 'Bearer ' + api_user_token}

    # Compression
    input_image_path = img
    output_image_path = "./img/compressed_image.jpg"
    compress_img(input_image_path, output_image_path)
    img = output_image_path

    # Single/Several Dishes Detection
    url = 'https://api.logmeal.es/v2/image/segmentation/complete'
    resp = requests.post(url,files={'image': open(img, 'rb')},headers=headers)

    # Ingredients information
    url = 'https://api.logmeal.es/v2/recipe/ingredients'
    response = requests.post(url,json={'imageId': resp.json()['imageId']}, headers=headers)
    final_info = response.json() # display ingredients info

    food_name = final_info['foodName']
    return food_name


# Test of the call
# food_name_test = get_ingredients(selected_files)
# print(food_name_test)
