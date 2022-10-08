from django.http import HttpResponseRedirect
from django.shortcuts import render, HttpResponse, redirect
from ello.models import Add_Hotal,promotions,exclusive_partners,Holiday_packages, whats_new
# Create your views here.
from django.core.paginator import Paginator
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from ello.form import PASignUpForm
from ello.models import User
# from django.views.generic import CreateView
# from django.contrib.auth.models import User 
from django.contrib.auth import get_user_model
import math
# import datetime import timesnce
from collections import OrderedDict
import math
from ello.decorator import admin_required

User = get_user_model()



@admin_required()
def home(request):
       hotal = Add_Hotal.objects.all()[:3]
       perm = {'hotal':hotal}

       return render(request, "home.html", perm)

@admin_required()
def users_list(request):
       
       no_of_posts = 7
       print(request.GET)
       page = request.GET.get('page')
       if page is None:
           page = 1
       else:
           page = int(page)
      


       '''This function is used to access the data from the database and sending it to the frontend.'''
       user_all = User.objects.all()
       
       length = len(user_all)
       user_all = user_all[(page-1)*no_of_posts: page*no_of_posts]
        
       if page>1:
           prev = page-1
       else:
           prev = None
       
       if page<math.ceil(length/no_of_posts):
           nxt = page + 1
       else:
           nxt = None


       params = {'user_all' : user_all,'prev' : prev, 'nxt' : nxt}

       return render(request, "users-list.html", params)



# def user_filter(request):
#        # hotal = Add_Hotal.objects.all()
#        # user_all = User.objects.all()
#        query = request.GET['query']
#        user_all = User.objects.filter(username__icontains=query)

#        context = {'user_all' : user_all}
#        return render(request, 'user_search.html', context)

       

@admin_required()
def forgot_password(request):
       return render(request, "forgot-password.html")



def login_user(request):
       print('xxxxxxxxxxxxxxx')
       print(request.POST)
       if request.method=="GET":
              print('helo')
           
        # Get the post parameters
              username = request.GET.get('username')
              password = request.GET.get('password')
              print(username)
              print(password)
              # check for errorneous input
              user = authenticate(username = username, password = password)
              print(user)
              if user is not None:
                     login(request, user)
                     return redirect('/home')
       return render(request, "login.html")


@admin_required()
def search(request):
       x = Add_Hotal.objects.all()
       tottal_hotal = len(x)
       # hotal = Add_Hotal.objects.all()
       query = request.GET['query']
       hotal = Add_Hotal.objects.filter(Hotal_Name__icontains=query)

       context = {'hotal' : hotal, 'tottal_hotal':tottal_hotal}
       return render(request, 'search.html', context)

@admin_required()
def user_search(request):
       # hotal = Add_Hotal.objects.all()
       # user_all = User.objects.all()
       query = request.GET['query']
       user_all = User.objects.filter(username__icontains=query)

       context = {'user_all' : user_all}
       return render(request, 'user_search.html', context)




@admin_required()
def hotal_view(request, id):
      
       if request.method=="POST":
              hotal = Add_Hotal.objects.all()
              Hotal_id = Add_Hotal.objects.get(pk=id)

              
              cotext = {'Hotal_id':Hotal_id, 'hotal':hotal}

              return render(request, 'hotal_view.html', cotext)
       return render(request, "hotal_view.html")


# class pasign_up(CreateView):
#     model = User
#     form_class = PASignUpForm
#     template_name = 'createuser.html'

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('home')



