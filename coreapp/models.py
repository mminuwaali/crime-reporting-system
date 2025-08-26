from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('investigating', 'Investigating'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    )
    
    CATEGORY_CHOICES = (
        ('theft', 'Theft'),
        ('assault', 'Assault'),
        ('fraud', 'Fraud'),
        ('vandalism', 'Vandalism'),
        ('harassment', 'Harassment'),
        ('other', 'Other'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='complaints')
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date_of_incident = models.DateField()
    time_of_incident = models.TimeField(null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"
    
    class Meta:
        ordering = ['-created_at']

class Response(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, related_name='responses')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_from_police = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Response to {self.complaint.title}"
    
    class Meta:
        ordering = ['created_at']

class Evidence(models.Model):
    complaint = models.ForeignKey(Complaint, on_delete=models.CASCADE, related_name='evidence')
    file = models.FileField(upload_to='evidence/')
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Evidence for {self.complaint.title}"
