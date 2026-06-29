import uuid
from datetime import datetime
from typing import List, Optional

from taskmanager.model import Task
from taskmanager.repository import TaskRepository

_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S"


class TaskService:

    def __init__(self, repository: TaskRepository):
        self.repository = repository

    def get_all_tasks(self) -> List[Task]:
        return self.repository.find_all()

    def get_task_by_id(self, task_id: str) -> Optional[Task]:
        return self.repository.find_by_id(task_id)

    def create_task(self, task: Task) -> Task:
        task.id = str(uuid.uuid4())
        now = datetime.now().strftime(_DATETIME_FORMAT)
        task.createdAt = now
        task.updatedAt = now
        if not task.status:
            task.status = "TODO"
        return self.repository.save(task)

    def update_task(self, task_id: str, updated: Task) -> Optional[Task]:
        existing = self.repository.find_by_id(task_id)
        if existing is None:
            return None
        existing.title = updated.title
        existing.description = updated.description
        existing.status = updated.status
        existing.category = updated.category
        existing.assignedTo = updated.assignedTo
        existing.dueDate = updated.dueDate
        existing.updatedAt = datetime.now().strftime(_DATETIME_FORMAT)
        return self.repository.save(existing)

    def delete_task(self, task_id: str) -> bool:
        return self.repository.delete_by_id(task_id)
