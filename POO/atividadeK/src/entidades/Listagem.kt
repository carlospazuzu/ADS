package entidades

import kotlin.reflect.jvm.internal.impl.load.kotlin.JvmType

class Listagem(t: String, pai: String)
{
    val listaCartao: ArrayList<Cartao> = ArrayList<Cartao>()
    // val logs: ArrayList<Log> = ArrayList<Log>() // TODO logs pertencem aos cartoes e nao as listas
    var estaArquivada: Boolean = false

    var titulo: String = t
    var quadroPai: String = pai

    fun criarNovoCartao(titulo: String, descr: String, pai: String)
    {
        val novoCartao = Cartao(titulo, descr, pai)

        listaCartao.add(novoCartao)
    }
}