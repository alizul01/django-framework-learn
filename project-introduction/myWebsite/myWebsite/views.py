from django.http import HttpResponse

def about(response):
    judul = '<h1> Ini adalah about </h1>'
    subjudul = '<h2> Selamat datang di website Django! </h1>'
    
    output = judul + subjudul
    return HttpResponse(output)