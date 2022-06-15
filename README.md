
# Django Models Activity (Zuri)

Create a simple Django App using Zuri Student ID (I4G013983ANI) as name of project

## TASK
- created repo on github
- cloned repo to local
- Created VirtualEnviroment env
- Created a new app *blog* and added to **INSTALLED_APPS**
- Created model **Post** inside *blog*

## Post Requirements
- Title : A string of maxlength 200, use Django’s models.CharField
- Text : Any amount of text, use Django’s TextField
- Author : A Foreign Key to the current user model. Make use of Django’s get_user_model function.
- Created_date : A date-time column, use Django’s models.DateTimeField. 
- Published_date : A date-time column, use Django’s models.DateTimeField. 
