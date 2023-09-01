import json, os, random
from discord.ext import commands
import discord

def main():
    if os.path.exists('config.json'):
        with open('config.json') as f:
            config_data = json.load(f)
            
    else:
        template = {'prefix': '!', 'token':''}
        with open('config.json','w') as f:
            json.dump(template, f)

    prefix = config_data ["prefix"]
    token = config_data ["token"]
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix = prefix, intents= intents, description= "Bot lobo")
    
        #Lista de Saludos
    Saludos_predefinidos = [
        "¡Hola, manada!",
        "¿Cómo están todos hoy?",
        "Lobos, ¡aullamos a la luna!",
    ]

        #Lista de consejos millonario
    Consejo_millonario=[
        "El pobre es pobre porque quiere",
        "Un dolar mas, es un paso mas para dejar de ser pobre",
        "No es depresion, es flojera, ponte a chambear",
        "YA PONTE A CHAMBEAR",
        "Compra 3 departamentos, rentas 2 y vives en uno",
        "Si no te gusta tu trabajo, entonces viaja"
    ]

        #Lista de Frases
    frases_predefinidas = [
        "Mi intel Core i5 me da el calor que ninguna mujer me ha querido dar",
        "Ya le diste una. Ya le diste dos. Ya le diste tre. Y tu tiempo se acabo. Ese niño es muy tonto, se parece a su papa",
        "El madrugador recibe el gusano.",
        "Presumes ser leona y ni a gata callejera llegas",
        "Demasiado grande para los calzones",
        "Cuando te falta sexo te masturbas y asunto arreglado, ¿Pero qué haces cuando te falta amor? ¿Cómo haces para masturbarte el corazón?",
        "Es un país libre, señor; el hombre es mío, y haré con él lo que me plazca..",
        "Un pobre es como un rico pero sin dinero",
        "Recuerden ser siempre fuertes y valientes.",
        "¡Un lobo nunca camina solo!",
        "No vivas con falsedades ni miedos, porque terminarás odiándote a ti mismo.",
        "A la víbora víbora de la mar , por aquí pueden pasar",
        "Cuando yo tenía tu edad, tenía tus mismos años.",
        "A veces las personas calladas son las que casi no hablan.",
        "Muchas veces el camino fácil no es difícil.",
        "La piedra que me lanzas hoy puede ser con la que me drogue mañana",
        "Me gustaría insultarte, pero no lo haría tan bien como lo hizo la naturaleza.",
        "Amigas no son las que te dicen Te amo, amigas son las que te restriegan las tetas en la cara",
        "Nunca pierdas el tino, porque si lo pierdes, pierdes el camino",
        "Soy frio porque cuando fui caliente tuve un hijo",
        "Las personas que mienten, nunca dicen la verdad",
        "Si me vas a tratar como tu juguete, quiero ser el que vibra.",
        "Si algún día bajo la mirada será para ver cómo me la chupan",
        "Si me ves correr, es porque me estoy cagando",
        "La gente le teme a lo que le da miedo.",
        "Si el río suena es por que no estas sordo",
        "No dejes que otra persona decida por ti, es tu responsabilidad arruinar tu propia vida",
        "Baby, I'm preying on you tonight Hunt you down eat you alive Just like animals Animals Like animals-mals",
        "la vida es dificil, si fuera facil se llamaria ""administracion de empresas"" "
    ]


        #Lista de Rol
    Rol_predefinido = [

        "La luz de la luna llena cae sobre ti, y tus músculos se expanden mientras te transformas en un imponente hombre lobo.",
        "Tu furia bestial y tus poderosos músculos te convierten en una fuerza imparable de la naturaleza.",
        "A medida que la noche avanza, tus músculos se tensan bajo tu piel, ansiosos por liberar su poder en la caza.",
        "La gente te mira con asombro y temor cuando te cruzan, maravillados por tu figura musculosa y tu aura salvaje de hombre lobo.",
        "Los aullidos de otros lobos resuenan en la distancia, y sientes la urgencia de unirte a la manada con tu fuerza sobrenatural.",
        "Tus garras afiladas y tus músculos poderosos son tus principales armas mientras defiendes tu territorio como el líder de la manada.",
        "La lucha interna entre tu lado humano y tu instinto animal se refleja en la tensión de tus músculos mientras luchas por mantener el control.",
        "En las noches de luna llena, tus músculos se hinchan mientras te conviertes en un depredador hábil y temido en la oscuridad.",
        "La transformación es dolorosa pero electrizante, ya que tus huesos se reorganizan y tus músculos se ajustan para abrazar tu forma de hombre lobo.",
        "Tus ojos amarillos brillan intensamente entre la densa melena, mientras utilizas tus músculos para recorrer el bosque con agilidad y velocidad."
    ]

    # Directorio donde se encuentran las imágenes
    #image_directory = "c:\Users\juanf\Documents\bot discord\Nuevo Bot"


    #Comando para saludar
    @bot.command(name="Saludar", description= "Un saludo")
    async def saludar(ctx):
        Saludo_Random = random.choice(Saludos_predefinidos)
        await ctx.reply(Saludo_Random)

    #Comando para frases
    @bot.command(name="Auh", description= "Dice una frase")
    async def Frases_predefinidas(ctx):
        Un_lobo_dice = random.choice(frases_predefinidas)
        await ctx.send(Un_lobo_dice)

    #Comando que corrige
    @bot.command(name="auh", description= "Te corrige")
    async def Corrige(ctx):
        await ctx.reply("Asi no va el comando, TONTUELO!!!")

    #Comando para el Rol
    @bot.command(name="Rol", description="El lobo da un mini rol")
    async def Rol(ctx):
        Rol_lobo = random.choice(Rol_predefinido)
        await ctx.send(Rol_lobo)

    #Comando para consejos millonario
    @bot.command(name="Consejo", description="El lobo te dara un consejo millonari")
    async def Consejo(ctx):
        lobo_millonario = random.choice(Consejo_millonario)
        await ctx.send(lobo_millonario)

    

    #Eventos
    bot.run(token)


if __name__ == "__main__":
    main()

