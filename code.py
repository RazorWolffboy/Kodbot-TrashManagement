@bot.command()
async def tm (ctx):
    TM_image = random.choice(os.listdir('TM_Images'))
    picture = discord.File(f'TM_Images/{TM_image}')
    text = "Aqui está uma dica de como preservar o meio ambiente e descartar seu lixo corretamente!"
    await ctx.send(content=text, file=picture)
