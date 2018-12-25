import numpy as np
import math
import matplotlib.pyplot as plt

infile = open("gmm.txt")
x = infile.read().splitlines()
x = [float(x) for x in x]
#print str(min(a))+ " , "+ str(max(a))
#print a
#print len(a)
itern = 100

p = np.zeros((itern,2))
mu = np.zeros((itern,2))
sigm = np.zeros((itern,2))
pr_tem = [0]*itern
pr = [0]*itern

p[0,0] = 0.2
p[0,1] = 0.8
mu[0,0] = 0.
mu[0,1] = 6.
sigm[0,0] = 10.
sigm[0,1] = 10.

q = np.zeros((len(x),2))

for i in range (len(x)):
    for k in range(2):
        pr_tem [0] += p[0,k]*math.exp(math.pow((x[i]-mu[0,k]),2)/(-2*math.pow(sigm[0,k],2)))/math.sqrt(2*math.pi*math.pow(sigm[0,k],2))
    pr[0] = pr[0] + math.log(pr_tem[0])
for t in range(1,itern):
    denum_tem =0.
    q_sum = [0.]*2
    mu_num = [0.]*2
    sig_num = [0.]*2
    q_denum = 0.
    for i in range(len(x)):
        for k in range(2):
            denum_tem += p[t-1,k]*math.exp(math.pow((x[i]-mu[t-1,k]),2)/(-2*math.pow(sigm[t-1,k],2)))/math.sqrt(2*math.pi*math.pow(sigm[t-1,k],2))
        for k in range(2):
            q[i,k] = (p[t-1,k]*math.exp(math.pow((x[i]-mu[t-1,k]),2)/(-2*math.pow(sigm[t-1,k],2)))/math.sqrt(2*math.pi*math.pow(sigm[t-1,k],2)))/denum_tem
            q_sum[k] += q[i,k]
            q_denum += q[i,k]
            mu_num[k] += q[i,k]*x[i]
            sig_num[k] += q[i,k]*math.pow((x[i]-mu[t-1,k]),2)
    for k in range(2):
        p[t,k] = q_sum[k]/q_denum
        mu[t,k] = mu_num[k]/q_sum[k]
        sigm[t,k] = sig_num[k]/q_sum[k]
        print "p= "+str(p[t,k])+",   mu= "+str(mu[t,k])+ ",   sigma= "+str(sigm[t,k])
    for i in range(len(x)):
        for k in range(2):
            pr_tem [t] += p[t,k]*math.exp(math.pow((x[i]-mu[t,k]),2)/(-2*math.pow(sigm[t,k],2)))/math.sqrt(2*math.pi*math.pow(sigm[t,k],2))
        pr[t] = pr[t] + math.log(pr_tem[t])
index=[]
for i in range(100):
    index.append(i+1)

plt.plot(index,pr,linewidth="4")
#plt.ylim((0,400))
print "\nLog-likelihood: \n"
print pr
plt.show()  
print "\nInitializations: \n"  
print "pa= ",p[0,0]
print "pb= ",p[0,1]
print "ma= ",mu[0,0]
print "mb= ",mu[0,1]
print "sigma_a= ",sigm[0,0]
print "sigma_b= ",sigm[0,1]


      