from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse, Http404
from home.utils import WaistSizePredictor
from home.models import Measurement 

# Get data from database for predict model
def get_measurement_data():
    measurements = Measurement.objects.all() 
    data = []
    for m in measurements:
        payload = {'height': m.height, 'weight': m.weight, 'age': m.age, 'waist': m.waist}
        data.append(payload)
    return data

# check form inputs or raise error
def validate_float_inputs(value):
    try:
        float(value)
    except:
        raise Http404

# Get waist detail
def get_waist(request):
    if request.method == "GET":
        # get post data
        height, age, weight = request.GET.get('height', ''), request.GET.get('age', ''), request.GET.get('weight', '')
        # Validate waist
        validate_float_inputs(height), validate_float_inputs(age), validate_float_inputs(weight)
        try:
            # init predictor
            predictor = WaistSizePredictor(data=get_measurement_data())
            # setting up user input data
            predictor.set_prediction_data(height, age, weight)
            # prediction details
            predicted_waist = predictor.predict()
            # return response as json
            return JsonResponse({"waist": round(predicted_waist[0], 2)}) 
        except Exception as e:
            # raise error if any issue
            raise Http404     
    else:
        # raise error if request is not GET
        raise Http404
        
# Update waist
def update_waist(request):
    if request.method == "POST":
        # get post data
        height, age, weight, waist = request.POST.get('height', ''), request.POST.get('age', ''), request.POST.get('weight', ''), request.POST.get('waist', '')
        # Validate waist
        validate_float_inputs(height), validate_float_inputs(age), validate_float_inputs(weight), validate_float_inputs(waist)
        
        try:
            # Create new object
            m, created = Measurement.objects.get_or_create(height=height, weight=weight, age=age, waist=waist)
            # checking object is a new object or not, if new, this will be stored as user created item for filtering the data in the future
            if created:
                m.user_created = True
                m.save()
            # returning json response of model
            return JsonResponse(m.get_json())
        except Exception as e:
            raise Http404
    else:
        # raise error if request is not POST
        raise Http404
        
# Index page
class Index(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        # object for first load
        page_object = Measurement.objects.filter().first()
        context = super().get_context_data(**kwargs)
        context['page_object'] = page_object
        return context 
