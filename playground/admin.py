from django.contrib import admin
from .models import Student, Teacher, Subject

# Register your models here.
class PlaygroundAdminSite(admin.AdminSite):
    site_header = 'Playground admin site'

playground_site = PlaygroundAdminSite(name='playground_admin')
playground_site.site_header = 'JOSHUA ADMIN'
admin.site.site_header = 'JOSHUA ADMIN'

# Subject admin with number of students column
class SubjectAdminSite(admin.ModelAdmin):
    model = Subject
    list_display = ['name', 'student_count','teacher_count']
    search_fields = ['name',]

    def student_count(self, obj):
        return obj.student_set.count()

    student_count.short_description = 'Number of Students'
    
    def teacher_count(self, obj):
        return obj.teacher_set.count()

    teacher_count.short_description = 'Number of teachers'

# Register the Subject model with the custom admin site
playground_site.register(Subject, SubjectAdminSite)
admin.site.register(Subject, SubjectAdminSite)

class TeacherAdminSite(admin.ModelAdmin):
    model = Teacher
    list_display = ['name','grade_assigned']
    list_filter = ['grade_assigned']
    search_fields = ['name',]
    
playground_site.register(Teacher, TeacherAdminSite)
admin.site.register(Teacher, TeacherAdminSite)
    
class StudentAdminSite(admin.ModelAdmin):
    model = Student
    fields = ['name', 'admno', 'grade', 'age','gender','subjects']
    list_display = ('name', 'admno', 'grade','gender')
    list_filter = ['grade']
    list_display_links = ['name']
    search_fields = ['name',]
    actions = ['promote_to_next_grade']

    def promote_to_next_grade(self, request, queryset):
        subjects = ['Maths', 'English', 'Kiswahili', 'French', 'Computer Studies']
        for subject_name in subjects:
            Subject.objects.get_or_create(name=subject_name)
        
        grade_1_to_3_subjects = Subject.objects.filter(name__in=['Maths', 'English', 'Kiswahili'])
        grade_4_subjects = Subject.objects.filter(name__in=['Maths', 'English', 'Kiswahili', 'French'])
        grade_5_to_6_subjects = Subject.objects.filter(name__in=['Maths', 'English', 'Kiswahili', 'French', 'Computer Studies'])

        for student in queryset:
            current_grade = student.grade
            if current_grade.isdigit():
                current_grade_int = int(current_grade)
                if current_grade_int >= 6:
                    student.delete()
                else:
                    student.grade = str(current_grade_int + 1)
                    student.save()

                    # Assign subjects based on the new grade
                    if current_grade_int + 1 <= 3:
                        student.subjects.set(grade_1_to_3_subjects)
                    elif current_grade_int + 1 == 4:
                        student.subjects.set(grade_4_subjects)
                    elif 5 <= current_grade_int + 1 <= 6:
                        student.subjects.set(grade_5_to_6_subjects)
                    student.save()
            else:
                # Handle non-numeric grade logic, if applicable
                pass
        self.message_user(request, "Selected students have been promoted to the next grade, assigned appropriate subjects, or removed if they finished grade 6.")
    
    promote_to_next_grade.short_description = "Promote selected students to the next grade, assign subjects, or remove if they finished grade 6"

# Register the Student model with the StudentAdminSite
playground_site.register(Student, StudentAdminSite)
admin.site.register(Student, StudentAdminSite)