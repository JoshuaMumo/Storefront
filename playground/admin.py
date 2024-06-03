from django.contrib import admin
from .models import Student, Teacher, Subject

# Register your models here.
admin.site.site_header = 'JOSHUA ADMIN'
admin.site.register(Teacher)
admin.site.register(Subject)

class StudentAdminSite(admin.ModelAdmin):
    model = Student
    fields = ['name', 'admno', 'grade', 'subjects']
    list_display = ('name', 'admno', 'grade')
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
admin.site.register(Student, StudentAdminSite)