@admin_required()
def hotel_list(request):
       x = Add_Hotal.objects.all()
       tottal_hotal = len(x)


       # if request.method=="GET":
       #        sort_by = request.GET.get('sort')

       #        if sort_by == 'recently_added': 
       #         adverts = hotal.order_by('-date')
       #        elif sort_by == 'price_low_to_high':
       #            adverts = hotal.order_by('-price')
       #        elif sort_by == 'price_high_yo_low':
       #            adverts = hotal.order_by('price')
       #        else:
       #            adverts = Add_Hotal.objects.all()
       # else:
       #        adverts = Add_Hotal.objects.all()

       print(request.GET)
       
              
       no_of_posts = 3
    # print(request.GET)
       page = request.GET.get('page')
       if page is None:
           page = 1
       else:
           page = int(page)
      


       '''This function is used to access the data from the database and sending it to the frontend.'''
       hotal = Add_Hotal.objects.all()
       
       length = len(hotal)
       hotal = hotal[(page-1)*no_of_posts: page*no_of_posts]
       
       if page>1:
           prev = page-1
       else:
           prev = None
       
       if page<math.ceil(length/no_of_posts):
           nxt = page + 1
       else:
           nxt = None



       params = {'hotal' : hotal, 'prev' : prev, 'nxt' : nxt, 'tottal_hotal':tottal_hotal}
       return render(request, "hotel-list.html", params)


@admin_required()
def hotel_list_filter(request):
       
       x = Add_Hotal.objects.all()
       tottal_hotal = len(x)

       print(request.GET)
       hello = request.GET.get('resently_added')
       if request.method=="GET":
              if hello is None:
                     hello = Add_Hotal.objects.all()
              else:
                     hello = str(hello)
              if hello == 'newfirst':
                     hotal = Add_Hotal.objects.all().order_by("-Hotal_id")
              if hello == 'oldfirst':
                     hotal = Add_Hotal.objects.all().order_by("Hotal_id")
              elif hello == 'a_to_z':
                     hotal = Add_Hotal.objects.all().order_by('Hotal_Name')
              elif hello == 'z_to_a':
                     hotal = Add_Hotal.objects.all().order_by('-Hotal_Name')
              elif hello == 'price_low_to_hight':
                     hotal = Add_Hotal.objects.all().order_by('hotal_new_price')
              elif hello == 'price_high_to_low':
                     hotal = Add_Hotal.objects.all().order_by('-hotal_new_price')
              elif hello == '5-star_hotal':
                     hotal = Add_Hotal.objects.all().filter(hotal_ratting__icontains=5)
              elif hello == '4-star_hotal':
                     hotal = Add_Hotal.objects.all().filter(hotal_ratting__icontains=4)
              elif hello == '3-star_hotal':
                     hotal = Add_Hotal.objects.all().filter(hotal_ratting__icontains=3)
              elif hello == '2-star_hotal':
                     hotal = Add_Hotal.objects.all().filter(hotal_ratting__icontains=2)
              elif hello == '1-star_hotal':
                     hotal = Add_Hotal.objects.all().filter(hotal_ratting__icontains=1)
              elif hello == '0-star_hotal':
                     hotal = Add_Hotal.objects.all().filter(hotal_ratting__icontains=0)
              else:
                     hotal = Add_Hotal.objects.all()
       

       params = {'hotal' : hotal,'tottal_hotal':tottal_hotal}
       return render(request, "hotel_list_filter.html", params)

