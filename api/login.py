from django.http import JsonResponse
import json

def signUp(request):
    if(request.method=='POST'):
        input_json = json.loads(request.body)

        email = input_json['email']
        first_name = input_json['firstName']
        last_name = input_json['lastName']
        password = input_json['password']
        print(email)
        print(first_name)
        print(last_name)
        print(password)
        '''
        TODO:
        -----
        Check if email already present in database.
        If not, add email, pwd, firstname,lastname to database and return "SUCCESS"
        If yes, return message "FAILURE"
        '''
        returnJson={
            'message': "SUCCESS"
        }
        return JsonResponse(returnJson)
