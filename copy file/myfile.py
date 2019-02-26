import tkinter.filedialog
tkinter.filedialog.askopenfilename()
from_file = tkinter.filedialog.askopenfilename()
to_file = tkinter.filedialog.asksaveasfilename()

from_file = open(from_file, 'r')
contents = from_file.read()
from_file.close()

to_file = open(to_file, 'w')
to_file.write('copy/n')
to_file.write(contents)
to_file.close()
