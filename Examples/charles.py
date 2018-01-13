import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import math
from astropy.io import fits
import gc
import matplotlib.cm as cm
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


def zoom(data, factor, centerpt):
   wid = data.shape[0]
   hgt = data.shape[1]
   cenx = wid / factor
   ceny = hgt / factor
   newwid = wid / factor
   newhgt = hgt / factor
   plt.imshow(data[(cenx - newwid/factor):(cenx + newwid/factor), (ceny - newhgt/factor):(ceny + newhgt/factor)])


def coadd_stdev(basefn, startnum, ndrcount, xx, yy, wid, hgt):
   sd = 0.0000
   sn = startnum 

   # create pedestal
   print('Creating PEDESTAL')
   tempfn = basefn + str(sn) + '.fits'
   sn += 1
   print(tempfn)
   pp = (fits.getdata(tempfn))[xx:xx+wid,yy:yy+hgt]
   pp.shape
   for ii in range(ndrcount-1):
     tempfn = basefn + str(sn+ii) + '.fits'
     print(tempfn)
     pp += (fits.getdata(tempfn))[xx:xx+wid,yy:yy+hgt] 

   # create signal
   print('\nCreating SIGNAL')
   sn = startnum+ndrcount
   tempfn = basefn + str(sn) + '.fits'
   sn += 1
   print(tempfn)
   ss = (fits.getdata(tempfn))[xx:xx+wid,yy:yy+hgt]
   for ii in range(ndrcount-1):
     tempfn = basefn + str(sn+ii) + '.fits'
     print(tempfn)
     ss += (fits.getdata(tempfn))[xx:xx+wid,yy:yy+hgt]

   # create coadd
   cc = pp - ss
   # divide coadd by ndrcount
   print('Mean of coadd before applying divisor:' + str(np.mean(cc)))
   cc = cc / ndrcount
   print('Mean of coadd after applying divisor:' + str(np.mean(cc)))
   sd = np.std(cc)
   print('Standard Deviation of coadd after applying divisor:' + str(sd))
   return sd 

def coadd(basefn, startnum, ndrcount):
   sn = startnum

   # create pedestal
   print('Creating PEDESTAL')
   tempfn = basefn + str(sn) + '.fits'
   sn += 1
   print(tempfn)
   pp = (fits.getdata(tempfn))
   pp.shape
   for ii in range(ndrcount-1):
     tempfn = basefn + str(sn+ii) + '.fits'
     print(tempfn)
     pp += (fits.getdata(tempfn))

   # create signal
   print('\nCreating SIGNAL')
   sn = startnum+ndrcount
   tempfn = basefn + str(sn) + '.fits'
   sn += 1
   print(tempfn)
   ss = (fits.getdata(tempfn))
   for ii in range(ndrcount-1):
     tempfn = basefn + str(sn+ii) + '.fits'
     print(tempfn)
     ss += (fits.getdata(tempfn))

   # create coadd
   cc = pp - ss
   # divide coadd by ndrcount
   print('Mean of coadd before applying divisor:' + str(np.mean(cc)))
   cc = cc / ndrcount
   print('Mean of coadd after applying divisor:' + str(np.mean(cc)))
   print('\n\n')
   return cc



