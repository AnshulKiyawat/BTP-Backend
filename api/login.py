from django.http import JsonResponse

'''
TODO: Remove this comment

@Anupam Don't overcomplicate things

Don't write html, js or any other code for frontend
We are trying to keep backend and frontend separate
This way, we can intergrate any front-end (web/mobile/desktop app)

Simple easy 4 steps to follow:
------------------------------
1. Validate if request is GET/POST/etc
2. Do the backend processing
3. Return JSON
4. (Optional) throw an error if request method is invalid


React will handle calling the apis. It just needs the json as output


Each api/python file defines functionality
Example: this login.py wil have all methods related to login
(like signUp, login, forgotPassword, resetPassword)

All we need from the backend is to take a request, process it and give a json response.

Start with the basic signup functionality

Create a POST request api to signUp
-- takes emailId, password, confirmPassword as parameters from post request
-- checks if email is already taken
-- checks if passwords match
-- checks if email ends in '@lnmiit.ac.in'
-- creates user in database (choose whether mongo or sql)
-- responds with a success json message

React will validate the json and figure out what's happening

You can add hashing and salting later. Just get it running first

You can use apps like Jmeter or extensions like Postman (for chrome browser) to
simulate post requests. Please try to hurry up. We have to finish this by 30th

Sample code shown below:
'''
def sampleHelloWorldApi(request):
    if(request.method=='GET'):
        print(request) #You can check the terminal and see the syntax
        returnJson={
            'helloWorld': 'Hello World'
        }
        return JsonResponse(returnJson)
