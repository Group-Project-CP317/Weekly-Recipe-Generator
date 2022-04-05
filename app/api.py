from django.shortcuts import render, redirect, get_object_or_404
import requests , json

class Api():
    def __init__(self):
        self.recipe_api_key_head = {
            'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
            'x-rapidapi-key': "1854f2c48amshad3ccc45453e6dep1253c2jsne2afdcdb4fe3",
        }


class Recipe(Api):
    def __init__(self):
        Api.__init__(self)

    def get_random_recipe(self,tags = "",number = 1):
        querystring = { "tags":tags , "number":number }
        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"
        response = requests.request("GET", url, headers=self.recipe_api_key_head, params=querystring)
        return response
    

    def search_recipe(self,name = "Pasta",diet = "",cusine =" ",exclude_ing = "",intolerances = "",type="",number=1,offset = 0):

        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"

        querystring = {"query":name,"number":number,"diet":diet,"excludeIngredients":exclude_ing,"intolerances":intolerances,"offset":offset,"type":type,"cuisine":cusine}

        response = requests.request("GET", url, headers=self.recipe_api_key_head, params=querystring)

        return response


    def get_recipe_info_by_id(self,id = "535835"):
        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/"+id+"/information"
        response = requests.request("GET", url, headers=self.recipe_api_key_head)
        return response 


    def write_json(self,response,key,filename='db.json'):
        with open(filename,'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data[key] = response.text 
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)
    
    def read_json(self,key,filename="db.json",open_f = True):
        
        data = json.load(open(filename))
        
        data[key] = json.loads(data[key])
        
        return  data[key]

    def get_recipe_nutrition_by_id(self,id = "535835"):
        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/1003464/nutritionWidget.json"

        response = requests.request("GET", url, headers=self.recipe_api_key_head)
        return response 