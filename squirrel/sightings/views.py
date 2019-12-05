from django.shortcuts import render,get_object_or_404
from .models import squirrel
from .forms import create_squirrel,update_squirrel
from django.http import HttpResponse,HttpResponseRedirect

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

    return HttpResponse('Update successfully!')


def update_nothing(request):

    return HttpResponse('No update happens')


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
