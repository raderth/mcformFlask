from flask import Flask, render_template, request
from discord_webhook import DiscordWebhook, DiscordEmbed

app = Flask(__name__)
    

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST": #on form submission
        username = request.form["username"]
        age = request.form["age"]
        country = request.form["country"]
        play = request.form["play"] #how often are you likely to play?
        join = request.form["join"] #why would you like to join?
        fav = request.form["fav"] #favourite aspect of Minecraft?
        discord = request.form["discord"] #do you use Discord a lot?
        mature = request.form["mature"]
        smp = request.form["smp"] #previous smp(s)
        time = request.form["time"] #how long have you been playing Minecraft
        guidelines = request.form["guidelines"]

        webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1096090761575018587/iNNmDj8pQlwaAq-7CxbBaLRu_nEkJOVNJaUJo_4Fh5Co6nLlDnr-2Qt8UTrAaXUQonj9')
        
        # create embed object for webhook
        embed = DiscordEmbed(title='Your Title', description='Lorem ipsum dolor sit', color='03b2f8')
        
        # set timestamp (default is now)
        embed.set_timestamp()
        
        # add fields to embed
        embed.add_embed_field(name='Field 1', value='Lorem ipsum')
        embed.add_embed_field(name='Field 2', value='dolor sit')
        
        # add embed object to webhook
        webhook.add_embed(embed)
        
        response = webhook.execute()

        return render_template("success.html")
      
    return render_template("form.html")

app.run(host='0.0.0.0', port=81)
