nome = ["Anna","Gabriel","Hellena","João"]
nome1, nome2, nome3, nome4 = ["Anna","Gabriel","Hellena","João"]
nomes, *resto= ["Anna","Gabriel","Hellena","João"]
_,_, nomes1, *_= ["Anna","Gabriel","Hellena","João"]

print(nome2)
print(nomes, resto)
print(nomes1)
print(nome[1])