import commands
cmd = 'docker exec -it gdefects4dll-rebug /bin/bash /test/torch-61345/torch-61345-buggy.sh'
(status, output) = commands.getstatusoutput(cmd)
print("status: " + str(status))
print("output: " + output)

import subprocess
res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) # 使用管道
print("# 标准输出")
print(res.stdout.read())  # 标准输出
for line in res.stdout.readlines():
    print(line)
res.stdout.close()

import os
cmd = 'docker exec -it gdefects4dll-rebug /bin/bash /test/torch-61345/torch-61345-buggy.sh'
result = os.system(cmd)
print(result)

import os
cmd = 'docker exec -it gdefects4dll-rebug /bin/bash /test/torch-61345/torch-61345-buggy.sh'
result = os.popen(cmd)
print(result.read())