import urllib2
import urllib
import sys
import time

try:
    from lxml import etree
except:
    import xml.etree.cElementTree as etree

class Citem:
    def __init__(self,item=None):
        self.hits = None
        self.word = None
        self.tokens = None
        if item is not None:
            if isinstance(item,str):
                self.load_from_string(item)
            else:
                self.load_from_item_node(item)
            
    def load_from_string(self,line):
        ## Example line: 22865,"de server van"
        line = line.strip()
        pos = line.find(',')
        self.hits = int(line[:pos])
        self.word = line[pos+2:-1]
        self.tokens = self.word.split(' ')
        
    def load_from_item_node(self,item_node):
        hits_node = item_node.find('hits')
        if hits_node is not None:
            self.hits = int(hits_node.text)
        
        word_node = item_node.find('word')
        if word_node is not None:
            self.word = str(word_node.text)
            self.tokens = self.word.split(' ')
            
    def __str__(self):
        if self.word is not None and self.hits is not None:
            s = str(self.tokens)+' ->'+str(self.hits)+' hits'
        else:
            s = 'None'
        return s
    
    def __repr__(self):
        return self.__str__()
    
    def get_hits(self):
        return self.hits
    
    def get_word(self):
        return self.word
    
    def get_tokens(self):
        return self.tokens
    

class Cgoogle_web_nl:
    def __init__(self):
        self.url='http://www.let.rug.nl/gosse/bin/Web1T5_freq.perl'
        self.sleep_this_time = 5	#First time to sleep in case of error
        self.max_trials = 20        
        self.limit = 1000
        self.min_freq = 100
        self.items = []
            
    
    def set_limit(self,l):
        if not isinstance(l, int):
            print>>sys.stderr,'Parameter for set_min_freq must be an integer and not ',type(m)
            sys.exit(-1)
        self.limit = l
        
    def set_min_freq(self,m):
        if not isinstance(m, int):
            print>>sys.stderr,'Parameter for set_min_freq must be an integer and not ',type(m)
            sys.exit(-1)
        self.min_freq = m
    
    def query(self,this_query,fixed='shown'):
        #http://www.let.rug.nl/gosse/bin/Web1T5_freq.perl?
        #query=interessante%20*&
        #mode=XML&limit=10000&
        #threshold=40&optimize=on&wildcards=listed+normally
        #&fixed=shown&.cgifields=debug&.cgifields=optimize
        dict_params = {}
        dict_params['query'] = this_query
        dict_params['mode']='XML'
        #dict_params['mode']='csv'
        dict_params['limit']=self.limit
        dict_params['threshold']=self.min_freq
        dict_params['optimize']='on'
        dict_params['wildcards']='listed normally'
        dict_params['fixed']=fixed
        dict_params['.cgifields']='debug'
        dict_params['.cgifields']='optimize'
        params = urllib.urlencode(dict_params)
        #print>>sys.stderr,self.url+'?%s' % params
        
        
        done = False
        this_url = None
        trials = 0
        while not done:
            try:
                this_url = urllib2.urlopen(self.url+'?%s' % params)   
                code = this_url.getcode()
            except Exception as e:
                code = -1
                print>>sys.stderr,str(e)

            if code == 200:                
                done = True
            else:
                print>>sys.stderr,'Got an error (code '+str(code)+') querying google web nl, with "'+this_query+'", retrying...'
                print>>sys.stderr,'Trial ',trials,' waiting ',self.sleep_this_time,'seconds'
                time.sleep(self.sleep_this_time)
                trials += 1
                self.sleep_this_time += 1
                if trials == self.max_trials:
                    print>>sys.stderr,'Maximum number of trials reached. Giving up...'
                    done = True
                    this_url = None
        
        if this_url is not None:
            if dict_params['mode'] == 'XML':
                xml_obj = etree.parse(this_url)
                this_url.close()

                for item_node in xml_obj.findall('item'):
                    self.items.append(Citem(item_node))
                del xml_obj
            else: #CSV
                first_line = True
                ## The first line is frequency,"N-gram"
                for line in this_url:
                    if not first_line:
                        self.items.append(Citem(line))
                    first_line = False                
                
    
    
    def get_items(self):
        for item in self.items:
            yield item
            
    def get_all_items(self):
        return self.items
    
    def len(self):
        return len(self.items)
    def __iter__(self):
        for item in self.items:
            yield item
