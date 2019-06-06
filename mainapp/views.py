from django.shortcuts import render
from django.views.generic import View
from django.contrib import messages
from .forms import *


def mainpage(request):
    Cell.objects.filter(if_checks_cell = True).delete()
    return render(request,'mainapp/start_page.html')


class MessageCreate(View):

    def get(self,request):
        form = AddMessageForm()
        return render(request,'mainapp/create_mess_page.html',context={'form':form})

    def post(self,request):
        bound_form = AddMessageForm(request.POST)

        if bound_form.is_valid():
            bound_form.save()
            messages.success(request, 'The message is placed in the cell')
            form = AddMessageForm()
            return render(request,'mainapp/create_mess_page.html',context={'form':form})
        return render(request,'mainapp/create_mess_page.html',context={'form':bound_form})


class LoginCell(View):

    def get(self,request):
        form = LoginCellForm()
        return render(request,'mainapp/login_cell_page.html',context = {'form':form})

    def post(self,request):
        bound_form = LoginCellForm(request.POST)

        if bound_form.is_valid():
            if Cell.objects.filter(name = bound_form.cleaned_data['cell']).exists():
                cell = Cell.objects.get(name = bound_form.cleaned_data['cell'])
                all_the_messages = cell.messages.all()
                cell.if_checks_cell = True
                cell.save()
                return render(request,'mainapp/view_messages_page.html',context={'messages':all_the_messages,'cell':cell})

            bound_form.add_error('cell', 'The specified cell "{}" does not exist'.format(bound_form.cleaned_data['cell']))
            return render(request, 'mainapp/login_cell_page.html',context = {'form':bound_form})

        bound_form.add_error('cell', 'The entered data is not valid')
        return render(request, 'mainapp/login_cell_page.html', context={'form': bound_form})

























