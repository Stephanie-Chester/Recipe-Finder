#Import the required library for the HTTP requests
import requests

# Edamam API base URL
API_ENDPOINT = "https://api.edamam.com/search"

# Edamam app ID and app key credentials
APP_ID = "ef8a4e30"
APP_KEY = "d07790d70e60afde31416c1a949bae21"

# Function to search for recipes based on a given query
def find_recipes(query):
    # Parameters to be sent with the API request
    params = {
        "q": query,          # The query search term
        "app_id": APP_ID,    # My Edamam app ID
        "app_key": APP_KEY   # My Edamam app key
    }

    # An HTTP GET request is made to the Edamam API
    response = requests.get(API_ENDPOINT, params=params)

    # If the request was successful (HTTP status code 200)
    if response.status_code == 200:
        # Parse the JSON response and return the 'recipes'
        data = response.json()
        return data['hits']
    else:
        # Print the error code if the request was not successful
        print("Error:", response.status_code)
        return []

# Main function
def main():
    # Get input from the user for the recipe search term
    query = input("Enter a search term for a recipe: ")

# Call the function to search for recipes
    recipes = find_recipes(query)

    # If recipes are found, print them
    if recipes:
        for index, recipe in enumerate(recipes, 1):
            print(f"{index}. {recipe['recipe']['label']} - {recipe['recipe']['url']}")
    else:
        # If no recipes are found, print a message letting the user know
        print("Sorry, no recipes have been found for the ingredient you have entered.")

# This conditional ensures the main function is called only when this script is run directly, 
# and not when imported as a module
if __name__ == "__main__":
    main()
