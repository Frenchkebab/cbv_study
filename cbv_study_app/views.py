from django.shortcuts import render
from djang.views.generic import Templateview

def murlsyview(request):
    return render(request, 'cbv_study_app/myview.html')