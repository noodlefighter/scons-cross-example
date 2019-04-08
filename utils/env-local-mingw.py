import os

tchian = ''
env_option = {
    "CC"    : tchian + 'gcc',
    "CXX"   : tchian + 'g++',
    "LD"    : tchian + 'g++',
    "AR"    : tchian + 'ar',
    "STRIP" : tchian + 'strip',
}

env = Environment(**env_option)
env.Append(ENV = {'PATH' : os.environ['PATH']})
Export('env')
