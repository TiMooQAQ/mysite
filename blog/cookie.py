#判断是否登录
def checkcookie(request,object):
    cookie = request.COOKIES.get('cookie')
    if object.objects.filter(cookie=cookie).exists():
        return True
    else:
        return False