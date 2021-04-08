from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView

from ecommerce.models import Sell, Product, ProductExit

SHIPPING_BASE = 8
SHIPPING_CUT = 10


class ComputeShipping(APIView):
    def get(self, request, sell_id):
        sell_obj = Sell.objects.filter(id=sell_id).first()
        data = {}
        if sell_obj is not None:
            total_price = sell_obj.get_total_price()
            data = {"shippingCost": SHIPPING_BASE}
            if total_price >= SHIPPING_CUT:
                data = {"shippingCost": 0}
        return JsonResponse(data)


class CartUpdate(View):
    def get(self, request, sell_id):
        data = {}

        sell_obj = Sell.objects.filter(id=sell_id).first()

        data['cartId'] = sell_id

        total_price = sell_obj.get_total_price()
        data['total_price'] = total_price

        data["shippingCost"] = SHIPPING_BASE
        if total_price >= SHIPPING_CUT:
            data["shippingCost"] = 0

        data['total_price_shipping'] = total_price + data["shippingCost"]

        products = Product.objects.filter()
        data['products'] = products

        return render(request, 'products.html', data)


class ProductsListing(View):
    def get(self, request):
        data = dict()
        sell_obj = Sell()
        sell_obj.save()

        for product in Product.objects.filter():
            product_exit = ProductExit()
            product_exit.product = product
            product_exit.quantity = 0
            product_exit.sell = sell_obj
            product_exit.save()

        # return redirect(CartUpdate)
        return HttpResponseRedirect(f'/ecommerce/cart/{sell_obj.id}/')