@admin_required()
def add_hotel(request):
       if request.method == "POST":
              # Hotal_id = request.POST.get('Hotal_id')
              Hotal_Name = request.POST.get('hotalname')
              hotal_new_price = request.POST.get('newprice')
              hotal_discreption = request.POST.get('dec')
              Hotal_Location = request.POST.get('loc')
              Hotal_Latitude = request.POST.get('lat')
              Hotal_Longitude = request.POST.get('long')
              Hotal_images1 = request.FILES.get('img1')
              # recettion images
              reception_images1 = request.FILES.get('reception_images1')
              reception_images2 = request.FILES.get('reception_images2')
              reception_images3 = request.FILES.get('reception_images3')
              reception_images4= request.FILES.get('reception_images4')
              reception_images5 = request.FILES.get('reception_images5')
              # bedroom images
              bedroom_images1 = request.FILES.get('bedroom_images1')
              bedroom_images2 = request.FILES.get('bedroom_images2')
              bedroom_images3 = request.FILES.get('bedroom_images3')
              bedroom_images4= request.FILES.get('bedroom_images4')
              bedroom_images5 = request.FILES.get('bedroom_images5')
              # washroom images
              washroom_images1 = request.FILES.get('washroom_images1')
              washroom_images2 = request.FILES.get('washroom_images2')
              washroom_images3 = request.FILES.get('washroom_images3')
              washroom_images4= request.FILES.get('washroom_images4')
              washroom_images5 = request.FILES.get('washroom_images5')
              # exterior images
              Exterior_images1 = request.FILES.get('Exterior_images1')
              Exterior_images2 = request.FILES.get('Exterior_images2')
              Exterior_images3 = request.FILES.get('Exterior_images3')
              Exterior_images4= request.FILES.get('Exterior_images4')
              Exterior_images5 = request.FILES.get('Exterior_images5')
              # garden images
              garden_images1 = request.FILES.get('garden_images1')
              garden_images2 = request.FILES.get('garden_images2')
              garden_images3 = request.FILES.get('garden_images3')
              garden_images4= request.FILES.get('garden_images4')
              garden_images5 = request.FILES.get('garden_images5')
              date = request.POST.get('datetime.today()')

              data = Add_Hotal(Hotal_Name=Hotal_Name, hotal_new_price=hotal_new_price,
              hotal_discreption = hotal_discreption, Hotal_Location=Hotal_Location, Hotal_Latitude=Hotal_Latitude, Hotal_Longitude=Hotal_Longitude, Hotal_images1=Hotal_images1,
               date=date,
              reception_images1=reception_images1,reception_images2=reception_images2,reception_images3=reception_images3,reception_images4=reception_images4,reception_images5=reception_images5,
              bedroom_images1=bedroom_images1,bedroom_images2=bedroom_images2,bedroom_images3=bedroom_images3,bedroom_images4=bedroom_images4,bedroom_images5=bedroom_images5,
              washroom_images1=washroom_images1,washroom_images2=washroom_images2,washroom_images3=washroom_images3,washroom_images4=washroom_images4,washroom_images5=washroom_images5,
              Exterior_images1=Exterior_images1,Exterior_images2=Exterior_images2,Exterior_images3=Exterior_images3,Exterior_images4=Exterior_images4,Exterior_images5=Exterior_images5,
              garden_images1=garden_images1,garden_images2=garden_images2,garden_images3=garden_images3,garden_images4=garden_images4,garden_images5=garden_images5, 
              )
       
              data.save()
       return render(request, "add-hotel.html")



@admin_required()
def logoutuser(request):
       logout(request)
       return redirect('login')



@admin_required()
def delete_hotal(request, id):
       print(request.GET)
       if request.method=="POST":
              dell = Add_Hotal.objects.get(pk=id)
              dell.delete()
              return redirect('hotel-list')

@admin_required()
def delete_hotal(request, id):
       print(request.GET)
       if request.method=="POST":
              dell = Add_Hotal.objects.get(pk=id)
              dell.delete()
              return redirect('search')

@admin_required()
def delete_hotal(request, id):
       print(request.GET)
       if request.method=="POST":
              dell = Add_Hotal.objects.get(pk=id)
              dell.delete()
              return redirect('hotel_list_filter')


@admin_required()
def update_hotal(request, id):
       if request.method=="POST":
              update = Add_Hotal.objects.all()
              Hotal_id = Add_Hotal.objects.get(pk=id)
              cotext = {'Hotal_id':Hotal_id, 'update':update}
              return render(request, 'update_hotal.html', cotext)
