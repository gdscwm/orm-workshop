# orm-workshop
Fall 2024 Workshop


## Introduction to Databases 

### What is a Schema?

A **schema** defines db structure. It is a blueprint that outlines the organization of data in terms of tables, columns, data types, and relationships between tables. 

- **Tables**: Collections of related data. Each table in a database represents a specific entity, like "Users" or "Orders."
- **Columns**: Attributes of the table. For example, a "Users" table might have columns such as "id," "name," and "email."
- **Data Types**: Defines the type of data that can be stored in each column (e.g., integers, strings, dates).
- **Constraints**: Rules applied to columns, such as uniqueness, primary keys (which uniquely identify each row locally), and foreign keys (which create relationships between tables).

### Types of Databases

There are different types of databases:

- **Relational Databases**: Store data in structured tables with defined relationships. (SQLite, MySQL, PostgreSQL, and SQL Server)
- **Non-Relational (NoSQL) Databases**: Stores unstructured data, ie documents, key-value pairs, or graphs. (MongoDB, Redis)

## SQL Lite 

### What is SQLite?

**SQLite** is a relational database, that stores all its data in a single file.

### Step-by-Step Instructions

1. **Open Your Terminal or Command Prompt**:

   Open your terminal (macOS/Linux) or command prompt (Windows) to start working with SQLite.

2. **Install SQLite (if not already installed):**

   - **Windows**: Download the SQLite tools from the [SQLite Download Page](https://www.sqlite.org/download.html) and extract the files to a directory (e.g., `C:\sqlite`). Add this directory to your system's PATH.
   - DO NOT INSTALL dll for Windows

   To add a variable to your path in Windows:

   Right-click on the Start Button

   Select “System” from the context menu.

   Click “Advanced system settings”

   Go to the “Advanced” tab

   Click “Environment Variables…”

   Click variable called “Path” and click “Edit…”

   Click “New”
  
   - **macOS**: SQLite comes pre-installed. You can check the version by running `sqlite3 --version` in your terminal.
   - **Linux**: Install SQLite using your package manager. For example, on Ubuntu or Debian-based systems, run:


   ```bash
   sudo apt-get install sqlite3


### Creating SQLite File 

To create a new SQLite database use this in the command prompt: ``` sqlite3 example_db.db ```

This will create a new database called example_db. 

You can create an example table using: 

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);
```

This will create a table with id, name, and email columns.
You can change the name of field or add more.

To add some example data you can do: ``` INSERT INTO users (name, email) VALUES ('Random User', 'random@example.com'); ```
     
To view all users you can use the wildcard operator: ``` SELECT * FROM users; ```

### OOP Review 

Classses, objects, inheritance, encapsulation, polymorphism 

## Object Relational Model

### Orm interacts with a database using a programming language instead of doing direct SQL queries.
You can do database queries through python instead of directly with SQL. 

## Python setup 

### Create Python env

To set up a python env use: ```python -m venv venv```

Activate the env with: ``` source venv/bin/activate``` 
On Windows use: ``` venv\Scripts\activate ```

Install the requirements file with: ``` pip install -r requirements.txt ```
This will install all of the needed libraries. 

### Create Basic schema file. 

File is stored under workshop1 ```models.py```

## Workshop 2


There is a file in the workshop1 folder named models.py containing a basic database schema.
If you missed the first workshop you can clone the git repo and run that file, or download it to your local directory if you don't have git installed.

Run the ```models.py``` file from the last workshop. It should create a database file in your local directory named example.db

If there is an error or you cannot figure something out ask one of the GDSC memebers for assistance. You may be missing something from the previous workshop. 



### Review
We have gone through creating a database with sqlite and creating a basic schema for a database using ORM with Python. 

### Connect to DB

Now let's connect to the database and add some data. 

In the same directory(folder) as the previous databasee schema was created, create a file called ```add_data.py```

Go ahead and run the ```models.py``` file from the last workshop as well.

In the new file, we need to import some sql libraries and include the imports from the classes we created.

Include these lines at the top of the new ```add_data.py``` file.

```
from sqlalchemy import create_engine
from models import Base, User  
from sqlalchemy.orm import sessionmaker
```

Now we can create an instance of the db session and add some data. 

To connect to the db create a create_engine session. 

```
engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()
```
### OOP 

Last workshop we talked about OOP Programming.
One of the benefits is we can easily add new users from the class we created.

Let's look at the fields we need for creating a new user.
How do you think we would structure code for adding a user to the Database?

Each user will need a name and email. 
Let's go ahead and create some users to put into our DB. 

```
user1 = User(name='John Doe', email='john@example.com')
user2 = User(name='Jane Smith', email='jane@example.com')
```

And we need to use session.add() for the db instance. 

```
session.add(user1)
session.add(user2)


session.commit()
```

Let's include a print statment to make sure the users got added to the db.

```print("Sample data added successfully!")```

Run the script to see that the data was added.

Databases support a number of actions to manipulate data:

- INSERT creates a new entry in a table. When you run session.add(...) you are performing an INSERT operation
- SELECT is used to read data from a table. You can apply a number of query params to this retrieve only the records that match specific criteria. This is useful when you have a table with hundreds of entries, we don't want to return all of that to the user at once. We will see how to use this shortly.
- UPDATE is used to update existing records.
- DELETE is used to delete records.
- JOIN is used to select records from a second table based on records that have been selected from the first. We will see how this is used later on. 

We probably also want to see the data we included in the db. Go add and include a statement for viewing all of the users. 
We can use OOP to access the attributes of our users in a for loop. 

```
users = session.query(User).all()
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
```

If everything was done correctly, the users id, name, and email will be printed.

To query only data that matches specific criteria you can use the `filter()` function:
```
filtered_users = session.query(User).filter(User.name == "John Doe")
for user in filtered_users:
    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
```

Only John Doe's information should be printed.

## Creating another table.

Now we have a database, we can connect to the database, and we can populate in with data.

Let's add another table to the database.

Following the syntax we used to create the Base class, we can create another table called Post and use it to store user's posts.

We will add to import some new properties for the new table.
Make sure relationship has been imported from sqlalchemy.orm.

```from sqlalchemy.orm import relationship```

And include Foreign Key.

``` from sqlalchemy import Column, Integer, String, create_engine,ForeignKey ```

Let's create a Post class for the new table. 

```
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
```

We need a few more things to add to the class. We want to create a relationship between the User and the Post tables. Let's use a ForeignKey to connected the tables.

```user_id = Column(Integer, ForeignKey('users.id'))```
We can also establish a relationship between the author (User) and the post.
```author = relationship('User', back_populates='posts')```

Now the Post class has been connected to the User class, but we still have to connect the User class to the Post class.

Go into the User class and add this line after posts to do that:
```posts = relationship('Post', back_populates='author')```

Run the ```models.py``` file. It should run without error. If there is an error ask one of the GDSC memebers for assistance. 

## Add a post

Now go into the add_data.py file and create a post.

```post1 = Post(title='Hello World', content='This is my first post!', author=user1)```

Add the post to the session. 

``` session.add(post1) ```

And print out the post:

```
for post in user.posts:
        print(f"  Post ID: {post.id}, Title: {post.title}, Content: {post.content}")
```

Cool, now we can connect multiple attributes of a database! This is an example of a JOIN statement as mentioned earlier. 
