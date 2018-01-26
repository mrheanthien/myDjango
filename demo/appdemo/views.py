from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from appdemo.models import Server

class ServerForm(ModelForm):
    class Meta:
        model = Server
        fields = ['name', 'ip', 'order']

def server_list(request, template_name='appdemo/appdemo_list.html'):
    appdemo = Server.objects.all()
    data = {}
    data['object_list'] = appdemo
    return render(request, template_name, data)

def server_create(request, template_name='appdemo/appdemo_form.html'):
    form = ServerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('server_list')
    return render(request, template_name, {'form':form})

def server_update(request, pk, template_name='appdemo/appdemo_form.html'):
    server = get_object_or_404(Server, pk=pk)
    form = ServerForm(request.POST or None, instance=server)
    if form.is_valid():
        form.save()
        return redirect('server_list')
    return render(request, template_name, {'form':form})

def server_delete(request, pk, template_name='appdemo/appdemo_confirm_delete.html'):
    server = get_object_or_404(Server, pk=pk)    
    if request.method=='POST':
        server.delete()
        return redirect('server_list')
    return render(request, template_name, {'object':server})