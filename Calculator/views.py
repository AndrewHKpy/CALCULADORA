from django.shortcuts import render, HttpResponse



def home(request):
   if request.method == "POST":
      numero1 = float(request.POST.get("numero1", 0))
      numero2 = float(request.POST.get("numero2", 0))
      operacao = request.POST.get("Operação")
      resultado = calcular_resultado(numero1, numero2, operacao)
      return render(request,'home.html', {"resultado": resultado})

   return render(request, "home.html")
    
def calculate(request):
   if request.method == "POST":
      numero1 = float(request.POST.get("numero1", 0))
      numero2 = float(request.POST.get("numero2", 0))
      operacao = request.POST.get("Operação")
      resultado = calcular_resultado(numero1, numero2, operacao)
      return render(request,'home.html', {"resultado": resultado})

   return HttpResponse("Requisição invalida")



def calcular_resultado(numero1, numero2, Operação):
   if Operação == "somar":
      return numero1 + numero2
   
   elif Operação == "subtrair":
      return numero1 - numero2
   
   elif Operação == "multiplicar":
      return numero1 * numero2
   
   elif Operação == 'dividir':
      if numero1 and numero2 != 0:
         return numero1 / numero2
      else:
         return "Erro: Não é possivel dividir por 0"
   
   else:
      return 'erro: Operação invalida'
      
