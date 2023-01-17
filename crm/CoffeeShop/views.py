from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .orderForm import createOrderForm
from django.forms import inlineformset_factory
from .orderFilter import OrderFilter


# Create your views here.


def home(request):
    # return HttpResponse("Home Page")
    
    # render data from database
    orders =  Order.objects.all()
    customers= Customer.objects.all()
    
    total_customers = customers.count()
    total_orders = orders.count()
    
    total_delivered = orders.filter(status='Delivered').count()
    total_pending = orders.filter(status='Pending').count()
    
    # container dictionaries for sending data to webpage
    
    container = {
        'orders':orders,
        'customers':customers,
        'total_customers':total_customers,
        'total_orders':total_orders,
        'total_delivered':total_delivered,
        'total_pending':total_pending
    }
    
    return render(request, 'CoffeeShop/dashboard.html', container)




def products(request):
    products = Product.objects.all()
    
    
    return render(request, 'CoffeeShop/products.html', {'products':products})





def customers(request,pk):
    
    # queries from database
    customer= Customer.objects.get(id=pk)
    orders= customer.order_set.all()
    order_count = orders.count()
    
    ########  Order filter code start #############
    
    myFilter = OrderFilter(request.GET, queryset = orders)
    orders = myFilter.qs
    
    
    ########  Order filter code end #############
    
    
    container = {
        'customer':customer,
        'orders':orders,
        'order_count':order_count,
        'myFilter':myFilter,
    }
    
    return render(request, 'CoffeeShop/customers.html', container)




def createOrder(request, pk):
    ########## Normal ways #############
    # form = createOrderForm ()
    # if request.method == 'POST':
    #     form = createOrderForm(request.POST)
        
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')
    
    # container = {'form':form}
    
    ######### Formset ways ################
    orderFormSet = inlineformset_factory( Customer, Order, fields = ('product','status'), extra = 3)
    customer = Customer.objects.get(id=pk)
    formset = orderFormSet(queryset=Order.objects.none(),instance=customer)
    
    if request.method == 'POST':
        formset = orderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    
    container = {'formset':formset}
    
    return render(request,'CoffeeShop/createOrder.html', container)



def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form = createOrderFrom(instance = order)
    
    if request.method == 'POST':
        form = createOrderFrom(request.POST, instance = order)
        
        if form.is_valid():
            form.save()
            return redirect('/')
    
    container = {'form':form}
    
    return render(request,'CoffeeShop/createOrder.html', container)





def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    container ={'item':order}
    return render(request, 'CoffeeShop/deleteOrder.html', container)