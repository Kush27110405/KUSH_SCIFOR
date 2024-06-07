class FileProcessor:
    def process(self):
        raise NotImplementedError("Subclasses should implement this method")
    
class TextFileProcessor(FileProcessor):
    def __init__(self,filename):
        self.filename = filename

    def process(self):
        with open(self.filename, 'r') as file:
            content = file.read()
            print(f"Processing Text file :{self.filename}")
            print(content)

class BinaryFileProcessor(FileProcessor):
    def __init__(self,filename):
        self.filename = filename

    def process(self):
        with open(self.filename, 'rb') as file:
            content = file.read()
            print(f"Processing Binary file :{self.filename}")
            print(content)

def processing_files(files):
    if not(isinstance(files,list)):
        raise ValueError("Wrong argument. Only lists can be passed as argument")
    elif not all(isinstance(i,TextFileProcessor) or isinstance(i,BinaryFileProcessor) for i in files):
        raise ValueError(" list must contain only text or  binary files")
    else:
        for i in files:
            i.process()

files = [TextFileProcessor("example.txt"), BinaryFileProcessor("example.bin")]
processing_files(files)
    
