from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request, 'Analyze/analyze.html')
    
def about(request):
    input = request.GET.get('text', 'default')
    checkbox = request.GET.get('removepunctuation', 'off')
    capitalize = request.GET.get('capitalize', 'off')
    spaceremover = request.GET.get('spaceremover', 'off')
    if checkbox == 'on':
        text_not_needed = "!@$%^&*[]#?></;:'\/"
        analyzed = ""
        for char in input:
            if char not in text_not_needed:
                analyzed = analyzed + char

        user_text = {
            'Task':'Removed Punctuations',
            'analyzed_text':analyzed 
        }
        return render(request, 'Analyze/analyzed.html', user_text)

    elif capitalize == 'on':
        analyzed = ""
        for char in input:
            analyzed = analyzed + char.upper()

        user_text = {
            'Task':'Capitalize Text',
            "analyzed_text" : analyzed
        }
        return render(request, 'Analyze/analyzed.html', user_text)


    elif spaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(input):
            if (input[index] == " " and input[index + 1] == " "):
                pass
            else:
                analyzed = analyzed + char
            
        
        user_text = {
            'Task':'Remove space',
            "analyzed_text" : analyzed
        }
        return render(request, 'Analyze/analyzed.html', user_text)

    else: 
        return HttpResponse("<h3>Your text has not been analyzed</h3>")

def analyzed(request):
    return render(request, 'analyzed2.html')
