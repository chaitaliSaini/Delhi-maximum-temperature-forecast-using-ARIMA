library(zoo)
library(xts)
library(astsa)

#read data from csv file
dat<- read.csv("add file path",header=TRUE)

#create xts object for our data
x <- xts(dat$Temp, as.Date(dat$Date, format='%d-%m-%Y'))
mylen <- length(x)


#create differenced,log data 
dlx <- diff(log(x))
dlx<-dlx[2:mylen]
d2lx<-diff(dlx)
ddlx <- diff(d2lx,12)
ddlx<-ddlx[14:length(ddlx)]
#ddlx is stationary, hence d=2,D=1
#to plot ddlx use plot(ddlx)


#analyze acf2 plot to infer arima model
acf2(ddlx,max.lag=36)
#To determine p and q, we will analyse the ACF and PACF plots between lag 1 to lag 12. ACF cuts off at lag 2 and PACF is geometric. Hence,we can say that p=0 and q=2.
#For P and Q, we will consider lag 12, lag 36, lag 48. ACF tails off and PACF is significant till lag 1. Therefore, P=1 and Q=0.
sarima(x,p=0,d=2,q=2,P=1,D=1,Q=0,S=12)


#forecasting 
par(mfrow=c(1,2))
sarima.for(x, n.ahead=8, 0,2,2,1,1,0,12)
plot(x)

