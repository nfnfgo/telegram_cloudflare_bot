import subprocess

def GetEnvVar(name):
    if name=='':
        raise Exception('Empty variable name string is NOT allowed')
    p=subprocess.run(f'echo ${name}',shell=True,stdout=subprocess.PIPE)
    if p.returncode==0:
        return p.stdout
    else:
        raise Exception('Failed when read env variable from shell')


if __name__=='__main__':
    # give user warning, because this action will rewrite config file
    print('Now you are trying to rewrite the bot_config.py by reading environment varialbe')
    print('This action may damage the config info, and you may backup config file in advance.')
    print('\nEnter \'yes\' to continue, Press Ctrl+C to exit.')
    # let user confirm
    str=input()
    if str=='yes'

    # rewrite part
    rv_list=['$BOT_TOKEN','$ADMIN_ID']
    for vari in rv_list:
        value=GetEnvVar(vari)
        print(value)