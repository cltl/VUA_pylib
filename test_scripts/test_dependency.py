#!/usr/bin/env python


from NafParserPy import NafParser
from VUA_pylib.feature_extractor.constituency import Cconstituency_extractor
from VUA_pylib.feature_extractor.dependency import Cdependency_extractor

file='naf_examples/10007YRK-H1B1-2SFM-K2HY.txt_8795bbbd2f30103f0ef2f098a183c457.naf'

naf_obj = NafParser(file)


extractor = Cdependency_extractor(naf_obj)
sp = extractor.get_shortest_path('t446','t453')
print sp


sp2 = extractor.get_shortest_path_spans(['t444','t445','t446'], ['t451','t452','t454'])
print sp2


print 'Path to root', extractor.get_path_to_root('t460')


print 'Path to root for span',extractor.get_shortest_path_to_root_span(['t444','t445','t446'])
#extractor = Cconstituency_extractor(naf_obj)
#===============================================================================
# print extractor.get_deepest_phrase_for_termid('t363')
# print extractor.get_path_for_termid('t363')
# print extractor.get_deepest_phrase_for_termid('t359')
# print extractor.get_path_for_termid('t359')
# print extractor.get_deepest_phrase_for_termid('t567')
# print extractor.get_path_for_termid('t567')
# print extractor.get_deepest_phrase_for_termid('t717')
# print extractor.get_path_for_termid('t717')
#===============================================================================

#print extractor.get_path_from_to('t363','t365')



