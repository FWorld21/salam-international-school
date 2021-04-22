from os import getcwd, chdir, system
from django.shortcuts import render
from . import models
from django.contrib import messages
from time import sleep


# Create your views here.
def ru_home(request):
    context = {'page': 'home', 'lang': 'ru'}
    return render(request, 'school_site/home.html', context=context)


def en_home(request):
    context = {'page': 'home', 'lang': 'en'}
    return render(request, 'school_site/home.html', context=context)


def uz_home(request):
    context = {'page': 'home', 'lang': 'uz'}
    return render(request, 'school_site/home.html', context=context)


def ru_teachers(request):
    context = {'page': 'teachers', 'lang': 'ru', 'teachers': models.Teachers.objects.all()}
    return render(request, 'school_site/our teachers.html', context=context)


def en_teachers(request):
    queryset = models.Teachers.objects.all()

    context = {'page': 'teachers', 'lang': 'en', 'teachers': queryset}
    return render(request, 'school_site/our teachers.html', context=context)


def uz_teachers(request):
    context = {'page': 'teachers', 'lang': 'uz', 'teachers': models.Teachers.objects.all()}
    return render(request, 'school_site/our teachers.html', context=context)


def ru_circles(request):
    context = {'page': 'circles', 'lang': 'ru'}
    return render(request, 'school_site/circles.html', context=context)


def en_circles(request):
    context = {'page': 'circles', 'lang': 'en'}
    return render(request, 'school_site/circles.html', context=context)


def uz_circles(request):
    context = {'page': 'circles', 'lang': 'uz'}
    return render(request, 'school_site/circles.html', context=context)


def ru_call_request(request):
    initials = request.GET.get('initials')
    phone = request.GET.get('phone')
    comment = request.GET.get('comment')

    if initials is None and phone is None:
        context = {'page': 'call-request', 'lang': 'ru'}
        return render(request, 'school_site/form page.html', context=context)
    elif initials is None or len(initials) < 2:
        messages.error(request, "Вы не ввели Ф.И.О")
    elif phone is None or len(phone) < 2:
        messages.error(request, "Вы не ввели номер телефона")
    else:
        try:
            int(phone)
            try:
                int(initials)
                messages.error(request, "Вы ввели некорректные данные в Ф.И.О")
            except ValueError:
                start_path = getcwd()
                chdir('./school_site/bot/')

                if len(comment) < 4:
                    system(f'python telegram_bot.py --initials "{initials}" --phone "{phone}" --comment "-" ')
                else:
                    system(f'python telegram_bot.py --initials "{initials}" --phone "{phone}" --comment "{comment}" ')

                chdir(start_path)
                messages.success(request, "Ваша заявка успешно отправлена!")
                sleep(5)
        except ValueError:
            messages.error(request, "Вы ввели некорректный номер телефона")

    context = {'page': 'call-request', 'lang': 'ru'}
    return render(request, 'school_site/form page.html', context=context)


def en_call_request(request):
    initials = request.GET.get('initials')
    phone = request.GET.get('phone')
    comment = request.GET.get('comment')

    if initials is None and phone is None:
        context = {'page': 'call-request', 'lang': 'en'}
        return render(request, 'school_site/form page.html', context=context)
    elif initials is None or len(initials) < 2:
        messages.error(request, "Full name is not entered")
    elif phone is None or len(phone) < 2:
        messages.error(request, "Phone number is not entered")
    else:
        try:
            int(phone)
            try:
                int(initials)
                messages.error(request, "Incorrect data in your full name")
            except ValueError:
                start_path = getcwd()
                chdir('./school_site/bot/')

                if len(comment) < 4:
                    system(f'python telegram_bot.py --initials "{initials}" --phone "{phone}" --comment "-" ')
                else:
                    system(f'python telegram_bot.py --initials "{initials}" --phone "{phone}" --comment "{comment}" ')

                chdir(start_path)
                messages.success(request, "Application has been submitted!")
                sleep(5)
        except ValueError:
            messages.error(request, "Invalid phone number")

    context = {'page': 'call-request', 'lang': 'en'}
    return render(request, 'school_site/form page.html', context=context)


def uz_call_request(request):
    initials = request.GET.get('initials')
    phone = request.GET.get('phone')
    comment = request.GET.get('comment')

    if initials is None and phone is None:
        context = {'page': 'call-request', 'lang': 'uz'}
        return render(request, 'school_site/form page.html', context=context)
    elif initials is None or len(initials) < 2:
        messages.error(request, "To'liq ismingizni kiritmadingiz")
    elif phone is None or len(phone) < 2:
        messages.error(request, "Telefon raqamingizni kiritmadingiz")
    else:
        try:
            int(phone)
            try:
                int(initials)
                messages.error(request, "To'liq ismingizga noto'g'ri ma'lumotlarni kiritdingiz")
            except ValueError:
                start_path = getcwd()
                chdir('./school_site/bot/')

                if len(comment) < 4:
                    system(f'python telegram_bot.py --initials "{initials}" --phone "{phone}" --comment "-" ')
                else:
                    system(f'python telegram_bot.py --initials "{initials}" --phone "{phone}" --comment "{comment}" ')

                chdir(start_path)
                messages.success(request, "Arizangiz qabul qilindi!")
                sleep(5)
        except ValueError:
            messages.error(request, "Noto'g'ri telefon raqamini kiritdingiz")

    context = {'page': 'call-request', 'lang': 'uz'}
    return render(request, 'school_site/form page.html', context=context)
