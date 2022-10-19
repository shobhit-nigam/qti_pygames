class Unix:
    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it safer")

class Linux(Unix):
    def free(self):
        print("opensource and free")

class mobileOS:
    def ui(self):
        print("great UI")

class Android(Linux, mobileOS):
    def hardware(self):
        print("integrates well with the hardware")


obju = Unix()
objl = Linux()
obja = Android()

obja.secure()
