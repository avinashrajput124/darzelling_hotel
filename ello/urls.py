from django.urls import path
from ello import views,ApiViews

 

urlpatterns = [
    path("", views.home, name="home.html"),
    path("home", views.home, name="home.html"),
    path("login", views.login_user, name="loginuser"),
    path("users_list/", views.users_list, name="users-list.html"),
    path("user_search", views.user_search, name="user_search.html"),
    path("search", views.search, name='search.html'),


    path("edit_hotal/<int:id>", views.edit_hotal, name='edit_hotal'),
    path("update_hotal/<int:id>", views.update_hotal, name='update_hotal'),
    path("delete_hotal/<int:id>", views.delete_hotal, name='delete_hotal'),


    path('hotal_view/<int:id>', views.hotal_view, name="hotal_view"),
    path('offers_for_you',views.offers_for_you, name="offers_for_you"),
    path('promotions_save',views.promotions_save, name="promotions_save"),
    path('promotion_list',views.promotion_list, name="promotion_list"),
    path('view_promotion/<int:id>',views.view_promotion, name="view_promotion"),
    path('edit_promotion/<int:id>',views.edit_promotion, name="edit_promotion"),
    path('update_promotion',views.update_promotion, name="update_promotion"),
    path('exclusive_partners',views.exclusive_partners, name="exclusive_partners"),
    path('holiday_packages',views.holiday_packages, name="holiday_packages"),

    path('logout', views.logoutuser, name="handleLogout"),
    path("add_hotel", views.add_hotel, name='add-hotel.html'),
    path("hotel_list/", views.hotel_list, name='hotel-list'),
    path("hotel_list_filter/", views.hotel_list_filter, name='hotel_list_filter'),
    path("forgot-password", views.forgot_password, name='forgot-password.html'),



    # api urls
    path("hotel",ApiViews.hotel,name='hotel'),

    #add single Hotel
    path("add_single_hotel/<int:Hotal_id>",ApiViews.add_single_hotel,name='add_single_hotel')



]