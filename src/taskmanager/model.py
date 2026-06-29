from dataclasses import dataclass, fields
from typing import Optional


@dataclass
class Task:
    id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    category: Optional[str] = None
    assignedTo: Optional[str] = None
    dueDate: Optional[str] = None
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

    def to_dict(self) -> dict:
        valid_field_names = {f.name for f in fields(self)}
        return {k: v for k, v in self.__dict__.items() if k in valid_field_names}

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        valid_keys = {f.name for f in fields(cls)}
        return cls(**{k: v for k, v in data.items() if k in valid_keys})
