package aplicacao

import entidades.Quadro
import java.util.Scanner

class App()
{
    val listaQuadro: ArrayList<Quadro> = ArrayList<Quadro>()

    fun run()
    {
        val reader = Scanner(System.`in`)
        var running = true

        while (running)
        {
            println("\n===== TRELLO =====\n")
            println("1. Criar Novo Quadro")
            println("0. Sair")

            print("\nDigite uma opcao: ")
            var escolha = reader.nextInt()

            when(escolha)
            {
                0 -> running = false
                1 ->
                {
                    print("\nDigite o nome do novo Quadro: ")
                    val nome = readLine()!!

                    criarNovoQuadro(nome)
                }
                2 ->
                {
                    // TODO
                }
                else -> println("\nPor favor, escolha um opcao valida")
            }
        }
    }

    fun criarNovoQuadro(nome: String)
    {
        val quadro = Quadro(nome)

        this.listaQuadro.add(quadro)
    }
}