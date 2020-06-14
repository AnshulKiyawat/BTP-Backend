from django.http import JsonResponse
import json

from database_models.models import Users


def signUp(request):
    if(request.method=='POST'):
        input_json = json.loads(request.body)

        email = input_json['email']
        first_name = input_json['firstName']
        middle_name = input_json['middleName']
        last_name = input_json['lastName']
        password = input_json['password']

        try:
            Users.objects.get(email=email)
            returnJson={
                'message': "FAILURE",
                'reason' : "User Already Exists"
            }
        except:
            if not email.endswith('@lnmiit.ac.in'):    
                returnJson={
                    'message': "FAILURE",
                    'reason': "Email does not end with '@lnmiit.ac.in'"
                }
            elif len(first_name) == 0:
                returnJson={
                    'message': "FAILURE",
                    'reason': "First name is necessary"
                }
            elif len(password) < 8:
                returnJson={
                    'message': "FAILURE",
                    'reason': "Password less than 8 characters"
                }
            elif len(password) > 30:
                returnJson={
                    'message': "FAILURE",
                    'reason': "Password longer than 30 characters"
                }
            elif not any(char.isdigit() for char in password):
                returnJson={
                    'message': "FAILURE",
                    'reason': "Password should have atleast one digit from 0-9"
                }
            elif not any(char.isupper() for char in password):
                returnJson={
                    'message': "FAILURE",
                    'reason': "Password should have atleast one uppercase ASCII character"
                }
            elif not any(char.islower() for char in password):
                returnJson={
                    'message': "FAILURE",
                    'reason': "Password should have atleast one lowercase ASCII character"
                }
            elif not any(char in ['!','@','#','$','%','^','&','*','(',')'] for char in password):
                returnJson={
                    'message': "FAILURE",
                    'reason': "Password should have atleast special symbol among: !,@,#,,$,%,^,&,*,(,)"
                }
            else:
                 Users(email=email,password=password,first_name=first_name,last_name=last_name).save()
                 returnJson={
                    'message': "SUCCESS",
                    'reason': "User created"
                }

    else:
        returnJson={
            'message': "FAILURE",
            'reason': "Server could not process the data sent."
        }
        
    return JsonResponse(returnJson)
