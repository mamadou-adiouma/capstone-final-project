from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from capstonefinalapp.models import MenuItem, Booking
from capstonefinalapp.serializers import MenuItemSerializer, BookingSerializer
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.
# Clients
def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "htmls/about.html")


def menu(request):
    items = MenuItem.objects.all()
    return render(request, "htmls/menu.html", {'items': items})


def single_menu_item(request, pk=None):
    if pk:
        item = MenuItem.objects.get(pk=pk)
    else:
        item = ''
    return render(request, "htmls/menu_item.html", {"menu_item": item})
# ===============================================================================


# APIS

class MenuItemView(generics.ListCreateAPIView):
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        permissions_classes=[IsAuthenticated]
        if  self.request.method == 'POST':
            permissions_classes = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permissions_classes]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    def get_permissions(self):
        permissions_classes=[IsAuthenticated]
        if  self.request.method == 'POST':
            permissions_classes = [IsAuthenticated, IsAdminUser]
            permissions_classes = [IsAuthenticated, IsAdminUser]
        return [permission() for permission in permissions_classes]
