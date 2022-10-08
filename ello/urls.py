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
    path('promotion_list_filter',views.promotion_list_filter, name="promotion_list_filter"),
    path('view_promotion/<int:id>',views.view_promotion, name="view_promotion"),
    path('edit_promotion/<int:id>',views.edit_promotion, name="edit_promotion"),
    path('update_promotion',views.update_promotion, name="update_promotion"),
    path('distroy/<int:id>',views.distroy, name="distroy"),
    path('exclusive_partners_save',views.exclusive_partners_save, name="exclusive_partners_save"),
    path('exclusive_partners_list',views.exclusive_partners_list, name="exclusive_partners_list"),
    path('distroy_exclusive_list/<int:id>',views.distroy_exclusive_list, name="distroy_exclusive_list"),
    path('view_exclusive/<int:id>',views.view_exclusive, name="view_exclusive"),
    path('edit_exclusive/<int:id>',views.edit_exclusive, name="edit_exclusive"),
    path('update_exclusive',views.update_exclusive, name="update_exclusive"),
    path('holiday_packages_save',views.holiday_packages_save, name="holiday_packages_save"),
    path('list_holiday_packages',views.list_holiday_packages, name="list_holiday_packages"),
    path('view_holiday_packages/<int:id>',views.view_holiday_packages, name="view_holiday_packages"),
    path('edit_holiday_packages/<int:id>',views.edit_holiday_packages, name="edit_holiday_packages"),
    path('distroy_holiday_packages/<int:id>',views.distroy_holiday_packages, name="distroy_holiday_packages"),
    path('update_holiday_packages',views.update_holiday_packages, name="update_holiday_packages"),
    path('whats_new_save',views.whats_new_save, name="whats_new_save"),
    path('list_whats_new',views.list_whats_new, name="list_whats_new"),
    path('view_whats_new/<int:id>',views.view_whats_new, name="view_whats_new"),
    path('edit_whats_new/<int:id>',views.edit_whats_new, name="edit_whats_new"),
    path('update_whats_new',views.update_whats_new, name="update_whats_new"),

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