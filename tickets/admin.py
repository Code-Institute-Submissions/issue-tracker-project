from django.contrib import admin
from .models import Ticket, Comment, Vote, Payment

admin.site.register(Ticket)
admin.site.register(Comment)
admin.site.register(Vote)
admin.site.register(Payment)
