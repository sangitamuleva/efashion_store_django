from django import template

register=template.Library()

@register.filter(name='currency')
def currency (number):
    
    return '₹ ' + str(number)



@register.filter(name='order_total')
def order_total (price,quantity):
    
    return price * quantity