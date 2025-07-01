from djongo import models

# Create your models here.
class CalculationResult(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    c = models.IntegerField()
    d = models.IntegerField()
    e = models.IntegerField()
    average = models.FloatField()
    avg_above_50 = models.BooleanField()
    positive_count = models.IntegerField()
    even_or_odd_bitwise = models.CharField(max_length=255)
    original_list = models.JSONField()
    sorted_list = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"CalculationResult {self.id}"