# -*- coding: utf-8 -*-
"""NotadoAluno.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z7V3Bt5No06P2GijBXW5ahHm5uV-V1Wi
"""

nota1 = float(input("informe sua primeira nota"))
nota2 = float(input("informe sua segunda nota"))
nota3 = float(input("informe sua terceira nota"))

media = (nota1+nota2+nota3)/3

if(media >= 7 ):
    print('aprovado')
elif(media >= 4 ):
    print('reprovado')
else:
    print('para final')
print(f'situação do aluno {media}')