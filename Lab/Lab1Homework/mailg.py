from gmail import GMail, Message
from random import choice
import time


gmail = GMail('ndexpacc@gmail.com', '[dogexpacc]')
html_template = """<p>Dear team,</p>
<p>This morning I woke up with {{symptoms}} and after I went to the doctor, I was diagnosed with {{sickness}}. I, therefore, would like to take today off in compliance with the doctor's direction.</p>
<p>Best regards,</p>
<p>Andy</p>"""
symtoms = ["headache", "stomachache", "dizziness", ]
sickness = ["cold", "flu", ]
html_content = html_template.replace("{{symptoms}}", choice(symtoms)).replace("{{sickness}}", choice(sickness))
msg = Message('Sick leave', to='C4E.201708@gmail.com', html=html_content,) #attachments=['C:\\Users\\lupin\Downloads\\12.jpg'])

while True:
    ts = time.localtime()
    if ts <= 7:
        sleep(7200)
    else:
        gmail.send(msg)
        break
