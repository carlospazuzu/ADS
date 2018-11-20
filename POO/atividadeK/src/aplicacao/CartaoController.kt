package aplicacao

import entidades.Cartao
import entidades.Comentario
import entidades.Dados

class CartaoController
{
    val dados: Dados = Dados.getInstance()

    fun run(cartao: Cartao)
    {
        var running = true
        while (running)
        {
            println("\nCartao: ${cartao.titulo}")
            println(cartao.descricao + "\n")
            println("1. Visualizar cartao")
            println("2. Adicionar comentario")
            println("0. Sair")

            print("Selecione a opcao desejada: ")
            var opcao = dados.reader.nextInt()

            when (opcao)
            {
                0 -> running = false
                1 ->
                {
                    println("Comentarios:\n")
                    for (comentario in cartao.listaComentarios)
                    {
                        print(comentario.comentario)
                    }
                    println()
                }
                2 ->
                {
                    println("\nDigite o comentario que deseja inserir: ")
                    val novoComentario = readLine()!!

                    cartao.listaComentarios.add(Comentario(novoComentario))
                }
            }
        }
    }
}