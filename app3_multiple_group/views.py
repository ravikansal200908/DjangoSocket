from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request, group_name):
        data = {'group_name': group_name}
        return render(request, 'index.html', data)
