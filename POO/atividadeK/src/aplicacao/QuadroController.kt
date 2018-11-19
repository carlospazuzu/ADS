package aplicacao

import entidades.Dados
import java.util.*

class QuadroController
{
    val dados: Dados = Dados.getInstance()
    val listaController: ListaController = ListaController()

    fun run(numeroQuadro: Int)
    {
        var running = true

        while (running)
        {
            println("Quadro: ${dados.listaQuadro[numeroQuadro].titulo}")
            println("*** OPÇOES DO QUADRO ***\n")
            println("1. Adicionar Listagem")
            println("2. Acessar Listagem")
            println("0. Sair")

            print("\nSelecione a opcao desejada: ")
            var opcao = dados.reader.nextInt()

            when(opcao)
            {
                0 -> running = false
                // OPCAO ADICIONAR NOVA LISTAGEM
                1 ->
                {
                    print("Digite o nome da nova lista: ")
                    val nome = readLine()!!

                    dados.listaQuadro[numeroQuadro].criarNovaListagem(nome)
                }
                // OPCAO ACESSAR LISTAGEM
                2 ->
                {
                    if (dados.listaQuadro[numeroQuadro].listaListagem.size > 0)
                    {
                        var i = 0
                        println("Selecione a lista: \n")

                        for (lista in this.dados.listaQuadro[numeroQuadro].listaListagem)
                        {
                            println("$i. ${lista.titulo}")
                            i++
                        }

                        print("\nDigite a lista que deseja acessar: ")

                        var opcaoLista = dados.reader.nextInt()

                        // TODO: fazer o mesmo esquema pra lista
                        listaController.run(dados.listaQuadro[numeroQuadro].listaListagem[opcaoLista])
                    }
                    else
                        println("\nNenhuma lista vinculada a este quadro.\n")
                }
                else ->
                    println("\nPor favor, selecione uma opcao valida!\n")
            }
        }

    }
}