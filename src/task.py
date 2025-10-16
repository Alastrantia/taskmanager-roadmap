class Task:
    def __init__(self, description, status, createdAt, updatedAt):
        self.id = id
        self.description = description
        self.status = status
        self.createdAt = createdAt
        self.updatedAf = updatedAt
    
    def update(self, description):
        self.description = description
        return f"Updated task successfully! New description: {description}"
    
    def mark_done(self):
        self.status = "done"
        return "Marked task as done!"
    
    def mark_progress(self):
        self.status = "in_progress"
        return "Marked task as in progress!"