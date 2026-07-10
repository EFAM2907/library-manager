
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print('no debe estar vacio')
       

def pedir_numero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print('deben ser numeros')


def pedir_email():
    while True:
        email = pedir_texto("Correo electronico: ")

        if "@" not in email:
            print("El correo debe contener un '@'.")
            continue

        if "." not in email:
            print("El correo debe contener un punto.")
            continue

        if email.rindex(".") < email.index("@"):
            print("El punto debe estar después del '@'.")
            continue

        return email

    
def pedir_booleano(mensaje):
    while True:
        opcion = input(f'{mensaje} si/no: ').lower()
        if opcion == 'si':
            return True
        elif opcion == 'no':
            return False
        print('responde si o no')
    
    
    
