import numpy as np
import pylab as pl
import json
import random as rd
import scipy.stats as ss
import sys
"""
H0 = % of former prisoners employed in an unsubsidized job after release is the same
or lower for program participants and control group, p=0.05
"""

alpha=0.05
#control group percent
P_0=52.1*0.01 
#program group percent
P_1=53.3*0.01

#control group
n_0=409
#program group
n_1=564

#lets get the counts by multiplying by the sample size
Nt_0=P_0*n_0
Nt_1=P_1*n_1

#define the sample proportion first
sp=(P_0*n_0+P_1*n_1)/(n_1+n_0)
print ('Sample Proportion = %s' % (sp))

sp_stdev= lambda p, n: np.sqrt( p * ( 1 - p ) /n[0] +  p * ( 1 - p )/n[1]  )


sp_stdev_2y=sp_stdev((Nt_0+Nt_1)/(n_0+n_1),[n_0,n_1])
"""
no need to print, just kept for my ref
print ((P_0, n_0, n_1, sp_stdev_2y))
"""


zscore = lambda p0, p1, s : (p0-p1)/s
z_2y = zscore(P_1, P_0, sp_stdev_2y)
print ('Z score = %s' % (z_2y))

#z table gives me P = 0.6443 for z =0.37

p_2y=1-0.6443


def report_result(p,a):
    print ('is the p value {0:.2f} smaller than the critical value {1:.2f}? ')
    if p<a:
        print ("YES!")
    else: print ("NO!")
    
    print ('the Null Hypothesis is') 
    print ('rejected' if p<a  else 'not rejected') 

    
report_result(p_2y, alpha)

## p is less than alpha, fail to reject H0 ##

"""
Chi-Squared test
H0 = employment rates for the program group is equal to  control group 
for six consecutive months
"""

Ntot = 973
expected = 564*409*131.579*841.429
sample_values = [[.147*564,.853*564],[.119*409,.881*409]]
 
chisqstat= lambda N, values, expect : N*((values[0][0]*values[1][1]-values[0][1]*values[1][0])**2)/(expect)

print (chisqstat(Ntot,  sample_values, expected))

# Table gives me 3.84 at DF = 1, alpha = 0.05

## Chi^2 is less than table, fail to reject H0




