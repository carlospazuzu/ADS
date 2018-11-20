package entidades

import utils.Helper
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

class Comentario
{
    var comentario: String = ""

    constructor(comentario: String)
    {
        this.comentario = Helper.getTimeStampAtual() + " - " + comentario
    }
}