def ndrtest(basefn):
   startnum = 1
   xx = [100,  200,  0,	   50] 
   yy = [0,    0,    0,	   100]
   wid = [40,  40,   40,   20]
   hgt = [4,   4,    4,	   20]

   ndrs = [1,4,9,16,25,36]
   plc = ["b-o", "g-o", "r-o", "c-o"]
   pli = ['m-o', 'y-o', 'k-o', '#008000']

   plt.clf()
   coadds = np.zeros((len(ndrs),2048,2048))
   for ii in range(len(ndrs)):
      coadds[ii,:,:] = coadd(basefn, startnum, ndrs[ii])

   sd = np.zeros((len(xx),len(ndrs)), dtype=np.float)

   print("\nGot coadded images, processing subarrays...\n")
   for suba in range(len(xx)):  # len(xx) is the number of subarrays we've defined in xx, yy, wid, hgt
      for ii in range(len(ndrs)):
	 subarray = coadds[ii, xx[suba]:xx[suba]+wid[suba],yy[suba]:yy[suba]+hgt[suba]]
         sd[suba,ii] = np.std(subarray)
      print(sd[suba,:])
      lbl = 'Real ' + str(suba)
      plt.plot(ndrs, sd[suba,:], plc[suba], label=lbl)

   print("\nPrinting ideals for 7, 6, 5...\n")
   
   ideal = [5.0, 6.0, 7.0, 7.5] 
   for ii in range(len(ideal)):
      ideal_sd = [ideal[ii], ideal[ii]/2, ideal[ii]/3, ideal[ii]/4, ideal[ii]/5, ideal[ii]/6]
#      line = plt.plot(ndrs, ideal_sd)
      lbl = 'Ideal '+str(ideal[ii])
      plt.plot(ndrs, ideal_sd, pli[ii], label=lbl)


   plt.legend(loc='upper right', numpoints = 1);
   plt.xlabel("NDRs (data taken at 1, 4, 9, 16, 25, and 36 NDRs)")
   plt.ylabel("Noise in ADU (conversion is 2e-/ADU)")
   plt.title("Read Noise with NDRs, (darks taken with a bias of 213 mV)")
   plt.grid(True)
   

def ndrtest3(basefn):
   startnum = 1
   xx = [100,  200,  0]
   yy = [0,    0,    0]
   wid = [40,  40,   40]
   hgt = [4,   4,    4]

   ndrs = [1,4,9,16,25,36]

   plt.clf()
   coadds = np.zeros((len(ndrs),2048,2048))
   for ii in range(len(ndrs)):
      coadds[ii,:,:] = coadd(basefn, startnum, ndrs[ii])

   sd = np.zeros(len(ndrs), dtype=np.float)

   print("\nGot coadded images, processing subarrays...\n")
   for suba in range(len(xx)):  # len(xx) is the number of subarrays we've defined in xx, yy, wid, hgt
      for ii in range(len(ndrs)):
         subarray = coadds[ii, xx[suba]:xx[suba]+wid[suba],yy[suba]:yy[suba]+hgt[suba]]
         sd[ii] = np.std(subarray)
      print(sd)
      plt.plot(ndrs, sd)
      plt.plot(ndrs, sd, 'ro')

   print("\nPrinting ideals for 7, 6, 5...\n")

   ideal = np.float(7)
   sd = [ideal, ideal/2, ideal/3, ideal/4, ideal/5, ideal/6]
   plt.plot(ndrs, sd)
   plt.plot(ndrs, sd, 'ro')
   ideal = np.float(6)
   sd = [ideal, ideal/2, ideal/3, ideal/4, ideal/5, ideal/6]
   plt.plot(ndrs, sd)
   plt.plot(ndrs, sd, 'ro')
   ideal = np.float(5)
   sd = [ideal, ideal/2, ideal/3, ideal/4, ideal/5, ideal/6]
   plt.plot(ndrs, sd)
   plt.plot(ndrs, sd, 'ro')
   plt.xlabel("NDRs (data taken at 1, 4, 9, 16, 25, and 36 NDRs)")
   plt.ylabel("Noise in ADU (conversion is 2e-/ADU)")
   plt.title("Read Noise with NDRs, (darks taken with a bias of 213 mV)")
   plt.grid(True)



def ndrtest2(basefn):
   startnum = 1
   xx = [100,  200,  0] 
   yy = [0,    0,    0]
   wid = [40,  40,   40]
   hgt = [4,   4,    4]

   ndrs = [1,4,9,16,25,36]
#   sd = np.zeros((3,6))
#   for suba in range(3):
#      for ii in range(6):
#	 sd[suba,ii] = coadd(basefn, startnum, ndrs[ii], xx[suba], yy[suba], wid[suba], hgt[suba])
#	 plt.plot(sd[0,0:5], ndrs) 
   sd = np.zeros(6)
   for suba in range(3):
      for ii in range(6):
	 sd[ii] = coadd_stdev(basefn, startnum, ndrs[ii], xx[suba], yy[suba], wid[suba], hgt[suba])
      plt.plot(ndrs, sd)

   return sd


