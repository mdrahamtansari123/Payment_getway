from django.shortcuts import render
from .models import Coffee

# Create your views here.

import razorpay
from django.views.decorators.csrf import csrf_exempt

def Razor_Pay(request):
  if request.method == "POST":
      name = request.POST.get("name")
      amount = int(request.POST.get("amount"))*100 
      client=razorpay.Client(auth =("rzp_test_Ry0NdyRbZevRle" , "9kPb02DDhfBNr1LmjFVkJONX"))
      payment=client.order.create({'amount':amount, 'currency':'INR' , 'payment_capture' : '1'})
      coffee=Coffee(name = name , amount = amount , payment_id = payment['id'])
      coffee.save()
      return render(request , 'coffee/index.html', {'payment':payment})
  return render(request , 'coffee/index.html')

@csrf_exempt
def Success(request):
 if request.method=="POST":
     a=request.POST
     print(a)
     order_id=""
     for key,val in a.items():
      if key=="razorpay_order_id":
        order_id = val
        break
     user=Coffee.objects.filter(payment_id=order_id).first() 
     user.paid=True
     user.save()
 return render(request , 'coffee/success.html')   