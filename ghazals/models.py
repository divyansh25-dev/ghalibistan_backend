from django.db import models

# Create your models here.
class Poem(models.Model):
    name = models.TextField()
    author = models.TextField(blank=True)
    interpretation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey('auth.user',related_name='poems',on_delete=models.DO_NOTHING)


    
class PoemReactions(models.Model):
    reacted_by = models.ForeignKey('auth.user',related_name='poem_reaction',on_delete=models.CASCADE)
    reaction = models.TextField()
    poem = models.ForeignKey(Poem,related_name='poem_reaction_2',on_delete=models.CASCADE) 
    



