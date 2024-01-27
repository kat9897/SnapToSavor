import requests

img = '/Users/marilynzhang/Desktop/Banana-4183238557.jpg' 
api_user_token = 'f08be828bbf2a3a4c1185de9ff1cc307b15875be'
headers = {'Authorization': 'Bearer ' + api_user_token}

# Single/Several Dishes Detection
url = 'https://api.logmeal.es/v2/image/segmentation/complete'
resp = requests.post(url,files={'image': open(img, 'rb')},headers=headers)

# Ingredients information
url = 'https://api.logmeal.es/v2/recipe/ingredients'
response = requests.post(url,json={'imageId': resp.json()['imageId']}, headers=headers)
final_info = response.json() # display ingredients info

food_name = final_info['foodName'][0]
print(food_name)