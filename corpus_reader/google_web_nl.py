import urllib
import sys

try:
    from lxml import etree
except:
    import xml.etree.cElemenTree as etree

class Citem:
    def __init__(self,item_node=None):
        self.hits = None
        self.word = None
        self.tokens = None
        if item_node is not None:
            self.load_from_item_node(item_node)
            
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
    
    def get_hits(self):
        return self.hits
    
    def get_word(self):
        return self.word
    
    def get_tokens(self):
        return self.tokens
    

class Cgoogle_web_nl:
    def __init__(self):
        self.url='http://www.let.rug.nl/gosse/bin/Web1T5_freq.perl'
        self.limit = 10000
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
    
    def query(self,this_query):
        #http://www.let.rug.nl/gosse/bin/Web1T5_freq.perl?
        #query=interessante%20*&
        #mode=XML&limit=10000&
        #threshold=40&optimize=on&wildcards=listed+normally
        #&fixed=shown&.cgifields=debug&.cgifields=optimize
        dict_params = {}
        dict_params['query'] = this_query
        dict_params['mode']='XML'
        dict_params['limit']=self.limit
        dict_params['threshold']=self.min_freq
        dict_params['optimize']='on'
        dict_params['wildcards']='listed normally'
        dict_params['fixed']='shown'
        dict_params['.cgifields']='debug'
        dict_params['.cgifields']='optimize'
        params = urllib.urlencode(dict_params)
        
        this_url = urllib.urlopen(self.url+'?%s' % params)       
        xml_obj = etree.parse(this_url)
        this_url.close()

        for item_node in xml_obj.findall('item'):
            self.items.append(Citem(item_node))
        del xml_obj
    
    def get_items(self):
        for item in self.items:
            yield item
            
