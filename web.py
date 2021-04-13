from urllib.request import Request,urlopen
from urllib.error import HTTPError

class fasta:
    def __init__(self,parent,accession_id,server_id):
        self.parent=parent
        self.sequence = ""
        self.metadata = ""
        self.result = ""
        self.accession = accession_id
        if (server_id>2):
            self.serverid = 2
        elif (server_id<0):
            self.serverid = 0
        else:
            self.serverid = server_id
        self.readdata()

        

    def readdata(self):
        preurls = ['https://www.ncbi.nlm.nih.gov/sviewer/viewer.cgi?tool=portal&sendto=on&log$=seqview&db=protein&dopt=fasta&sort=&val=',
                   'https://www.rcsb.org/fasta/entry/',
                   'https://www.uniprot.org/uniprot/']
        posturls = ['&from=begin&to=end&maxplex=1',
                    '/download',
                    '.fasta']
        url = preurls[self.serverid]+self.accession+posturls[self.serverid]
        self.parent.updateconsole(url)
        try:
            with urlopen(Request(url)) as response:
                data = response.read()
                temp_seq = data.decode('utf-8')
                if temp_seq.startswith(">"):
                    self.result = temp_seq
                    self.metadata = temp_seq.split(sep='\n',maxsplit=1)[0]
                    self.sequence="".join(temp_seq.split(sep='\n',maxsplit=1)[1].split('\n'))
                    self.parent.updateconsole("Obtained "+self.metadata+" successfully")
                else:
                    raise HTTPError(url,404,"","",response)
        except HTTPError as error:
            self.parent.updateconsole('Accession Id error (or) try another server')
        except:
            self.parent.updateconsole('Unknown Error occured, check your internet connection')
