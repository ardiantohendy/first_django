from django.db import models

# Create your models here.
class Feature:
    def __init__(self, id: int, title: str, desc: str, icon: str):
        self.id = id
        self.title = title
        self.desc = desc
        self.icon = icon