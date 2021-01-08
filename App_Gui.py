import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar 
import matplotlib.pyplot as plt 
from Model.GraficaComparasion import DiffusionTrendComparison
from ProfileTreshold import *
from Profile import *
from Threshold import * 
from MakeGrap import *


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'SIMULACIÓN'
        self.left = 0
        self.top = 0
        self.width = 1300
        self.height = 1200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.setStyleSheet("color: blue;"
                        "background-color: green;"
                        "selection-color: yellow;"
                        "selection-background-color: blue;")
        self.show()
    
class MyTableWidget(QWidget):
    
    def loadTabs(self):
        self.tabs = QTabWidget()
        # self.tabG1 = QWidget()
        # self.tabG2 = QWidget()
        # self.tabG3 = QWidget()
        # self.tabG4 = QWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        # self.tab6 = QWidget()
        self.tabs.resize(300,200)

        # self.tabs.addTab(self.tabG1,"Grafo Barabaási-Albert")       
        # self.tabs.addTab(self.tabG2, "Grafo Erdos-Rényi")
        # self.tabs.addTab(self.tabG3,"Grafo Watts y Strogatz")
        # self.tabs.addTab(self.tabG4,"Grafo Facebook")
        
        self.tabs.addTab(self.tab1,"Simulacion")
        self.tabs.addTab(self.tab2,"Barabási–Albert")
        self.tabs.addTab(self.tab3,"Erdös–Rényi")
        self.tabs.addTab(self.tab4,"Watts y Strogatz")
        self.tabs.addTab(self.tab5,"Facebook")
        # self.tabs.addTab(self.tab6,"Mapa de calor")

        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("INICIAR SIMULACIÓN")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)

        # Tab para Graph
        # self.figureG1 = plt.figure() 
        # self.canvasG1 = FigureCanvas(self.figureG1) 
        # self.toolbarG1 = NavigationToolbar(self.canvasG1, self) 
        # self.tabG1.layout = QVBoxLayout(self)
        # self.tabG1.layout.addWidget(self.toolbarG1) 
        # self.tabG1.layout.addWidget(self.canvasG1) 
        # self.tabG1.setLayout(self.tabG1.layout)


        # Graficsa para Fig 1
        self.figure = plt.figure() 
        self.canvas = FigureCanvas(self.figure) 
        self.toolbar = NavigationToolbar(self.canvas, self) 
        self.pushButton1.clicked.connect(self.graficas_barabasabi)         
        self.tab2.layout = QVBoxLayout(self)
        self.tab2.layout.addWidget(self.toolbar) 
        self.tab2.layout.addWidget(self.canvas) 
        self.tab2.setLayout(self.tab2.layout)

        # Graficsa para Fig 2
        self.figure2 = plt.figure() 
        self.canvas2 = FigureCanvas(self.figure2) 
        self.toolbar2 = NavigationToolbar(self.canvas2, self) 
        self.tab3.layout = QVBoxLayout(self)
        self.tab3.layout.addWidget(self.toolbar2) 
        self.tab3.layout.addWidget(self.canvas2) 
        self.tab3.setLayout(self.tab3.layout)

        # # Graficsa para Fig 3
        self.figure3 = plt.figure() 
        self.canvas3 = FigureCanvas(self.figure3) 
        self.toolbar3 = NavigationToolbar(self.canvas3, self) 
        self.tab4.layout = QVBoxLayout(self)
        self.tab4.layout.addWidget(self.toolbar3) 
        self.tab4.layout.addWidget(self.canvas3) 
        self.tab4.setLayout(self.tab4.layout)

        # # Graficsa para Facebook
        self.figure4 = plt.figure() 
        self.canvas4 = FigureCanvas(self.figure4) 
        self.toolbar4 = NavigationToolbar(self.canvas4, self) 
        self.tab5.layout = QVBoxLayout(self)
        self.tab5.layout.addWidget(self.toolbar4) 
        self.tab5.layout.addWidget(self.canvas4) 
        self.tab5.setLayout(self.tab5.layout)

        self.AddGraphs()
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        self.loadTabs()
    
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
    
    # def plotGraphs(self):
        


    def AddGraphs(self):

        self.ax1 = self.figure.add_subplot(221)
        self.ax2 = self.figure.add_subplot(222)         
        self.ax3 = self.figure.add_subplot(223)         
        self.ax4 = self.figure.add_subplot(224) 

        self.ax11 = self.figure2.add_subplot(221)
        self.ax12 = self.figure2.add_subplot(222)         
        self.ax13 = self.figure2.add_subplot(223)         
        self.ax14 = self.figure2.add_subplot(224)

        self.ax21 = self.figure3.add_subplot(321)
        self.ax22 = self.figure3.add_subplot(322)         
        self.ax23 = self.figure3.add_subplot(323)         
        self.ax24 = self.figure3.add_subplot(324)  
        self.ax25 = self.figure3.add_subplot(325)         
        self.ax26 = self.figure3.add_subplot(326) 

        self.ax31 = self.figure4.add_subplot(321)
        self.ax32 = self.figure4.add_subplot(322)         
        self.ax33 = self.figure4.add_subplot(323)         
        self.ax34 = self.figure4.add_subplot(324)  
        self.ax35 = self.figure4.add_subplot(325)         
        self.ax36 = self.figure4.add_subplot(326)          

    def graficas_barabasabi(self):
        print('Inicio de Simulación')
        # self.ag1 = self.figureG1.add_subplot(111)
        # G = nx.petersen_graph()
        # nx.draw(G, with_labels=True, font_weight='bold')
        # nx.draw_shell(G,with_labels=True, font_weight='bold')
        # self.canvasG1.draw_idle()

        g = make_graph(1)
        self.graficar(0.05, 0.1, 0.1, 0, 0, g, "Fig 1 a).png", self.ax1)
        self.graficar(0.05, 0.4, 0.1, 0, 0, g, "Fig 1 b).png", self.ax2)
        self.graficar(0.05, 0.8, 0.1, 0, 0, g, "Fig 1 c).png", self.ax3)
        self.graficar(0.05, 0.4, 0.2, 0, 0, g, "Fig 1 d).png", self.ax4)
    
        g2 = make_graph(2)
        self.graficar(0.05, 0.1, 0.1, 0, 0, g2, "Fig 2 a).png", self.ax11)
        self.graficar(0.05, 0.4, 0.1, 0, 0, g2, "Fig 2 b).png", self.ax12)
        self.graficar(0.05, 0.8, 0.1, 0, 0, g2, "Fig 2 c).png", self.ax13)
        self.graficar(0.05, 0.4, 0.2, 0, 0, g2, "Fig 2 d).png", self.ax14) 

        g3 = make_graph(3)
        self.graficar(0.05, 0.1, 0.1, 0, 0, g3, "Fig 3 a).png", self.ax21)
        self.graficar(0.05, 0.4, 0.1, 0, 0, g3, "Fig 3 b).png", self.ax22)
        self.graficar(0.05, 0.8, 0.1, 0, 0, g3, "Fig 3 c).png", self.ax23)
        self.graficar(0.05, 0.4, 0.2, 0, 0, g3, "Fig 3 d).png", self.ax24)    
        self.graficar(0.05, 0.4, 0.3, 0, 0, g3, "Fig 3 e).png", self.ax25)
        self.graficar(0.05, 0.4, 0.4, 0, 0, g3, "Fig 3 f).png", self.ax26) 

        g4 = make_graph_db('facebook-wall.txt.anon', 'Facebook')
        self.graficar(0.05, 0.1, 0.1, 0, 0, g, "Fig 4 a).png", self.ax31)
        self.graficar(0.05, 0.4, 0.1, 0, 0, g, "Fig 4 b).png", self.ax32)
        self.graficar(0.05, 0.8, 0.1, 0, 0, g, "Fig 4 c).png", self.ax33)
        self.graficar(0.05, 0.4, 0.2, 0, 0, g, "Fig 4 d).png", self.ax34)    
        self.graficar(0.05, 0.4, 0.3, 0, 0, g, "Fig 4 e).png", self.ax35)
        self.graficar(0.05, 0.8, 0.2, 0, 0, g, "Fig 4 f).png", self.ax36)

        self.canvas.draw()

    def graficar(self, if_seed, profile, threshold, p, a, g, name, pl):
        m1, t1, it1 = make_pt_graph_simulation(if_seed, profile, threshold, p, a, g)
        m2, t2 = make_p_graph_simulation(if_seed, profile, p, a, g)
        m3, t3 = make_t_graph_simulation(if_seed, threshold, p, a, g)
        viz = DiffusionTrendComparison([m1, m2, m3],[t1, t2, t3], plt = pl)
        viz.plot(filename=name)    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())