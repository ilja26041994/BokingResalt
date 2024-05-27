from django.db.models import Sum
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Booking, Basket
from rooms.models import Room
from django.contrib.auth.models import User


def add_to_basket(request):
    room_id = request.POST.get('room_id')

    room = Room.objects.get(id=room_id)
    basket = Basket.objects.create(user=request.user, room=room)
    basket.save()

    return HttpResponseRedirect(reverse('room_detail', args=[room_id]))


def add_booking(request):
    if request.method == 'POST':
        user = request.user

        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')
        description = request.POST.get('description')

        room_list = Basket.objects.filter(user=user)

        booking = Booking.objects.create(user=user, check_in=check_in, check_out=check_out, description=description)
        booking.save()

        for item in room_list:
            booking.room.add(item.room)

        for item in room_list:
            room = item.room
            room.is_available = False
            room.save()
            item.delete()

        return HttpResponseRedirect(reverse('room_list'))

    else:
        return None


def get_basket(request):
    if request.user.is_authenticated:
        user = request.user

        items_on_basket = Basket.objects.filter(user=user)
        sum_items = items_on_basket.aggregate(Sum('room__price'))

        # lazy loading
        # 1) формирование запроса
        # 2) Момент вызова
        # 3) выполнение запроса

        return render(request, 'booking/booking.html', {'items_on_basket': items_on_basket, 'sum_items': sum_items.get('room__price__sum')})
    else:
        return None


def delete_booking(request):
    return None