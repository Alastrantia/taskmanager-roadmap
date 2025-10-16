import uuid

class Task:
    def __init__(self, description, status, createdAt, updatedAt, id=uuid.uuid4()):
        self.id = str(id)
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAt = updatedAt