from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse, Http404
from home.utils import WaistSizePredictor
from home.models import Measurement 


def get_measurement_data():
    measurements = Measurement.objects.all() 
    data = []
    for m in measurements:
        payload = {'height': m.height, 'weight': m.weight, 'age': m.age, 'waist': m.waist}
        data.append(payload)
    return data

def validate_float_inputs(value):
    try:
        float(value)
    except:
        raise Http404

def get_waist(request):
    if request.method == "GET":
        height, age, weight = request.GET.get('height', ''), request.GET.get('age', ''), request.GET.get('weight', '')
        validate_float_inputs(height), validate_float_inputs(age), validate_float_inputs(weight)
        try:
            predictor = WaistSizePredictor(data=get_measurement_data())
            predictor.set_prediction_data(height, age, weight)
            predicted_waist = predictor.predict()
            return JsonResponse({"waist": round(predicted_waist[0], 2)}) 
        except Exception as e:
            raise Http404     
    else:
        raise Http404
    
def update_waist(request):
    if request.method == "POST":
        height, age, weight, waist = request.POST.get('height', ''), request.POST.get('age', ''), request.POST.get('weight', ''), request.POST.get('waist', '')
        validate_float_inputs(height), validate_float_inputs(age), validate_float_inputs(weight), validate_float_inputs(waist)
        print(height, age, weight, waist )
        try:
            m, created = Measurement.objects.get_or_create(height=height, weight=weight, age=age, waist=waist)
            if created:
                m.user_created = True
                m.save()
            return JsonResponse(m.get_json())
        except Exception as e:
            raise Http404
    else:
        raise Http404
        

class Index(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        page_object = Measurement.objects.filter().first()
        context = super().get_context_data(**kwargs)
        context['page_object'] = page_object
        return context 