from operator import itemgetter
import sys
import cPickle



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
    
    def get_label(self):
        return self.label
    
    def get_features(self):
        for name,value in self.features:
            yield name,value
            
    def get_all_features(self):
        return self.features
    
    
class Cfeature_index:
    def __init__(self):
        self.idx = {}
    
    def get_number_feat(self,feat):
        return self.idx.get(feat,None)
    
    def add_feat(self,feat):
        num_feat = len(self.idx)+1
        self.idx[feat] = num_feat
        return num_feat
        
        
    def compose_feat(self,name,value):
        return name+'###'+value
    
    
    def __encode_features(self,feats,modify_index=True):
        feats_for_example = {}
        clean_feats = ''
        for name, value in feats:
            my_feat = self.compose_feat(name, value)
            clean_feats+=my_feat+' '
            num_feat = self.get_number_feat(my_feat)
            if num_feat is None:
                if modify_index:
                    num_feat = self.add_feat(my_feat)
            
            if num_feat is not None:
                if num_feat in feats_for_example:
                    feats_for_example[num_feat] += 1
                else:
                    feats_for_example[num_feat] = 1
        return sorted(feats_for_example.items(),key=itemgetter(0)),clean_feats
         
            
    def encode_feature_file_to_svm(self,feat_file_obj,out_fic=sys.stdout):
        for example in feat_file_obj:
            class_label = example.get_label()
            out_fic.write(class_label)
            feats_for_example, clean_feats =self.__encode_features(example.get_all_features())
                                                                   
            for feat,freq_feat in feats_for_example:
                value = freq_feat
                out_fic.write(' %d:%d' % (feat,value))
            out_fic.write(' #'+clean_feats.encode('utf-8')+'\n')
            
    def encode_example_for_classification(self, feats,out_fic,my_class='0'):
        feats_for_example, clean_feats =self.__encode_features(feats,modify_index=False)
        out_fic.write(my_class)
        for feat,freq_feat in feats_for_example:
                value = freq_feat
                out_fic.write(' %d:%d' % (feat,value))
        out_fic.write(' #'+clean_feats.encode('utf-8')+'\n')        
    
    def save_to_file(self,filename):
        fic = open(filename,'wb')
        cPickle.dump(self.idx, fic, protocol=0)
        fic.close()
        
    def load_from_file(self,filename):
        fic = open(filename,'rb')
        self.idx = cPickle.load(fic)
        fic.close()

                
    
class Cfeature_file:
    def __init__(self,filename=None):
        self.filename = filename

    def __iter__(self):
        if self.filename is not None:
            fic = open(self.filename,'r')
            for line in fic:
                if line[0] != '#':
                    yield Cexample(line.decode('utf-8'))
            fic.close()
    
   
              
            