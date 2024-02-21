# for-fun
messing around with things

I was working on a Phantasy Start Online (EP 1) fanfic for NaNoWriMo
and I wanted to get sector ID's to names correct... 
I coded this up based on what i found online. This is not the blue-burst with the offset, but I think I could easily add that in the future.
I tried to clean up my pylint issues.
I then threw the code at FastAPI to make it an API call because I had never used it before.

1. clone this repo
2. install requirements.txt (pip install -r requirements.txt)
3. cd into the dir
4. maybe you need to chmod +x main.py
5. ./main.py
6. access via: yourhost:8000/sectid/yourname
7. also use /docs for the auto-generated swagger docs from FastAPI

FastAPI is cool!

IF YOU USE THE DOCKER CONTAINER!

standard docker build from Dockerfile :
'''sudo docker build --file Dockerfile --tag pso-sect-id:latest'''
#tag it whatever you want really.

run '''sudo docker iamges''' to get image id for next command:
then to run:
'''sudo docker run -p 8081:5000 -d -name "pso-sect-id" <image id>'''

#whatever port you want; if you are using a vm and likely have multiple interfaces. I hardcoded port 5000 in main.py
#you can do something more like
'''sudo docker run -p 192.168.1.2:8080:5000 -name "pso-sect-id" <image id>'''
