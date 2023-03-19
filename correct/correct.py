'''
A pyscript gets runned. how can i add 

now i need to correct the 

create a class which is correcting everything basically  

i need to prompt it together somehow. 

Put 1 into a loop 

1.
    The following file:

    [file]

    produces the following error:

    [terminal  output]

    How to fix that? Respond in rewriting the whole file with the correct version.

2.
    Check if execution failed. If yes go to next step else print "Script executed successfully."


load 

- [ ] make response 
 
- [ ] change file 
- [ ] check for error 
- [ ] parse error
- [ ] return if next cycle or not 
- [ ] implement loop 
- [ ] run and see if it works


goal is to run correct.py fileyouwishtocorrect 

'''

class Correct():
    def __init__(self, file):
        self.file = file
        self.corrected = []

    def read_file(self):
        with open(self.file, "r") as f:
            content = f.read()
        return content

    def prompt(self):
        prompt = f'''The following file:

        {self.file}

        produces the following error:

        {self.read_file()}

        How to fix that? Respond in rewriting the whole file with the correct version. Nothing else. Show only the code.'''
        return prompt

    def change_file(self):

        pass






    