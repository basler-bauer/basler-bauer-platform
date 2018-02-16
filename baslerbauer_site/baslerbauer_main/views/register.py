from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from baslerbauer_main.models import Producer


@csrf_exempt
def register(request):
    @csrf_protect
    def user_register(request):
        user = User.objects.create_user(username=request.POST.get("email"),password=request.POST.get("password"));
        p = Producer.objects.get(pk=request.POST.get("producer"))
        p.user=user
        p.save()
        return HttpResponse("Registered")
    if request.method == 'POST':
        return user_register(request)
    else:
        template = loader.get_template('baslerbauer_main/register.html')
        context = {
            'producer_list': Producer.objects.all()
        }
        return HttpResponse(template.render(context, request))
