import os

SConscript('utils/env-local.py')
#SConscript('utils/env-local-mingw.py')
#SConscript('utils/env-target.py')
Import('env')

objs = []
for subdir in ['app', 'libs']:
    o = SConscript('%s/SConscript' % subdir)
    objs.append(o)

env.Program("myapp", objs)
