# for-fun
messing around with things

I was working on a Phantasy Start Online (EP 1) fanfic for NaNoWriMo
and I wanted to get sector ID's to names correct... 
I coded this up based on what i found online. This is not the blue-burst with the offset, but I think I could easily add that in the future.
I tried to clean up my pylint issues.
I then threw the code at FastAPI to make it an API call because I had never used it before.

1. install uvicorn
2. git clone this
3. cd into the dir
4. run by: uvicorn main:app
(I have to specify my host because I've got a vbox vm running it - so mine looks like: uvicorn main:app --host x.x.x.x
5. access via: yourhost:8000/sectid/<yourname>
6. also use /docs for the auto-generated swagger docs from FastAPI
FastAPI is cool!
