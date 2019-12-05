from django.shortcuts import render,get_object_or_404
from .models import squirrel
from .forms import create_squirrel,update_squirrel
from django.http import HttpResponse,HttpResponseRedirect

def map(request):
    sightings = squirrel.objects.all()
    context = {
            'sightings':sightings,
            }
    return render(request,'sightings/map.html',context)

def stats(request):


    n = len(squirrel.objects.all())

    n_am = len(squirrel.objects.filter(Shift='AM'))
    n_pm = len(squirrel.objects.filter(Shift='PM'))
    pct_am = round(n_am/n*100,2)
    pct_pm = round(n_pm/n*100,2)

    n_black = len(squirrel.objects.filter(Primary_fur_color='Black'))
    n_gray = len(squirrel.objects.filter(Primary_fur_color='Gray'))
    n_cinnamon = len(squirrel.objects.filter(Primary_fur_color='Cinnamon'))
    pct_black = round(n_black/n*100,2)
    pct_gray = round(n_gray/n*100,2)
    pct_cinnamon = round(n_cinnamon/n*100,2)

    n_adult = len(squirrel.objects.filter(Age='Adult'))
    n_juvenile = len(squirrel.objects.filter(Age='Juvenile'))
    pct_adult = round(n_adult/n*100,2)
    pct_juvenile = round(n_juvenile/n*100,2)

    n_gp = len(squirrel.objects.filter(Location='Ground Plane'))
    n_ag = len(squirrel.objects.filter(Location='Above Ground'))
    pct_gp = round(n_gp/n*100,2)
    pct_ag = round(n_ag/n*100,2)



    context = {
            'pct_am': pct_am,
            'pct_pm': pct_pm,
            'pct_black': pct_black,
            'pct_gray': pct_gray,
            'pct_cinnamon': pct_cinnamon,
            'pct_adult': pct_adult,
            'pct_juvenile': pct_juvenile,
            'pct_plane': pct_gp,
            'pct_above': pct_ag,
            'total_number':n,

            }
    return render(request,'sightings/stat.html',context)

def thank_you(request):

    return HttpResponse('Thank you!')


def all_squirrels(request):
    squirrels = squirrel.objects.all()
    context = {
            'squirrels':squirrels,
            }
    return render(request,'sightings/all_squirrels.html',context)


def add_sighting(request):
    if request.method == 'POST':        
        form = create_squirrel(request.POST)
        if form.is_valid():
            form.save()   
            return HttpResponseRedirect('/sightings/thanks/')
    else:
        form = create_squirrel()
    return render(request,'sightings/add.html',{'form':form})


def update_successful(request):

    context={
            'text':'Update successfully!'
            }

    return render(request,'sightings/return.html',context)


def update_nothing(request):

    context={
            'text':'No update happens!'
            }

    return render(request,'sightings/return.html',context)


def update_sighting(request,unique_id):
    target = squirrel.objects.get(Unique_id=unique_id)
    if request.method == 'POST':
        form = update_squirrel(request.POST,instance=target)
        if form.is_valid():
            if form.has_changed():
                form.save()
                return HttpResponseRedirect('/sightings/success')
            else:
                return HttpResponseRedirect('/sightings/no_update/')
    else:
        form = update_squirrel(instance=target)
    return render(request,'sightings/update.html',{'form':form,'unique_id':unique_id})


def delete(request,unique_id):
    target_squirrels = get_object_or_404(squirrel,Unique_id=unique_id)
    target_squirrels.delete()
    return HttpResponse('Successfully delete!')
