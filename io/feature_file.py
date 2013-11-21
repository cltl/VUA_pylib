
class Cexample:
    def __init__(self,str_line=None):
        self.label = ''
        self.features = []
        if str_line is not None:
            self.load_from_line(str_line)
        
    def load_from_line(self,str_line):
        fields = str_line.strip().split('\t')
        self.label = fields[0]
        for feat in fields[1:]:
            first_equal = feat.find('=')
            if first_equal != -1:
                name = feat[:first_equal]
                value = feat[first_equal+1:]
                self.features.append((name,value))

    def __str__(self):
        s  = 'Label: '+self.label+'\n'
        s += 'Feats: '+str(self.features) 
        return s
    
    
    
class Cfeature_file:
    def __init__(self,filename=None):
        self.filename=filename


    def __iter__(self):
        if self.filename is not None:
            fic = open(self.filename,'r')
            for line in fic:
                yield Cexample(line)
            fic.close()
            
     
            
              
            