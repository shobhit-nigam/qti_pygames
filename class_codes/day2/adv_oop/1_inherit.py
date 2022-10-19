class Unix:
    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it safer")

class Linux(Unix):
    def free(self):
        print("opensource and free")

obju = Unix()
objl = Linux()

objl.cmd()
objl.free()
