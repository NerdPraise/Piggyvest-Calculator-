from calendar import monthrange
from django.shortcuts import render
from .models import Interest 
from django.utils import timezone
from datetime import timedelta, datetime
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
import csv
from django.core.files.storage import FileSystemStorage

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
            plan = request.POST.get("plan")
            start_date = str(timezone.now()).split(" ")[0]
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = request.POST.get("end")
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
            if plan == "Daily": 
                duration = end_date - start_date 
                duration = duration.days 
                average = amount / duration

                piggybank = round(average / 1.0002739, 2)
                safelock_15 = round(average/ 1.0004246, 2)
                flex_dollar = round(average / 1.0001643, 2)
                investify = round(average / 1.0006849, 2)
                word = "days"
            elif plan == "Monthly":
                duration = 0
                while start_date <= end_date:
                    start_date += timedelta(days=monthrange(start_date.day,start_date.month)[1])
                    duration += 1
                average = amount / duration 
                piggybank = round(average / 1.00833, 2)
                safelock_15 = round(average/ 1.01291, 2)
                flex_dollar = round(average / 1.005, 2)
                investify = round(average / 1.0208, 2)
                word = "months"
            elif plan == "Bi-Monthly":
                duration = 0
                while start_date <= end_date:
                    start_date += timedelta(days=monthrange(start_date.day,start_date.month)[1])
                    duration += 1
                duration = duration // 2
                average = amount / duration
                piggybank = round(average / 1.0166, 2)
                safelock_15 = round(average/ 1.02583, 2)
                flex_dollar = round(average / 1.01, 2)
                investify = round(average / 1.04166, 2)

            
            
        except:
            data = {"error":"Invalid details"}
            return JsonResponse(data)
        
        data = {
            "success":f"""For {duration} {word}
Plan:PiggyBank, Estimate saving: ₦{piggybank}
Plan:Safelock, Estimate saving: ₦{piggybank} to ₦{safelock_15} 
Plan:Target, Estimate saving is ₦{piggybank}
Plan:Flex, Estimate saving is ₦{piggybank}
Plan:Flex Dollar, Estimate saving is ₦{flex_dollar}
Plan:Investify, Estimate saving is between ₦{piggybank} to ₦{investify}"""
        }
        return JsonResponse(data)
        
@csrf_exempt
def export_data(request):
    content = request.POST.get("data[]")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="you.csv"'

    writer = csv.writer(response)
    for line in content:
        writer.writerow(line)

    return response