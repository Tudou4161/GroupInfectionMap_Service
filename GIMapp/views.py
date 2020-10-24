from django.template.loader import render_to_string
from django.views.generic import View
from django.shortcuts import render
from django.conf import settings

# def show_map(request):
#        context = {}
#        template_name = "polls/GroupInfeectinMap.html"
#        if settings.DEBUG == True:
#            if "/" in template_name and template_name.endswith('.html'):
#                filename = template_name[(template_name.find("/")+1):len(template_name)-len(".html")] + "_flat.html"
#            elif template_name.endswith('.html'):
#                filename = template_name[:len(template_name)-len(".html")] + "_flat.html"
#            else:
#                raise ValueError("The template name could not be parsed or is in a subfolder")
#            #print(filename)
#            html_string = render_to_string(template_name, context)
#            #print(html_string)
#            filepath = "../templates_cdn/" + filename
#            print(filepath)
#            f = open(filepath, 'w+')
#            f.write(html_string)
#            f.close()
#        return render(request, template_name, context)




def main(request):
    return render(request, "main.html")
    
def input(request):
    return render(request, "input.html")

def result(request):
    latitude = request.POST["latitude"]
    longitude = request.POST["longitude"]
    context = {
        "lat": latitude,
        "lon": longitude
    }

    return render(request, "result.html", context)


def result2(request):
    return render(request, "result2.html")


# def main2(request):
#     return render(request, 'main2.html')



# def main3(request):
#     return render(request, 'main3.html')