package entidades

class Listagem(t: String)
{
    val listaCartao: ArrayList<Cartao> = ArrayList<Cartao>()
    val logs: ArrayList<Log> = ArrayList<Log>() // TODO logs pertencem aos cartoes e nao as listas
    var estaArquivada: Boolean = false

    var titulo: String = t

    fun criarNovoCartao(titulo: String, descr: String)
    {
        val novoCartao = Cartao(titulo, descr)

        listaCartao.add(novoCartao)
    }
}