"""Demonstração da execução de duas threads acessando e alterando uma
mesma variável.
"""
import threading, time

alterned_word = '' # variável global

class MainThread(threading.Thread):
    """Classe MainThread que herda threading.Thread"""
    def __init__(self, word, cv):
        """Construtor.
        :param word: uma palavra de entrada para processamento
        :param cv: objeto threading.Condition() para controlar o acesso a thread"""
        self.word = word
        self.cv = cv
        threading.Thread.__init__(self)


    def run(self):
        """Método run que executa a thread e o bloco abaixo."""
        global alterned_word
        for letter in self.word:
            with self.cv:
                alterned_word += letter
                print('***', alterned_word, self.word)
                self.cv.wait()


def main():
    cv = threading.Condition() # objeto para controlar acesso e execução da thread

    word_1 = 'shoe'
    word_2 = 'cold'

    t1 = MainThread(word_1, cv)
    t2 = MainThread(word_2, cv)

    t1.start()
    t2.start()

    # enquanto uma das threads estiverem ativas envie notificações para liberar a próxima thread
    while t1.is_alive() or t2.is_alive():
        with cv:
            cv.notify()
    print('Resultado final:', alterned_word)
        

if __name__ == '__main__':
    main()
