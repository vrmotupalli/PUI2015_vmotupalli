import numpy as np
import pylab as pl
import json
import random as rd
import scipy.stats as ss
    
#distributions = ['pois', 'gaus', 'chisq', 'cauchy', 'lnorm', 'binomial']
distributions = ['poisson','gaussian','chisq','cauchy','lnorm','binomial']



s = json.load( open('fbb_matplotlibrc.json') )
pl.rcParams.update(s)

#standardize mean, define degrees of freedom
mymean=100
df = 100
# mysize with random. 100 samples N>10, N<2000
mysize = rd.sample(range(10,2000),100)

distlist = {}
for dist in distributions:
    distlist[dist]={}

#Distributions with inputs based on Googling the calls
for x in mysize:
    distlist['poisson'][x]=np.random.poisson(mymean, x)
    distlist['normal'][x] = np.random.normal(mymean,10,x)
    distlist['binomial'][x] = np.random.binomial(mymean*2,0.5,x)
    distlist['chisq'][x] = np.random.chisquare(df,x)
    distlist['cauchy'][x] = np.random.standard_cauchy(x)
    distlist['lnorm'][x] = np.random.lognormal(mymean,1,x)

#holding array for means
means = []

for dist in distlist:
    plotMeanN = pl.figure(figsize=(6,6))
    #adding based on peer input
    axesMeanN = plotMeanN.add_subplot(111)
    for n in distlist[dist]:
        means.append(distlist[dist][n].mean())
        axesMeanN.plot(n,distlist[dist][n].mean(),'o')
        axesMeanN.set_xlabel('sample size')
        axesMeanN.set_ylabel('sample mean')
        axesMeanN.set_title(dist)
        axesMeanN.plot([min(mysize), max(mysize)], [mymean,mymean], 'k')
        
print (len(means))
n, bins, patches = pl.hist(means, bins=100, normed=1)
pl.ylabel('N')
pl.xlabel('sample mean')
pl.title('Sample Means')
x = np.linspace(97,103,100)

#ss.norm.fit from class code
param = ss.norm.fit(means)
y = ss.norm.pdf(bins, param[0], param[1])
pl.plot(bins,y,'r-')