
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class App(QMainWindow):
    """ Creates a new application window """
    def __init__(self):
        super().__init__()

        self.title = 'Stet pyQt'

        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.statusBar().showMessage('Initialized Stet')
        self.show()


if __name__ == '__main__':
    """ Creates application and window """
    app = QApplication(sys.argv)
    ex = App()

    import zmq

    context = zmq.Context()

    print('connecting to server')
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    for request in range(10):
        print("Sending request %s …" % request)
        socket.send(b"Hello")

        #  Get the reply.
        message = socket.recv()
        print("Received reply %s [ %s ]" % (request, message))


    sys.exit(app.exec_())
