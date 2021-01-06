def sed(string_p, string_re, file1, file2='file2'):
    """Lê um arquivo e escreve o seu conteúdo em outro.
       Caso no arquivo haja a string_p é subistiúda pela string_re.

        :param string_p: string padrão
        :param string_re: string de substituição
        :param file1: arquivo a ser lido
        :param file2: arquivo a ser escrito
        :return: novo arquivo com os dados
    """

    
    try:
        with open(file1, 'r') as f1:
            copy = open(file2, 'w')
            for line in f1:
                line = line.strip()
                if string_p in line: 
                    line = line.replace(string_p, string_re)
                copy.write('%s \n' % line)
            copy.close()
    except:
        print('Erro durante o processo!')


if __name__ == '__main__':
    sed('arquivo 2', 'substituído', 'file1')
