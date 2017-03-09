from flask import Flask
import mlab
from models.task import Task
from flask_restful import Api
from resources.task_resource import *

mlab.connect()
app = Flask(__name__)
api = Api(app)

# task = Task(name="Quan", local_id="hsjdhaskj123", done=False)
# task.save()

all_tasks = Task.objects()
# for task in all_tasks:
#     print(mlab.item2json(task))

# my_task = Task.objects(name="Quan").first()
# print(mlab.item2json(my_task))

# my_task.update(set__done=True)

# my_task.delete()



api.add_resource(TaskListRes, "/tasks")
api.add_resource(TaskRes, "/tasks/<task_id>")
api.add_resource(TaskUpdateRes, "/task/<task_id>")
api.add_resource(TaskDelRes, "/task/<task_id>")

if __name__ == '__main__':
    app.run()
