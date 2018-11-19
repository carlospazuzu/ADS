package aplicacao

import entidades.Dados
import entidades.Listagem

class ListaController
{
    val dados: Dados = Dados.getInstance()

    fun run(lista: Listagem)
    {
        var running = true

        while (running)
        {
            println("\nLista: ${lista.titulo}")
            println("*** OPCOES DE LISTA ***\n")

            println("1. Criar novo cartao")
            println("2. Acessar cartao")
            println("0. Sair")

            print("\nSelecione a opcao: ")

            var opcao = dados.reader.nextInt()

            when(opcao)
            {
                0 -> running = false
                1 ->
                {

                }
                2 ->
                {

                }
                else ->
                        println("\nPor favor, digite uma opcao valida!\n")
            }
        }
    }
}