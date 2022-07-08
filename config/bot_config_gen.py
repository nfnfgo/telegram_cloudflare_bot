import subprocess
import r_path

def GetEnvVar(name):
    if name=='':
        raise Exception('Empty variable name string is NOT allowed')
    p=subprocess.run(f'echo ${name}',shell=True,stdout=subprocess.PIPE)
    if p.returncode==0:
        return p.stdout.decode().replace('\n','')
    else:
        raise Exception('Failed when read env variable from shell')


if __name__=='__main__':
    # give user warning, because this action will rewrite config file
    print('Now you are trying to rewrite the bot_config.py by reading environment varialbe')
    print('This action may damage the config info, and you may backup config file in advance.')
    print('\nEnter \'yes\' to continue, Press Ctrl+C to exit.')
    # let user confirm
    str=input()
    while True:
        if str=='yes':
            break

    # rewrite part
    rv_list=['BOT_TOKEN','ADMIN_ID'] # define what keywords should be rewrite
    res_dict={} # use to storage result
    for vari in rv_list:
        value=GetEnvVar(vari)
        if value=='':
            print('Warning: Got an empty env value, auto skip it.')
            continue
        res_dict[vari]=value
    
    # start to use bot_config_example to generate the file we want
    with open(r_path.r_path+'/config/bot_config_example.py','r') as f:
        text=f.read()
    for vari,value in res_dict.items():
        text=text.replace(vari,value)
    with open(r_path.r_path+'/config/bot_config.py','w') as f:
        f.write(text)
