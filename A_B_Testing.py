import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro


pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

control_group = pd.read_excel("datasets/ab_testing_data.xlsx", sheet_name="Control Group")
test_group = pd.read_excel("datasets/ab_testing_data.xlsx", sheet_name="Test Group")

def grafik_manager(parameter1, parameter2):
    plt.scatter(parameter1, parameter2),
    plt.xlabel("Purchase"),
    plt.ylabel("Earning")
    return plt.show()

# Yönetici için hazırlanabilecek satın alım/kazanç grafikleri
grafik_manager(control_group["Purchase"], control_group["Earning"])

grafik_manager(test_group["Purchase"], test_group["Earning"])

# Etkileşim, tıklanma gibi metirklerin değerlendirilmesi
def grafik1_ekip(parameter1, parameter2):
    plt.scatter(parameter1, parameter2)
    plt.xlabel("Impression")
    plt.ylabel("Purchase")
    return plt.show()

grafik1_ekip(control_group["Impression"], control_group["Purchase"])
grafik1_ekip(test_group["Impression"], test_group["Purchase"])

def grafik2_ekip(parameter1, parameter2):
    plt.scatter(parameter1, parameter2)
    plt.xlabel("Click")
    plt.ylabel("Purchase")
    return plt.show()

grafik2_ekip(control_group["Click"], control_group["Purchase"])
grafik2_ekip(test_group["Click"], test_group["Purchase"])

############################
# 1. Varsayım Kontrolü
############################

# 1.1 Normallik Varsayımı
# 1.2 Varyans Homojenliği

############################
# 1.1 Normallik Varsayımı
############################

# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1:..sağlanmamaktadır.


test_istatistigi, pvalue = shapiro(control_group["Purchase"])
print('Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue))

#control_group normallik varsayımı için p value değeri 0.05  ten büyük
#o halde varsayım H0 varsayımı reddedilemez

test_istatistigi, pvalue = shapiro(test_group["Purchase"])
print('Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue))
#test_group normallik varsayımı için pvalue değeri 0.05 ten büyük
#o halde varsayım H0 varsayımı reddedilemez


############################
# 1.2 Varyans Homojenligi Varsayımı
############################

# H0: Varyanslar Homojendir
# H1: Varyanslar Homojen Değildir

from scipy import stats

stats.levene(control_group["Purchase"],test_group["Purchase"])

#pvalue değeri = 0.108, 0.05 ten büyüktür varyanslar homojendir

############################
# 2. Hipotezin Uygulanması
############################

test_istatistigi, pvalue = stats.ttest_ind(control_group["Purchase"],
                                           test_group["Purchase"],
                                           equal_var=True)

print('Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue))

#pvalue değeri=0.3493, 0.05ten büyük
## H0: M1 = M2 (iki grup ortalamaları arasında istatistiksel olarak anlamlı bir fark yoktur.)

