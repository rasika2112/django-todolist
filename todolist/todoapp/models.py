from django.db import models

# Model to save the todoList


class TodoListItem(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item + '|' + str(self.completed)
