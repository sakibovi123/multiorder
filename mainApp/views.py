from django.shortcuts import render, redirect, HttpResponse
from .models import Gig, GigManager, Order
from django.views import View

def get_home_page(request):
    
    gigs = Gig.objects.all().order_by('-id')
    
    print(gigs)
    
    args = {
        'gigs': gigs
    }
    return render(request, 'index.html', args)


      
class GigDetails(View):
    def get(self, request, id):
        gig_details = Gig.objects.get(pk=id)
        
        cart = request.session.get('cart')
        
        if not cart:
            request.session['cart'] = {}
    
        args = {
        'gig_details': gig_details     
        }
        return render(self.request, 'gig_details.html', args)
    
def post(request):
    cart = request.session.get('cart', {})
    print(cart)
    package_id = request.POST.get('package_id')
    remove = request.POST.get('remove')
        
    if cart:
        quantity = cart.get(package_id)
        if quantity:
            cart[package_id] = quantity + 1
        else:
            cart[package_id] = 1
    else:
        cart = {}
        cart[package_id] = 1
        
    request.session['cart'] = cart
        
    print('CART:', request.session['cart'])
        
    return redirect('CartView')
        
        
class CartView(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        ids = list(request.session.get('cart').keys())
        cart_products = GigManager.get_gig(ids)
        print(cart)
        context = {
            'cart_products': cart_products
        }
        return render(self.request, 'cart.html', context)



class OrderCheckoutView(View):
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        ids = list(request.session.get('cart').keys())
        cart_products = GigManager.get_gig(ids)
        print(cart)
        context = {
            'cart_products': cart_products
        }
        return render(self.request, 'checkout.html', context)


    def post(self, request):
        cart = request.session.get('cart')
        name = request.POST.get('name')

        packages = GigManager.get_gig(list(cart.keys()))
        user = request.user
        
        for package in packages:

            order = Order(
                    name = name,
                    user = user,
                    package = package,
                    price = package.price,
                    seller = package.gig.seller
                )
            print(package)
            print(order)

            order.save()
            request.session['cart'] = {}

            return HttpResponse("Order Has Been Placed!")






























































