# support/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ticket, Message
from .forms import TicketForm, MessageForm

@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('ticket_detail', ticket_id=ticket.id)
    else:
        form = TicketForm()
    return render(request, 'support/create_ticket.html', {'form': form})

@login_required
def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    form = MessageForm()
    return render(request, 'support/ticket_detail.html', {'ticket': ticket, 'form': form})

@login_required
def reply_to_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.ticket = ticket
            message.sender = request.user
            message.save()
            return redirect('ticket_detail', ticket_id=ticket.id)
    else:
        form = MessageForm()
    return render(request, 'support/reply_to_ticket.html', {'form': form})
