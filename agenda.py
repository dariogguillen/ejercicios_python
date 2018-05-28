from os import system


class Contacto ():
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo


class Agenda ():
    def __init__(self):
        self._contactos = []

    def agregar(self, nombre, telefono, correo):
        contacto = Contacto(nombre, telefono, correo)
        self._contactos.append(contacto)
        print('')
        self.imprimir_contacto(contacto)
        self.regresar()

    def buscar_contacto(self, nombre):
        for contacto in self._contactos:
            if contacto.nombre.lower() == nombre.lower():
                _contacto = contacto
                return _contacto
        else:
            _contacto = False
            return _contacto

    def elimiar_contacto(self, nombre):
        contacto = self.buscar_contacto(nombre)
        if contacto:
            self.imprimir_contacto(contacto)
            del self._contactos[self._contactos.index(contacto)]
            print(f'    Contacto eliminardo')
            self.regresar()
        else:
            print('')
            print('    Contacto no encontrado.')
            self.regresar()

    def lista_contactos(self):
        for contacto in self._contactos:
            self.imprimir_contacto(contacto)
        print('')
        self.regresar()

    def imprimir_contacto(self, contacto):
        print('    *---*---*---*---*---*---*---*')
        print(f'    {contacto.nombre.title()}')
        print(f'    {contacto.telefono}')
        print(f'    {contacto.correo}')
        print('    *---*---*---*---*---*---*---*')

    def buscar_imprimir(self, nombre):
        _nombre = self.buscar_contacto(nombre)
        if _nombre:
            self.imprimir_contacto(_nombre)
        else:
            print('')
            print('    Contacto no encontrado.')

    def actualizar_contacto(self, nombre):
        def guardar_cambios(contacto, index):
            self._contactos[index] = contacto

        self.buscar_imprimir(nombre)
        contacto = self.buscar_contacto(nombre)
        if contacto:
            index_contacto = self._contactos.index(contacto)
            print('')
            print('    ¿Qué quieres cambiar?')
            print('')
            opcion = input('    [n]ombre, [t]elefono, [c]orreo : ')

            if opcion == 'n':
                print('')
                n = input('    Ingresa el nuevo nombre: ')
                contacto.nombre = n
                guardar_cambios(contacto, index_contacto)
                hacer_mas = self._cambiar_mas()
                if hacer_mas:
                    self.actualizar_contacto(contacto.nombre)
                else:
                    return
            elif opcion == 't':
                print('')
                t = input('    Ingresa el nuevo telefono: ')
                contacto.telefono = t
                guardar_cambios(contacto, index_contacto)
                hacer_mas = self._cambiar_mas()
                if hacer_mas:
                    self.actualizar_contacto(contacto.nombre)
                else:
                    return
            elif opcion == 'c':
                print('')
                c = input('    Ingresa el nuevo correo: ')
                contacto.correo = c
                guardar_cambios(contacto, index_contacto)
                hacer_mas = self._cambiar_mas()
                if hacer_mas:
                    self.actualizar_contacto(contacto.nombre)
                else:
                    return
            else:
                print('')
                print('    * --- Ingresa una opcion valida. --- *')
                print('')
                system('clear')
                self.actualizar_contacto(nombre)

        else:
            print('')
            print('    Contacto no encontrado.')
            self.regresar()

    def _cambiar_mas(self):
        print('')
        print('    ¿Quieres cambiar algo más?')
        print('')
        opcion = input('    [S]i, [N]o : ')
        print('')
        continuar = False
        if opcion.lower() == 's':
            continuar = True
        elif opcion.lower() == 'n':
            continuar = False
        else:
            print('    Ingresa una opcion valida')
            self._cambiar_mas()

        return continuar

    def regresar(self):
        print('')
        opcion = input('    [r]egresar  -  [s]alir : ')
        if opcion.lower() == 'r':
            system('clear')
            return
        elif opcion.lower() == 's':
            system('clear')
            exit()
        else:
            print('')
            print('    Opción no valida')
            self.regresar()


def run():
    system('clear')
    agenda = Agenda()

    while True:
        system('clear')
        print('')
        print('    B I E N V E N I D O  A  L A  A G E N D A ! ! !')
        print('')
        opcion = str(input('''
    ¿Qué deseas hacer?

    [a]ñadir contacto
    [ac]tualizar contacto
    [b]uscar contacto
    [e]liminar contacto
    [l]istar contactos
    [s]alir

    Ingresa la opcion: '''))

        if opcion.lower() == 'a':
            system('clear')
            print('')
            print('    **A Ñ A D I R  C O N T A C T O**')
            print('')
            nombre = input('    Ingresa el nombre: ')
            telefono = input('    Ingresa el telefono: ')
            correo = input('    Ingresa el correo: ')

            agenda.agregar(nombre, telefono, correo)

        elif opcion.lower() == 'ac':
            system('clear')
            print('')
            print('    **A C T U A L I Z A R  C O N T A C T O**')
            print('')
            nombre = input('    Ingresa el nombre del contacto a actualizar: ')
            agenda.actualizar_contacto(nombre)

        elif opcion.lower() == 'b':
            system('clear')
            print('')
            print('    **B U S C A R  C O N T A C T O**')
            print('')
            nombre = input(
                '    Ingresa el nombre del contacto que quieres buscar: ')
            print('')
            agenda.buscar_imprimir(nombre)
            print('')
            agenda.regresar()

        elif opcion.lower() == 'e':
            system('clear')
            print('')
            print('    **E L I M I N A R  C O N T A C T O**')
            print('')
            nombre = input('    Ingresa el nombre del contacto a eliminar: ')
            agenda.elimiar_contacto(nombre)

        elif opcion.lower() == 'l':
            system('clear')
            print('')
            print('    **L I S T A  D E  C O N T A C T O**')
            print('')
            agenda.lista_contactos()

        elif opcion.lower() == 's':
            system('clear')
            exit()
        else:
            system('clear')
            print('')
            print('    O P C I Ó N  N O  V A L I D A  I N T E N T A  D E  N U E V O .')
            print('')


if __name__ == '__main__':
    run()
