from django.http import JsonResponse
import json

from database_models.models import Users

# @Anupam
# import projects table from database_models.models
# import project_owner table from database_models.models
# Both the tables doesn't yet exist create it there

project_id  = 0

def generate_project_id():
    project_id = project_id + 1
    return project_id

    if(request.method=='POST'):
def createProject(request):
        input_json = json.loads(request.body)

        email = input_json['email']
        password = input_json['password']
        title = input_json['title']
        members = input_json['members']
        start_date = input_json['startDate']
        end_date = input_json['endDate']
        skills_required = input_json['skillsRequired']
        mentor = input_json['mentor']
        description = input_json['description']
        project_id = generate_project_id()

        try:
            user = Users.objects.get(email=email)
            if(password == user.password):
                '''
                    Verified email and password

                    TODO: @Anupam
                    --------------
                    1. Validate if all entries are present.

                    2. Do any other required validations

                    3. Create an entry in "project_owner" table email, project_id in table

                    4. Create an entry in table "projects" with project_id,members,title, start_date, end_date, skills_required, mentor, description

                    5. Return success message as JSON
                '''
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


def deleteProject(request):
    if(request.method=='POST'):
        input_json = json.loads(request.body)

        email = input_json['email']
        password = input_json['password']
        project_id = input_json['projectId']

        try:
            user = Users.objects.get(email=email)
            if(password == user.password):
                '''
                    Verified email and password

                    TODO: @Anupam
                    --------------
                    1. Check if project_id is valid
                    2. Check if 'email' is owner of the project
                    3. Remove the entry from both the tables
                    4. Return Success Message as JSON

                '''
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
