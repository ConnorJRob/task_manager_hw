from db.run_sql import run_sql
from models.task import Task
from models.user import User
from repositories import user_repository

#(CRUD) - READ-ALL
def select_all():
    # create an empty tasks list
    tasks = []
     # create a SQL statement
    sql = "SELECT * FROM tasks"
    # execute a SQL statement
    # get results
    results = run_sql(sql)
    # I want to get a list of Task objects returned
    for row in results:
        user = user_repository.select(row['user_id'])
        task = Task(
            row['description'],
            user,
            row['duration'],
            row['completed'],
            row['id'])
        tasks.append(task)
    return tasks

#(CRUD) - CREATE 
def save(task):
    sql = "INSERT INTO tasks(description, user_id, duration, completed) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [task.description, task.user.id, task.duration, task.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    task.id = id
    return task

#(CRUD) - READ-ONE
def select(id):
    task = None
    sql = "SELECT * FROM tasks WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result != None:
        user = user_repository.select(result['user_id'])
        task = Task(result['description'], user, result['duration'], result['completed'], result['id'])
    return task

#(CRUD) - DELETE-ALL
def delete_all():
    sql = "DELETE FROM tasks"
    run_sql(sql)

#(CRUD) - DELETE-ONE
def delete_one(id):
    sql = "DELETE FROM tasks WHERE id = %s"
    values = [id]
    run_sql(sql, values)

#(CRUD) - UDATE-ONE
def update_one(task):
    sql = "UPDATE tasks SET (description, assignee, duration, completed) = (%s, %s, %s, %s) WHERE id = %s"
    values = [task.description, task.user.id, task.duration, task.completed, task.id]
    run_sql(sql, values)