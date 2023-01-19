from django.shortcuts import render
from chat.models import chat
import openai

# Create your views here.


def fun(r):
    say = 'Welcome to Ai Chatbot '
    if r.method == 'POST':
        msg2 = r.POST["inp"]
        msg = msg2.lower()
        if msg == 'hi' or msg == 'hai':
            say = "Hi! How Can I Help You"
            kgf = "Hi! How Can I Help You🙌"
            create = chat(my=msg2, res=kgf)
            create.save()
        elif msg == 'hello':
            say = "Hello! How are You"
            kgf = "Hello! How are You😎"
            create = chat(my=msg2, res=kgf)
            create.save()
        elif msg == 'ok' or msg == 'okay' or msg == 'k':
            kgf = "😎🎶🎶🤷‍♂️"
            say = 'okay sir'
            create = chat(my=msg2, res=kgf)
            create.save()
        elif 'about your creator' in msg or 'tell your creator' in msg:
            kgf = """My creater is Name is : mohamath.  
            He is Now Reading BET Degree in University of Kelaniya.   """

            say = """My creater is Name is : mohamath.  
            He is Now Reading BET Degree in University of Kelaniya.  
             """

            create = chat(my=msg2, res=kgf)
            create.save()
        elif 'your name' in msg:
            kgf = "My Name is SJ. I am Python Chatbot👌 Created By mohamath"
            say = "My Name is SJ. I am Python Chatbot Created By mohamath"
            create = chat(my=msg2, res=kgf)
            create.save()
        elif 'your creator' in msg or 'your creater' in msg:
            kgf = "My creater is mohamath"
            say = "My creater is mohamath U o k student"
            create = chat(my=msg2, res=kgf)
            create.save()
        elif msg == 'cool':
            kgf = "okay... i will be cool🤷‍♂️."
            say = "okay... i will be cool."
            create = chat(my=msg2, res=kgf)
            create.save()
        elif msg != '':
            openai.api_key = "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"
            j = msg
            response = openai.Completion.create(
                model="text-davinci-003", prompt=f"{j}", temperature=0, max_tokens=100)
            # [ text-davinci-003 , text-ada-001 ] - Models
            say = kgf = response['choices'][0]["text"]
            create = chat(my=msg2, res=kgf)
            create.save()
    data = chat.objects.all()
    return render(r, 'chat.html', {'sj': data, 's': say})
