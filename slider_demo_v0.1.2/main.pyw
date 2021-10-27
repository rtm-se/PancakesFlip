from mainwindow import MainWindow
from slider import Slider

main_win = MainWindow()
slider = Slider(main_win.WIN)

if __name__ == '__main__':

    main_win.main_loop(slider)
