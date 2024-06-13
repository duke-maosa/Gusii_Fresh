from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ticket
from django.contrib import messages
from .forms import TicketForm, MessageForm

@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)  # Don't save to database yet
            ticket.user = request.user  # Assign the logged-in user to the ticket
            ticket.save()  # Now save to database
            messages.success(request, 'Your ticket has been created successfully!')
            return redirect('support:ticket_detail', ticket_id=ticket.id)
    else:
        form = TicketForm()
    return render(request, 'support/create_ticket.html', {'form': form})


@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    form = MessageForm()
    return render(request, 'home/index.html', {'ticket': ticket, 'form': form})

@login_required
def reply_to_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
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
    return render(request, 'support/ticket_detail.html', {'ticket': ticket, 'form': form})
