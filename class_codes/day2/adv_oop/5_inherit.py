class Unix:

    def __init__(self):
        print("init of unix")

    def cmd(self):
        print("great CLI")

    def secure(self):
        print("rwx makes it safer")

class Linux(Unix):

    def free(self):
        print("opensource and free")


#obju = Unix()
objl = Linux()

objl.cmd()
