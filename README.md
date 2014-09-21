### Send Message by Sell with python
================================
Send many messages, with Skype, 
reposirtory ref : [https://github.com/awahlig/skype4py](https://github.com/awahlig/skype4py) 


Hi, start It. We install this app, would read this step

### Requirements
Your SO Linux, (test in ubuntu)
Is very likely that you already have installed
You nedd install python 2.x


###Step 1
change name by terminal 
to variables of configuration:

    mv config.dist.py config.py
 

###Step 2
Change these parameter:
    user  = '****'  # userName Skype
    timeSend = 5
    messages = []

###Step 3
The file must have execution permission
    sudo chmod 777 loopSkype.py

execute program in terminal
    python loopSkype.py

