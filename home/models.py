from django.db import models

# Base Model for app the related models
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Measurement Model
class Measurement(BaseModel):
    height = models.DecimalField(max_digits= 5, decimal_places=2)
    weight = models.DecimalField(max_digits= 5, decimal_places=2)
    age = models.DecimalField(max_digits= 5, decimal_places=2)
    waist = models.DecimalField(max_digits= 5, decimal_places=2)
    user_created = models.BooleanField(default=False)
    
    # Get json value of the object
    def get_json(self):
        return {
            "height": self.height,
            "weight": self.weight,
            "age": self.age,
            "waist": self.waist,
            "user_created": self.user_created
        }
    
    # Get string name
    def __str__(self):
        return f'object-{self.pk}-height-{self.height}-weight-{self.weight}-age{self.age}-{self.age}'
    
    class Meta:
        ordering = ['-pk']
