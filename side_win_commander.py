# This is a Side Win Commander program


from PySide2.QtCore import QIODevice, QStandardPaths, Qt, Slot
from PySide2.QtGui import QWindow, QColor, QIcon
from PySide2.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QCheckBox, QToolButton
from PySide2.QtWidgets import QTabWidget, QTextEdit, QComboBox, QGridLayout, QButtonGroup, QLineEdit, QLabel, QGroupBox
from PySide2 import QtWidgets
import sys
import datetime
from controls3 import *
import win32api, win32con, win32gui, win32clipboard
import win32com.client
import pyautogui

###############################################################

term_title = 'Side Win Commander'

window_min_height = 600
window_min_width = 500

tmpl_default = 'cmd.exe'

msg_1 = 'msg_1'
msg_2 = 'msg_2'

time_stamp = 1            # to add time stamp (1) or not (0)
echo = 0                  # show echo (1) or not (0)
new_line = 1              # set add_time = 1 after receiving '\r' or '\n'

# Names of notebook's tables
tab1Name = 'Basic'
tab2Name = 'USB'
tab3Name = 'ls'
tab4Name = 'cat'
tab5Name = 'AT'
tab6Name = 'dmesg'
tab7Name = 'IP'
tab8Name = 'Edit'

###############################################################

# Tab button [0,1,2,3]:
# 0 - label of the button
# 1 - command to send
# 2 - foreground color
# 3 - background color

# --------------- TAB1 BUTTONS ---------------
T1_0 = [[' ', ' ', '', ''],
       ['root', 'root', '', 'yellow'],
       ['oelinux123', 'oelinux123', '', 'yellow'],
       ['whoami', 'whoami', '', 'light blue'],
       ['who', 'who', '', ''],
       ['id', 'id', '', ''],
       ['hostname', 'hostname', '', ''],
       ['pwd', 'pwd', '', 'light blue'],
       ['ls -l', 'ls -l', '', 'light blue'],
       ['ls -a', 'ls -a', '', 'light blue'],
       ['ls -F', 'ls -F', '', 'light blue'],
       ['df -h', 'df -h', '', 'light blue'],
       ['df -a', 'df -a', '', 'light blue'],
       ['df -x tmpfs', 'df -x tmpfs', '', 'light blue'],
       [' ', '', '', ''],
       ['shutdown -r now', 'shutdown -r now', 'red', ''],
       ['shutdown -h now', 'shutdown -h now', 'red', '']]


T1_1 = [['cat /proc/cpuinfo', 'cat /proc/cpuinfo', '', 'light blue'],
       ['cat /proc/meminfo', 'cat /proc/meminfo', '', ''],
       ['fdisk -l', 'fdisk -l', '', ''],
       [' ', ' ', '', ''],
       ['lsmod', 'lsmod', '', ''],
       ['tree', 'tree', '', '#00dd00'],
       ['echo $PATH', 'echo $PATH', '', 'light blue'],
       [' ', ' ', '', '#33CCCC'],
       ['uptime', 'uptime', '', '#33CCCC'],
       [' ', '', '', '#33CCCC'],
       [' ', ' ', '', ''],
       ['arch', 'arch', '', 'yellow'],
       ['uname -a', 'uname -a', '', 'yellow'],
       ['uname -rs', 'uname -rs', '', 'yellow'],
       ['lsusb', 'lsusb', '', 'yellow'],
       ['lspci', 'lspci', '', 'yellow'],
       ['', '', '', ''],
       ['', '', '', '']]

