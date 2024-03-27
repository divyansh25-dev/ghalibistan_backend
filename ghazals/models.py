from django.db import models

# Create your models here.
class Ghazal(models.Model):
    name = models.TextField()
    interpretation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey('auth.user',related_name='ghazals',on_delete=models.CASCADE)
    
class Discussion(models.Model):
    comment = models.TextField()
    reply_to_id = models.IntegerField(max_length=100,null=True, blank=True)
    ghazal = models.ForeignKey(Ghazal, related_name='discussions_ghazals', on_delete=models.CASCADE)
    commented_by = models.ForeignKey('auth.user',related_name='discussions_user',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Reaction(models.Model):
    
    reaction = models.BooleanField(blank=False)
    reacted_by = models.ForeignKey('auth.user',related_name='reactions_user',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    discussion = models.ForeignKey(Discussion,related_name='reactions_discussion',on_delete=models.CASCADE)

    