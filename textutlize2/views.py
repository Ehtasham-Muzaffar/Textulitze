from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analiz(request):
    djtext=request.POST.get('text','defulat')
    punchs=request.POST.get('punch','off')
    capita=request.POST.get('capita','off')
    newline=request.POST.get('newline','off')
    space=request.POST.get('space','off')
    count=request.POST.get('count','off')
    punchation=""""'\][/.,<>+_)(*&^%$#@~!;|:|':"'{}{}":>?<<|!~:"|"""
    if punchs =='on':
        analizs=""
        for char in djtext:
            if char not in punchation:
                analizs=analizs+char

        parms={'removed':'removed Punchation','analize':analizs}
        return render(request,'analiz.html',parms)
    elif capita=='on':
        analizs=""
        for char in djtext:
            analizs=analizs+char.upper()

        parms={'removed':'Upper Case','analize':analizs}
        return render(request,'analiz.html',parms)
    elif newline=='on':
        analizs=""
        for char in djtext:
            if char !='\n':
                analizs=analizs+char

        parms={'removed':'New Line','analize':analizs}
        return render(request,'analiz.html',parms)
    elif space=='on':
        analizs=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):

                analizs = analizs+char
        parms = {'removed': 'Space remove', 'analize': analizs}
        return render(request, 'analiz.html', parms)
    elif count=='on':
        analizs=""
        for index,char in enumerate(djtext):
            analizs=index
        parms = {'removed': 'Space remove', 'analize': analizs}
        return render(request, 'analiz.html', parms)

    else:
        parms={'text':djtext}
        return render(request,'analiz.html',parms)
