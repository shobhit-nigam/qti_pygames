class Unix:
    max_files = 50

    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it safer")

class Linux(Unix):
    max_files = 120
    def free(self):
        print("opensource and free")

obju = Unix()
objl = Linux()

objl.cmd()
objl.free()

# error
obju.free()
