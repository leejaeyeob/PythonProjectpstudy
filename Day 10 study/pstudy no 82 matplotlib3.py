from matplotlib import font_manager, rc
import matplotlib.pyplot as plt

font_path = 'C:/windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
figure = plt.figure()
axes = figure.add_subplot(111)
data = [0.18, 0.3, 3.33, 3.75, 0.38, 25, 0.25, 2.75, 0.1]
vitamin = ['비타민A, 비타민b1, 비타민b2, 나이아신, 비타민 b6, 비타민 C, 비타민D, 비타민 E, 엽산']
axes.pie(data, labels=vitamin, autopct='%0.1f%')
plt.axis('equal')
plt.show()