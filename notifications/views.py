from django.shortcuts import render, redirect, get_object_or_404
from .models import Notification
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def notifications_list(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')

    # Pagination
    paginator = Paginator(notifications, 10)  # Show 10 notifications per page
    page = request.GET.get('page')
    try:
        notifications = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        notifications = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        notifications = paginator.page(paginator.num_pages)

    return render(request, 'notifications/notification_list.html', {'notifications': notifications})

@login_required
def mark_as_read(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id, user=request.user)
    notification.is_read = True
    notification.save()
    return redirect('notifications_list')

@login_required
def mark_all_as_read(request):
    notifications = Notification.objects.filter(user=request.user, is_read=False)
    for notification in notifications:
        notification.is_read = True
        notification.save()
    return redirect('notifications_list')

@login_required
def delete_notification(request, notification_id):
    notification = get_object_or_404(Notification, pk=notification_id, user=request.user)
    notification.delete()
    return redirect('notifications_list')

@login_required
def delete_all_notifications(request):
    notifications = Notification.objects.filter(user=request.user)
    notifications.delete()
    return redirect('notifications_list')
