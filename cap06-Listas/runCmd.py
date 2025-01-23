import subprocess

CMD = "tracert -h 4 -d 200.17.143.129"
p = subprocess.Popen (CMD, stdout=subprocess.PIPE)
result = p.communicate()[0].decode('cp850')

print (result)