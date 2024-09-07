#example adding data
from sqlalchemy import create_engine
from models import Base, User, Post  
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

user1 = User(name='John Doe', email='john@example.com')
user2 = User(name='Jane Smith', email='jane@example.com')

session.add(user1)
session.add(user2)

post1 = Post(title='Hello World', content='This is my first post!', author=user1)

session.add(post1)

session.commit()

print("Sample data added successfully!")


users = session.query(User).all()
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
    for post in user.posts:
        print(f"  Post ID: {post.id}, Title: {post.title}, Content: {post.content}")