with open('message_info.json','r') as f:
    text=f.read()

text=text.replace('\'','\"')

with open('message_info.json','w') as f:
    f.write(text)