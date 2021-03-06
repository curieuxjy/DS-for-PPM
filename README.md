# DS-for-PPM
Basic Education of Data Science for Production Process Monitoring
```
(국가 경쟁력 강화를 위한 소재∙부품∙장비 산업 전문인력 양성과정)
데이터 사이언스 분야 생산공정 모니터링 이미지 처리 기법 강의 및 관련 실습
- 오유근(홍익대학교 기계시스템디자인공학과 교수)
- 기간: 2020.02.12(수)~02.14(금) 09:00~18:00

교육내용 :
- 데이터 사이언스 개요
- 실시간 생산장비 데이터 취득 및 저장 기법
- 데이터 변환 및 가시화 기법, 데이터 분석 및 머신 러닝 기법
- 생산공정 모니터링 관련 이미지 처리 기법, 딥러닝을 활용한 이미지 분석 기법
 
실습교육 :
- 실시간 데이터 취득 및 저장 기법
- 머신러닝 활용 데이터베이스 데이터 분석
- 딥러닝 활용 생산공정 이미지 데이터 분석
- Spyder 사용
```
- - -
## Day 1
- Python review
- Data acquistion
    - Website data scraping (image, 일기예보, 실시간주가)
    - IMU(Inertial Measurement Unit) data
    <img src="./day1/1.png" width="70%" height="70%"></img>

### Code List
|Content|Code|
|-|-|
|Python basic(Spyder)|[Code](./day1/untitled0.py)|
|Call by reference, Scope of variable|[Code](./day1/untitled1.py)|
|Class(OOP)|[Code](./day1/untitled2.py)|
|Image practice 1|[Code](./day1/untitled3.py)|
|Image practice 2|[Code](./day1/untitled4.py)|
|Weather forecasting practice 1|[Code](./day1/untitled5.py)|
|Weather forecasting practice 2|[Code](./day1/untitled6.py)|
|Current stock price practice 1|[Code](./day1/untitled7.py)|
|Timer|[Code](./day1/untitled8.py)|
|Current stock price practice 2*|[Code](./day1/untitled9.py)|
|IMU toy code|[Code](./day1/untitled10.py)|
|IMU data plotting|[Code](./day1/untitled11.py)|

