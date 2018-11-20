package entidades

import java.util.Scanner

class Dados private constructor()
{
    val listaQuadro: ArrayList<Quadro> = ArrayList<Quadro>()
    val listaEtiqueta: ArrayList<Etiqueta> = ArrayList<Etiqueta>()

    companion object {
        private val instance: Dados = Dados()

        @Synchronized
        fun getInstance(): Dados
        {
            return instance
        }
    }
}