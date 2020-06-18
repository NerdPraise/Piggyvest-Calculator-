from django.shortcuts import render
from .models import Interest 
from datetime import timedelta,date, datetime
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


SAFELOCK_RATE15 = 0.155
PIGGYBANK_RATE = INVESTIFY_RATE10 = TARGET_RATE = FLEX_RATE = SAFELOCK_RATE10 = 0.10
FLEX_DOLLAR = 0.06
INVESTIFY_RATE25 = 0.25

def index(request):
    return render(request, "cal/index.html")


@csrf_exempt
def create_info(request):
    data = {}
    if request.method == "POST":
        try:
            amount = int(request.POST.get("amount"))
            start_date = request.POST.get("start")
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = request.POST.get("end")
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            duration = end_date - start_date
            duration = duration / timedelta(days=365)
            piggybank = round(amount *  PIGGYBANK_RATE * duration, 4)
            safelock_15 = round(amount *  SAFELOCK_RATE15 * duration, 4)
            flex_dollar = round(amount *  FLEX_DOLLAR * duration, 4)
            investify =round( amount *  INVESTIFY_RATE25 * duration, 4)
        except:
            data = {"error":"Invalid details"}
            return JsonResponse(data)

        data = {
            "success":f"""Piggybank interest is ₦{piggybank}
Safelock interest is ₦{piggybank} to ₦{safelock_15} 
Target interest is ₦{piggybank}
Flex interest is ₦{piggybank}
Flex dollar interest is ₦{flex_dollar}
Investify interest is between ₦{piggybank} to ₦{investify}"""
        }
        return JsonResponse(data)
        

