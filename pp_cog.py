import os
import nextcord,time
from nextcord.ext import commands
from discord import application_command
from nextcord.ext.commands import cooldown, BucketType
from discord.ext.commands import cooldown, BucketType   
from discord.ui import Button, View
from discord import ButtonStyle
myserverid= 835199166346821632



class Compact(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    @nextcord.slash_command(name="adaptivequiz",guild_ids=[1043840825118957569])
    async def quiz(self,interaction:nextcord.Interaction):
        answers = {}

        embed = nextcord.Embed(title="Adaptive learning quiz",description="Choose the answer that is most correct!")
        embed.add_field(name=f"Question 1",value = "Which one of these is an apple?")
        view = View(timeout=None)
        view.add_item(Button(label="🍎",custom_id=f"{interaction.user.id}apple"))
        view.add_item(Button(label="🍊",custom_id=f"{interaction.user.id}orange"))
        view.add_item(Button(label="🍌",custom_id=f"{interaction.user.id}banana"))
        view.add_item(Button(label="🍇",custom_id=f"{interaction.user.id}grape"))

        await interaction.response.send_message(embed=embed,view=view)
        t_0 = time.time()
        def check(new_int:nextcord.Interaction):
            return new_int.user.id == interaction.user.id and new_int.data.get("custom_id",None) in [button.custom_id for button in view.children]
        
        ans = await self.bot.wait_for("interaction",check=check,timeout=180)
        if ans.data["custom_id"] == f"{interaction.user.id}apple":
            answers[1]={"a":True,"time":time.time()-t_0}
        else:
            answers[1]={"a":False,"time":time.time()-t_0}
        
        embed.clear_fields()
        view.clear_items()

        embed.add_field(name=f"Question 2",value ="Which one of these is an 🍎?")
        view.add_item(Button(label="apple",custom_id=f"{interaction.user.id}apple"))
        view.add_item(Button(label="orange",custom_id=f"{interaction.user.id}orange"))
        view.add_item(Button(label="banana",custom_id=f"{interaction.user.id}banana"))
        view.add_item(Button(label="grape",custom_id=f"{interaction.user.id}grape"))

        await interaction.edit_original_message(embed=embed,view=view)
        t_0 = time.time()
        ans = await self.bot.wait_for("interaction",check=check,timeout=180)
        if ans.data["custom_id"] == f"{interaction.user.id}apple":
            answers[2]={"a":True,"time":time.time()-t_0}
        else:
            answers[2]={"a":False,"time":time.time()-t_0}



        embed.clear_fields()
        view.clear_items()

        embed.add_field(name=f"Question 3",value ="Click the MP3 Above to try and listen to the question!")
        file = nextcord.File("apple.mp3")
        view.add_item(Button(label="🍎",custom_id=f"{interaction.user.id}apple"))
        view.add_item(Button(label="🍊",custom_id=f"{interaction.user.id}orange"))
        view.add_item(Button(label="🍌",custom_id=f"{interaction.user.id}banana"))
        view.add_item(Button(label="🍇",custom_id=f"{interaction.user.id}grape"))

        await interaction.edit_original_message(embed=embed,view=view,file=file)
        t_0 = time.time()
        ans = await self.bot.wait_for("interaction",check=check,timeout=180)
        if ans.data["custom_id"] == f"{interaction.user.id}apple":
            answers[3]={"a":True,"time":time.time()-t_0}
        else:
            answers[3]={"a":False,"time":time.time()-t_0}
        


        embed.clear_fields()
        view.clear_items()

        embed.add_field(name=f"Question 4",value ="Click the MP3 Above to try and listen to the question!")
        file = nextcord.File("apple.mp3")
        view.add_item(Button(label="apple",custom_id=f"{interaction.user.id}apple"))
        view.add_item(Button(label="orange",custom_id=f"{interaction.user.id}orange"))
        view.add_item(Button(label="banana",custom_id=f"{interaction.user.id}banana"))
        view.add_item(Button(label="grape",custom_id=f"{interaction.user.id}grape"))

        await interaction.edit_original_message(embed=embed,view=view,file=file)
        t_0 = time.time()
        ans = await self.bot.wait_for("interaction",check=check,timeout=180)
        if ans.data["custom_id"] == f"{interaction.user.id}apple":
            answers[4]={"a":True,"time":time.time()-t_0}
        else:
            answers[4]={"a":False,"time":time.time()-t_0}
        





        embed.clear_fields()
        view.clear_items()

        embed.add_field(name=f"Question 5",value ="Which one of these is an 🍎?")
        files = [nextcord.File("1.mp3"),nextcord.File("2.mp3"),nextcord.File("3.mp3"),nextcord.File("4.mp3")]

        view.add_item(Button(label="1",custom_id=f"{interaction.user.id}apple"))
        view.add_item(Button(label="2",custom_id=f"{interaction.user.id}orange"))
        view.add_item(Button(label="3",custom_id=f"{interaction.user.id}banana"))
        view.add_item(Button(label="4",custom_id=f"{interaction.user.id}grape"))

        await interaction.edit_original_message(embed=embed,view=view,files=files)
        t_0 = time.time()
        ans = await self.bot.wait_for("interaction",check=check,timeout=180)
        if ans.data["custom_id"] == f"{interaction.user.id}apple":
            answers[5]={"a":True,"time":time.time()-t_0}
        else:
            answers[5]={"a":False,"time":time.time()-t_0}
        
        embed.clear_fields()
        embed.add_field(name=f"Question 6",value ="Which one of these is an apple?")
        files = [nextcord.File("1.mp3"),nextcord.File("2.mp3"),nextcord.File("3.mp3"),nextcord.File("4.mp3")]

        await interaction.edit_original_message(embed=embed,view=view,files=files)
        t_0 = time.time()
        ans = await self.bot.wait_for("interaction",check=check,timeout=180)
        if ans.data["custom_id"] == f"{interaction.user.id}apple":
            answers[6]={"a":True,"time":time.time()-t_0}
        else:
            answers[6]={"a":False,"time":time.time()-t_0}
        

        embed.clear_fields()
        view.clear_items()
        string = ""
        for i in range (1,7):
            string +=f"Question {i}: {'  correct' if answers[i]['a'] else 'incorrect'}, time: {round(answers[i]['time'],3)} seconds\n"

        answer_form = [round(answers[i]['time'],3) for i in range(1,7)]
        
        string+=f"You spent a total of {round(sum(answer_form))} seconds on this quiz!\n"

        time_str = round(answers[1]['time'],3)+ round(answers[2]['time'],3)
        time_ask = round(answers[3]['time'],3)+ round(answers[4]['time'],3)
        time_ans = round(answers[5]['time'],3)+ round(answers[6]['time'],3)
        if time_str == min([time_str,time_ask,time_ans]):
            string+= "You spent the least amount of time on string/nonverbal based questions!"
        elif time_ask == min([time_str,time_ask,time_ans]):
            string+= "You spent the least amount of time on verbal-ask based questions!"
        elif time_ans == min([time_str,time_ask,time_ans]):
            string+= "You spent the least amount of time on verbal-answer based questions"
        
        embed.add_field(name="You completed the quiz!",
            value=string)
        await interaction.edit_original_message(embed=embed,view=view)
        

def setup(bot):
    bot.add_cog(Compact(bot))