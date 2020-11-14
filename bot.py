#Дискорд Бот "DabiBot"
#Версия: 1.0.1.1
#Автор: AloneBown#3518

import discord
import typing
from discord.ext import commands

PREFIXx = '!'

bot = commands.Bot(command_prefix=PREFIXx)
bot.remove_command('help')
bad_words = ['Ниггер','негр', 'нигга', 'уебан', 'уебище', 'гнида', 'гомик', 'педераст', 'пидор', 'хохол', 'кацап', 'хохланд','Блядь','Сука','блеадь','пидорас', 'чмо', 'долбоеб', 'хуй', 'нахуй','На хуй','придурок', 'конченый','Хер','Даун','Daun','Dayn','Fisting ass','Бич','Bitch','пентюх','Блат','Блэт']
glory = ['Слава Арстоцке!']

#Отчет о включении бота
@bot.event
async def on_ready():
    print('Бот запущен')

@bot.event
async def on_command_error(ctx, error):
    pass

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    msg = message.content.lower()
    
    if msg in bad_words:
        await message.delete()
        return
    if msg in glory:
        await message.add_message('Glory toArstozka')
    
@bot.event
async def on_reaction_add(reaction, user):
  ChID = '774997225167257642'
  if reaction.message.channel.id != ChID:
    return
  if reaction.emoji == "1️⃣":
    CSGO = discord.utils.get(user.server.roles, name="Minecraft")
    await client.add_roles(user, CSGO)
#Пинг понг
@bot.command()
async def ping(ctx):
    await ctx.send('pong!')

#Сказать что то через бота
@bot.command()
async def say(ctx, arg: str):
    await ctx.channel.purge(limit = 1)
    await ctx.send(arg)

#Привет боту
@bot.command()
async def hello(ctx):
    await ctx.send('Привет! Я рад тебя видеть!')

#Удар
#@bot.command()
#async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='без причины'):
#    slapped = ", ".join(x.name for x in members)
#    await ctx.send('{} ударил, потому что {}'.format(slapped, reason))

#Чистка
@bot.command()
@commands.has_permissions( manage_messages = True )
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit = 1)
    await ctx.channel.purge(limit = amount)
    await ctx.send('Чистка окончена')