@admin_required()
def edit_hotal(request, id):
       print(request.POST)
       if request.method == "POST":
              Hotal_Name = request.POST.get('hotalname')
              hotal_new_price = request.POST.get('newprice')
              hotal_new_price_premium = request.POST.get('hotal_new_price_premium')
              hotal_discreption = request.POST.get('dec')
              Hotal_Location = request.POST.get('loc')
              Hotal_Latitude = request.POST.get('lat')
              Hotal_Longitude = request.POST.get('long')
              Hotal_images1 = request.FILES.get('img1')
              # recettion images
              reception_images1 = request.FILES.get('reception_images1')
              reception_images2 = request.FILES.get('reception_images2')
              reception_images3 = request.FILES.get('reception_images3')
              reception_images4= request.FILES.get('reception_images4')
              reception_images5 = request.FILES.get('reception_images5')
              # bedroom images
              bedroom_images1 = request.FILES.get('bedroom_images1')
              bedroom_images2 = request.FILES.get('bedroom_images2')
              bedroom_images3 = request.FILES.get('bedroom_images3')
              bedroom_images4= request.FILES.get('bedroom_images4')
              bedroom_images5 = request.FILES.get('bedroom_images5')
              # washroom images
              washroom_images1 = request.FILES.get('washroom_images1')
              washroom_images2 = request.FILES.get('washroom_images2')
              washroom_images3 = request.FILES.get('washroom_images3')
              washroom_images4= request.FILES.get('washroom_images4')
              washroom_images5 = request.FILES.get('washroom_images5')
              # exterior images
              Exterior_images1 = request.FILES.get('Exterior_images1')
              Exterior_images2 = request.FILES.get('Exterior_images2')
              Exterior_images3 = request.FILES.get('Exterior_images3')
              Exterior_images4= request.FILES.get('Exterior_images4')
              Exterior_images5 = request.FILES.get('Exterior_images5')
              # garden images
              garden_images1 = request.FILES.get('garden_images1')
              garden_images2 = request.FILES.get('garden_images2')
              garden_images3 = request.FILES.get('garden_images3')
              garden_images4= request.FILES.get('garden_images4')
              garden_images5 = request.FILES.get('garden_images5')
              date = request.POST.get('datetime.today()')

              data = Add_Hotal(Hote_id=id,Hotal_Name=Hotal_Name, hotal_new_price=hotal_new_price,hotal_new_price_premium=hotal_new_price_premium,
              hotal_discreption = hotal_discreption, Hotal_Location=Hotal_Location, Hotal_Latitude=Hotal_Latitude, Hotal_Longitude=Hotal_Longitude, Hotal_images1=Hotal_images1,
                     date=date,
              reception_images1=reception_images1,reception_images2=reception_images2,reception_images3=reception_images3,reception_images4=reception_images4,reception_images5=reception_images5,
              bedroom_images1=bedroom_images1,bedroom_images2=bedroom_images2,bedroom_images3=bedroom_images3,bedroom_images4=bedroom_images4,bedroom_images5=bedroom_images5,
              washroom_images1=washroom_images1,washroom_images2=washroom_images2,washroom_images3=washroom_images3,washroom_images4=washroom_images4,washroom_images5=washroom_images5,
              Exterior_images1=Exterior_images1,Exterior_images2=Exterior_images2,Exterior_images3=Exterior_images3,Exterior_images4=Exterior_images4,Exterior_images5=Exterior_images5,
              garden_images1=garden_images1,garden_images2=garden_images2,garden_images3=garden_images3,garden_images4=garden_images4,garden_images5=garden_images5, 
              )
              data.save()
       # return render(request, "update_hotal.html")
       else:
           return render(request, 'update_hotal.html') 
       return render(request, "update_hotal.html")


def offers_for_you(request):
       return render(request,'offers_for_you.html')

# Promotions------------------------------
def promotions_save(request):
       if request.method=="POST":
              hotel_name=request.POST.get('hotel_name')
              promotions_images1=request.FILES.get('promotions_images1')
              promotions_images2=request.FILES.get('promotions_images2')
              promotions_images3=request.FILES.get('promotions_images3')
              promotions_images4=request.FILES.get('promotions_images4')
              data=promotions(hotel_name=hotel_name,promotions_images1=promotions_images1,promotions_images2=promotions_images2,promotions_images3=promotions_images3,promotions_images4=promotions_images4)
              data.save()
              messages.success(request,'Promotion save sucessfully')
              return render(request,'promotions.html')
       return render(request,'promotions.html')

def promotion_list(request):
       data=promotions.objects.all()
       return render(request,'promotion_list.html',{'data':data})

