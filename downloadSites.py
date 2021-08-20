

import requests

catch = []

def GET_SECT():
    website = input('[GET-HTTPS] ')
    META_HEAD = input('[FILENAME.html] ')
    return website,META_HEAD


class DownloadSites:
    def __init__(self,website):
        self.website = website
        self.EXTENSION = ['.html']
        
    def httpsRequest(self):
        self.request = requests.get(self.website)
        return self.website

    def BuildSite(self,meta_title):
        with open(meta_title+self.EXTENSION[0],'wb') as META_HEAD:
            META_HEAD.write(self.request.text.encode('UTF-8'))
            return "[SUCCESS] +200 <HTTP_REQUEST>"


if __name__ == "__main__":
    statement = GET_SECT()
    catch.append(statement) #save outputs

    ScrappySite = DownloadSites(statement[0])
    print(ScrappySite.httpsRequest())
    print(ScrappySite.BuildSite(statement[1]))
