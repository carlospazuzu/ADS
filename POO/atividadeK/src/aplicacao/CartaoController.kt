package aplicacao

import entidades.Cartao
import entidades.Comentario
import entidades.Dados
import utils.Helper

class CartaoController
{
    val dados: Dados = Dados.getInstance()

    fun run(cartao: Cartao)
    {
        var running = true
        while (running)
        {
            println("\nCartao: ${cartao.titulo} - Pertencente à lista ${cartao.listaPai}")
            println(cartao.descricao + "\n")
            println("ETIQUETAS: " + cartao.getStringEtiquetas())
            println("1. Visualizar cartao")
            println("2. Adicionar comentario")
            println("3. Adicionar Etiqueta")
            println("0. Sair")

            print("Selecione a opcao desejada: ")
            var opcao = Helper.reader.nextInt()

            when (opcao)
            {
                0 -> running = false
                // OPCAO VISUALIZAR CARTAO
                1 ->
                {
                    println("Comentarios:\n")
                    for (comentario in cartao.listaComentarios)
                    {
                        print(comentario.comentario)
                    }
                    println()
                }
                // OPCAO ADICIONAR COMENTARIO
                2 ->
                {
                    println("\nDigite o comentario que deseja inserir: ")
                    val novoComentario = readLine()!!

                    cartao.listaComentarios.add(Comentario(novoComentario))
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
                            continue
                        }
                    }
                    else
                        println("\nEste cartao nao possui nenhuma etiqueta!\n")
                }
            }
        }
    }
}