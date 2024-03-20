from django.shortcuts import render # Create your views here.


def home(request):
    return render(request, 'recipes/pages/home.html', context=
           { 'name': 'apenas um teste'}       
                  
                  ) #Aqui a pagina, nome do template a ser renderizado, e o terceiro argumento é um dicionário que representa o contexto a ser passado para o template             
                                                            
                        
