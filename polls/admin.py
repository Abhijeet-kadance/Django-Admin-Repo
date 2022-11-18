from django.contrib import admin

# Register your models here.

from polls.models import Person, Course, Grade

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name","show_average")

    def show_average(self, obj):
        from django.db.models import Avg
        result = Grade.objects.filter(person=obj).aggregate(Avg("grade"))
        print(result)
        return result["grade__avg"]
        
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    pass

# class ScenarioAdmin(admin.ModelAdmin):
#     list_display = (
#         "name","user","start","end","nb_hours","activate_button"
#     )

#     def get_urls(self):
#         urls = super().get_urls()
#         my_urls = [
#             path('activate-scenario/<int:pk>/',self.activate_scenario,name="admin_activate"),
#         ]
#         return my_urls + urls

#     def activate_scenario(self, request, pk):
#         context = dict(
#             slef.admin_site.each_context(request),
#         )

    