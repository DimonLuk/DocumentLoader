"""
This odule if the collection of functions.
Using them you are able to
1) Scan target file(.doc or .pdf) and find which words are the most common for it
2) Donwload .doc or .pdf files from google
3) Scan downloaded files and decide if they are usable
imports: win32com.client
TODO Deal with pdf
TODO: create neural network which will make decision for you
"""
debug = True
import win32com.client
def getTextFromWordDocument(path, fileName, *, debugging=False):
    import win32com.client
    """
    Using: path where will be created temporary files, filename with .doc or pdf
    Returns: text from original file
    """
    app = win32com.client.Dispatch("Word.Application")
    pathToFile = r"%s\%s" % (path, fileName)
    return app.Documents.Open(pathToFile).Content.Text



    

def getTextFromPdfDocument(path, fileName, *, debugging=False): #TODO
    """
    Using: path where will be created temporary files, filename with .doc or pdf
    Returns: text from original file
    """
    from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
    from pdfminer.converter import TextConverter
    from pdfminer.layout import LAParams
    from pdfminer.pdfpage import PDFPage
    from io import StringIO
    
    pathToFile = r"%s\%s" % (path, fileName)
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(pathToFile, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text[:-1]


def createArrayOfWords(text, *, debuggin=False):
    """
    
    """
    import re
    text = text.lower()
    text = re.findall("\w+", text)
    return text
def countEveryWord(words):
    from collections import Counter
    c = Counter(words)
    del c["та"]
    del c["на"]
    del c["таеп"]
    del c["з"]
    del c["в"]
    del c["і"]
    del c["що"]
    del c["зв"]
    del c["їх"]
    del c["ня"]
    del c["для"]
    del c["gc"]
    for i in range(1000):
        tmp = "%s" % i
        del c[tmp]
    alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lalphabet = alphabet.lower()
    for i in alphabet:
        del c[i]
    for i in lalphabet:
        del c[i]

    return c



def getResultOfCounting(countedWords, accuracy, path, *, write=False):
    if write:
        pathToFile = r"%s\readyToExplore.txt" % path
        with open(pathToFile, "w") as file:
            for i in countedWords.most_common(accuracy):
                file.write("%s:%s\n" % i)
    if not write:
        return countedWords.most_common(accuracy)
        

    
if __name__ == "__main__":
    if debug:
        #print(getTextFromWordDocument("D:\Projects\AIIDocumentFinder\AIDocumentFinder", "Test.doc"))
        #print(getTextFromPdfDocument("D:\Projects\AIIDocumentFinder\AIDocumentFinder", "Test.pdf"))
        #print(createArrayOfWords(getTextFromWordDocument("D:\Projects\AIIDocumentFinder\AIDocumentFinder", "Test.doc")))
        #print(createArrayOfWords(getTextFromPdfDocument("D:\Projects\AIIDocumentFinder\AIDocumentFinder", "realtest1.pdf")))
        #print(createArrayOfWords(getTextFromWordDocument("D:\Projects\AIIDocumentFinder\AIDocumentFinder", "realtest1.doc")))
        #print(getTextFromWordDocument("D:\Projects\AIIDocumentFinder\AIDocumentFinder", "Test.doc"))
        #print(createArrayOfWords(getTextFromWordDocument("D:\Projects\AIIDocumentFinder\AIDocumentFinder", "Test.doc")))
        #print(countEveryWord(createArrayOfWords(getTextFromWordDocument("D:\Projects\AIIDocumentFinder\AIDocumentFinder", "realtest1.doc"))))
        #countEveryWord(createArrayOfWords(getTextFromWordDocument("D:\Projects\AIIDocumentFinder\AIDocumentFinder", "realtest1.doc")))
        print(getResultOfCounting(countEveryWord(createArrayOfWords(getTextFromWordDocument("D:\Projects\AIIDocumentFinder\AIDocumentFinder", "realtest1.doc"))), 10, "D:\Projects\AIIDocumentFinder\AIDocumentFinder"))