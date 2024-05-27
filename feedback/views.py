from django.shortcuts import render, HttpResponseRedirect
from .models import Feedback, TicketStatus, TicketCategory
from django.urls import reverse


def create_ticket(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    category_id = request.POST.get('category_id')
    user = request.user

    ticket_status = TicketStatus.objects.get(id=1)
    ticket_category = TicketCategory.objects.get(id=category_id)

    feedback = Feedback.objects.create(
        title=title,
        description=description,
        status=ticket_status,
        category=ticket_category,
        user=user,
    )

    feedback.save()

    return HttpResponseRedirect(reverse('room_list'))


def feedback_list(request):
    user = request.user
    feedbacks = Feedback.objects.filter(user=user)
    return render(request, 'feedback/feedback_list.html', {'feedbacks': feedbacks})


def feedback_detail(request, id):
    feedback = Feedback.objects.get(id=id)
    return render(request, 'feedback/feedback_detail.html', {'feedback': feedback})


from django.shortcuts import render

# Create your views here.
