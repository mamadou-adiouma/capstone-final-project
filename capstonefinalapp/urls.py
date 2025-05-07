from django.urls import  path
from capstonefinalapp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("menu-item/", views.menu, name="menu"),
    path("menu-item/<int:pk>/", views.single_menu_item, name="menu-item"),

    path('api/menu/', views.MenuItemView.as_view()),
    path('api/menu/<int:pk>', views.SingleMenuItemView.as_view()),
    # path('booking/', views.BookingView().as_view()),
]