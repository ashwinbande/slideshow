import json
from django.http import HttpResponse
from django.shortcuts import render
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from .models import Presentation, FeedBack, Slide


class FeedBackForm(ModelForm):

    class Meta:
        model = FeedBack
        fields = '__all__'


def home_view(request):
    context = {
        'presentations': Presentation.objects.all()
    }
    return render(request, 'home.html', context)


def presentation_view(request, pk):

    def get_slide_obj(slide):
        return {
            'image': slide.image.url,
            'audio': slide.audio.url,
            'name': slide.name,
            'id': slide.id,
        }
    try:
        presentation = Presentation.objects.get(pk=pk)
        slides = map(lambda slide: {'slide': slide, 'form': FeedBackForm(instance=slide)},
                     presentation.slide_set.all())
        context = {
            'presentation': presentation,
            'domain': request.META['HTTP_HOST'],
            'slides': list(map(get_slide_obj, presentation.slide_set.all())),
        }
    except Presentation.DoesNotExist:
        return render(request, 'not_found.html')
    return render(request, 'presentation.html', context)


@csrf_exempt
def feedback_view(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        mobile = body.get('mobile')
        slide = Slide.objects.get(pk=body.pop('slide'))

        try:
            obj = FeedBack.objects.get(mobile=mobile, slide=slide)
            for key, value in body.items():
                setattr(obj, key, value)
            obj.save()
        except FeedBack.DoesNotExist:
            print('updated object')
            obj = FeedBack(**body, slide=slide)
            obj.save()
        return HttpResponse('Content Updated')
