'''
You are writing code for a security company that writes antimalware
to identify potentially harmful files. Given a list of filenames file_list
(a list of strings), complete filter_files() so that it returns a new list
of files from file_list, but without any with an executable ".exe" extension.

Example 1:
file_list = ["run.exe", "README.md", "virus.exe"]
output = ["README.md"]

Example 2:
file_list = ["class_slides.pdf", "id_ed25519.pub", "virus.exe"]
output = ["class_slides.pdf", "id_ed25519.pub"]

Example 3:
file_list = []
output = []

Example 4:
file_list = ["virus.exe"]
output = []

Example 5:
file_list = ["wierd.exe.pdf"]
output = ["wierd.exe.pdf"]

HINT: How do we iterate through a sequence?
HINT: Of the following, how do we check if a string has/doesn't have
a certain prefix/suffix?:
str.split()
str.join()
str.find()
str.startswith()
str.endswith()
'''

def filter_files(file_list):
    new_list = []
    #TODO: YOUR CODE BELOW
    
    return new_list

# ignore this code
def solution(*args):
    return filter_files(*args)
