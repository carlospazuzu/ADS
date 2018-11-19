package entidades

class Listagem(t: String)
{
    val listaCartao: ArrayList<Cartao> = ArrayList<Cartao>()
    val logs: ArrayList<Log> = ArrayList<Log>()
    var estaArquivada: Boolean = false

    var titulo: String = t
/*
    constructor(titulo: String)
    {
        this.titulo = titulo
    }
*/
    fun criarNovoCartao(titulo: String)
    {
        val novoCartao = Cartao(titulo)

        listaCartao.add(novoCartao)
    }
}