T1_2 = [['mount', 'mount', '', '#FFB273'],
       ['mount -o remount,rw /', 'mount -o remount,rw /', '', '#FFB273'],
       ['mount -o remount,ro /', 'mount -o remount,ro /', '', '#FFB273'],
       [' ', ' ', '', ''],
       [' ', ' ', '', ''],
       ['', '', '', ''],
       ['cd', 'cd', '', '#33eeCC'],
       ['cd..', 'cd..', '', '#33eeCC'],
       ['cd../..', 'cd../..', '', '#33eeCC'],
       ['', '', '', ''],
       ['', '', '', 'light blue'],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', '#77dd77'],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', '']]

T1 = [T1_0, T1_1, T1_2]


# --------------- TAB2 BUTTONS ---------------
T2_0 = [['Get enable', 'cat /sys/devices/virtual/android_usb/android0/enable', '', ''],
       ['disable USB', 'echo 0 > sys/devices/virtual/android_usb/android0/enable', '', 'red'],
       ['enable USB', 'echo 1 > sys/devices/virtual/android_usb/android0/enable', '', '#77dd77'],
       ['Get VID', 'cat /sys/devices/virtual/android_usb/android0/idVendor', '', ''],
       ['Get PID', 'cat /sys/devices/virtual/android_usb/android0/idProduct', '', ''],
       ['iManufacturer', 'cat /sys/devices/virtual/android_usb/android0/iManufacturer', '', ''],
       ['iProduct', 'cat /sys/devices/virtual/android_usb/android0/iProduct', '', ''],
       ['Get USB functions', 'cat /sys/devices/virtual/android_usb/android0/functions', '', ''],
       ['Get remote_wakeup', 'cat /sys/devices/virtual/android_usb/android0/remote_wakeup', '', ''],
       ['Get USB state', 'cat /sys/devices/virtual/android_usb/android0/state', '', ''],
       ['iSerial', 'cat /sys/devices/virtual/android_usb/android0/iSerial', '', ''],
       [' ', ' ', '', ''],
       ['', '', '', ''],
       [' ', ' ', '', '#FFB273'],
       [' ', ' ', '', '#77dd77'],
       [' ', ' ', '', '#77dd77'],
       [' ', ' ', '', '#77dd77'],
       [' ', ' ', '', '#77dd77'],
       ['', '', '', '']]

T2_1 = [['ls -l .../android0', 'ls -l /sys/devices/virtual/android_usb/android0', '', ''],
       ['ls -l /dev', 'ls -l /dev', '', ''],
       ['ls -l /', 'ls -l /', '', ''],
       [' ', ' ', '', '#bbddbb'],
       ['ls -l /etc/init.d', 'ls -l /etc/init.d', '', ''],
       ['', '', '', ''],
       [' ', ' ', '', ''],
       [' ', ' ', '', ''],
       [' ', ' ', '', ''],
       [' ', ' ', '', ''],
       ['', '', '', ''],
       [' ', ' ', '', ''],
       [' ', ' ', '', ''],
       [' ', ' ', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', '']]

T2_2 = [[' ', ' ', '', ''],
       [' ', ' ', '', ''],
       [' ', ' ', '', ''],
       ['', '', '', ''],
       [' ', ' ', '', ''],
       [' ', ' ', '', ''],
       [' ', ' ', '', ''],
       ['', '', '', ''],
       [' ', ' ', '', ''],
       [' ', ' ', '', ''],
       [' ', ' ', '', ''],
       ['', '', '', ''],
       [' ', ' ', '', ''],
       [' ', ' ', '', ''],
       [' ', ' ', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', '']]

T2 = [T2_0, T2_1, T2_2]


# --------------- TAB3 BUTTONS ---------------
T3_0 = [['cd /', 'cd /', '', ''],
       ['ls -l /bin', 'ls -l /bin', '', ''],
       ['ls -l /dev', 'ls -l /dev', '', ''],
       ['ls -l /etc', 'ls -l /etc', '', ''],
       ['ls -l /sbin', 'ls -l /sbin', '', ''],
       ['ls -l /proc', 'ls -l /proc', '', ''],
       ['ls -l /sys', 'ls -l /sys', '', ''],
       ['ls -l /usr', 'ls -l /usr', '', ''],
       ['ls -l /tmp', 'ls -l /tmp', '', ''],
       ['ls -l /boot', 'ls -l /boot', '', ''],
       ['ls -l /data', 'ls -l /data', '', ''],
       ['ls -l /firmware', 'ls -l /firmware', '', ''],
       ['ls -l /lib', 'ls -l /lib', '', ''],
       ['ls -l /linuxrc', 'ls -l /linuxrc', '', ''],
       ['ls -l /media', 'ls -l /media', '', ''],
       ['ls -l /mnt', 'ls -l /mnt', '', ''],
       ['ls -l /var', 'ls -l /var', '', ''],
       ['ls -l /target', 'ls -l /target', '', '']]

T3_1 = [['ls -l /dev/ttyU*', 'ls -l /dev/ttyU*', '', ''],
       ['ls -l /dev/ttyA*', 'ls -l /dev/ttyA*', '', ''],
       ['ls -l /dev/ttyH*', 'ls -l /dev/ttyH*', '', '#ffbb88'],
       ['ls -l /dev/ttyG*', 'ls -l /dev/ttyG*', '', '#ffbb88'],
       ['ls -l /dev/tty*', 'ls -l /dev/tty*', '', ''],
       [' ', ' ', '', '#ffbb88'],
       [' ', ' ', '', '#ffbb88'],
       [' ', ' ', '', '#ffbb88'],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', '']]

T3_2 = [['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', '']]

T3 = [T3_0, T3_1, T3_2]


# --------------- TAB4 BUTTONS ---------------
T4_0 = [['cat /etc/inittab', 'cat /etc/inittab', '', ''],
       ['cat /proc/cpuinfo', 'cat /proc/cpuinfo', '', ''],
       ['cat /proc/meminfo', 'cat /proc/meminfo', '', ''],
       ['cat /proc/version', 'cat /proc/version', '', ''],
       ['kernel log', 'cat /proc/kmsg', '', ''],
       [' ', ' ', '', '#00dd00'],
       [' ', ' ', '', '#33CCCC'],
       [' ', ' ', '', '#33CCCC'],
       [' ', ' ', '', '#33CCCC'],
       [' ', ' ', '', 'yellow'],
       [' ', ' ', '', 'yellow'],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', '']]

T4_1 = [['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', '']]

T4_2 = [['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', '']]

T4 = [T4_0, T4_1, T4_2]


# --------------- TAB5 BUTTONS ---------------
T5_0 = [['echo -en "AT\r" > /dev/smd10', 'echo -en "AT\r" > /dev/smd10', '', ''],
       ['echo -en "ATI\r" > /dev/smd10', 'echo -en "ATI\r" > /dev/smd10', '', ''],
       ['', '', '', ''],
       ['echo -en "AT+XIIC?\r" > /dev/smd10', 'echo -en "AT+XIIC?\r" > /dev/smd10', '', ''],
       ['echo -en "AT+XIIC=1\r" > /dev/smd10', 'echo -en "AT+XIIC=1\r" > /dev/smd10', '', ''],
       ['echo -en "AT+XIIC=0\r" > /dev/smd10', 'echo -en "AT+XIIC=0\r" > /dev/smd10', '', ''],
       ['echo -en "AT\r" > /dev/smd10', 'echo -en "AT\r" > /dev/smd10', '', ''],
       ['echo -en "AT\r" > /dev/smd10', 'echo -en "AT\r" > /dev/smd10', '', ''],
       ['echo -en "AT\r" > /dev/smd10', 'echo -en "AT\r" > /dev/smd10', '', ''],
       ['echo -en "AT\r" > /dev/smd10', 'echo -en "AT\r" > /dev/smd10', '', ''],
       ['echo -en "AT\r" > /dev/smd10', 'echo -en "AT\r" > /dev/smd10', '', ''],
       ['echo -en "AT\r" > /dev/smd10', 'echo -en "AT\r" > /dev/smd10', '', ''],
       ['echo -en "AT\r" > /dev/smd10', 'echo -en "AT\r" > /dev/smd10', '', ''],
       ['echo -en "AT\r" > /dev/smd10', 'echo -en "AT\r" > /dev/smd10', '', ''],
       ['echo -en "AT\r" > /dev/smd10', 'echo -en "AT\r" > /dev/smd10', '', ''],
       ['echo -en "AT\r" > /dev/smd10', 'echo -en "AT\r" > /dev/smd10', '', ''],
       ['echo -en "AT\r" > /dev/smd10', 'echo -en "AT\r" > /dev/smd10', '', ''],
       ['echo -en "AT\r" > /dev/smd10', 'echo -en "AT\r" > /dev/smd10', '', ''],
       ['', '', '', ''],
       [' ', ' ', '', ''],
       ['', '', '', '']]

T5_1 = [['Get GPS state', 'echo -en "AT\$MYGPSPWR?\r" > /dev/smd10', '', '#33DDCC'],
       ['GPS on', 'echo -en "AT\$MYGPSPWR=1\r" > /dev/smd10', '', '#33DDCC'],
       ['GPS off', 'echo -en "AT\$MYGPSPWR=0\r" > /dev/smd10', '', '#33DDCC'],
       ['', '', '', ''],
       ['Clear GPS Data', 'echo -en "AT+GPSDEL\r" > /dev/smd10', '', '#33DDCC'],
       [' ', ' ', '', '#33DDCC'],
       ['GGA data only', 'echo -en "AT\$MYGPSCFG=2,1\r" > /dev/smd10', '', '#33DDCC'],
       ['RMC data only', 'echo -en "AT\$MYGPSCFG=2,2\r" > /dev/smd10', '', '#33DDCC'],
       ['GSV data only', 'echo -en "AT\$MYGPSCFG=2,4\r" > /dev/smd10', '', '#33DDCC'],
       ['GGA, GSV data', 'echo -en "AT\$MYGPSCFG=2,5\r" > /dev/smd10', '', '#33DDCC'],
       ['All data', 'echo -en "AT\$MYGPSCFG=2,4294967295\r" > /dev/smd10', '', '#33DDCC'],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', '']]

T5_2 = [['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', '']]

T5 = [T5_0, T5_1, T5_2]


# --------------- TAB6 BUTTONS ---------------
T6_0 = [['dmesg', 'dmesg', '', ''],
       ['dmesg | tail -n 20', 'dmesg | tail -n 20', '', ''],
       ['dmesg | grep -i usb', 'dmesg | grep -i usb', '', ''],
       ['dmesg | grep -i tty', 'dmesg | grep -i tty', '', ''],
       [' ', ' ', '', '#00dd00'],
       [' ', ' ', '', '#33CCCC'],
       [' ', ' ', '', '#33CCCC'],
       [' ', ' ', '', '#33CCCC'],
       [' ', ' ', '', 'yellow'],
       [' ', ' ', '', 'yellow'],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', '']]

T6_1 = [['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', '']]

T6_2 = [['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', '']]

T6 = [T6_0, T6_1, T6_2]


# --------------- TAB7 BUTTONS ---------------
T7_0 = [['ifconfig', 'ifconfig', '', ''],
       ['ip help', 'ip help', '', ''],
       ['ip addr show', 'ip addr show', '', ''],
       ['ip link show', 'ip link show', '', ''],
       ['ip neigh show', 'ip neigh show', '', ''],
       ['ip route show', 'ip route show', '', ''],
       [' ', ' ', '', ''],
       ['iwconfig -h', 'iwconfig -h', '', ''],
       ['iwconfig', 'iwconfig', '', ''],
       [' ', ' ', '', ''],
       ['iw help', 'iw help', '', '#33DDCC'],
       ['iw list', 'iw list', '', '#33DDCC'],
       [' ', ' ', '', ''],
       [' ', ' ', '', ''],
       ['', '', '', ''],
       ['iptables -h', 'iptables -h', '', '#33CCCC'],
       ['iptables -L -n -v', 'iptables -L -n -v', '', '#33CCCC'],
       [' ', ' ', '', ''],
       [' ', ' ', '', ''],
       ['', '', '', ''],
       ['', '', '', '']]

T7_1 = [['ping -c 4 ya.ru', 'ping -c 3 ya.ru', '', ''],
       ['ping -c 4 google.com', 'ping -c 3 google.com', '', ''],
       ['ping -c 4 8.8.8.8', 'ping -c 4 8.8.8.8', '', ''],
       [' ', ' ', '', ''],
       ['traceroute ya.ru', 'traceroute ya.ru', '', '#ffbb88'],
       ['traceroute google.com', 'traceroute google.com', '', '#ffbb88'],
       ['traceroute 8.8.8.8', 'traceroute 8.8.8.8', '', '#ffbb88'],
       [' ', ' ', '', ''],
       [' ', ' ', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', '']]

T7_2 = [['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', ''],
       ['', '', '', '']]

T7 = [T7_0, T7_1, T7_2]


# --------------- TAB8 BUTTONS ---------------
T8 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.hndl = None
        self.setWindowTitle(term_title)
        self.statusBar().showMessage('Welcome!')
        # central widget
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        # self.setMinimumSize(window_min_width, window_min_height)
        hbox = QHBoxLayout(centralWidget)
        # create vbox
        vbox = QVBoxLayout()
        # add vbox to main window
        hbox.addLayout(vbox)
        # create FindWin and bind handlers
        self.find_win_panel = FindWin()
        self.find_win_panel.tmpl_field.setText(tmpl_default)
        self.find_win_panel.go_btn.clicked.connect(self.get_top_window)
        # create any_panels and bind handlers
        self.any_panel_1 = SendAny()
        self.any_panel_2 = SendAny()
        self.any_panel_3 = SendAny()
        self.any_panel_1.any_btn.clicked.connect(self.send_any)
        self.any_panel_2.any_btn.clicked.connect(self.send_any)
        self.any_panel_3.any_btn.clicked.connect(self.send_any)
        # create notebook
        self.notebook = Notebook()
        # add tables to the notebook
        self.notebook.add_tab_btn(tab1Name, T1, self.send)
        self.notebook.add_tab_btn(tab2Name, T2, self.send)
        self.notebook.add_tab_btn(tab3Name, T3, self.send)
        self.notebook.add_tab_btn(tab4Name, T4, self.send)
        self.notebook.add_tab_btn(tab5Name, T5, self.send)
        self.notebook.add_tab_btn(tab6Name, T6, self.send)
        self.notebook.add_tab_btn(tab7Name, T7, self.send)
        self.notebook.add_tab_edit(tab8Name, 10, T8, self.send_any)
        # add controls to side panel
        vbox.addWidget(self.find_win_panel)
        vbox.addWidget(self.any_panel_1)
        vbox.addWidget(self.any_panel_2)
        vbox.addWidget(self.any_panel_3)
        vbox.addWidget(self.notebook)

    def windowEnumHandler(self, hwnd, windows_found):
        windows_found.append((hwnd, win32gui.GetWindowText(hwnd), win32gui.IsWindowVisible(hwnd)))

    def find_top_window(self, template):
        self.hndl = None
        windows = []
        win32gui.EnumWindows(self.windowEnumHandler, windows)
        for i in windows:
            if template.lower() in i[1].lower():
                print('find_top_window(): top window found, template: ', template)
                print('Handle: ', i[0])
                print('Title: ', i[1])
                print('\r\n')
                self.hndl = i[0]
                self.find_win_panel.info.setStyleSheet('color: green;')
                self.find_win_panel.info.setText('Target OK!')
                break
        if not self.hndl:
            print('find_top_window(): top window not found, template: ', template)
            print('\r\n')
            self.find_win_panel.info.setStyleSheet('color: red;')
            self.find_win_panel.info.setText('Target not found')

    def get_top_window(self):
        tmpl = self.find_win_panel.tmpl_field.text()
        if tmpl:
            self.find_top_window(tmpl)

    def send(self, btn):
        global cmd_end
        if self.hndl:
            cmd_to_send = btn.getCmd()
            if cmd_to_send:
                self.write(cmd_to_send)

    def send_any(self):
        global cmd_end
        if self.hndl:
            ref = self.sender()      # get object created received signal
            cmd_to_send = ref.parent().any_field.text()       # get text from any_field using parent
            if cmd_to_send:
                self.write(cmd_to_send)

    def write(self, data):
        win32gui.ShowWindow(self.hndl, win32con.SW_SHOW)
        win32gui.SetForegroundWindow(self.hndl)
        for each in data:
            pyautogui.press(each)
        pyautogui.press('enter')

    def closeEvent(self, event):
        event.accept()


def main():
    app = QApplication([])
    main_win = MainWindow()
    main_win.resize(window_min_width, window_min_height)
    main_win.show()
    # sys.exit(app.exec())  # PySide6
    sys.exit(app.exec_())  # PySide2


if __name__ == '__main__':
    main()
