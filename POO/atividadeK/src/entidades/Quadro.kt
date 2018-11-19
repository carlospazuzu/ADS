package entidades

class Quadro(nome: String)
{
    var titulo: String = nome
    val listaListagem: ArrayList<Listagem> = ArrayList<Listagem>()

    fun arquivarListagem(nomeListagem: String): Boolean
    {
        for (listagem in this.listaListagem)
        {
            if (listagem.titulo == nomeListagem)
            {
                listagem.estaArquivada = true
                return true
            }
        }

        return false
    }
}