def ramp2(basefn, startnum, imgcount, xx, yy, wid, hgt):
   mms = np.zeros(shape=(imgcount))  # could also use np.empty
   
   tempfn = basefn + str(startnum) + '.fits'
   pp = (fits.getdata(tempfn))[xx:xx+wid,yy:yy+hgt];
   ii = startnum+1
   while ii < imgcount:
      tempfn = basefn + str(startnum+ii) + '.fits'
      ss = (fits.getdata(tempfn))[xx:xx+wid,yy:yy+hgt]
      cc = pp-ss
      pp = ss
      sd = np.std(cc)
      mms[ii] = sd
      ii = ii+1
   return mms

def ramp1(basefn, startnum, imgcount, xx, yy, wid, hgt):
   mms = np.zeros(shape=(imgcount))  # could also use np.empty
   
   tempfn = basefn + str(startnum) + '.fits'
   pp = fits.getdata(tempfn);
   ii = startnum+1
#   for ii in range(imgcount):
   while ii < imgcount:
      tempfn = basefn + str(startnum+ii) + '.fits'
      ss = fits.getdata(tempfn)
      cc = pp-ss
      sd = np.std(cc[xx:xx+wid,yy:yy+hgt])
      mms[ii] = sd
      ii = ii+1
   return mms

def get_means_from_ramp(basefn, startnum, imgcount, jump, xx, yy, wid, hgt):
   mns = np.zeros(shape=(imgcount/jump))  # could also use np.empty
   ii = 0
#   for ii in range(imgcount):
   jj = 0
   while ii < imgcount:
      tempfn = basefn + str(startnum+ii) + '.fits'
      print(tempfn)
      ss = fits.getdata(tempfn)
      mns[jj] = np.mean(ss[xx:xx+wid,yy:yy+hgt])
      ii = ii+jump
      jj = jj+1
   return mns


def get_medians_from_ramp(basefn, startnum, imgcount, xx, yy, wid, hgt):
   mns = np.zeros(shape=(imgcount))  # could also use np.empty
   ii = 0
#   for ii in range(imgcount):
   while ii < imgcount:
      tempfn = basefn + str(startnum+ii) + '.fits'
      print(tempfn)
      ss = fits.getdata(tempfn)
      mns[ii] = np.median(ss[xx:xx+wid,yy:yy+hgt])
      ii = ii+1
   return mns


def getdata(basefn, startnum, imgcount, jump):
   readcount = imgcount/jump
   data = np.zeros(shape=(readcount,2048,2048))
   ii = startnum
   jj = 0
   while ii < imgcount:
      fname = basefn + str(ii) + '.fits'
      print(fname)
      data[jj,:,:] = fits.getdata(fname)
      ii = ii + jump
      jj = jj + 1
   return data

def getx(count):
   x = np.zeros(shape=(count))
   for ii in range(count):
      x[ii] = ii+1
   return x

def fntest(pm, line=0):
   print(pm)
   print(line)

def getpixeldata(data, col, row):
   pd = data[:,col,row]
   return pd

def plotmxplusb1(polyfitresults, length):
   xx = getx(length)
   ln = polyfitresults[0] * xx + polyfitresults[1] 
   plt.plot(ln)
   return ln


def plotmxplusb2(polyfitresults, length):
   xx = getx(length)
   ln = polyfitresults[0][0] * xx + polyfitresults[0][1] 
   plt.plot(ln)
   return ln

def polyfit1(data, length=0):
   if length==0:
      xx = getx(data.shape[0])
      p = np.polyfit(xx, data, 1)
   else:
      xx = getx(length)
      p = np.polyfit(xx, data[0:length], 1)
   return p

