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
   - **macOS**: SQLite comes pre-installed. You can check the version by running `sqlite3 --version` in your terminal.
   - **Linux**: Install SQLite using your package manager. For example, on Ubuntu or Debian-based systems, run:
DO NOT INSTALL dll for Windows

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
