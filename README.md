#VUA_pylib#

Library in python with includes several functionalities for dealing with NAF/KAF files

The library is a python package and it is divided into several subpackages

##VUA_pylib.feature_extractors##

Contains functions to extract information from a NAF/KAF file

###VUA_pylib.feature_extractors.constituency###


####class Cconstituency_extractor####

Extract information from the constituency layer in a NAF file

Functions
+ get_deepest_phrase_for_termid(termid) --> gets the deepest phrase for a term identifier
+ get_least_common_subsumer(termid1, termid2) --> gets the least common subsumer of both ids in the constituency tree


###VUA_pylib.feature_extractors.dependency###

####class Cdependency_extractor###

Extract information from the dependency layer in a NAF file

Functions
+ get_shortest_path(term1,term2) --> gets the shortest dependency path from term1 to term2
+ get_shortest_path_spans(span1,span2) --> gets the shortest dependency path between 2 span of term ids
+ get_path_to_root(termid) --> gets the shortest dependency path from the termid to the sentence root
+ get_shortest_path_to_root_span(span) --> gets the shortest dependency path from the span of termids to the sentence root




Contact
------
* Ruben Izquierdo
* Vrije University of Amsterdam
* ruben.izquierdobevia@vu.nl


