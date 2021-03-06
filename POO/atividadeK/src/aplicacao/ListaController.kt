package aplicacao

import entidades.Dados
import entidades.Listagem
import utils.Helper

class ListaController
{
    val dados: Dados = Dados.getInstance()
    val cartaoController: CartaoController = CartaoController()

    fun run(lista: Listagem)
    {
        var running = true

        while (running)
        {
            println("\nLista: ${lista.titulo} - Pertencente ao Quadro ${lista.quadroPai}")
            println("*** OPCOES DE LISTA ***\n")

            println("1. Criar novo cartao")
            println("2. Acessar cartao")
            println("0. Sair")

            print("\nSelecione a opcao: ")

            var opcao = Helper.reader.nextInt()

            when(opcao)
            {
                0 -> running = false
                // OPCAO CRIAR NOVO CARTAO
                1 ->
                {
                    print("\nDigite o nome do novo cartao: ")
                    val nome = readLine()!!

                    print("\nDigite uma descricao para o novo cartao: ")
                    val desc = readLine()!!

                    lista.criarNovoCartao(nome, desc, lista.titulo)
                }
                // OPCAO ACESSAR CARTAO
                2 ->
                {
                    if (lista.listaCartao.size > 0)
                    {
                        var i = 0
                        for (cartao in lista.listaCartao)
                        {
                            println("$i. ${cartao.titulo} - ${cartao.descricao}")
                            i++
                        }

                        print("\nSelecione o cartao: ")
                        val selec = Helper.reader.nextInt()

                        if (selec < 0 || selec >= lista.listaCartao.size)
                        {
                            println("\nIndice invalido\n")
                        }
                        else
                            cartaoController.run(lista.listaCartao[selec])
                    }
                    else
                        println("\nNao existem cartoes atrelados a esta lista.\n")
                }
                else ->
                        println("\nPor favor, digite uma opcao valida!\n")
            }
        }
    }
}