from django.shortcuts import render, get_object_or_404,HttpResponseRedirect,Http404
from django.http import HttpResponse
from django.views import View
from .models import KirrURL
from .forms import SubmitURLForm

from analytics.models import ClickEvent
# Create your views here.

"""
def test_view(request):
    return HttpResponse("some stuff")


def kirr_redirect_view(request, shortcode=None, *args, **kwargs):    # function based view
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    # return HttpResponse('hello {sc}'.format(sc=obj.url))
    return HttpResponseRedirect(obj.url)
 """


def home_view_fbv(request, *args,**kwargs):
    if request.method=='POST':
        print(request.POST)
    return render(request,"shortener/home.html",{})


class HomeView(View):

    def get(self, request, *args,**kwargs):
        new_form = SubmitURLForm()
        context = {
            "title": "Kirr.Co",
            "form": new_form
        }
        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        # print(request.POST.get("url"))
        form = SubmitURLForm(request.POST)
        context = {
            "title": "Kirr.Co",
            "form": form
        }
        template = "shortener/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            obj,created = KirrURL.objects.get_or_create(url=new_url)
            context ={
                "object":obj,
                "created":created
            }
            if created:
                template="shortener/success.html"
            else:
                template ="shortener/already-exists.html"

        return render(request,template,context)


class URLRedirectView(View):                                              # class based view
    def get(self, request,shortcode=None, *args,**kwargs):
        # print(args)
        # print(kwargs)
        # obj = get_object_or_404(KirrURL, shortcode=shortcode)
        qs=KirrURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count()!=1 and not qs.exists():
            raise Http404
        obj = qs.first()
        print(ClickEvent.objects.create_event(obj))
        # return HttpResponse('hello again {sc}'.format(sc=obj.url))
        return HttpResponseRedirect(obj.url)

    # def post(self, request, *args, **kwargs):
        # return HttpResponse()







    '''
    def kirr_redirect_view(request, shortcode=None, *args, **kwargs):    # function based view
    # print(request.user)
    # print(request.user.is_authenticated())
    # print(args)
    # print(kwargs)
    # print("method is :\n")
    print(request.method)

    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    # obj_url = obj.url


    # try:
    #     obj = KirrURL.objects.get(shortcode=shortcode)
    # except:
    #     obj = KirrURL.objects.all().first()

    # obj_url =None
    # qs = KirrURL.objects.filter(shortcode__iexact=shortcode)
    # if qs.exists() and qs.count()==1:
    #     obj = qs.first()
    #     obj_url = obj.url
    return HttpResponse('hello {sc}'.format(sc=obj.url))


    '''