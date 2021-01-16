from django.shortcuts import render

import datetime
# Create your views here.

# Fucntion with logic with datetime library, sending a boolean to the html template
def index(request):
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.month == 9 and now.day == 6
    })