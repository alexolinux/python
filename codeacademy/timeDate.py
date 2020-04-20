from datetime import datetime
# Pyscript para exibicao de Hora Atual.

now = datetime.now()

print (('Current Date: \t%02d/%02d/%04d') % (now.month, now.day, now.year))
print (('Current Time: \t%02d:%02d:%02d') % (now.hour, now.minute, now.second))