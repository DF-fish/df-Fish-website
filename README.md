# df-Fish-website
Django Weblog -- introductory data science

To get this code running on your windows machine:

1. Make sure you have the newest version of Python installed.
2. Create a directory for your project files.  (c:\users\user_name\DF-Website-Main)
3. Start up the command line as administrator
4. Navigate to the directory you created in step two by running `CD c:\users\user_name\DF-Website-Main` and then run `python -m venv data-fish-env` to create your virtual environment (VE). (data-fish-env is what I named my virtual environment, but you can name yours whatever you like)
5. Navigate to the VE by running `CD c:\users\user_name\DF-Website\data-fish-env\Scripts` and activate the VE by navigating to data-fish-env and running `activate`.
6. Navigate to the directory you created in step two by running `CD c:\users\user_name\DF-Website-Main` and then run `git clone https://github.com/DF-fish/df-Fish-website`
7. Navigate to `c:\TheDataFish\df-Fish-website` and run the command: `pip install -r requirements.txt` to install all of the requirements for this project into the VE.
8. Make all your migrations by running `python manage.py makemigrations`, which will create a script for django to create the database for your project.  Then run `python manage.py migrate` so django can create the database using the migrations it created.
9. Now you should now be able to run your project from the folder by using the manage.py script.  The command to run it is: `python manage.py runserver`.  When you open a browser at localhost:8000 you should be able to see that site running in the development environment :)
10. Then you will have to Ctrl-C to stop the dev server, then navigate to the project `CD c:\users\user_name\DF-Website-Main\DF-Fish\df-Fish-website` and run `python manage.py runserver`. 
