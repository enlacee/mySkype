# import Skype4Py.skype
import  Skype4Py
import time
from random import randint
from array import array
# import variable configuration
import config

skype = Skype4Py.Skype()
skype.Attach()  

# configuracion
paramUserSkype = config.user
paramMessage = config.messages
paramSleep = config.timeSend

print '================= SKYPE 4.3 =================='
print 'Init messages to userName: ' + str(paramUserSkype)
print 'Number of frases is: ' + str(len(paramMessage))
print '================= SKYPE 4.3 =================='

if (len(paramMessage) > 0):
    i = 1
    while i > 0:
        indice = randint(0,len(paramMessage)-1)
        messageBluche = paramMessage[indice]
        print 'Message : #', i
        print 'paramMessage[',str(indice),'] :',messageBluche
        skype.SendMessage(paramUserSkype, messageBluche)
        time.sleep(paramSleep)
        i += 1
else:
    print 'Not exists message to send. (error configuration): verified : config.py'