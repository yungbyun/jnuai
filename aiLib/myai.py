import numpy as np # 수학 연산 수행을 위한 모듈
import pandas as pd # 데이터 처리를 위한 모듈
import seaborn as sns # 데이터 시각화 모듈
import matplotlib.pyplot as plt # 데이터 시각화 모듈

# 다양한 분류 알고리즘 패키지를 임포트함.
from sklearn.linear_model import LogisticRegression  # Logistic Regression 알고리즘
#from sklearn.cross_validation import train_test_split # 데이타 쪼개주는 모듈

from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier  # for K nearest neighbours
from sklearn import svm  #for Support Vector Machine (SVM) Algorithm
from sklearn import metrics #for checking the model accuracy
from sklearn.tree import DecisionTreeClassifier #for using Decision Tree Algoithm

class MyDataFrame: #gildong
    data_frame = 0

    def load_csv(self, f):
        # CSV 파일 읽어오기
        self.data_frame = pd.read_csv(f)

    def show_file_info(self):
        self.data_frame.info()

    def show_head(self):
        print(self.data_frame.head())

    def show_col_name(self):
        for col in self.data_frame.columns:
            print(col)

    def show_cols(self):
        print(self.data_frame.columns)

    def show_hist(self):
        self.data_frame.hist(edgecolor='black', linewidth=1.2)
        fig = plt.gcf()
        fig.set_size_inches(12, 10)
        plt.show()

    def plot(self, a, b, c):
        # 읽어온 데이터 표시하기
        cl = self.data_frame[c].unique()

        col = ['orange', 'blue', 'red', 'yellow', 'black', 'brown']

        fig = self.data_frame[self.data_frame[c] == cl[0]].plot(kind='scatter', x=a, y=b, color=col[0], label=cl[0])

        for i in range(len(cl) - 1):
            self.data_frame[self.data_frame[c] == cl[i + 1]].plot(kind='scatter', x=a, y=b, color=col[i + 1], label=cl[i + 1],
                                                        ax=fig)
        fig.set_xlabel(a)
        fig.set_ylabel(b)
        fig.set_title(a + " vs. " + b)
        fig = plt.gcf()
        fig.set_size_inches(10, 6)
        plt.show()

    def show_boxplot(self, a, b):
        f, sub = plt.subplots(1, 1, figsize=(8, 6))
        sns.boxplot(x=self.data_frame[a], y=self.data_frame[b], ax=sub)
        sub.set(xlabel=a, ylabel=b)
        plt.show()

    def show_violenplot(self, a, b):
        plt.figure(figsize=(8, 6))
        plt.subplot(1, 1, 1)
        sns.violinplot(x=a, y=b, data=self.data_frame)
        plt.show()

    def show_heatmap(self):
        plt.figure(figsize=(12, 8))
        sns.heatmap(self.data_frame.corr(), annot=True, cmap='cubehelix_r')
        plt.show()

    def prepare_data(self, input_cols, target_col, ratio):
        train, test = train_test_split(self.data_frame, test_size=ratio)
        # train=70% and test=30%
        print(train.shape)
        print(test.shape)

        # 학습용 문제, 학습용 정답
        train_X = train[input_cols]  # 키와 발크기만 선택
        train_y = train[target_col]  # 정답 선택

        # 테스트용 문제, 테스트용 정답
        test_X = test[input_cols]  # taking test data features
        test_y = test[target_col]  # output value of test data
        return train_X, train_y, test_X, test_y

    def drop(self, col):
        self.data_frame.drop(col, axis=1, inplace=True)

    def show_unique(self, col):
        print(self.data_frame[col].unique())

    def to_numeric(self, col, m, new_col):
        self.data_frame[new_col] = self.data_frame[col].map(m)


class MyModel: #youngja
    train_X = []
    train_y = []

    test_X = []
    test_y = []

    def set_data(self, i, j, k, l):
        self.train_X = i
        self.train_y = j
        self.test_X = k
        self.test_y = l

    def run_SVM(self):
        gildong = svm.SVC()
        gildong.fit(self.train_X, self.train_y)  # 가르친 후
        prediction = gildong.predict(self.test_X)  # 얼마나 맞히는지 테스트

        rate1 = metrics.accuracy_score(prediction, self.test_y) * 100
        print('인식률: {0:.1f}'.format(rate1))


    def run_LR(self):
        cheolsu = LogisticRegression()
        cheolsu.fit(self.train_X, self.train_y)
        prediction = cheolsu.predict(self.test_X)

        rate2 = metrics.accuracy_score(prediction, self.test_y) * 100
        print('인식률: {0:.1f}'.format(rate2))


    def run_DT(self):
        youngja = DecisionTreeClassifier()
        youngja.fit(self.train_X, self.train_y)
        prediction = youngja.predict(self.test_X)

        rate3 = metrics.accuracy_score(prediction, self.test_y) * 100
        print('인식률: {0:.1f}'.format(rate3))

    def run_NN(self):
        minsu = KNeighborsClassifier(n_neighbors=3)  # this examines 3 neighbours for putting the new data into a class
        minsu.fit(self.train_X, self.train_y)
        prediction = minsu.predict(self.test_X)

        rate4 = metrics.accuracy_score(prediction, self.test_y) * 100
        print('인식률: {0:.1f}'.format(rate4))


from abc import *
class MachineLearning(metaclass = ABCMeta):
    df = MyDataFrame()
    model = MyModel()

    input_cols = 0
    target_col = 0
    file_name = 0

    @abstractmethod
    def set_file(self):
        pass

    def load_csv(self):
        self.df.load_csv(self.file_name)

    def show_info(self):
        self.df.show_file_info()
        self.df.show_cols()

    def visualize(self):
        # self.df.show_hist()
        # self.df.show_boxplot('Species', 'SepalWidthCm')
        pass

    @abstractmethod
    def set_input_cols(self):
        pass

    @abstractmethod
    def set_target_col(self):
        pass

    def prepare_data(self):
        a, b, c, d = self.df.prepare_data(self.input_cols, self.target_col, 0.4)
        self.model.set_data(a, b, c, d)

    def run_models(self):
        self.model.run_LR()
        self.model.run_DT()
        self.model.run_NN()
        self.model.run_SVM()

    @abstractmethod
    def preprocess(self):
        pass

    def run(self):
        self.set_file()

        # (1) 데이터 로드
        self.load_csv()
        # (2) 데이터 정보 표시
        self.show_info()

        self.preprocess()

        # (3) 데이터 시각화
        self.visualize()

        self.set_input_cols()
        self.set_target_col()

        # (4) 학습/테스트 데이터 준비하기
        self.prepare_data()
        # (5) 머신러닝 모델 실행하기
        self.run_models()


class Application:
    @staticmethod
    def run(ml):
        ml.run()

