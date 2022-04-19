from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View

from donation.models import Donation, Institution, Category


class LandingPage(View):
    def get(self, request):
        num_of_bags = Donation.objects.all().aggregate(Sum('quantity'))['quantity__sum'] or 0
        institutions = Institution.objects.all()
        num_of_institutions = Institution.objects.all().count()
        context = {
            'num_of_bags': num_of_bags,
            'institutions': institutions,
            'num_of_institutions': num_of_institutions
        }
        return render(request, 'index.html', context)


class AddDonation(View):
    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        context = {
            'categories': categories,
            'institutions': institutions
        }
        if request.user.is_authenticated:
            return render(request, 'form.html', context)
        else:
            return redirect('login')

    def post(self, request):
        categories = request.POST.getlist('categories[]')
        institution = request.POST.get('organization')
        quantity = request.POST.get('bags')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zip_code = request.POST.get('postcode')
        phone = request.POST.get('phone')
        date = request.POST.get('data')
        time = request.POST.get('time')
        pick_up_comment = request.POST.get('more_info')
        user = request.user

        donation = Donation.objects.create(quantity=quantity, address=address, phone_number=phone,
                                           city=city, zip_code=zip_code, pick_up_date=date, pick_up_time=time,
                                           pick_up_comment=pick_up_comment,
                                           institution_id=institution, user=user)

        for category in categories:
            donation.categories.add(category)
        donation.save()

        return render(request, 'form-confirmation.html')


class DonationConfirmation(View):
    def get(self, request):
        return render(request, 'form-confirmation.html')
