class Unix:
    max_files = 50

    def cmd(self):
        print("great CLI, plain black&white")

    def secure(self):
        print("rwx makes it safer")

class Linux(Unix):
    max_files = 120
    def free(self):
        print("opensource and free")

    def cmd(self):
        super().cmd()
        print("or")
        print("attractive CLI, vibrant colours")

    def open_files(self):
        print(f"maximum files that can be opened in user mode = {self.max_files}")
        print(f"maximum files that can be opened in kernel mode = {super().max_files}")


obju = Unix()
objl = Linux()

objl.cmd()