def view_promotion(request,id):
       Hotal_id=promotions.objects.get(pk=id)
       return render(request,'view_promotion.html',{'Hotal_id':Hotal_id})
def edit_promotion(request,id):
       data=promotions.objects.get(pk=id)
       return render(request,'edit_promotion.html',{'data':data})

def promotion_list_filter(request):
       x = promotions.objects.all()
       tottal_hotal = len(x)
       hello = request.GET.get('resently_added')
       if request.method=="GET":
              if hello is None:
                     hello = promotions.objects.all()
              else:
                     hello = str(hello)
              if hello == 'newfirst':
                     hotal = promotions.objects.all().order_by("-id")
              if hello == 'oldfirst':
                     hotal = promotions.objects.all().order_by("id")
              elif hello == 'a_to_z':
                     hotal = promotions.objects.all().order_by('hotal_name')
              elif hello == 'z_to_a':
                     hotal = promotions.objects.all().order_by('-hotal_name')
              else:
                      hotal = Add_Hotal.objects.all()

              context = {'hotal' : hotal,'tottal_hotal':tottal_hotal}
       return render(request, "hotel_list_filter.html", context)
def update_promotion(request):
       if request.method=="POST":
              id=request.POST.get('id')
              if request.FILES.get('promotions_images1') is not None:
                     promotions.promotions_images1=request.FILES.get('promotions_images1')
              else:
                     promotions.promotions_images1=promotions.promotions_images1

              hotel_name=request.POST.get('hotel_name')
              promotions_images2=request.FILES.get('promotions_images2')
              promotions_images3=request.FILES.get('promotions_images3')
              promotions_images4=request.FILES.get('promotions_images4')
              data=promotions(id=id,hotel_name=hotel_name,promotions_images2=promotions_images2,promotions_images3=promotions_images3,promotions_images4=promotions_images4)
              print(data)
              data.save()
              return render(request,'promotion_list.html')
       return render(request,'edit_promotion.html')
def distroy(request,id):
       data=promotions.objects.get(pk=id)
       data.delete()
       return redirect('promotion_list')


#  Exclusive partners-----------------------


def exclusive_partners_save(request):
       if request.method=="POST":
              exclusive_partners_images1=request.FILES.get('exclusive_partners_images1')
              exclusive_partners_images2=request.FILES.get('exclusive_partners_images2')
              exclusive_partners_images3=request.FILES.get('exclusive_partners_images3')
              exclusive_partners_images4=request.FILES.get('exclusive_partners_images4')
              data=exclusive_partners(exclusive_partners_images1=exclusive_partners_images1,exclusive_partners_images2=exclusive_partners_images2,exclusive_partners_images3=exclusive_partners_images3,exclusive_partners_images4=exclusive_partners_images4)
              data.save()
              return render(request,'exclusive_partners.html')
       return render(request,'exclusive_partners.html')

def exclusive_partners_list(request):
       data=exclusive_partners.objects.all()
       return render(request,'list_exclusive_partners.html',{'data':data})


def view_exclusive(request,id):
       Hotal_id=exclusive_partners.objects.get(pk=id)
       return render(request,'view_exclusive.html',{'Hotal_id':Hotal_id})
def edit_exclusive(request,id):
       data=exclusive_partners.objects.get(pk=id)
       return render(request,'edit_exclusive_partners.html',{'data':data})

def distroy_exclusive_list(request,id):
       data=exclusive_partners.objects.get(pk=id)
       data.delete()
       return redirect('promotion_list')

def update_exclusive(request):
       if request.method=="POST":
              id=request.POST.get('id')
              exclusive_partners_images1=request.FILES.get('exclusive_partners_images1')
              exclusive_partners_images2=request.FILES.get('exclusive_partners_images2')
              exclusive_partners_images3=request.FILES.get('exclusive_partners_images3')
              exclusive_partners_images4=request.FILES.get('exclusive_partners_images4')
              data=exclusive_partners(id=id,exclusive_partners_images1=exclusive_partners_images1,exclusive_partners_images2=exclusive_partners_images2,exclusive_partners_images3=exclusive_partners_images3,exclusive_partners_images4=exclusive_partners_images4)
              data.save()
              return redirect('exclusive_partners_list')
       return render(request,'edit_exclusive_partners.html')


