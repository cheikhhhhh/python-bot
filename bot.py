import discord 
from discord.ext import commands
from data import *
from data import Queue
import atexit
import json
import random

import pickle
import asyncio 
import time 
import pandas as pd
import requests
from bs4 import BeautifulSoup


 
client_historique = Stack(None)
message_obj = Message(None,None,None)

intents = discord.Intents.all()
user_stacks = {}
user_stacksid= {}
user_stacksdata = {}
user_stacksidhash = hashtable_user(100)

client = commands.Bot(command_prefix="!", intents = intents)


df = pd.read_csv('cine.csv')
@client.command(name="film")
async def film_command(message):
    df_sorted = df.sort_values('Note presse', ascending=False)
    top_movies= df_sorted.head(5)
    await message.channel.send(f"Voici les 5 meilleurs films notés pour chaque catégorie :\n{top_movies}")

@client.command(name="nasa")
async def nasa_pic_command(ctx):
    url = "https://api.nasa.gov/planetary/apod"

    params = {
        "api_key": "SooP05Z47gfB2bM62jzGFGH8RxLV44nW7YfdJwMY"
    }
    response = requests.get(url, params=params)
    data = json.loads(response.content)
    await ctx.send(data["url"])


@client.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban_command(ctx, member: discord.Member):
    try:
        await member.ban()
        await ctx.send(f"{member.mention} a été banni")
    except discord.Forbidden:
        await ctx.send("Je n'ai pas les permissions nécessaires pour bannir ce membre.")


@client.command(name="del")
async def delete(ctx):
    client_historique.push("del")
    await ctx.channel.purge(limit=10)

@client.command(name="Menu")
async def Menu(ctx):
  await ctx.channel.send("choisis une option : \n")
  await ctx.channel.send("1) historique\n")
  await ctx.channel.send("2)\n")
  await ctx.channel.send("3) \n")
  await ctx.channel.send("1) historique 1 \n")

@client.command(name="arriere")
async def forward(ctx):
    data = client_historique.forward()
    if data:
        await ctx.send(data)
    else:
        await ctx.send("fin de l'historique.")

@client.command(name="avant")
async def backward(ctx):
    data = client_historique.backward()
    if data:
        await ctx.send(data)
    else:
        await ctx.send("debut de l'hisotirque.")

@client.command(name='chifoumi')
async def chifoumi(ctx, choix):
    valid_choices = ['pierre', 'feuille', 'ciseaux']
    if choix not in valid_choices:
        await ctx.send(f"Veuillez choisir l'un des mots suivants : {', '.join(valid_choices)}")
        return
    
    client_choix = random.choice(valid_choices)
    
    if choix == client_choix:
        await ctx.send(f"J'ai choisi {client_choix}. Égalité !")
    elif (choix == 'pierre' and client_choix == 'ciseaux') or \
         (choix == 'feuille' and client_choix == 'pierre') or \
         (choix == 'ciseaux' and client_choix == 'feuille'):
        await ctx.send(f"J'ai choisi {client_choix}. Tu as gagné !")
    else:
        await ctx.send(f"J'ai choisi {client_choix}. J'ai gagné !")




@client.command(name="historyname")
async def history(ctx, user_name):
    # Vérifier si l'utilisateur a déjà une pile d'historique
    if user_name not in user_stacks:
        await ctx.channel.send("cette utilisateur n'a pas d'historique.")
        return

    print(user_stacks)
    # Obtenir la pile d'historique de l'utilisateur correspondant
    user_stack = user_stacks[user_name]

    # Récupérer l'historique des messages de l'utilisateur
    history_list = user_stack.append1()
    print(history_list)
    history_str = '\n'.join(history_list) #comme un concat avec tout les éléments qui retourne a la lgien un par un 

    # Envoyer l'historique des messages à l'utilisateur
    await ctx.channel.send(f"historique de {user_name}:\n{history_str}")


@client.command(name="historyid")
async def historyid(ctx, user_id):
    # Vérifier si l'utilisateur a déjà une pile d'historique
    if int(user_id) not in user_stacksid:
      await ctx.channel.send("cette utilisateur n'a pas d'historique.")
      print(user_stacksid)
      return
      
    user_stackid = user_stacksid[int(user_id)]
    user_stackid.append1()
    print(user_stackid.tolist())
    print(user_stacksid[int(user_id)])

    history_list = user_stacksidhash.append2(int(user_id) , user_stackid.tolist())
    print(user_stacksidhash)
    # Obtenir la pile d'historique de l'utilisateur correspondant
    history_str = (history_list) #comme un concat avec tout les éléments qui retourne a la lgien un par un 

    # Envoyer l'historique des messages à l'utilisateur
    await ctx.channel.send(f"historique de {user_stacksidhash.get(int(user_id))}:\n{history_str}")

@client.command(name="clear_history")
async def clear_history(ctx, user_id):
    # Vérifier si l'utilisateur a une Stack
    if user_id in user_stacks:
        # Supprimer la Stack de l'utilisateur
        del user_stacks[user_id]
        await ctx.channel.send("L'historique de l'utilisateur a été effacé.")
    else:
        await ctx.channel.send("cette utilisateur n'a pas  d'historique.")


@client.command(name="history2")
async def history2(ctx):
    txt = client_historique.goin()
    if txt:
        await ctx.channel.send(txt)
    else:
        await ctx.channel.send("No history available.")

@client.event
async def on_ready():
    print("Le bot est prêt !")


@client.event
async def on_typing(channel, user, when):
     await channel.send(user.name+" is typing")

@client.event
async def on_member_join(member):
    general_channel = client.get_channel(977137496720826368)
    await general_channel.send("Bienvenue sur le serveur ! "+ member.name)

@client.event
async def on_message(message):
    
  if message.author == client.user:
    return

  user_id = message.author.id
  user_name = message.author.name
  data = message.content
  message_obj = Message(user_name, user_id, data)


    # Si l'utilisateur n'a pas encore de Stack, créez-en une pour lui
  if data not in user_stacksdata:
    user_stacksdata[data] = Stack(None)
  if user_name not in user_stacks:
    user_stacks[user_name] = Stack(None)
  if user_id not in user_stacksid:
    user_stacksid[user_id] =Stack(None)
    
    # Ajoutez le message à la Stack de l'utilisateur correspondant
  user_stack = user_stacks[user_name]
  user_stackdata = user_stacksdata[data]
  user_stackid = user_stacksid[user_id]
  user_stackdata.push(data)
  user_stackid.push(message_obj.data)
  user_stack.push(message_obj.data)
  client_historique.push(message_obj.data)

  if message.content.startswith("quoi"):
    client_historique.push("quoicoubeh")
    await message.channel.send("quoicoubeh")

  if message.content.startswith("hein"):
    client_historique.push("hein")
    await message.channel.send("apanyan")

  await client.process_commands(message)

@client.command()
async def test(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')

# Fonction appelée à la fermeture du bot pour sauvegarder les données
def save_data():
    txt = client_historique.append1()

    print(txt)
    with open('data.txt', 'a') as file:    
        json.dump(txt, file)
    


# Enregistrement de la fonction "save_data" pour qu'elle soit appelée à la fermeture du bot
atexit.register(save_data)

client.run("MTA5MzgzNzY3MjkxMDQ0MjYxOA.GiWtZ5.lBB-dpP-HZwCMD33AETMJbBSpZpb8GvpM9GJ1Q")
