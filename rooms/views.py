from django.shortcuts import render, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.urls import reverse
from .models import Room, RoomType
from booking.models import Basket


def room_list(request):
    rooms = Room.objects.filter(is_deleted=False)
    if request.user.is_authenticated:
        basket_count = Basket.objects.filter(user=request.user).count()
        return render(request, 'rooms/room_list.html', {'rooms': rooms, 'count_rooms': basket_count})
    return render(request, 'rooms/room_list.html', {'rooms': rooms})


def room_detail(request, room_id):
    room = Room.objects.get(id=room_id)

    if request.user.is_authenticated:
        is_in_basket = Basket.objects.filter(user=request.user, room=room).exists()

        return render(request, 'rooms/room_detail.html', {'room': room, 'is_in_basket': is_in_basket})
    return render(request, 'rooms/room_detail.html', {'room': room})


def room_create(request):
    if request.method == 'POST':
        room_type_id = request.POST.get('room_type_id')
        number = request.POST.get('number')
        beds = request.POST.get('beds')
        price = request.POST.get('price')
        is_available = request.POST.get('is_available') == 'on'
        image = request.FILES.get('image')
        description = request.POST.get('description')

        print(type(room_type_id), type(number), type(beds), type(price))
        try:
            if not room_type_id or not number or not beds or not price or not is_available or not description:
                raise ValidationError('Поля не могут быть пустыми')

            room_type_id = int(room_type_id)
            number = int(number)
            beds = int(beds)
            price = int(price)

            if (
                not isinstance(room_type_id, int)
                or not isinstance(number, int)
                or not isinstance(beds, int)
                or not isinstance(price, int)
            ):
                raise ValidationError('Поля должны быть числовыми')

            if not isinstance(is_available, bool):
                raise ValidationError('Поле is_available должно быть типа bool')

            room_type = RoomType.objects.get(id=room_type_id)

            room = Room.objects.create(
                room_type=room_type,
                number=number,
                beds=beds,
                price=price,
                is_available=is_available,
                image=image,
                description=description
            )
            room.save()

            return HttpResponseRedirect(reverse('room_list'))

        except ValidationError as e:
            error_message = str(e)
            data = {
                'room_types': RoomType.objects.all(),
                'number': number,
                'beds': beds,
                'price': price,
                'is_available': is_available,
                'image': image,
                'error_message': error_message
            }
            return render(request, 'rooms/room_create.html', data)
    else:
        room_types = RoomType.objects.all()
        data = {
            'room_types': room_types
        }
        return render(request, 'rooms/room_create.html', data)


def room_update(request, room_id):
    if request.method == 'POST':
        room_type_id = request.POST.get('room_type_id')
        number = request.POST.get('number')
        beds = request.POST.get('beds')
        price = request.POST.get('price')
        is_available = request.POST.get('is_available') == 'on'
        image = request.FILES.get('image')
        description = request.POST.get('description')

        try:
            room = Room.objects.get(id=room_id)

            if not room_type_id or not number or not beds or not price or not description:
                raise ValidationError('Поля не могут быть пустыми')

            room_type_id = int(room_type_id)
            number = int(number)
            beds = int(beds)
            price = int(price)

            if (
                not isinstance(room_type_id, int)
                or not isinstance(number, int)
                or not isinstance(beds, int)
                or not isinstance(price, int)
            ):
                raise ValidationError('Поля должны быть числовыми')

            if not isinstance(is_available, bool):
                raise ValidationError('Поле is_available должно быть типа bool')

            room.room_type = RoomType.objects.get(id=room_type_id)
            room.number = number
            room.beds = beds
            room.price = price
            room.is_available = is_available
            if image:
                room.image = image
            room.description = description

            room.save()

            return HttpResponseRedirect(reverse('room_detail', args=[room_id]))

        except ValidationError as e:
            error_message = str(e)
            return render(request, 'rooms/room_update.html', {'error_message': error_message})
    else:
        room = Room.objects.get(id=room_id)
        room_types = RoomType.objects.all()
        data = {
            'number': room.number,
            'beds': room.beds,
            'price': room.price,
            'is_available': room.is_available,
            'image': room.image,
            'description': room.description,
            'room_id': room_id,
            'room_type_id': room.room_type.id,
            'room_types': room_types
        }
        return render(request, 'rooms/room_update.html', data)


def room_delete(request, room_id):
    if request.method == 'POST':
        room = Room.objects.get(id=room_id)

        room.is_deleted = True
        room.save()

        return HttpResponseRedirect(reverse('room_list'))

    else:
        room = Room.objects.get(id=room_id)
        data = {
            'room_id': room.id,
            'number': room.number
        }
        return render(request, 'rooms/room_delete.html', data)
