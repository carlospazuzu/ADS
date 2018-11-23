package entidades

import utils.Helper

class Cartao(tit: String, desc: String, pai: String)
{
    var titulo: String = tit
    var descricao: String = desc
    var listaPai: String = pai

    var etiquetas: ArrayList<Etiqueta> = ArrayList<Etiqueta>()
    var listaComentarios: ArrayList<Comentario> = ArrayList<Comentario>()
    var logs: ArrayList<Log> = ArrayList<Log>()

    fun inserirLog(acao: String)
    {
        logs.add(Log(Helper.getTimeStampAtual() + " - " + acao))
    }

    fun inserirEtiqueta(etiqueta: Etiqueta)
    {
        etiquetas.add(etiqueta)
    }

    fun removerEtiqueta(posicao: Int)
    {
        etiquetas.removeAt(posicao)
    }

    fun getStringEtiquetas(): String
    {
        var str = ""
        val size = etiquetas.size
        var i = 0

        for (etq in etiquetas)
        {
            if (i == size - 1)
                str += etq.titulo
            else
                str += etq.titulo + ", "
            i++
        }

        return str
    }
}
