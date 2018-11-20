package entidades

import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

class Comentario
{
    var comentario: String = ""

    constructor(comentario: String)
    {
        val atual = LocalDateTime.now()

        val formato = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss")
        val formatado = atual.format(formato)

        this.comentario = formatado + " - " + comentario
    }
}