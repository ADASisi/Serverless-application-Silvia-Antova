import azure.functions as func
import logging
import json
import pyodbc

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="first_trigger")

def first_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    
def function_1(req: func.HttpRequest) -> func.HttpResponse:
    movies = []
    try:
        req_body = req.get_json()
        movie_info = {
            'Title': req_body.get('title'),
            'Year': req_body.get('year'),
            'Genre': req_body.get('genre'),
            'Description': req_body.get('description'),
            'Director': req_body.get('director'),
            'Actors': req_body.get('actors')
        }
        movies.append(movie_info)

        return func.HttpResponse("Movie information saved successfully", status_code=200)
    except Exception as e:
        return func.HttpResponse(f"An error occurred: {str(e)}", status_code=500)
    

def second_trigger(req: func.HttpRequest) -> func.HttpResponse:
    ratings = []
    try:
        req_body = req.get_json()
        rating_info = {
            'Title': req_body.get('title'),
            'Opinion': req_body.get('opinion'),
            'Rating': req_body.get('rating'),
            'Date_Time': req_body.get('date_time'),
            'Author': req_body.get('author')
        }
        ratings.append(rating_info)

        return func.HttpResponse("Rating information saved successfully", status_code=200)
    except Exception as e:
        return func.HttpResponse(f"An error occurred: {str(e)}", status_code=500)


def third_trigger(req: func.HttpRequest) -> func.HttpResponse:
    try:
        if mytimer.past_due:
            print('The timer is past due!')
        

        average_ratings = {}
        count_ratings = {}
    
        for rating in ratings:
            title = rating['Title']
            rating_value = int(rating['Rating'])
        
        if title not in average_ratings:
            average_ratings[title] = rating_value
            count_ratings[title] = 1
        else:
            average_ratings[title] += rating_value
            count_ratings[title] += 1
    
        for title in average_ratings:
            average_ratings[title] /= count_ratings[title]
        
        print("Average Ratings:")
        for title, average_ratings in average_ratings.items():
            print(f"{title}: {average_ratings}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")


