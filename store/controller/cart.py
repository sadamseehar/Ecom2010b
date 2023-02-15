from django.shortcuts import render,redirect

from django.contrib import messages

from django.http.response import JsonResponse
from store.models import Product,Cart

def addtocart(request):
    if request.method == "POST":
         prod_id = int(request.POST.get('product_id'))
         product_check = Product.objects.get(id=prod_id)
         if(product_check):
            if(Cart.objects.filter(user=request.user , product_id = prod_id)):
                return JsonResponse({'status':'product already in cart'})
            else : 
                prod_qty = int(request.POST.get('product_qty'))

                if product_check.quantity >= prod_qty:
                    Cart.objects.create(user=request.user , product_id = prod_id , product_qty = prod_qty)
                    return JsonResponse({'status':'Product added'})

                else : 
                    return JsonResponse({'status':'only' + str(product_check.quantity)+"quantity available"})
         else :
            return JsonResponse({'status':'no such producrt'})
    else: 
        return JsonResponse({'status':'login to continue'})

    return redirect("/")


def cartview(request):
    cart = Cart.objects.filter(user = request.user)
    context = {'cart':cart}
    return render(request,"store/cart.html",context)

                    


def updatecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id')) # 1
        
        if(Cart.objects.filter(user=request.user, product_id=prod_id )):
            prod_qty = int(request.POST.get('product_qty')) #4
            cart = Cart.objects.filter(product_id=prod_id,user=request.user)
            cart.product_qty = prod_qty
            cart.save()
    return redirect("/")          
