from django.db import models


class Product(models.Model):
    """Product model for storing product information."""
    name = models.CharField(max_length=100, help_text="Product name")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Product price")
    description = models.TextField(help_text="Detailed product description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"{self.name} - ${self.price}"