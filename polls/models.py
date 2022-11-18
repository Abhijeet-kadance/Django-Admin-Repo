from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Person(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()
    courses = models.ManyToManyField("Course", blank=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
    
    class Meta:
        ordering = ("last_name", "first_name")

class Course(models.Model):
    name = models.TextField()
    year = models.IntegerField()

    class Meta:
        unique_together = ("name", "year", )
    
    def __str__(self):
        return f"{self.name}, {self.year}"

class Grade(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.grade}, {self.person}, {self.course}"

# class Scenario(models.Model):

#     name = models.TextField()

#     def activate_button(self):
#         return format_html('<a href="{}" class="link">Activate</a>',reverse_lazy("admin:admin_activate_scenario", args=[self.pk])
#         )