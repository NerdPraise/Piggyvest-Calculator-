from django.shortcuts import render
from .models import Interest 
from datetime import timedelta,date, datetime
from django.http import JsonResponse, HttpResponse

SAFELOCK_RATE15 = 0.155
PIGGYBANK_RATE = INVESTIFY_RATE10 = TARGET_RATE = FLEX_RATE = SAFELOCK_RATE10 = 0.10
FLEX_DOLLAR = 0.06
INVESTIFY_RATE25 = 0.25

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
        piggybank = round(amount *  PIGGYBANK_RATE * duration, 4)
        safelock_15 = round(amount *  SAFELOCK_RATE15 * duration, 4)
        flex_dollar = round(amount *  FLEX_DOLLAR * duration, 4)
        investify25 =round( amount *  INVESTIFY_RATE25 * duration, 4)

        context = {
            "piggybank" : piggybank,
            "safelock15": safelock_15,
            "investify25": investify25,
            "flex_dollar":flex_dollar,
        }
    return render(request, "cal/index.html", context)

