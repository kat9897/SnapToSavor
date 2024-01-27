import requests

from .. import API_KEY

def parse_recipe(state):
    res = get_random_recipes(state)
    first_recipe = res["recipes"][0]
    recipe = {
        "RecipeID": first_recipe["id"],
        "RecipeName": first_recipe["title"],
        "Description": "",
        "RecipeThumbnailLink": first_recipe["image"],
        "DatePosted": "",
        "RecipeIngredients": [],
        "Ingredients": []
    }
    for ingred in first_recipe["extendedIngredients"]:
        # RecipeIngredients
        single_rec_ingred = {
            "RecipeID": first_recipe["id"],
            "IngredientID": "",
            "Quantity": 0,
            "QuantityUnit": "ml"
        }
        single_rec_ingred["IngredientID"] = ingred["id"]
        single_rec_ingred["Quantity"] = ingred["measures"]["us"]["amount"]
        single_rec_ingred["QuantityUnit"] = ingred["measures"]["us"]["unitShort"]
        recipe["RecipeIngredients"].append(single_rec_ingred)

        # Ingredients
        ingred_response = get_ingredient(state, int(ingred["id"]))
        single_ingred = {
                "IngredientID": int(ingred["id"]),
                "IngredientName": ingred_response["name"],
                "Description": "",
                "Sugar_g": 0,
                "Sodium_mg": 0,
                "Fats_g": 0,
                "Protein_g": 0,
                "Vitamin_A_mcg": 0,
                "Vitamin_B_mcg": 0,
                "Vitamin_C_mcg": 0,
                "Vitamin_D_mcg": 0,
                "Fiber_g": 0,
                "Calories": 0
        }

        # Nutrients
        for res_nutrient in ingred_response["nutrition"]["nutrients"]:
            res_nutrient_title = res_nutrient["name"].strip()
            if res_nutrient_title in "Sugar":
                single_ingred["Sugar_g"] = res_nutrient["amount"]
            elif res_nutrient_title in "Fat":  
                single_ingred["Fats_g"] = res_nutrient["amount"]
            elif res_nutrient_title in "Protein":
                single_ingred["Protein_g"] = res_nutrient["amount"]
            elif res_nutrient_title in "Sodium":
                single_ingred["Sodium_mg"] = res_nutrient["amount"]
            elif res_nutrient_title in "Vitamin A":
                single_ingred["Vitamin_A_mcg"] = res_nutrient["amount"]
            elif res_nutrient_title in "Vitamin C":
                single_ingred["Vitamin_C_mcg"] = res_nutrient["amount"]
            elif "Vitamin B" in res_nutrient_title:
                single_ingred["Vitamin_B_mcg"] = res_nutrient["amount"]
            elif res_nutrient_title in "Vitamin D":
                single_ingred["Vitamin_D_mcg"] = res_nutrient["amount"]
            elif res_nutrient_title in "Fiber":
                single_ingred["Fiber_g"] = res_nutrient["amount"]
            elif res_nutrient_title in "Calories":
                single_ingred["Calories"] = res_nutrient["amount"]
        recipe["Ingredients"].append(single_ingred)

    print(recipe)

def get_random_recipes(state):
    parameters = {
        "apiKey": API_KEY,
        "number": 5
    }
    response = requests.get("https://api.spoonacular.com/recipes/random", params=parameters)
    res = response.json()
    return res

def get_ingredient(state, id):
    # id = 9266
    heads = {
        "Content-Type": "application/json"
    }
    parameters = {
        "apiKey": API_KEY,
        "amount": 1
    }
    response = requests.get(f"https://api.spoonacular.com/food/ingredients/{id}/information", params=parameters, headers=heads)
    res = response.json()
    return res