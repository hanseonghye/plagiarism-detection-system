import itertools
import os
import subprocess
import networkx as nx
import matplotlib.pyplot as plt


def match_score_local(a,b):
    data=subprocess.check_output(('./source/lcs_pro',a,b))
    #print data
    return int(data)


def get_sequence_from(filename):
    #print('get sequence from ' + filename + '...')
    ps = subprocess.Popen(('./source/lex_pro', filename), stdout=subprocess.PIPE)
    string = subprocess.check_output(('./source/re_pro'), stdin=ps.stdout)
    ps.wait()
    return string


