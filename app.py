import re

extrato=open('extrato.txt','r',encoding='utf-8')

pat=re.compile(r'(.+\nDocto.+)')
extrato=extrato.read()

result=pat.findall(extrato)
pat2=re.compile(r'\S+')
print(len(result))
resultado_grupo=[]
for x in result:

    resultado_grupo.append(pat2.findall(x))
    

resultado1=[]

def classificar(grupo):
    ob={'classificador':[]}
    
    for i,x in enumerate(grupo):
        if x == 'Docto':
            ob['pk']=grupo[i+1]
            ob['valor']=float(grupo[i+2].replace(',','.'))
            return ob
       
        ob['classificador'].append(x)
    


classificacao=map(classificar,resultado_grupo)

lista=list(classificacao)
negativos=([x['valor'] for x in lista if x['valor'] < 0])

print(sum(negativos))