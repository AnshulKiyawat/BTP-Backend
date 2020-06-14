# BTP-Backend

WHILE UPLOADING TO GIT, DO NOT PUSH THE RUNTIME GENERATED FILES
- Any __pycache__ directories
- Any mongo/sql databases generated during runtime

Keep all the __init.py__ files. They need to  empty files. They are used by python to identify directories


Executing:
1. Install python
2. Install django
3. Navigate to folder having manage.py
4. $ python3 manage.py migrate --run-syncdb
5. $ python3 manage.py runserver

(Use python2 if you want. Also need to standardize this as syntax is slightly different and will cause compile time problems)

#TODO: 
Create a gitignore file that ignores all pycache and databases. @Anshul...can you do it?

Important files
- btp/urls.py: Defines urls through which we can call apis
- api folder: Has functionality of apis
- init files: Leave them blank. Used to define directories
- Rest of the files: Settings files. Don't meddle if you don't know django and are not using a reference 
