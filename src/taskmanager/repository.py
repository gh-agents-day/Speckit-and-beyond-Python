import json
import os
from typing import List, Optional

from taskmanager.model import Task


class TaskRepository:

    def __init__(self, data_file: str = "data/tasks.json"):
        self.data_file = data_file
        self._ensure_file_exists()

    def _ensure_file_exists(self) -> None:
        parent = os.path.dirname(self.data_file)
        if parent:
            os.makedirs(parent, exist_ok=True)
        if not os.path.exists(self.data_file):
            with open(self.data_file, "w", encoding="utf-8") as f:
                json.dump([], f)

    def find_all(self) -> List[Task]:
        with open(self.data_file, "r", encoding="utf-8") as f:
            return [Task.from_dict(item) for item in json.load(f)]

    def find_by_id(self, task_id: str) -> Optional[Task]:
        return next((t for t in self.find_all() if t.id == task_id), None)

    def save(self, task: Task) -> Task:
        tasks = self.find_all()
        tasks = [t for t in tasks if t.id != task.id]
        tasks.append(task)
        self._persist(tasks)
        return task

    def delete_by_id(self, task_id: str) -> bool:
        tasks = self.find_all()
        filtered = [t for t in tasks if t.id != task_id]
        if len(filtered) == len(tasks):
            return False
        self._persist(filtered)
        return True

    def _persist(self, tasks: List[Task]) -> None:
        with open(self.data_file, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in tasks], f, indent=2)
