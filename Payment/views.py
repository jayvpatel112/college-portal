from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum
MERCHANT_KEY = 'WRITE_YOUR_MERCHANT_KEY'

# Create your views here.
@csrf_exempt
def pay(request):
    if request.method=='POST':
        # print('We are using post request')
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip_code']
        fees = request.POST['fees']
        print(name, email, phone)

        if len(name)<2 or len(email)<3 or len(phone)<10 :
            messages.error(request, 'Plese fill the form correctly')
        else :
            paymentdetail = paymentDetail(name=name, email=email, phone=phone, address=address,city=city, state=state, zip_code=zip_code, fees=fees)
            paymentdetail.save()
            messages.success(request, 'your message has been successfully sent')
        
        # return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
        #request paytm to transfer the amount to your account after payment by user
        param_dict={
            'MID': 'WRITE_YOUR_MERCHANT_ID',
            'ORDER_ID': 'dddgfgfeeed',
            'TXN_AMOUNT': str(fees),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/Payment/handlerequest/',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return  render(request, 'Payment/paytm.html', {'param_dict': param_dict})
        # return render(request, 'shop/checkout.html')
        
        # return redirect('home')

    return render(request, 'Payment/pay.html')



@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    
    # return HttpResponse('done')
    
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'Payment/paymentstatus.html', {'response': response_dict})
