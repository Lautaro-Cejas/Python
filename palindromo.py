class test():
    def __init__(self, cad):
        self.listaA = cad
    def palindromo(self):
        self.rever = 0
        for i in self.listaA:
            rever = i[::-1]
            if rever == i:
                print ('Esta palabra es palíndromo.')
            else:
                print ('Esta palabra no es palíndromo.')
prog = test(['menem','sos','otto','wow'])
prog.palindromo()