#Кик
@bot.command()
@commands.has_permissions( administrator = True )
async def  kick(ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge(limit = 1)

    await member.kick(reason = reason)
    await ctx.send (f'Пользователь {member.mention} был кинут с сервера по причине { reason }')

#Бан
@bot.command()
@commands.has_permissions( administrator = True )
async def ban(ctx, members: commands.Greedy[discord.Member],
              delete_days: typing.Optional[int] = 0, *,
              reason: typing.Optional[str]):
    """Mass bans members with an optional delete_days parameter"""
    await ctx.channel.purge(limit = 1)
    for member in members:
        await member.ban(delete_message_days=delete_days, reason=reason)
        await ctx.send (f'Пользователь {member.mention} был забанен на сервере по причине { reason }')

#Разбан
@bot.command()
@commands.has_permissions(manage_messages = True)
async def unban(ctx, *, member):
    await ctx.channel.purge(limit = 1)

    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user=ban_entry.user

        await ctx.guild.unban(user)
        await ctx.send (f'Пользователь {user.mention} был разбанен')

        return

#Мут
@bot.command()
@commands.has_permissions(manage_roles = True)
async def mute(ctx, member: discord.Member):
    await ctx.channel.purge(limit = 1)

    mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Mute')

    await member.add_roles(mute_role)
    await ctx.send(f'Пользователь {member.mention} был замьючен за нарушение правил')

#Размут
@bot.command()
@commands.has_permissions(manage_roles = True)
async def unmute(ctx, member: discord.Member):
    await ctx.channel.purge(limit = 1)

    mute_role = discord.utils.get(ctx.message.guild.roles, name = 'Mute')

    await member.remove_roles(mute_role)
    await ctx.send(f'Пользователь {member.mention} был размьючен')
    
@commands.command() # начало команды
@commands.has_permissions(administrator = True) # нужны права администратора? - да
async def ar(ctx, autoroles): #сама команда и что ей надо указать, это prefix, комаду и НАЗВАНИЕ роли.
    for guild in self.bot.guilds: # оно ищет на сервере людей
      for member in guild.members: # и тут делается все работа для member-a
        autoroles2 = discord.utils.get(ctx.message.guild.roles, name = CRB) # нахождение айди по названию, иначе будет ошибка(у меня)
        await member.add_roles(autoroles2) # само добавление роли
    emb = discord.Embed(description = 'Роли успешно добавлены ВСЕМ участникам Discord сервера.')
    await ctx.send(embed = emb) # теперь бот сообщает что всё вышло.

#------------------------------------------------КОМАНДА HELP---------------------------------------------------#

@bot.command()
async def help(ctx):
    await ctx.channel.purge(limit = 1)
    
    emb = discord.Embed(title = 'Навигация по командам', colour = discord.Colour.green())
    
    emb.set_author(name = bot.user.name, icon_url= bot.user.avatar_url)
    emb.add_field( name = '{}say'.format(PREFIXx), value = 'Сказать что-то с помощью бота, писать с " "')
    emb.add_field( name = '{}ping'.format(PREFIXx), value = 'Pong!')
    emb.add_field( name = '{}hello'.format(PREFIXx), value = 'Сказать привет боту')
    emb.add_field( name = '{}slap'.format(PREFIXx), value = 'Ударить кого-то (Отключена)')
    emb.add_field( name = '{}clear'.format(PREFIXx), value = 'Очистка чата (только модеры)')
    emb.add_field( name = '{}kick'.format(PREFIXx), value = 'Кикнуть пользователя с сервера (только админы)')
    emb.add_field( name = '{}ban'.format(PREFIXx), value = 'Забанить пользователя на сервере (только админы)')
    emb.add_field( name = '{}unban'.format(PREFIXx), value = 'Разбанить пользователя на сервере (только админы)')
    emb.add_field( name = '{}mute'.format(PREFIXx), value = 'Замутить пользователя за нарушение правил (только модеры)')
    emb.add_field( name = '{}unmute'.format(PREFIXx), value = 'Размутить пользователя (только модеры)')
    
    await ctx.send (embed = emb)

@bot.command()
async def help_ping(ctx):
    await ctx.channel.purge(limit=1)
    
    emb = discord.Embed(title = 'Помощь по команде: ping', colour=discord.Colour.green())

    emb.set_author(name = bot.user.name, icon_url= bot.user.avatar_url)
    emb.add_field( name = '{}ping'.format(PREFIXx), value = 'Pong!')
    emb.add_field(name='Назначение', value = 'Самая простая развлекательная команда')
    
    await ctx.send(embed=emb)

@bot.command()
async def help_say(ctx):
    await ctx.channel.purge(limit=1)
    
    emb = discord.Embed(title = 'Помощь по команде: ping', colour=discord.Colour.green())

    emb.set_author(name = bot.user.name, icon_url= bot.user.avatar_url)
    emb.add_field( name = 'Команда', value = '{}say'.format(PREFIXx))
    emb.add_field(name='Назначение', value = 'Сказать что-то через бота')
    emb.add_field(name='Пример', value = '!say "Random text"')
    
    await ctx.send(embed=emb)
#-----------------------------------------------------ВЫДАЧА ОШИБОК-------------------------------------------------------#
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send (f'{ctx.author.name}, укажите число удаляемых сообщений!')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'У вас нет прав использовать эту команду!')

@ban.error
async def ban_eror(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'У вас нет прав использовать эту команду!')

@unban.error
async def unban_eror(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'У вас нет прав использовать эту команду!')

@kick.error
async def kick_eror(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'У вас нет прав использовать эту команду!')

@mute.error
async def mute_eror(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'У вас нет прав использовать эту команду!')

@unmute.error
async def unmute_eror(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'У вас нет прав использовать эту команду!')




bot.run('NTczODk4NzMwMDIxOTc4MTEz.XMxi1w.T-feIPgp9qjQew2t8f3KuxiJWwk')
