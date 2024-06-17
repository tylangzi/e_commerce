from django.db import models


class Transport(models.Model):
    SHIPPINF_STATUS_CHOICES = (
        (1, '待发货'),
        (2, '已发货'),
        (3, '运输中'),
        (4, '到达目的地'),
        (5, '已签收'),
        (6, '运输异常'),
    )
    SHIPPING_METHOD_CHOICES = (
        (1, '公路运输'),
        (2, '水路运输'),
        (3, '航空运输'),
    )
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    shipping_method = models.CharField(max_length=50, choices=SHIPPING_METHOD_CHOICES)
    tracking_number = models.CharField(max_length=150)
    shipping_satus = models.CharField(max_length=20, choices=SHIPPINF_STATUS_CHOICES)
    established_delivery_date = models.DateField(null=True, blank=True)
    actual_delivery_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    current_location = models.CharField(max_length=100)
    destination = models.ForeignKey('Address', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.order}采用{self.shipping_method}的运输方式"
