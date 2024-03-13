import unittest
import Projeto1_for_main


class TestsProjeto1_for_main(unittest.TestCase):

    def test_digitar_numero_entre_1_e_50(self):
        print_list = []
        input_list = []
        input_output_list = ['0', '51', '3']

        def print1(text):
            print_list.append(text)

        def input1(text):
            input_list.append(text)
            return input_output_list.pop()
        Projeto1_for_main.main(print1, input1, len(input_output_list), 5)
        self.assertEqual(
            "['****************************************', 'Bem vindo ao meu joguinho de adivinhação', '****************************************', 'Teste: 1 de 3', 'Voce digitou: 3', 'Errou, seu chute foi menor do que o numero secreto.', 'Teste: 2 de 3', 'Voce digitou: 51', '\\n ---ATENCAO: DIGITE UM NUMERO ENTRE 1 E 50---', 'Teste: 3 de 3', 'Voce digitou: 0', '\\n ---ATENCAO: DIGITE UM NUMERO ENTRE 1 E 50---', '\\nFim de jogo!!!']",
            str(print_list),
            'programa está incorreto'
        )

    def test_digitar_numero_chute_menor_que_o_numero_secreto(self):
        print_list = []
        input_list = []
        input_output_list = ['1']

        def print1(text):
            print_list.append(text)

        def input1(text):
            input_list.append(text)
            return input_output_list.pop()
        Projeto1_for_main.main(print1, input1, len(input_output_list), 5)
        self.assertEqual(
            "['****************************************', 'Bem vindo ao meu joguinho de adivinhação', '****************************************', 'Teste: 1 de 1', 'Voce digitou: 1', 'Errou, seu chute foi menor do que o numero secreto.', '\\nFim de jogo!!!']",
            str(print_list),
            'programa está incorreto'
        )

    def test_digitar_numero_igual_ao_numero_secreto(self):
        print_list = []
        input_list = []
        input_output_list = ['5']

        def print1(text):
            print_list.append(text)

        def input1(text):
            input_list.append(text)
            return input_output_list.pop()
        Projeto1_for_main.main(print1, input1, len(input_output_list), 5)
        self.assertEqual(
            "['****************************************', 'Bem vindo ao meu joguinho de adivinhação', '****************************************', 'Teste: 1 de 1', 'Voce digitou: 5', '\\n-----Acertou-----', '\\nFim de jogo!!!']",
            str(print_list),
            'programa está incorreto'
        )


if __name__ == '__main__':
    unittest.main()
