from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import MainList, ListDetail
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse



# Create your views here.



def main_listing(request):
    current_user = request.user
    listing = MainList.objects.filter(log_user_id=current_user.id)
    return render(request, 'List/main_list.html', {'main_list': listing})


def product_list(request, pk):
    # All_objects = MainList.objects.filter(title = 'New List')[0]
    products = ListDetail.objects.filter(ID=pk)
    return render(request, 'List/product_list.html', {'products': products})


def auth_view(request):
    if request.method == 'POST':
        login_form_auth = AuthForm(request.POST)
        if login_form_auth.is_valid():
            username = login_form_auth.cleaned_data['username']
            password = login_form_auth.cleaned_data['password']
            user = authenticate(username= username, password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('main_list')
                else:
                    login_form_auth.add_error('__all__','Пользователь с таким логином или паролем не активен')
        else:
            login_form_auth.add_error('__all__','Неправильный логин или пароль')

    login_form_auth = AuthForm()
    return render(request, 'List/login.html', {'login_form_auth': login_form_auth})

def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


class AddListView(View):  # добавление листа с продуктами
    def get(self, request):
        add_list_form = AddList()
        return render(request, 'List/addlist.html', context={"add_list_form": add_list_form})

    def post(self, request):
        add_list_form = AddList(request.POST)
        if add_list_form.is_valid():
            title = add_list_form.cleaned_data['title']
            date = add_list_form.cleaned_data['published_date']
            MainList.objects.create(title= title, published_date= date, log_user_id= request.user)
            return HttpResponseRedirect('main_list')

        return render(request, 'List/addlist.html', context={"add_list_form": add_list_form})


class AddProductView(View):  # добавление продуктов в листе

    def get(self, request):
        add_product_list = AddProduct()
        return render(request, 'List/addproduct.html', context={'add_product_list': add_product_list})

    def post(self, request):
        add_product_list = AddProduct(request.POST)
        if add_product_list.is_valid():
            product_list = add_product_list.cleaned_data['product_list']
            product_count = add_product_list.cleaned_data['product_count']
            print(request)
            # rq = request.POST
            # pk = rq.__getitem__('pk')
            ListDetail.objects.create(product_list=product_list, product_count= product_count)
            # products = ListDetail.objects.filter(ID=pk)
            return HttpResponseRedirect('main_list')

        return render(request, 'List/addproduct.html', context={'add_product_list': add_product_list})


class UserFromView(View):

    def get(self, request):
        user_form = UserForm()
        return render(request, 'List/register.html', {'user_form': user_form})

    def post(self, request):
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
            User.objects.create_user(username=username, password=password)
            return HttpResponseRedirect('successful')

        return render(request, 'List/register.html', context={'user_form': user_form})

#     def clead(self):                                          #нужно доделать валидацию по паролю
#         clean_data = super(UserForm, self).clean()
#         clean_pass = clean_data.get('password')
#         if len(clean_pass) < 3:
#             msg = 'AGA'
#             self.add_error('password', msg)
#
# class ProductEditVies(View):             #нужно допилить редактирование продуктов в листе
#
#     def get(self, request, pk):
#         product_edit = ListDetail.object.get(pk = pk)
#         product_form = AddProduct(instance = product_edit)
#         return render(request, 'List/productsedit.html', {'product_form':product_form}, {'pk':pk})

# class Authlogin(LoginView):
#     template_name = 'List/login.html'

def successful(request):
    return render(request,'List/successful.html', {})