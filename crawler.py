import pandas
import numpy
import sklearn
import matplotlib.pyplot as plt
import math
import json
import io
import os
import glob

cumul = None

for dirpath,_,filenames in os.walk('.'):
    for f in filenames:
        fullpath = os.path.abspath(os.path.join(dirpath, f))
        if fullpath.endswith('.csv'):
            if cumul is None:
                kickstart_data = pandas.read_csv(fullpath)
                cumul = (kickstart_data[kickstart_data['category'].str.contains('\"id\":35,')])
            else:
                kickstart_data = pandas.read_csv(fullpath)
                games_item = (kickstart_data[kickstart_data['category'].str.contains('\"id\":35,')])
                cumul = cumul.append(games_item)


f = open("output.txt","w+")

f.write("number of video game projects: "+ str(cumul.shape[0]))
f.write('\n')

success = (cumul[cumul['state'].str.contains('successful')])
f.write("successful video game projects: "+ str(success.shape[0]))
f.write('\n')

live = (cumul[cumul['state'].str.contains('live')])
f.write("live video game projects: "+ str(live.shape[0]))
f.write('\n')

failed = (cumul[cumul['state'].str.contains('failed')])
f.write("failed video game projects: "+ str(failed.shape[0]))
f.write('\n')

f.write("average goal: "+ str(cumul['goal'].mean()))
f.write('\n')

f.write("median goal: "+ str(cumul['goal'].median()))
f.write('\n')

f.write("goal std: "+ str(cumul['goal'].std()))
f.write('\n')

f.write("average usd pledged: "+ str(cumul['usd_pledged'].mean()))
f.write('\n')

f.write("median usd pledged: "+ str(cumul['usd_pledged'].median()))
f.write('\n')

f.write("usd pledged std: "+ str(cumul['usd_pledged'].std()))
f.write('\n')

