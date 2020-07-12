from django.http import JsonResponse
import json

from database_models.models import Users
from database_models.models import Projects
from database_models.models import ProjectOwners
project_id  = 0

def generate_project_id():
    try:
        generate_project_id.project_id = generate_project_id.project_id + 1
    except:
        generate_project_id.project_id =0
    return generate_project_id.project_id


def create_project(request):
    if(request.method=='POST'):
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
                 Projects(title=title,members=members,start_date=start_date,end_date=end_date,skills_required=skills_required,mentor=mentor, description=description,project_id=project_id).save()
                 ProjectOwners(email=email,project_id=project_id).save()
                 returnJson={
                    'message': "SUCCESS",
                    'reason': "Project created"
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


def fetch_projects(request):
    if(request.method=='POST'):
        input_json = json.loads(request.body)

        email = input_json['email']
        password = input_json['password']
        try:
            project_ids = []
            return_values= []
            user = Users.objects.get(email=email)
            if(password == user.password):
                 project_owners = ProjectOwners.objects.all()
                 projects= Projects.objects.all()
                 for project_owner in project_owners:
                    if(project_owner.email == email):
                        project_ids.append(project_owner.project_id)
                 for project in projects:
                    for project_id in project_ids:
                        if(project.project_id == project_id):
                            return_values.append({'title':project.title, 'members':project.members, 'startDate':project.start_date, 'endDate':project.end_date,'skills_required':project.skills_required, 'mentor':project.mentor, 'description':project.description, 'project_id':project.project_id })
                 print(return_values)

                 returnJson={
                    'message': "SUCCESS",
                    'reason': "Project created",
                    'return_value': return_values
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


"""
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
"""
