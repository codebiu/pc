import subprocess

result = subprocess.run('dir',shell=True,stdout=subprocess.PIPE)

print(result.stdout.decode('GB2312'))