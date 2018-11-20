package entidades

class Cartao(tit: String, desc: String, pai: String)
{
    var titulo: String = tit
    var descricao: String = desc
    var listaPai: String = pai

    var etiquetas: ArrayList<Etiqueta> = ArrayList<Etiqueta>()
    var listaComentarios: ArrayList<Comentario> = ArrayList<Comentario>()

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
