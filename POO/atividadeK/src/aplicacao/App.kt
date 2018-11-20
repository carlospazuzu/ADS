package aplicacao

import entidades.Dados
import entidades.Etiqueta
import entidades.Quadro
import utils.Helper

class App()
{
    // val listaQuadro: ArrayList<Quadro> = ArrayList<Quadro>()
    val quadroController: QuadroController = QuadroController()
    val dados: Dados = Dados.getInstance()

    fun run()
    {
        var running = true

        while (running)
        {
            println("\n===== TRELLO =====\n")
            println("1. Criar Novo Quadro")
            println("2. Acessar Quadro")
            println("3. Criar Nova Etiqueta")
            println("0. Sair")

            print("\nDigite uma opcao: ")
            val escolha = Helper.reader.nextInt()

            when(escolha)
            {
                0 -> running = false
                // OPCAO CRIAR NOVO QUADRO
                1 ->
                {
                    print("\nDigite o nome do novo Quadro: ")
                    val nome = readLine()!!

                    criarNovoQuadro(nome)
                }
                // OPCAO ACESSAR QUADRO
                2 ->
                {
                    println("Selecione o quadro: \n")
                    var i = 0
                    if (this.dados.listaQuadro.size > 0)
                    {
                        for (quadro in this.dados.listaQuadro)
                        {
                            println("$i. ${quadro.titulo}")
                            i++
                        }

                        print("\nDigite o numero do quadro que deseja acessar: ")
                        val quadroNum = Helper.reader.nextInt()

                        quadroController.run(quadroNum)
                    }
                    else
                        println("\nNenhum quadro foi criado.\n")

                }
                // OPCAO CRIAR NOVA ETIQUETA
                3 ->
                {
                    print("\nDigite o nome da nova etiqueta: ")
                    val nomeEtiqueta = readLine()!!

                    dados.listaEtiqueta.add(Etiqueta(nomeEtiqueta))
                }
                else -> println("\nPor favor, escolha um opcao valida")
            }
        }
    }

    fun criarNovoQuadro(nome: String)
    {
        val quadro = Quadro(nome)

        this.dados.listaQuadro.add(quadro)
    }
}