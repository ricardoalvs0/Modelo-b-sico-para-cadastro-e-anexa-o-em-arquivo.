class Perfil:
    def __init__(self, altura, peso, ano_nascimento, sexo, estado_civil, _estado):
        self.altura = altura
        self.peso   = peso
        self._ano   = ano_nascimento
        self.sexo   = sexo
        self.estado_civil = estado_civil
        self.estado = _estado

    def lista_de_caracteristicas(self):
        lista_do_arquivo = []
        lista_do_arquivo.append(self.altura)
        lista_do_arquivo.append(self.peso)
        lista_do_arquivo.append(self._ano)
        lista_do_arquivo.append(self.sexo)
        lista_do_arquivo.append(self.estado_civil)
        lista_do_arquivo.append(self.estado)
        return lista_do_arquivo

    def criação_de_arquivo(self):
        '''arquivo = open('ArquivoX.txt', 'w')
        print(arquivo)
        arquivo = open('ArquivoX.txt', 'r')
        conteudo = []
        conteudo.append(self.lista_de_caracteristicas())
        conteudo_antigo = arquivo.readlines()
        print(conteudo, '\n', conteudo_antigo)'''
        conteudo = self.lista_de_caracteristicas()
        arquivo = open('ArquivoX.txt', 'w')
        arquivo.close()
        with open('ArquivoX.txt', 'r') as arquivo:
            conteudo_antigo = arquivo.readlines()
            with open('ArquivoX.txt', 'w') as arquivo:
                for j in conteudo_antigo:
                    arquivo.write(str(j))
                arquivo.write('\n')
                arquivo.write(str(conteudo))
            #arquivoX.write(str(conteudo_antigo))
            #arquivoX.write(str(conteudo))
        '''arquivo = open('ArquivoX.txt', 'w')
        for i in conteudo_antigo:
            arquivo.writelines(str(i).strip())
        arquivo.write('\n')
        for j in conteudo:
            arquivo.writelines(str(j).strip())
        arquivo.close()'''
        '''with open('ArquivoX.txt', 'w', encoding='utf-8') as arq:
            # CORPO DO WITH
            lista_escrita = self.lista_de_caracteristicas()
            for i in lista_escrita:
                arq.write(f'{i}\t')'''


def main():
    altura = (float(input('Sua altura: ')))
    peso = (float(input('Seu peso: ')))
    ano_nascimento = (int(input('Seu ano de nascimento: ')))
    sexo = (input('Seu sexo [M/F]: '))
    estado_civil = (input('Seu estado civil: '))
    _estado = (input('Estado onde nasceu: '))

    _pessoa = Perfil(altura, peso, ano_nascimento, sexo.strip(), estado_civil.strip(), _estado.strip())
    _pessoa.criação_de_arquivo()


main()