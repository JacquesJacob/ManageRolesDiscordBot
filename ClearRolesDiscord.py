import discord
import time
import socket
from discord.utils import get

intents = discord.Intents().all()
client = discord.Client(intents=intents)

remove_role = input("PUBG BRASIL BOT. Distribuição de cargos fim de temporada.\n"
                    "Informe qual role sera removida:\n")
add_role = input("Informe qual role sera adicionada:\n")
patent = input("Qual patente sera removida do nick (opções: 🥉 🏅 🥈 💠 👑 💎):\n")
confirmacao = input(f"Confirme as informações abaixo:\n"
                    f"Remover role: {remove_role}\n"
                    f"Adicionar role: {add_role}\n"
                    f"Remover patente: {patent}\n"
                    f"Voce confirma? (Y/N)\n")

if confirmacao == "Y":
    @client.event
    async def on_ready():
        print('Logged in as:')
        print(client.user.name)
        print(client.user.id)
        print('Discord Version: %s' % discord.__version__)
        print('---------')

        print('Servers connected to:')
        for guild in client.guilds:
            print("---------")
            print(guild.name)
            print(guild.id)
            print("---------")
            number = 0
            for member in guild.members:
                    print("------------")
                    number = number + 1
                    print("Lendo usuário: {} numero *** {} ***".format(member, number))
                    if not add_role:
                        print("Funçao para ser adicionada esta em branco!")
                    if not remove_role:
                        print("Funçao para ser removida esta em brando!")
                    if not patent:
                        print("Patente a ser removida esta em branco!")
                    for role in member.roles:
                        if role.name == remove_role:
                            time.sleep(0.3)
                            print("------")
                            print(member.name)
                            member = member
                            if add_role:
                                role2 = get(guild.roles, name=add_role)
                                await member.add_roles(role2)
                                print("Adicionado funçao {}".format(role2))
                            if remove_role:
                                role1 = get(guild.roles, name=remove_role)
                                await member.remove_roles(role1)
                                print("Removida funçao {}".format(role1))
                            if patent:
                                simbol = patent
                                nick = member.display_name
                                if simbol in nick:
                                    nick = nick.replace(patent, '')
                                    await member.edit(nick=nick)
                                    print("Nickname alterado para {}.".format(member.display_name))
                            print("*** ATUALIZADO COM SUCESSO ***")
                        #time.sleep(0.15)
                    print("Usuario {} pertencente aos grupos {}!".format(member, member.roles))
                    print("--------------")
            print("BATCH END!!!")
            await client.close()

else:
    print("Confirmação inválida!")
    time.sleep(3)
    exit(1)

client.run('DISCORD_BOT_TOKEN')
