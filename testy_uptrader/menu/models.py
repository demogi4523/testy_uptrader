from django.db import models

from menu.validators import validate_json_content


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
        html = """
         <ul id="{}">
            <li><a href="{}"><span class="caret">Beverages</span></a>
                <ul class="nested">
                    <li>Water</li>
                    <li>Coffee</li>
                    <li><span class="caret">Tea</span></li>
                </ul>
            </li>
        </ul> 
        """.format(self.name, '#')
        return html
