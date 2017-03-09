from flask_restful import Resource, reqparse
from models.task import Task
import mlab

class TaskListRes(Resource):
    def get(self):
        tasks = Task.objects()
        tasks_json = mlab.list2json(tasks)
        return tasks_json

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(name="name", type=str, location="json")
        parser.add_argument(name="local_id", type=str, location="json")
        parser.add_argument(name="done", type=str, location="json")
        body = parser.parse_args()

        name = body["name"]
        local_id = body["local_id"]
        done = body["done"]

        task = Task(name=name, local_id=local_id, done=done)

        task.save()

        added_task = Task.objects().with_id(task.id)
        return mlab.item2json(added_task)

class TaskRes(Resource):
    def get(self, task_id):
        task = Task.objects().with_id(task_id)
        return mlab.item2json(task)

class TaskDelRes(Resource):
    def delete(self, task_id):
        task = Task.objects().with_id(task_id)
        if task == None:
            return {"message": "Task not found"}
        else:
            task.delete()
            return {"message": "Deleted successfully"}

class TaskUpdateRes(Resource):
    def put(self, task_id):
        task = Task.objects().with_id(task_id)

        parser = reqparse.RequestParser()
        parser.add_argument(name="name", type=str, location="json")
        parser.add_argument(name="local_id", type=str, location="json")
        parser.add_argument(name="done", type=str, location="json")
        body = parser.parse_args()

        name = body["name"]
        local_id = body["local_id"]
        done = body["done"]

        task.update(name=name, local_id=local_id, done=done)

        updated_task = Task.objects().with_id(task.id)
        return mlab.item2json(updated_task)
