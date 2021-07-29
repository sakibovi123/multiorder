from django import template


register = template.Library()


@register.filter(name='gig_price_start')
def gig_price_start(queryset):
    return queryset.first().price


@register.filter(name='basic_in_cart')
def basic_is_in_cart(gig):
    pass

@register.filter(name="cart_quantity")
def cart_quantity(package_id, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == package_id.id:
            return cart.get(id)
    return 0


@register.filter(name="price_total")
def price_total(basic, cart):
    return basic.price * cart_quantity(basic, cart)
    