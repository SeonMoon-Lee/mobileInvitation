from django.shortcuts import redirect


def custom_page_not_found(request, exception):
    print(exception)
    return redirect('accountapp:login')  # 'home'은 홈 페이지의 URL 이름


def error500(request):
    return redirect('accountapp:login')
