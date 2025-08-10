# complaints/models.py

from django.db import models
from django.contrib.auth.models import User


class Complaint(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('INP', 'In Progress'),
        ('FIX', 'Fixed'),
        ('CLO', 'Closed'),
    ]

    name = models.CharField(max_length=120, blank=True)
    contact = models.CharField(max_length=64, blank=True)
    email = models.EmailField(blank=True, null=True)
    location = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.ImageField(upload_to='complaint_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='NEW')

    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_complaints',
        help_text='The technician this complaint is assigned to'
    )

    def __str__(self):
        return f"Complaint #{self.id} - {self.get_status_display()}"


class StatusUpdate(models.Model):
    complaint = models.ForeignKey(
        Complaint,
        on_delete=models.CASCADE,
        related_name='updates'
    )
    status = models.CharField(max_length=3, choices=Complaint.STATUS_CHOICES)
    comment = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Update {self.get_status_display()} for #{self.complaint.id}"
