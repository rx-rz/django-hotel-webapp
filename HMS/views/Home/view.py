from django.shortcuts import redirect, render


def home(request):
    context = {

    }
    return render(request, 'home.html', context)


# def rooms(request):
#     context = {
#
#     }
#     return render(request, 'rooms.html', context)
#
#
# def contacts(request):
#     context = {
#
#     }
#     return render(request, '', context)
#
#
# def social(request):
#     context = {
#
#     }
#     return render(request, '', context)
#
#
# def tranquille_desprit(request):
#     context = {
#
#     }
#     return render(request, 'home.html', context)
