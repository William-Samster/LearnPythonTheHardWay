#this is the 14th exercise of the book about prompting and passing

from sys import argv

script, user_name = argv
prompt = ">"

print(f"Hi {user_name}, I am {script} script")
print("I would like to ask you a few questions")

#print(f"Do you like me {user_name}?")

likes = input("Do you like me? >")
location = input("where do you live? >")
computer = input("What kind of computer do you have? >")

print(f"""
    Alright! So you said {likes} to whether you like me or not
    and you live in {location} and use a {computer}
    """
)