def finddeviation(p, a, length, printme=0):
   xx = getx(length)
   ln = p[0]*xx + p[1]
   for ss in range(length):
      dif = a[ss] - ln[ss]
      if printme > 0:
         print(str(dif) + ' : ' + str(a[ss]))
         print('5%: ' + str(0.05*a[ss]))
      if dif >= 0.05*a[ss]:
	 if printme > 0:
	    print('dif at ' + str(ss))
	 return ss
   return -1


def pixelstats1(data, col, row, printme=0):
   xx = getx(data.shape[0])
   p = np.polyfit(xx, data[:,col,row],1)
   if printme > 0:
      print(p)   
   return p[0]

def pixelstats2(data, col, row, pf=10, plotme=0):
   a = getpixeldata(data, col, row)
   if plotme > 0:
      plt.plot(a)
   p = polyfit1(a, pf)
   if plotme > 0:
      ln = plotmxplusb1(p, a.shape[0])
   cutoff = finddeviation(p, a, a.shape[0])
   if plotme > 0:
      if cutoff >= 0:
         plt.axhline(y=a[cutoff])
         plt.axvline(x=cutoff)
      else:
	 plt.axhline(y=a[cutoff])
	 plt.axvline(x=-1)
      plt.axhline(y=a[0])
   welldepth = a[0] - a[cutoff]
   depth = a[0] - a[a.shape[0]-1]
   if plotme > 0:
      print('Well Depth: ' + str(welldepth))
      print('Reset-Saturation: ' + str(depth))
   return (welldepth, depth)


def pixelstats3(data):
   sz = 2048
   ww = np.zeros(shape=(sz,sz))
   dd = np.zeros(shape=(sz,sz))
   row = 0
   while row < sz:
      col = 0
      while col < sz:
	 ww[col,row],dd[col,row] = pixelstats2(data, col, row, pf=20)	 
	 col = col + 1
      row = row + 1
   return (ww,dd)



def writefits(data, fname):
   fdata = np.float32(data)
   hdu = fits.PrimaryHDU()
   hdu.data = fdata
   hdu.writeto(fname)



def arraystats1(data):
   stats = np.array(shape=(2048,2048), dtype=float)
   for y in range(2048):
      print('doing row:' + str(y))
      for x in range(2048):
	 stats[x,y] = pixelstats1(data, x, y, 0)
   return stats


def compare_means(start, end, jump):
   plt.clf()
#   for ii in range(ndrcount-1):
   fnum = start
   while fnum < end:
      fname = 'reboot-000' + str(fnum) + '.Z.'
      print(fname)
      fnum = fnum+1
      print(fname)
      plt.plot(get_means_from_ramp(fname, 0, 800, jump, 0, 0, 2048, 2048))
   print('Done ' + fname)

def compare_medians():
   plt.clf()
#   for ii in range(ndrcount-1):
   fnum = 19
   while fnum < 27:
      fname = 'reboot-000' + str(fnum) + '.Z.'
      print(fname)
      fnum = fnum+1
      print(fname)
      plt.plot(get_medians_from_ramp(fname, 0, 800, 0, 0, 2048, 2048))
   print('Done ' + fname)


def ishell_plot_ramp():
   index = 19
   while index < 21:
      fname = "reboot-000" + str(index) + '.Z.XXX.fits'
      print(fname)
      index = index + 1

def my_format_coord2(x,y):
   data = X
   col = int(x+0.5)
   row = int(y+0.5)
   if col >= 0 and col < numcols and row >=0 and row < numrows:
      z = data[row,col]
      return 'x=%1.4f, y=%1.4f, z=%1.4f'%(x, y, z)
   else:
      return 'x=%1.4f, y=%1.4f'%(x, y)


def showfits(fname):
   data = fits.getdata(fname)
   showdata(data)

def showfitssd(fname, width, height):
   data = fits.getdata(fname)
   showdatasd(data,width,height)


