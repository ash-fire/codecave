import urllib

def download_file(download_url):
    response = urllib.urlopen(download_url)
    file = open("document.pdf", 'w')
    file.write(response.read())
    file.close()
    print("Completed")
    
def main():
    download_file("http://mensenhandel.nl/files/pdftest2.pdf")



if __name__ == "__main__":
    main()
