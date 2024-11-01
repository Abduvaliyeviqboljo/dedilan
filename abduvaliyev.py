import numpy as np

dmassiv = np.array([1,2,3,4,5,6])
dmassiv2 = np.array([[1,2,3], [4,5,6]])

sum_dmassiv = np.sum(dmassiv)
sum_dmassiv2 = np.sum(dmassiv2)
mean_d1 = np.mean(dmassiv)
mean_d2 = np.mean(dmassiv2)
prod_d1 = np.prod(dmassiv)
prod_d2 = np.prod(dmassiv2)

print("1d massiv:", dmassiv)
print("2d massiv:\n", dmassiv2)
print("1d yig'indisi:", sum_dmassiv)
print("1d o'rtachasi:", mean_d1)
print("1d ko'paytmasi:", prod_d1)
print("2d yig'indisi:", sum_dmassiv2)
print("2d o'rtachasi:", mean_d2)
print("2d ko'paytmasi:", prod_d2)

print("Abduvaliyev Iqboljon")