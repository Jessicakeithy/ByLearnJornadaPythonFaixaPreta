 # ByLearnJornadaPythonFaixaPreta
  
 nota1 = 7.5                                  
 nota2 = 4.8

 def verificar_aprovacao():
   media = calcular_media([nota1, nota2])

   if media >= 6:
     print('O aluno(a) foi aprovado.')
   else:
     print('O aluno(a) foi reprovado.')

 def calcular_media(notas):
   quantidade = len(notas)

   soma = 0
   for nota in notas:
     soma = soma + nota

     media = soma / quantidade
     return media

 verificar_aprovacao()
