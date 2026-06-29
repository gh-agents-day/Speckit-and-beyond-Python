import os

from flask import Flask, jsonify, request, send_from_directory

from taskmanager.model import Task
from taskmanager.repository import TaskRepository
from taskmanager.service import TaskService

# Paths relative to project root (two levels up from this file)
_BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
_DATA_FILE = os.environ.get(
    "APP_DATA_FILE", os.path.join(_BASE_DIR, "data", "tasks.json")
)
_STATIC_DIR = os.path.join(_BASE_DIR, "src", "static")

app = Flask(__name__)

_repository = TaskRepository(data_file=_DATA_FILE)
_service = TaskService(_repository)


# ── Frontend ──────────────────────────────────────────────────────────────────

@app.get("/")
def index():
    return send_from_directory(_STATIC_DIR, "index.html")


# ── API ───────────────────────────────────────────────────────────────────────

@app.get("/api/tasks")
def get_all_tasks():
    tasks = _service.get_all_tasks()
    return jsonify([t.to_dict() for t in tasks])


@app.get("/api/tasks/<task_id>")
def get_task(task_id: str):
    task = _service.get_task_by_id(task_id)
    if task is None:
        return "", 404
    return jsonify(task.to_dict())


@app.post("/api/tasks")
def create_task():
    data = request.get_json(force=True)
    task = Task.from_dict(data)
    created = _service.create_task(task)
    return jsonify(created.to_dict()), 201


@app.put("/api/tasks/<task_id>")
def update_task(task_id: str):
    data = request.get_json(force=True)
    task = Task.from_dict(data)
    updated = _service.update_task(task_id, task)
    if updated is None:
        return "", 404
    return jsonify(updated.to_dict())


@app.delete("/api/tasks/<task_id>")
def delete_task(task_id: str):
    deleted = _service.delete_task(task_id)
    if not deleted:
        return "", 404
    return "", 204