def showdata(data):
   fig = plt.figure()
   ax = fig.add_subplot(311)
   ax.imshow(data, cmap=cm.jet, interpolation='nearest')
   numrows,numcols = data.shape

   def my_format_coord(x,y):
      col = int(x+0.5)
      row = int(y+0.5)
      if col >= 0 and col < numcols and row >=0 and row < numrows:
         z = data[row,col]
         sa = data[row:row+width, col:col+height]
         sd = np.std(sa)
         return 'x=%1.4f, y=%1.4f, z=%1.4f, sd=%1.4f'%(x, y, z, sd)
      else:
         return 'x=%1.4f, y=%1.4f'%(x, y)

   ax.format_coord = my_format_coord
   plt.show()


def showdatasd(data, width, height):
   fig = plt.figure()
   ax = fig.add_subplot(111)
   ax.imshow(data, cmap=cm.jet, interpolation='nearest')
   numrows,numcols = data.shape

   def my_format_coord(x,y):
      col = int(x+0.5)
      row = int(y+0.5)
      if col >= 0 and col < numcols and row >=0 and row < numrows:
         z = data[row,col]
         sa = data[row:row+width, col:col+height]
         sd = np.std(sa)
         return 'x=%1.4f, y=%1.4f, z=%1.4f, sd=%1.4f'%(x, y, z, sd)
      else:
         return 'x=%1.4f, y=%1.4f'%(x, y)

   ax.format_coord = my_format_coord
   plt.show()

def processramp(fn):
   data = getdata(fn, 0, 800, 20)
   ww,dd = pixelstats3(data)
   writefits(ww, 'ww-'+fn+'.fits')
   writefits(dd, 'dd-'+fn+'.fits')

def pixelmask(data, ptf, tbflag):
   print('pixelmask')   



def fitsgrayscale(fn):
   Z = fits.getdata(fn)
   X = np.arange(0,Z.shape[0],1.0)
   Y = np.arange(0,Z.shape[1],1.0)
   X,Y = np.meshgrid(X,Y)
   return X,Y,Z


def jubly(fn):
   X,Y,Z = fitsgrayscale(fn)
   plt.plot_wireframe(X,Y,Z, rstride=15, cstride=15)
   plt.show()



def fits_wireframe(fn):
   fig = plt.figure()
   ax = fig.add_subplot(111, projection='3d')
   X,Y,Z = fitsgrayscale(fn)
   ax.plot_wireframe(X,Y,Z, rstride=15, cstride=15)
   plt.show()
   return Z

def fits_surface(fn):
   fig = plt.figure()
   ax = fig.add_subplot(111, projection='3d')
   X,Y,Z = fitsgrayscale(fn)
   ax.plot_surface(X, Y, Z, rstride=10, cstride=10, cmap=cm.jet)
   plt.show()

#def fits_trisurf(fn):
#   fig = plt.figure()
#   ax = fig.add_subplot(111, projection='3d')
#   X,Y,Z = fitsgrayscale(fn)
#   ax.plot_trisurf(X, Y, Z) #, rstride=10, cstride=10, cmap=cm.jet)
#   plt.show()

def fits_contour(fn):
   fig = plt.figure()
   ax = fig.add_subplot(111, projection='3d')
   X,Y,Z = fitsgrayscale(fn)
   ax.contourf(X, Y, Z, rstride=10, cstride=10, cmap=cm.jet)
   plt.show()



class Annotate(object):
    def __init__(self):
        self.ax = plt.gca()
        self.rect = Rectangle((0,0), 1, 1)
        self.x0 = None
        self.y0 = None
        self.x1 = None
        self.y1 = None
        self.ax.add_patch(self.rect)
        self.ax.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.ax.figure.canvas.mpl_connect('button_release_event', self.on_release)

    def on_press(self, event):
        print 'press'
        self.x0 = event.xdata
        self.y0 = event.ydata

    def on_release(self, event):
        print 'release'
        self.x1 = event.xdata
        self.y1 = event.ydata
        self.rect.set_width(self.x1 - self.x0)
        self.rect.set_height(self.y1 - self.y0)
        self.rect.set_xy((self.x0, self.y0))
        self.ax.figure.canvas.draw()


