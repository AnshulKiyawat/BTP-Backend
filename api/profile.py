from django.http import JsonResponse
import json

from database_models.models import Users

def get_profile_details(request):
    if(request.method=='POST'):
        input_json = json.loads(request.body)
        email = input_json['email']
        password = input_json['password']
        
        try:
            user = Users.objects.get(email=email)
            if(password == user.password):
                first_name= user.first_name
                middle_name= user.middle_name
                last_name= user.last_name
                profile_description= user.profile_description
                phone = user.phone
                date_of_birth = user.date_of_birth
                gender = user.gender
                returnJson={
                    'message': "SUCCESS",
                    'reason' : "Correct Details Entered",
                    'response':{'first_name':first_name,
                                'middle_name':middle_name,
                                'last_name': last_name,
                                'profile_description':profile_description,
                                'date_of_birth':date_of_birth,
                                'phone':phone,
                                'gender':gender,
                                'email':email
                                }
                }
            else:
                returnJson={
                    'message': "FAILURE",
                    'reason' : "Wrong password"
                }
        except Exception as e:
                print(e)
                returnJson={
                    'message': "FAILURE",
                    'reason': "Incorrect user id provided"
                }

    else:
        returnJson={
            'message': "FAILURE",
            'reason': "Server could not process the data sent."
        }

    return JsonResponse(returnJson)


def edit_profile_details(request):
    if(request.method=='POST'):
        input_json = json.loads(request.body)
        print('DEBUGGING:')
        print(input_json)
        email = input_json['email']
        password = input_json['password']
        middle_name = input_json['middle_name']
        first_name = input_json['first_name']
        last_name = input_json['last_name']
        profile_description = input_json['description']
        gender = input_json['gender']
        date_of_birth = input_json['date_of_birth']
        phone = input_json['phone']
        
        try:
            user = Users.objects.get(email=email)
            if(password == user.password):
                if len(first_name) == 0:
                    returnJson={
                        'message': "FAILURE",
                        'reason': "First name is necessary"
                    }
                else:
                    Users(email=email,password=password,first_name=first_name,middle_name=middle_name, last_name=last_name,profile_description=profile_description,gender=gender,date_of_birth=date_of_birth,phone=phone).save()
                    returnJson={
                            'message': "SUCCESS",
                            'reason': "User created"
                    }

                
            else:
                returnJson={
                    'message': "FAILURE",
                    'reason' : "Wrong password"
                }
        except Exception as e:
                print(e)
                returnJson={
                    'message': "FAILURE",
                    'reason': "Incorrect user id provided"
                }

    else:
        returnJson={
            'message': "FAILURE",
            'reason': "Server could not process the data sent."
        }

    return JsonResponse(returnJson)
