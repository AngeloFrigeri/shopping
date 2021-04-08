from django.http import JsonResponse
from rest_framework.views import APIView

from ecommerce.models import Sell


class ComputeShipping(APIView):
    def get(self, request, sell):
        sell_obj = Sell.objects.filter(id=sell).first()
        data = {}
        if sell_obj is not None:
            total_price = sell_obj.get_total_price()
            data = {"shippingCost": 5}
            if total_price >= 10:
                data = {"shippingCost": 0}
        return JsonResponse(data)
