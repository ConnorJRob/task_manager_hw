import pdb
from models.task import Task
from models.user import User

import repositories.task_repository as task_repository
import repositories.user_repository as user_repository

## deletes all rows from the database
# task_repository.delete_all()

# ## adds a new entry to the database
# task_1 = Task("Get Lunch", "John", 65, False)
# task_repository.save(task_1)

##task_1.mark_complete()
# task_repository.update_one(task_1)

## Using the select all function to search for and return all rows from the database table
# results = task_repository.select_all()

## prints the task objects retrtieved as dictionaries
# for task in results:
#     print(task.__dict__)

## The below print will just print the results as a list of objects
# print(results)

# #Using the select function to search for and return a single row from the database table using the given id - 1
#     # This will only work if the id number given currently exists in the database and has not been deleted
# print(task_repository.select(1))

user_repository.delete_all()
task_repository.delete_all()

user1 = User("Jack", "Jarvis")
user_repository.save(user1)

user2 = User("Victor", "McDade")
user_repository.save(user2)

task = Task("Walk Dog", user1, 60)
task_repository.save(task)

task2 = Task("Walk Cat", user1, 20)
task_repository.save(task2)

# for user in user_repository.select_all():
#     print(user.__dict__)

# for task in task_repository.select_all():
#     print(task)

# pdb.set_trace()

for task in (user_repository.tasks(user1)):
    print(task.__dict__)
