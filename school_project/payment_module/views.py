from django.shortcuts import redirect
from django.views.generic import View
from payment_module.models import Payment
from user_request_module.models import Service


class PayService(View):
    def post(self, request):
        service_id = request.POST.get('service_id')
        service = Service.objects.get(id=service_id)
        if service.servicer != "":
            payment = Payment.objects.create(
                service=service,
                amount=service.price,
                success=True
            )

        service.pay = payment
        service.save()

        return redirect('user_service_request')

