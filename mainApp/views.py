from django.shortcuts import render, redirect
from .models import Gig, GigManager
from django.views import View

def get_home_page(request):
    
    gigs = Gig.objects.all().order_by('-id')
    
    print(gigs)
    
    args = {
        'gigs': gigs
    }
    return render(request, 'index.html', args)


# def gig_details(request, id):
    
    

# def add_basic_package(request):
#     cart = request.session.get('cart', {})
#     basic = request.POST.get('package_id')
#     remove = request.POST.get('remove')
#     print(basic)
    
#     cart = {
#             'quantity': 1,
#             'gig_manager': request.POST['package_id']
#         }
#     if remove:
#         cart['package_id'] = cart['package_id'] - 1
#     else:
#         cart['package_id'] = cart['package_id'] + 1
        
#         return redirect('/')
    # if not cart:
    #     request.session['cart'] = {}
      
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



        # cart = {
        #     'quantity': 1,
        #     'gig_manage': request.POST['package_id']
        # }
        
        # if remove:
        #     cart['package_id'] = cart['package_id'] - 1
        # else:
        #     cart['pacakge_id'] = cart['package_id'] + 1
        
        # print('CART:', request.session['cart'])
        # return redirect('/')
        




# def get_checkout_page(request):
#     basic_ids = list(request.session.get('cart').keys())
#     basic_cart = Basic.get_basic_ids(basic_ids)
#     # basic = Basic.objects.all()
#     # quantity = request.POST.get('quantity')
#     # total_price = quantity * 
    
#     # basic_prices = list(map(self.basic_map_func, basic_cart))
   
#     print(basic_cart)
#     args = {
#         'basic_cart': basic_cart,
#         # 'total_price': total_price
#     }
#     return render(request, 'cart.html', args)
