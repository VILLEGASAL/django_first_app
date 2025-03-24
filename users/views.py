from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

names = ["john", "andrew", "michael"]

# Create your views here.
def Users(request):

    for name in names:
        print(name)
    
    return JsonResponse({"users": names}, status=200)

@csrf_exempt # type: ignore
def getUser(request):
    print("REQUEST METHOD: " + request.method)

    nameBody = request.POST.get("name")

    if request.method == "POST":
        
        if nameBody:
            nameBody = nameBody.lower()

            for name in names:
                if name == nameBody:
                    return JsonResponse({"User Found!": name})

        return HttpResponse("User not found!")
