
github link - https://github.com/samlessheart/LibraryManager.git
Herok link - https://librarymanagersam.herokuapp.com

This project have 3 main sections One consist Books and author models
one consist of User models
and one consist of Passbook model which record information of Borrowed and return books it also keeps information of due charges and etc

as a user you can see all the books you can borrow a book and you can return book you can see borrowed books in your dashboard

as a employee(librarian) you can see all the users you can update delete and create users

create virtual environment
Pull code from github from above link
install packages which are listed in Requirements.txt
run python manage.py makemigrations
run python manage.py migrate 
run python manage.py runserver

open http://127.0.0.1:8000/  in browser to open home page
you can navigate around to explre feature.

about Rest Framework

first you will need to generate JWT token 
go to http://127.0.0.1:8000/api/token/ in browser
input email and password and click on POST to generate tokens

YOu can use the generated access token for authentications.

to Get Book List 
Method = GET
http://127.0.0.1:8000/api/book_list/

To Get A detail of a Book 
mention a id of book in book_id in link
Method= GET
http://127.0.0.1:8000/api/book_detail/{book_id}/

To Update or Delete a book
Method = DELETE, PUT
http://127.0.0.1:8000/api/book_det/{book_id}/

To create a book
Method = POST
http://127.0.0.1:8000/api/book_create/


To get User list
method = GET
http://127.0.0.1:8000/api/user_list/


TO get detail of a user, To delete a user, or update a user  
replace user_id with id of a user
method = GET, PUT, DELETE
http://127.0.0.1:8000/api/user_det/{user_id}/

to borrow a book 
replace book_id with id of a book
method = POST
http://127.0.0.1:8000/api/{book_id}/

to get information of a borrowed books by a user
method = GET
http://127.0.0.1:8000/api/passbook/

to return a book
replace a passbook_id with id of a passbook
method = POST
http://127.0.0.1:8000/api/{passbook_id}/






