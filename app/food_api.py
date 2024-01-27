import requests

#saves a list of the different items!
# img format should be the file path of the image. Ex: /User
def get_ingredients(img):
    api_user_token = 'fb5a4c7df78e749b63d71a34cfd375c689a8e441'
    headers = {'Authorization': 'Bearer ' + api_user_token}

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
#food_name_test = get_ingredients('/Users/marilynzhang/Desktop/food_test_2.jpg')
#print(food_name_test)
