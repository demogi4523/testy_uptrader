from django.db import models

from menu.validators import validate_json_content
from menu.utils import iter_to_html

class Menu(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        primary_key=False,
        default='root',
        null=False,
    )
    content = models.JSONField(validators=[validate_json_content])

    def __str__(self) -> str:
        return self.name

    def to_html(self):
        html = iter_to_html(self.content, self.name)
        return html
