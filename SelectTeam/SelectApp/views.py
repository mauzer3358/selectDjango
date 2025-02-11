from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from .form import DirectorForm, VyborForm
from .models import DirectorModel



# Create your views here.

class main_page(TemplateView):
    template_name = 'main.html'

    def get(self, request):
        dir_list = DirectorModel.objects.all()
        data = {
            'dir_list': dir_list,
            'info': "Список всех",
            'title': "Главная страница"
        }
        return render(request, self.template_name, context=data)



class DirectorView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        context = {
            'form': DirectorForm,
            'title': "Добавить режиссера в базу"
        }
        return render(request, self.template_name, context)

    def post(self,request):
        form = DirectorForm(request.POST)

        if form.is_valid():
            form.save()
            #тут можно из формы подастовать переменные и дальше их использовать?
        context = {
            'form': form,
            'title': "Вроде добавилось"
        }
        return HttpResponseRedirect('/') #render(request, self.template_name, context)

class VyborView(TemplateView):
    template_name = 'index.html'


    def get(self, request):
        dir_list=[]
        context = {
            'form': VyborForm,
            'title': "Подбор режиссера",
            'dir_list': dir_list
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = VyborForm(request.POST)
        if form.is_valid():
            price_max = form.cleaned_data['price_max']
            opyt = form.cleaned_data['opyt']
            search_genre = form.cleaned_data['search_genre']
            dir_list = DirectorModel.objects.filter(experience__gte = opyt, price__lte = price_max)
            # #
            print(price_max, opyt, search_genre)
            print('dir_list', dir_list)
            # #form.save()
            # #тут можно из формы подастовать переменные и дальше их использовать?
            context = {
                'form': form,  # чтобы отобразились ошибки
                'title': "Выбор режиссера",
                'dir_list': dir_list,
                'info': "Выбранные режиссеры"
            }
            return render(request, self.template_name, context)
        else:
            context = {
                'form': form,  # чтобы отобразились ошибки
                'title': "Выбор  режиссера",
                'info': "Ошибка запроса"
            }
            return render(request, self.template_name, context)

    