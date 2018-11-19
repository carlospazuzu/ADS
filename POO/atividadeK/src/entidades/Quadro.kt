package entidades

class Quadro(nome: String)
{
    var titulo: String = nome
    val listaListagem: ArrayList<Listagem> = ArrayList<Listagem>()

    fun criarNovaListagem(nomeLista: String)
    {
        val novaListagem: Listagem = Listagem(nomeLista)

        listaListagem.add(novaListagem)
    }

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