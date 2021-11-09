# Smart Fridge

## Team Members
Shreeya Jain: sj3131 <br>
Shivang Bharadwaj: sb4539

## Access Information 
UNI used to access the database: sb4539 <br>
URL of web application: http://35.231.48.22:5000/

## Setup Instructions (edit)
1. Install all dependencies
2. Create sqlite database:
    * `flask db init`
    * `flask db migrate`
    * `flask db upgrade`
    * `python add_data.py`
3. Run the application `python run.py`

## Objective
Our objective was to construct a web-based Smart Refrigerator Management System that allows the user to manage the refrigerator contents and shopping lists efficiently. It includes functionalities such as adding new items along with their category, quantity, price, expiry date, and store information, removing or updating existing items, and alerting the user when an item is about to expire. This helps the user view the contents of the refrigerator remotely, prevents food wastage by keeping a track of the expiry dates, automatically generates a shopping list based upon expired or expiring items, and regulates the temperature 
setting for each location to improve the shelf life of items. All the functionalities mentioned in the proposal and as specified above have been implemented.
Additionally, each user can now view a summary of his/her spending habits in the form of 'total money spent on current contents across all fridges', 'total 
money spent on current contents in each fridge', and 'total money spent on current contents in each category across all fridges'. Each user can also update his 
profile information such as name, email, address, country code, phone, and budget.

## Web Pages

### Landing Page:
The Landing Page is the first web page in the application, where a user can either login or register. This functionality is provided by two clickable texts that 
are hyperlinked to the login and register web pages, respectively. 

### Register Page:
The Register Page registers a new user by adding his name, email, address, country code and phone number, budget, login ID, and password information to the user 
and login tables. The application validates the email and password according to their respective regular expressions -- email should look like abc@gmail.com 
and xy@hot.in but not abc@g.in or  xy@hot.i or abc@gmail or xy.in while the password should contain 8 characters of which there is at least 1 lowercase, 1 
uppercase, 1 digit, and 1 symbol. Additionally, the user budget should be positive and the email, phone, and login ID should be unique for each user.

### Login Page:
The Login Page authenticates the user with the login information stored in the login table and throws an error if the username or password is incorrect.

### Dashboard Page:
The Dashboard Page is the most important page for each user as it provides a list of hyperlinked fridges owned by the user, summary of the user's spending habits, 
functionality to add a new fridge for the user, and functionality to edit the user profile. The clickable text for each fridge's nickname will direct you to the
fridge web page. The spending summary is obtained by individual select queries that join the stores, fridge, and category tables and provides an aggregated sum 
of the price of contents for each group. The inputs on the page result in an insert query that adds the user id and fridge model and nickname into the fridge 
table. The edit profile clickable text directs you to the profile web page.

### Profile Page:
The Profile Page provides the user with his stored name, email, address, country code, phone, and budget information as textbox placeholders and allows the user
to edit any and all textboxes. The Update button results in an update query for the users table. 

### Fridge Page:
The Fridge Page provides a list of contents stored in the fridge along with its name, amount, unit, price, store, and category information and allows the user to
edit or delete existing contents, add a new content, create a shopping list, or edit the temperature settings. The content summary is obtained by a select query
that joins the stores, content, and category tables. Edit, delete, add item, and create shopping list are clickable texts that direct you to the edit, delete,
add, and shopping web pages, respectively. The location and temperature settings are obtained by a select query on the settings table while the inputs on the 
page and the submit button result in an update query on the settings table.

### Edit Page:
The Edit Page allows the user to edit the quantity of an existing content in the fridge. The name, category, price, and current quantity information is obtained
by a select query on the join of the stores, content, and category tables while the inputs on the page and the submit button result in an update query on the 
stores table. Note that the application throws an error when the new quantity is less than or equal to 0.

### Add Page:
The Add Page allows the user to add a new content to the fridge. The inputs on the page and the submit button result in an insert query on the stores table. 
This web page is especially interesting as it refers to the contents and categories already stored in the contents and category tables. When a user selects an 
existing content from the drop down menu, the application does not let him/her choose the category, since the application already knows this information. On the 
other hand, when the user adds a new content, the application runs an insert query on the content table first and then runs an insert query on the stores table.

### Shopping Page:
The Shopping List page provides the user with a shopping list -- a new shopping list is created every time the user is directed to this page. The shopping list
is obtained by a select query on the join of the stores, content, and category tables for contents that have expired or are expiring in the next 2 weeks. 
This provides the user essential information about expired or soon-to-expire items in the fridge.
