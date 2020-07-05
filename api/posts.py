from django.http import JsonResponse
import json

from database_models.models import Users
from database_models.models import Posts

def submit_post(request):
    if(request.method=='POST'):
        input_json = json.loads(request.body)

        email = input_json['email']
        password = input_json['password']
        content = input_json['content']
        date_of_post = input_json['dateOfPost']

        print(email)
        try:
            user = Users.objects.get(email=email)
            if(password == user.password):
                print('Verified User')
                Posts(email=email, content=content,date_of_post=date_of_post).save()
                returnJson={
                    'message': "SUCCESS",
                    'reason' : "Successfully added post"
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

def fetch_posts(request):
    if(request.method=='POST'):
        input_json = json.loads(request.body)

        email = input_json['email']
        password = input_json['password']
        
        print(email)
        try:
            user = Users.objects.get(email=email)
            if(password == user.password):
                posts=Posts.objects.all()
                print(posts)
                results = []
                for post in posts:
                    results.append({'email':post.email,'content':post.content,'date_of_post':post.date_of_post})
                returnJson={
                    'message': "SUCCESS",
                    'reason' : "Successfully added post",
                    'results': results
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
