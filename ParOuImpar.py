while True:
    def parOuimpar(n=0):
        if n%2==0:
            return True
        else:
            return False

    n=int(int(input("Digite um número: ")))
    if parOuimpar(n):
        print("PAR")
    else:
        print("NÃO É PAR")
    resp=str(input("DESEJA CONTINUAR ? [S] / [N]")).strip().upper()

    while resp not in 'SN':
        resp = str(input("DESEJA CONTINUAR ? [S] / [N]")).strip().upper()
    if resp=='N':
        break

print()
print("FIM DO PROGRAMA")
