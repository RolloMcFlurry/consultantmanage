from django.contrib import admin
from consultantmapp.models import Consultant, Skill, Contact, ConsSkill, SkillLevel


#admin.site.register(Consultant)
admin.site.register(SkillLevel)

class ConsultantAdmin(admin.ModelAdmin):
   # fields = ['consname', 'consemail']
    list_display = ('consname', 'consemail', 'add_date', 'desireperm')
    search_fields = ['consname']
    list_filter = ['add_date','desireperm']	


admin.site.register(Consultant, ConsultantAdmin)	


admin.site.register(ConsSkill)
admin.site.register(Skill)
admin.site.register(Contact)
