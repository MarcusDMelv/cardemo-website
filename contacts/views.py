from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect
from contacts.models import Contact
from django.contrib import messages
from django.core.mail import send_mail

def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        # todo add data to model Contact()

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id,user_id=user_id)
            if has_contacted:
                messages.error(request,'We understand you are eager to get started! We will contact you as soon as we can.')
                return redirect('/cars/' + car_id)
        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name,
                          last_name=last_name, customer_need=customer_need, city=city, state=state, email=email,
                          phone=phone, message=message)
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        """
         send_mail(
            'New Car Inquiry',
            'You have a new inquiry for '+car_title+'Please login to your admin account!',
            'HOST_EMAIL', # host email
            [admin_email],# todo super user admin email
            fail_silently=False,
        )
        """


        contact.save()
        messages.success(request,"Your request has been sent! We will reach back out to you shortly, Thank you.")
        return redirect('/cars/'+car_id)
