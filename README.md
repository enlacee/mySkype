### Send Message by Sell with python
================================
Send many messages atomatic, with Skype.
reposirtory ref : [https://github.com/awahlig/skype4py](https://github.com/awahlig/skype4py) 


Hi, start It. We install this app, would read this step

### Requirements
Your SO LINUX, (test in Ubuntu 13.10)
Is very likely that you already have installed
You nedd install **python 2.x**


###Step 1
Change name by terminal  of **config.dist.py to config.py**
to variables of configuration:

    mv config.dist.py config.py
 

###Step 2
Change these parameter:

    user  = '****'  # userName Skype
    timeSend = 5
    messages = [
    "message only read",
    "hello what your time?",
    "these is great",
    "moon in the skype",
    "live to back in story",
    "You defends with Jack Newton",
    "It is the fisrt class",
    "Where are you estudent",
    "do you is a mexican",
    "I fine and you",
    ]

###Step 3
The file must have execution permission

    sudo chmod 777 loopSkype.py
    
   
You should run the file in terminal

    python loopSkype.py

