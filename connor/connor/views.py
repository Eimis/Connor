from django.shortcuts import render


def main(request):
    '''Main app view for SPA
    '''

    return render(request, 'main.html', {})
