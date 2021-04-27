Intro:
    An api that allows users to create flashcards, connected to a 
    react frontend.


Setup:

   python3 -m venv venv
   
   source env/bin/activate

   pip install -r requirements.txt

   cd into directory 

   python manage.py createsuperuser

   python manage.py runserver

Overview: 

    Navigate to http://127.0.0.1:8000/api/flashcards/ to view or create flashcards
    
    
    Navigate to http://127.0.0.1:8000/api/flashcards/<int:id>/ to delete flashcards



    Fields that user can input data:

        Question
        Answer


   
