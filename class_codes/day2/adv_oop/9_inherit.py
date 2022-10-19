class Unix:
    def cmd(self):
        print("great command line")

    def secure(self):
        print("rwx makes it safer")

class Linux(Unix):
    def free(self):
        print("opensource and free")

    def portable(self):
        print("portable to many devices")

class mobileOS:
    def ui(self):
        print("great UI")

    def portable(self):
        print("portable phones")

class Android(mobileOS, Linux):
    def hardware(self):
        print("integrates well with the hardware")


obju = Unix()
objl = Linux()
obja = Android()

obja.portable()
