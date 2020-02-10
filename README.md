# Let It Zoom!

> Guess What image is

- how to play
  1. type the nickname and press the 'send' to sign up
  2. press the 'start' button and choose category
  3. guess what image is and raise your score!
  4. if you are in the top five, you will be in 'ranking'



- how to run

  1. download 'file_for_run' and 'letitzoom'

  2. run 'letitzoom' in the VS code

  3. make sure the 'settings.py' file code is correct especially below code

     ```python
   DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': '[your DB name]',
             'USER': 'root',
             'PASSWORD': '[your DB password]',
             'HOST': 'localhost',
             'PORT': 3306
         }
     }
     ```
  
     
  
  4. make database named as  'let_it_zoom' in heidSQL
  
  5. Terminal > new Ternimal
  
     ----In Terminal----
  
  6. `python manage.py makemigrations`
  
  7. `python manage.py migrate`
  
     ----In heidSQL----
  
  8. run two .sql files in 'file_for_run'
  
  9. `python manage.py runserver`
  
     *if you get sessions error, run `python manage.py make sessions`



- skills

  - python

    1. crawling : Requests
    2. web server : Django
    3. picture crop : Pillow

  - DB : Mysql

  - other language : JavaScript (JQuery) , HTML , CSS

    

- tools
  - VS code
  - HeidiSQL
  - Web Browser (Chrome)



<img width="947" alt="1_index" src="https://user-images.githubusercontent.com/58927491/74135379-8ebac480-4c2f-11ea-8335-8f44fe682955.PNG">
<br>
<img width="946" alt="3_select_cat" src="https://user-images.githubusercontent.com/58927491/74135407-9b3f1d00-4c2f-11ea-9858-cdcafafad3fa.PNG">
<br>
<img width="944" alt="4_playgame" src="https://user-images.githubusercontent.com/58927491/74135419-9f6b3a80-4c2f-11ea-91ff-8d15dc4e00f8.PNG">
<br>
<img width="953" alt="5_gameover" src="https://user-images.githubusercontent.com/58927491/74135430-a1cd9480-4c2f-11ea-8d41-f4212287a5b9.PNG">
<br>
<img width="910" alt="6_answer" src="https://user-images.githubusercontent.com/58927491/74135446-a4c88500-4c2f-11ea-92c9-4f2ad55cfe7f.PNG">
<br>
<img width="512" alt="2_ranking" src="https://user-images.githubusercontent.com/58927491/74135452-a7c37580-4c2f-11ea-9ccd-177c51974adb.PNG">



- Presentation

![슬라이드1](https://user-images.githubusercontent.com/58927491/74133854-d1c76880-4c2c-11ea-8f00-fbd969bbab43.JPG)
<br>
![슬라이드2](https://user-images.githubusercontent.com/58927491/74133857-d3912c00-4c2c-11ea-8f82-4382b9e76020.JPG)
<br>
![슬라이드3](https://user-images.githubusercontent.com/58927491/74133861-d4c25900-4c2c-11ea-8909-991949f8fa75.JPG)
<br>
![슬라이드4](https://user-images.githubusercontent.com/58927491/74133866-d5f38600-4c2c-11ea-81fb-48c94ed9a7ad.JPG)
<br>
![슬라이드5](https://user-images.githubusercontent.com/58927491/74133875-da1fa380-4c2c-11ea-9e86-faeeea3de589.JPG)
<br>
![슬라이드6](https://user-images.githubusercontent.com/58927491/74133879-dbe96700-4c2c-11ea-95df-dc986354703d.JPG)
<br>
![슬라이드7](https://user-images.githubusercontent.com/58927491/74133880-dd1a9400-4c2c-11ea-9122-d82397a0c942.JPG)
<br>
![슬라이드8](https://user-images.githubusercontent.com/58927491/74133881-de4bc100-4c2c-11ea-9b81-75979db26bf3.JPG)