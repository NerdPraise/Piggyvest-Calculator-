from django.shortcuts import render
from .models import Interest 
from datetime import timedelta,date, datetime
from django.http import JsonResponse, HttpResponse

PIGGYBANK_RATE = 0.10
SAFELOCK_RATE10 = 0.10
SAFELOCK_RATE15 = 0.155
TARGET_RATE = FLEX_RATE = 0.10
FLEX_DOLLAR = 0.06
INVESTIFY_RATE = 0.10
#  - 0.25%

def index(request):
    return render(request, "cal/index.html")

def create_info(request):
    context = {}
    if request.method == "POST":
        amount = int(request.POST.get("amount"))
        start_date = request.POST.get("start")
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = request.POST.get("end")
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        duration = end_date - start_date
        duration = duration / timedelta(days=365)
        print(duration)
        piggybank = round(amount *  PIGGYBANK_RATE * duration, 4)
        safelock_10 = round(amount *  SAFELOCK_RATE10 * duration, 4)
        safelock_15 = round(amount *  SAFELOCK_RATE15 * duration, 4)
        flex_dollar = round(amount *  FLEX_DOLLAR * duration, 4)
        investify =round( amount *  INVESTIFY_RATE * duration, 4)
        context = {
            "piggybank" : piggybank,
            "safelock10": safelock_10,
            "safelock15": safelock_15,
            "investify": investify,
            "flex_dollar":flex_dollar
        }
    return render(request, "cal/form.html", context)

