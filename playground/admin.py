from django.contrib import admin
from .models import Student, Teacher

# Register your models here.
admin.site.site_header = 'JOSHUA ADMIN'
admin.site.register(Teacher)

class StudentAdminSite(admin.ModelAdmin):
    model = Student
    fields = ['name', 'admno', 'grade','gender','age']
    list_display = ('name', 'admno', 'grade')
    actions = ['promote_to_next_grade']

    def promote_to_next_grade(self, request, queryset):
        for student in queryset:
            current_grade = student.grade
            if current_grade.isdigit():
                current_grade_int = int(current_grade)
                if current_grade_int >= 6:
                    student.delete()
                else:
                    student.grade = str(current_grade_int + 1)
                    student.save()
            else:
                pass
        self.message_user(request, "Selected students have been promoted to the next grade or removed if they finished grade 6.")
    
    promote_to_next_grade.short_description = "Promote selected students to the next grade or remove if they finished grade 6"
admin.site.register(Student, StudentAdminSite)