# holiday Packages------------------------------

def holiday_packages_save(request):
       if request.method=="POST":
              Holiday_packages_images1=request.FILES.get('Holiday_packages_images1')
              Holiday_packages_images2=request.FILES.get('Holiday_packages_images2')
              Holiday_packages_images3=request.FILES.get('Holiday_packages_images3')
              Holiday_packages_images4=request.FILES.get('Holiday_packages_images4')
              data=Holiday_packages(Holiday_packages_images1=Holiday_packages_images1,Holiday_packages_images2=Holiday_packages_images2,Holiday_packages_images3=Holiday_packages_images3,Holiday_packages_images4=Holiday_packages_images4)
              data.save()
              return render(request,'holiday_packages.html')
       return render(request,'holiday_packages.html')

def list_holiday_packages(request):
       data=Holiday_packages.objects.all()
       return render(request,'list_holiday_packages.html',{'data':data})

def view_holiday_packages(request,id):
       Hotal_id=Holiday_packages.objects.get(pk=id)
       return render(request,'view_holiday_packages.html',{'Hotal_id':Hotal_id})

def edit_holiday_packages(request,id):
       data=Holiday_packages.objects.get(pk=id)
       return render(request,'edit_holiday_packages.html',{'data':data})

def distroy_holiday_packages(request,id):
       data=Holiday_packages.objects.get(pk=id)
       data.delete()
       return redirect('list_holiday_packages')


def update_holiday_packages(request):
       if request.method=="POST":
              id=request.POST.get('id')
              Holiday_packages_images1=request.FILES.get('Holiday_packages_images1')
              Holiday_packages_images2=request.FILES.get('Holiday_packages_images2')
              Holiday_packages_images3=request.FILES.get('Holiday_packages_images3')
              Holiday_packages_images4=request.FILES.get('Holiday_packages_images4')
              data=Holiday_packages(id=id,Holiday_packages_images1=Holiday_packages_images1,Holiday_packages_images2=Holiday_packages_images2,Holiday_packages_images3=Holiday_packages_images3,Holiday_packages_images4=Holiday_packages_images4)
              data.save()
              return redirect('list_holiday_packages')
       return redirect('edit_holiday_packages')


#  whats new-----------------------------

def whats_new_save(request):
       if request.method=="POST":
              whats_new_images1=request.FILES.get('whats_new_images1')
              whats_new_images2=request.FILES.get('whats_new_images2')
              whats_new_images3=request.FILES.get('whats_new_images3')
              whats_new_images4=request.FILES.get('whats_new_images4')
              data=whats_new(whats_new_images1=whats_new_images1,whats_new_images2=whats_new_images2,whats_new_images3=whats_new_images3,whats_new_images4=whats_new_images4)
              data.save()
              return render(request,'whats_new_save.html')
       return render(request,'whats_new_save.html')

def list_whats_new(request):
       data=whats_new.objects.all()
       return render(request,'list_whats_new.html',{'data':data})


def view_whats_new(request,id):
       Hotal_id=whats_new.objects.get(pk=id)
       return render(request,'view_whats_new.html',{'Hotal_id':Hotal_id})
def edit_whats_new(request,id):
       data=whats_new.objects.get(pk=id)
       return render(request,'edit_whats_new.html',{'data':data})
def update_whats_new(request):
       if request.method=="POST":
              id=request.POST.get('id')
              whats_new_images1=request.FILES.get('whats_new_images1')
              whats_new_images2=request.FILES.get('whats_new_images2')
              whats_new_images3=request.FILES.get('whats_new_images3')
              whats_new_images4=request.FILES.get('whats_new_images4')
              data=whats_new(id=id,whats_new_images1=whats_new_images1,whats_new_images2=whats_new_images2,whats_new_images3=whats_new_images3,whats_new_images4=whats_new_images4)
              data.save()
              return redirect('list_whats_new')
       return redirect('edit_holiday_packages')

