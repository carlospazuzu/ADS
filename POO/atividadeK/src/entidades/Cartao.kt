package entidades

class Cartao(tit: String)
{
    var titulo: String = tit
    var listaComentarios: ArrayList<Comentario> = ArrayList<Comentario>()
}