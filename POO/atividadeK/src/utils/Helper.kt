package utils

import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
import java.util.*

class Helper private constructor()
{
    companion object {
        val reader = Scanner(System.`in`)

        fun getTimeStampAtual(): String
        {
            val atual = LocalDateTime.now()

            val formato = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss")
            val formatado = atual.format(formato)

            return formatado
        }
    }
}