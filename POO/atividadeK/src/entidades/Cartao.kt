package entidades

class Cartao(tit: String, desc: String)
{
    var titulo: String = tit
    var descricao: String = desc
    var listaComentarios: ArrayList<Comentario> = ArrayList<Comentario>()
}