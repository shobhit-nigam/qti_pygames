prices = {'aa':3, 'bb':6.2, 'dd':8, 'ff':4.3, 'yy':1}
gst = 0.18

newPrices = {k:v*(1+gst) for k, v in prices.items()}
print(newPrices)
