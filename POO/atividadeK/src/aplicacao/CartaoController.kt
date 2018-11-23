package aplicacao

import entidades.Cartao
import entidades.Comentario
import entidades.Dados
import entidades.Log
import utils.Helper

class CartaoController
{
    val dados: Dados = Dados.getInstance()

    fun mostrarComentarios(cartao: Cartao)
    {
        if (cartao.listaComentarios.size > 0)
        {
            println("Comentarios:")
            for (cmt in cartao.listaComentarios)
            {
                println(cmt.comentario)
            }
            println()
        }
        else
            println("\nNao existem comentarios neste cartao.\n")
    }

    fun mostrarLog(cartao: Cartao)
    {
        if (cartao.logs.size > 0)
        {
            val tempLogs: ArrayList<Log> = cartao.logs;
            tempLogs.reverse()

            println("Logs:")
            for (tmpl in tempLogs)
            {
                println(tmpl.log)
            }
            println()

        }
        else
            println("\nNao existem logs para este cartao.\n")
    }

    fun run(cartao: Cartao)
    {
        var running = true
        while (running)
        {
            println("\nCartao: ${cartao.titulo} - Pertencente à lista ${cartao.listaPai}")
            println(cartao.descricao + "\n")
            println("ETIQUETAS: " + cartao.getStringEtiquetas())
            println("\n1. Visualizar cartao")
            println("2. Adicionar comentario")
            println("3. Adicionar Etiqueta")
            println("4. Remover Etiqueta")
            println("5. Listar log de cartao")
            println("6. Listar comentarios")
            println("0. Sair\n")

            print("Selecione a opcao desejada: ")
            var opcao = Helper.reader.nextInt()

            when (opcao)
            {
                0 -> running = false
                // OPCAO VISUALIZAR CARTAO
                1 ->
                {
                    mostrarComentarios(cartao)
                    mostrarLog(cartao)
                }
                // OPCAO ADICIONAR COMENTARIO
                2 ->
                {
                    println("\nDigite o comentario que deseja inserir: ")
                    val novoComentario = readLine()!!

                    cartao.listaComentarios.add(Comentario(novoComentario))
                    cartao.inserirLog("Adicionou um novo comentario.")
                }
                // OPCAO ADICIONAR ETIQUETA
                3 ->
                {
                    if (dados.listaEtiqueta.size > 0)
                    {
                        var i = 0

                        for (etq in dados.listaEtiqueta)
                        {
                            println("$i. ${etq.titulo}")
                            i++
                        }
                        print("\nSelecione a etiqueta a ser inserida: ")
                        val escolha = Helper.reader.nextInt()

                        if (escolha < 0 || escolha >= dados.listaEtiqueta.size)
                        {
                            println("\nIndice inválido!\n")
                        }
                        else
                        {
                            cartao.inserirEtiqueta(dados.listaEtiqueta[escolha])
                            cartao.inserirLog("Adicionou a etiqueta " + dados.listaEtiqueta[escolha].titulo + ".")
                        }

                    }
                    else
                        println("\nNao existe nenhuma etiqueta disponivel!\n")
                }
                // OPCAO REMOVER ETIQUETA
                4 ->
                {
                    if (cartao.etiquetas.size > 0)
                    {
                        var i = 0
                        for (etq in cartao.etiquetas)
                        {
                            println("$i. ${etq.titulo}")
                            i ++
                        }
                        print("\nSelecione a etiqueta a ser removida: ")

                        val etqNum = Helper.reader.nextInt()

                        if (etqNum < 0 || etqNum >= cartao.etiquetas.size)
                        {
                            println("\nIndice invalido!\n")
                        }
                        else
                        {
                            cartao.inserirLog("Removeu a etiqueta " + cartao.etiquetas[etqNum] + ".")
                            cartao.removerEtiqueta(etqNum)
                        }

                    }
                    else
                        println("\nNao existem etiquetas anexadas a este cartao!\n")
                }
                // OPCAO VER LOGS
                5 ->
                {
                    mostrarLog(cartao)
                }
                // OPCAO VER COMENTARIOS
                6 ->
                {
                    mostrarComentarios(cartao)
                }
            }
        }
    }
}