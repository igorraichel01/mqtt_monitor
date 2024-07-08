import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel, QPushButton
from qt_material import apply_stylesheet

from display import Display
from variables import WINDOW_ICON_PATH
from cliente_madruga import MQTTClient
from MainWindow import MainWindow

def toggle_connection():
    if btn_connect.text() == 'Connect':
        try:
            mqtt_client.connect_to_broker(host_display.text(), int(port_display.text()))
            btn_connect.setText('Disconnect')
            log_display.setText("Conectado ao broker MQTT!")
        except ConnectionRefusedError:
            log_display.setText("Erro: Broker MQTT não encontrado.")
    else:
        mqtt_client.disconnect()
        btn_connect.setText('Connect')
        log_display.setText("Desconectado do broker MQTT.")

def subscribe_topic():
    topic = topic_display.text()
    mqtt_client.subscribe(topic)
    log_display.setText(f"Subscribed to topic: {topic}")

def publish_message():
    topic = topic_display.text()
    message = msg_display.text()
    mqtt_client.publish(topic, message)
    log_display.setText(f"Published message: {message} to topic: {topic}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_blue.xml')
    window = MainWindow()

    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    mqtt_client = MQTTClient(window)

    mqtt_client.connected.connect(lambda: log_display.setText("Conectado ao broker MQTT!"))
    mqtt_client.disconnected.connect(lambda: log_display.setText("Desconectado do broker MQTT."))
    mqtt_client.message_received.connect(lambda topic, message: log_display.setText(f"Tópico: {topic}\nMensagem: {message}"))

    host_display = Display()
    host_label = QLabel("Host:")
    window.addWToVlayout(host_label, 0, 0)
    window.addWToVlayout(host_display, 0, 1)
    host_label.setFixedSize(40, 10)

    btn_connect = QPushButton('Connect')
    btn_connect.setStyleSheet('font-size: 8px; color: white')
    btn_connect.setFixedSize(90, 36)
    window.addWToVlayout(btn_connect, 0, 2)

    port_display = Display()
    port_label = QLabel("Port:")
    window.addWToVlayout(port_label, 1, 0)
    window.addWToVlayout(port_display, 1, 1)
    port_label.setFixedSize(40, 10)

    topic_display = Display()
    topic_label = QLabel("Topic:")
    window.addWToVlayout(topic_label, 2, 0)
    window.addWToVlayout(topic_display, 2, 1)

    btn_subscribe = QPushButton('Subscribe')
    btn_subscribe.setStyleSheet('font-size: 8px; color: white')
    btn_subscribe.setFixedSize(90, 36)
    window.addWToVlayout(btn_subscribe, 2, 2)

    btn_publish = QPushButton('Publish')
    btn_publish.setStyleSheet('font-size: 8px; color: white')
    window.addWToVlayout(btn_publish, 3, 2)
    btn_publish.setFixedSize(90, 36)

    msg_display = Display()
    msg_label = QLabel("Message:")
    window.addWToVlayout(msg_label, 3, 0)
    window.addWToVlayout(msg_display, 3, 1)
    msg_label.setFixedSize(65, 20)

    log_display = Display()
    log_label = QLabel("Log:")
    window.addWToVlayout(log_label, 4, 0)
    window.addWToVlayout(log_display, 4, 1)

    btn_quit = QPushButton('Quit')
    btn_quit.setStyleSheet('font-size: 8px; color: white')
    window.addWToVlayout(btn_quit, 5, 2)

    # Conectando os botões às suas respectivas funções
    btn_connect.clicked.connect(toggle_connection)
    btn_subscribe.clicked.connect(subscribe_topic)
    btn_publish.clicked.connect(publish_message)
    btn_quit.clicked.connect(app.quit)

    window.show()
    app.exec()
