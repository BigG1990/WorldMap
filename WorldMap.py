#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 11:00:15 2019

@author: damon
"""

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from matplotlib.colors import LogNorm

#==================#
# Global parameter #
#==================#
idx_s = 175
idx_z = 10

#=============#
# Load tracks #
#=============#
ACE_lats=np.array([-33.9024 , -38.0369 , -44.5091 , -46.8753 , -46.7229 , -46.1047 ,
       -46.3842 , -50.2683 , -49.9485 , -52.5406 , -54.1096 , -54.5985 ,
       -52.7971 , -48.47355, -44.0407 , -46.5003 , -55.4176 , -64.8098 ,
       -67.1287 , -66.4431 , -65.5069 , -67.2894 , -67.3738 , -69.8776 ,
       -72.22965, -73.52455, -69.89435, -68.1734 , -62.5036 , -56.5064 ,
       -53.1702 , -53.1702 , -52.8889 , -54.99375, -54.2875 , -54.0173 ,
       -56.9832 , -59.4945 , -57.38   , -54.4213 , -50.4777 , -43.9803 ,
       -34.67905,       np.nan, -33.9039 , -21.5382 , -12.1014 ,  -3.06179,
         5.04944,  14.2767 ,  25.60195,  36.0928 ,  45.8072 ,  52.0774 ])
ACE_lons=np.array([  18.40976643,   22.45141667,   34.79678924,   37.86928846,
         38.00975035,   50.41168078,   52.39482639,   69.62534063,
         70.36508293,   75.17915649,   89.42023194,  104.54176111,
        120.0629021 ,  136.00286111,  146.99726056,  150.25317014,
        149.09291958,  146.42597569,  145.01187847,  146.22682986,
        157.62468531,  163.79808897,  -98.5648513 , -163.13398601,
       -136.95090278, -127.36486667, -108.29423776,  -84.44825278,
        -67.54585804,  -68.15531042,  -70.91222535,  -70.9067    ,
        -67.49659719,  -51.48373299,  -36.698725  ,  -36.38735739,
        -28.11534653,  -23.85471748,   -6.56622031,    3.32160792,
          7.60149544,   14.1604809 ,   17.2637566 ,   18.4233    ,
         18.3529007 ,    7.30036115,   -0.21689359,   -7.46936528,
        -13.81697326,  -17.99820833,  -18.90991458,  -15.47450801,
         -8.18479808,    2.65225088])

## ANT-XXVIII/5 ##
ANT28_lats=np.array([-53.13 , -49.818, -44.888, -39.908, -35.038, -30.23 , -24.006,
       -18.674, -12.988,  -6.69 ,  -0.936,   5.784,  11.494,  18.672,
        24.6  ,  28.14 ,  35.06 ,  40.658,  47.51 ])
ANT28_lons = np.array([-70.86 , -64.624, -57.836, -50.736, -44.104, -39.   , -37.434,
       -33.746, -30.296, -27.308, -25.144, -23.54 , -22.392, -21.46 ,
       -19.696, -15.42 , -12.926, -12.05 ,  -7.406])

## PS106 ##
PS106_lats = np.array([ 53.566826,  66.709496,  79.313952,  81.934188,  81.94028 ,
        81.872459,  81.798569,  80.852954,  78.251938,  76.204432,
        79.836701,  81.412169,  82.848827,  83.475407,  81.326312,
        79.410802,  73.707278])
PS106_lons = np.array([  8.555055,   2.551779,   8.419633,  10.295058,  10.288847,
        10.4545  ,  11.286242,  10.580766,  15.12248 ,  23.8961  ,
        31.091287,  32.617813,  32.806479,  27.91433 ,  16.929063,
        27.859356,  24.328301])

#=================================================#
# World Map - TROPOS cloud group CCN/INP activity #
#=================================================#
plt.figure(figsize=(12,12))
plt.grid(True)

m = Basemap(projection='robin',lon_0=0,resolution='c')
m.drawcoastlines()
m.drawparallels(np.arange(-80.,81.,60.),labels=[0,0,0,0],color='grey',fontsize=15)
m.drawmeridians(np.arange(-180.,181.,60.),labels=[0,0,0,0],color='grey',fontsize=15)
m.fillcontinents(alpha=0.4)

#=========#
# Melpitz #
#=========#
x0, y0= m(12.94, 51.53)
pl.scatter(x0, y0, s=idx_s, zorder=idx_z, marker='+',color='red') # CCN only

#=======#
# PS106 #
#=======#
x1, y1 = m(PS106_lons, PS106_lats)
#x1, y1 = m(32.385551, 83.716529)
plt.scatter(x1, y1, s=idx_s, zorder=idx_z, marker='.',color='#fb9a99')

#=======================#
# RACEPAK (Tuktoyaktuk) #
#=======================#
x2, y2 = m(-133.05, 69.48)
plt.scatter(x2, y2, s=idx_s, zorder=idx_z, marker='+', color='#a6cee3') # CCN only

#========================================#
# AEROCLOUD (Princess Elisabeth station) #
#========================================#
x3, y3 = m(23.35, -71.95)
plt.scatter(x3, y3, s=idx_s, zorder=idx_z, marker='+', color='#1f78b4') # CCN only

#=====#
# ACE #
#=====#
x4, y4 = m(ACE_lons, ACE_lats) #ACE-cruise
plt.scatter(x4, y4, s=idx_s, zorder=idx_z, marker='.', color='#b2df8a') # CCN & INP

#====================#
# CARRIBA (Barbados) #
#====================#
x5, y5 = m(-59.432906, 13.163726)
plt.scatter(x5, y5, s=idx_s, zorder=idx_z, marker='+', color='#33a02c') # CCN only

#=========#
# Beijing # 
#=========#
x6, y6 = m(116.3072, 39.9889) 
plt.scatter(x6, y6, s=idx_s, zorder=idx_z, marker='+', color='red') # CCN only?

#====================#
# Ice cores (Marcus) #
#====================#
x7, y7 = m(-38.47, 72.5737)
plt.scatter(x7, y7, s=idx_s, zorder=idx_z, marker='^', color='#e31a1c') # INP only
x8, y8 = m(17.4331, 78.8233)
plt.scatter(x8, y8, s=idx_s, zorder=idx_z, marker='^', color='#e31a1c')

#=========#
# PAMACIP #
#=========#
x9, y9 = m(-16.6667, 81.6)
plt.scatter(x9, y9, s=idx_s, zorder=idx_z, marker='^', color='#fdbf6f') # INP only

#=================#
# A-LIFE (Cyprus) #
#=================#
x10, y10 = m(32.4833, 34.7167)
plt.scatter(x10, y10, s=idx_s, zorder=idx_z, marker='.', color='#ff7f00') # CCN & INP

#=============#
# MarParCloud #
#=============#
x11, y11 = m(-24.8672, 16.8636)
plt.scatter(x11, y11, s=idx_s, zorder=idx_z, marker='.', color='#cab2d6') # CCN & INP

#====================================================#
# Arctic filters (Alert, Ny-Alesund, Barrow, Villum) #
#====================================================#
x12, y12 = m(-62.3667, 82.5) # Alert
plt.scatter(x12, y12, s=idx_s, zorder=idx_z, marker='^', color='#6a3d9a') # INP only
x13, y13 = m(11.9167, 78.9167) # Ny-Alesund
plt.scatter(x13, y13, s=idx_s, zorder=idx_z, marker='^', color='#6a3d9a') # INP only
x14, y14 = m(-156.7667, 71.3) # Barrow
plt.scatter(x14, y14, s=idx_s, zorder=idx_z, marker='^', color='#6a3d9a') # INP only
x15, y15 = m(-16.6667, 81.6) # Villum
plt.scatter(x15, y15, s=idx_s, zorder=idx_z, marker='^', color='#6a3d9a') # INP only

#======================#
# PICNIC (Puy de Dome) #
#======================#
x16, y16 = m(2.9658, 45.7722)
plt.scatter(x16, y16, s=idx_s, zorder=idx_z, marker='^', color='#ffed6f') # INP only

#===================================================#
# ANT-XXVIII/5 (Punta Arenas - Bremerhaven) in 2011 #
#===================================================#
x17, y17 = m(ANT28_lons, ANT28_lats)
plt.scatter(x17, y17, s=idx_s, zorder=idx_z, marker='+', color='#b15928') # CCN only

#========================================#
# ACORES #
#========================================#
x25, y25 = m(-28.,39.) 
plt.scatter(x25, y25, s=idx_s, zorder=idx_z, marker='+', color='#1fb4a6') # CCN only

## legend
plt.scatter(np.nan, np.nan, s=idx_s, zorder=idx_z, color='k', marker='^', label='INP only')
plt.scatter(np.nan, np.nan, s=idx_s, zorder=idx_z, color='k', marker='+', label='CCN only')
plt.scatter(np.nan, np.nan, s=idx_s, zorder=idx_z, color='k', marker='.', label='CCN & INP')
plt.legend(loc='best', markerscale=0.5, title='Measurements')

plt.savefig('world_map.pdf', dpi=600, orientation='portrait', bbox_inches='tight',transparent='true');
print('world_map.png'+' saved')
plt.show() 