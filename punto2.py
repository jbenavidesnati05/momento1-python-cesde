cuentas = []
idCuenta= 1

while idCuenta <= 10:
    cuenta = {}
    saldoCuenta = float(input(f'Ingrese el saldo de la cuenta  {idCuenta}: '))
    cuenta["idCuenta"] = idCuenta
    cuenta["saldoCuenta"] = saldoCuenta
    idCuenta = idCuenta + 1
    cuentas.append(cuenta)

def organizar(item):
  return item['saldoCuenta']

cuentas.sort(reverse=True, key=organizar)

print(cuentas)