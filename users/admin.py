from django.contrib import admin

from . import models
from .models import Student

from django.utils.translation import ngettext
from django.http import HttpResponse
import xlwt
# Register your models here.

#admin.site.register(models.Resume)

class studentAdmin(admin.ModelAdmin):
    list_filter = ('program','department')
    search_fields = ('firstName','lastName','rollNumber')
    actions = ['export',]
    list_display = ('firstName','lastName','rollNumber')
    def export(self, request, queryset):
        response = HttpResponse(content_type = 'application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="studentsData.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Users')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['First name', 'Last name', 'Email address','Phone Number','Roll Number','Program','Branch','Year','Resume']
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

         # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        for st in queryset:
            row = []
            row.append(st.firstName)
            row.append(st.lastName)
            row.append(st.email)
            row.append(st.ph_no)
            row.append(st.rollNumber)
            row.append(st.program)
            row.append(st.department)
            row.append(st.year)
            row.append("http://127.0.0.1:8000/resume/"+st.user.username)
                
                #values_list('firstName', 'lastName', 'email','ph_no','rollNumber','program','department','year')
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response
     
    export.short_description = "Download Data"


admin.site.register(Student,studentAdmin)