### Reference Link
- [Python underscore](https://mingrammer.com/underscore-in-python/)
- [Python file reading](http://pythonstudy.xyz/python/article/206-%ED%8C%8C%EC%9D%BC-%EB%8D%B0%EC%9D%B4%ED%83%80-%EC%B2%98%EB%A6%AC)
- [Timer](https://stackoverflow.com/questions/3393612/run-certain-code-every-n-seconds)
- [Android Sensor data](https://developer.android.com/guide/topics/sensors/sensors_motion?hl=ko)
- [Android Sensor APP - Sensorstream IMU+GPS](https://play.google.com/store/apps/details?id=de.lorenz_fenster.sensorstreamgps)

- - -
## Day 2
- Database programming (SQL)
- Machine Learning
    - Supervised learning: regression, classification
    - (Optional) Unsupervised learning: clustering, PCA
    <img src="./day2/sqlite-sample-database-diagram.PNG" width="70%" height="70%"></img>

### Code List
|Content|Code|
|-|-|
|SQL SELECT|[Code](./day2/untitled0.py)|
|SQL INSERT|[Code](./day2/untitled1.py)|
|StockPrice DB|[Code](./day2/untitled2.py)|
|Linear Regression|[Code](./day2/untitled3.py)|
|Moving Error|[Code](./day2/untitled4.py)|
|Body Weight vs. Brain Weight|[Code](./day2/untitled5.py)|
|Multivariate Linear Regression|[Code](./day2/untitled6.py)|
|Polynomial Regression|[Code](./day2/untitled7.py)|
|Ridge Regression|[Code](./day2/untitled8.py)|
|Time-Series Estimation|[Code](./day2/untitled9.py)|



### Reference Link
- [Spyder plotting in a New window](https://talkingaboutme.tistory.com/entry/ML-Spyder%EB%82%B4%EC%97%90%EC%84%9C-plot%EC%9D%84-new-window%EC%97%90-%ED%95%98%EA%B8%B0)
- [DataSet Source](https://people.sc.fsu.edu/~jburkardt/datasets/regression/regression.html)
- [MRNet](https://stanfordmlgroup.github.io/projects/mrnet/)
- [SQL tutorials](http://w3school.com/)
- [SQL reference site](https://www.w3schools.com/sql/default.asp)
- [SQL Python](http://pythonstudy.xyz/python/article/204-SQLite-%EC%82%AC%EC%9A%A9)
- [Machine Learning youtube](https://youtu.be/0_lKUPYEYyY)
- [Autoregression Models for Time Series Forecasting With Python](https://machinelearningmastery.com/autoregression-models-time-series-forecasting-python/)
- [11 Classical Time Series Forecasting Methods in Python (Cheat Sheet)](https://machinelearningmastery.com/time-series-forecasting-methods-in-python-cheat-sheet/)

- - -

## Day 3
- OpenCV 활용한ML
- Team project: rock vs paper Classification (1 Hour Limted)
<img src="./day3/1.png" width="70%" height="70%"></img>

### Code List
|Content|Code|
|-|-|
|OpenCV image test code|[Code](./day3/untitled0.py)|
|OpenCV video test code|[Code](./day3/untitled1.py)|
|Image Crop|[Code](./day3/untitled2.py)|
|Video Recording|[Code](./day3/untitled3.py)|
|Video Capture|[Code](./day3/untitled4.py)|
|Resize Video|[Code](./day3/untitled5.py)|
|Mouse Control|[Code](./day3/untitled6.py)|
|Boxing|[Code](./day3/untitled7.py)|
|Resize & Move Window|[Code](./day3/untitled8.py)|
|ROI|[Code](./day3/untitled9.py)|
|Drag and Capture|[Code](./day3/untitled10.py)|
|GreyScale Comparison(raw&module)|[Code](./day3/untitled11.py)|
|Image Comparison|[Code](./day3/untitled12.py)|
|Image Subtraction|[Code](./day3/untitled13.py)|
|Motion Difference Video|[Code](./day3/untitled14.py)|
|Image Threshold 1|[Code](./day3/untitled15.py)|
|Image Threshold 2|[Code](./day3/untitled16.py)|
|Otsu Algorithm|[Code](./day3/untitled17.py)|
|Adaptive Threshold|[Code](./day3/untitled18.py)|
|Perspective Transform|[Code](./day3/untitled19.py)|
|Matching|[Code](./day3/untitled20.py)|
|Hough Cricle|[Code](./day3/untitled21.py)|
|Perceptron|[Code](./day3/untitled22.py)|
|Logistic Regression|[Code](./day3/untitled23.py)|
|Support Vector Machine|[Code](./day3/untitled24.py)|
|KNN 1|[Code](./day3/untitled25.py)|
|KNN 2|[Code](./day3/untitled26.py)|
|SVD|[Code](./day3/untitled27.py)|
|Final Team Project|[Code](./day3/project.py)|

### Reference Link
- [OpenCV Codes(파이썬으로 만드는 OpenCV 프로젝트)](./day2/insightbook.opencv_project_python-master)
- [ip web cam](https://stackoverflow.com/questions/49978705/access-ip-camera-in-python-opencv)
- [opencv documentation](https://opencv-python.readthedocs.io/en/latest/#)
- [ipdb 사용](http://pythonstudy.xyz/python/article/505-Python-%EB%94%94%EB%B2%84%EA%B9%85-PDB)
- [Python Convex Optimization](https://cvxopt.org/)
- [Scikit-learn Classification](https://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html?highlight=random%20forest)
- [Gaussian Process](https://www.slideshare.net/JungkyuLee1/gaussian-processes)
- [SVD](https://www.fun-coding.org/recommend_basic6.html)

