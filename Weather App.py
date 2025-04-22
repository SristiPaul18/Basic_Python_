import sys
from http.client import HTTPException
import requests
from PyQt5.QtWidgets import QApplication, QDesktopWidget, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from requests import HTTPError


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.city_label = QLabel("Enter City name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        screen_geometry = QDesktopWidget().screenGeometry()
        window_width = 600  # Set your desired window width
        window_height = 800  # Set your desired window height
        center_x = (screen_geometry.width() - window_width) // 2
        center_y = (screen_geometry.height() - window_height) // 2

        # Set window size and position to center the window
        self.setGeometry(center_x, center_y, window_width, window_height)

        hbox = QHBoxLayout()

        vbox = QVBoxLayout()
        vbox.setSpacing(15)
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.emoji_label.setMinimumHeight(190)
        self.emoji_label.setContentsMargins(0, 5, 0, 5)

        self.setStyleSheet("""
                    QWidget {
                        background: qlineargradient(
                        x1: 0, y1: 0, x2: 1, y2: 1,
                        stop: 0 #0f0f0f,
                        stop: 1 #1c1c1c
                    );
                    color: white;
                    font-family: "Segoe UI", sans-serif;
                    }

                    QLabel, QPushButton {
                        font-family: 'Segoe UI', sans-serif;
                        color: white;
                        background: transparent;
                    }

                    QLabel#city_label {
                        font-size: 36px;
                        font-weight: 600;
                        padding: 10px;
                    }

                    QLineEdit#city_input {
                        font-size: 28px;
                        padding: 12px;
                        border: 2px solid #ccc;
                        border-radius: 8px;
                        background: transparent;
                        color: white;

                    }

                    QPushButton#get_weather_button {
                        font-size: 24px;
                        font-weight: bold;
                        padding: 10px;
                        background-color: #7F00FF; 
                        color: white;
                        border: none;
                        border-radius: 8px;
                    }

                    QPushButton#get_weather_button:hover {
                        background-color: #9B30FF;
                        border: 2px solid #357ABD;
                    }

                    QLabel#temperature_label {
                        font-size: 60px;
                        font-weight: 500;
                        margin-top: 20px;
                    }

                    QLabel#emoji_label {
                        font-size: 90px;
                        font-family: Segoe UI Emoji;
                        margin: 5px 0;
                    }

                    QLabel#description_label {
                        font-size: 28px;
                        font-style: italic;
                        color: #CCCCCC;
                    }
                """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "8698b7b557c6ca1e409cb432d7eed653"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()

            try:
                data = response.json()
            except ValueError:
                self.display_error("Invalid response from server.\nUnable to parse data.")
                return

            if data.get("cod") == 200:
                self.display_weather(data)
            else:
                self.display_error("City not found.\nPlease check your city name.")

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request:\nPlease check your input.")
                case 401:
                    self.display_error("Unauthorized:\nInvalid API Key.")
                case 403:
                    self.display_error("Forbidden:\nAccess denied.")
                case 404:
                    self.display_error("Not Found:\nCity not found.")
                case 500:
                    self.display_error("Server Error:\nTry again later.")
                case 502:
                    self.display_error("Bad Gateway:\nInvalid response from server.")
                case 503:
                    self.display_error("Service Unavailable:\nServer down.")
                case 504:
                    self.display_error("Gateway Timeout:\nNo response from server.")
                case _:
                    self.display_error(f"HTTP error occurred:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection.")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nRequest timed out.")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects:\nCheck the URL.")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()
        self.additional_info_label.clear()

    def display_weather(self, data):
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        feels_like_k = data["main"]["feels_like"]
        feels_like_c = feels_like_k - 273.15
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]
        wind_deg = data["wind"]["deg"]
        humidity = data["main"]["humidity"]
        visibility = data["visibility"]
        pressure = data["main"]["pressure"]

        self.temperature_label.setText(
            f"{temperature_c:.0f}°C <br><span style='font-size: 18px; color: #AAAAAA;'>Feels like: {feels_like_c:.0f}°C</span>")

        emoji = self.get_weather_picture(weather_id)

        if emoji.endswith(".png"):
            pixmap = QPixmap(emoji)
            self.emoji_label.setPixmap(pixmap.scaled(150, 150, Qt.KeepAspectRatio))
            self.emoji_label.setText("")
        else:
            self.emoji_label.setPixmap(QPixmap())
            self.emoji_label.setText(emoji)

        self.description_label.setText(f"{weather_description.capitalize()}")

        additional_info = (
            f"Wind: {wind_speed} m/s, {wind_deg}°\n"
            f"Humidity: {humidity}%\n"
            f"Visibility: {visibility / 1000} km\n"  
            f"Pressure: {pressure} hPa"
        )

        if hasattr(self, 'additional_info_label'):
            self.additional_info_label.deleteLater()

        self.additional_info_label = QLabel(additional_info, self)
        self.additional_info_label.setAlignment(Qt.AlignCenter)
        self.additional_info_label.setStyleSheet("font-size: 18px; color: #CCCCCC; margin-top: 20px;")
        self.layout().addWidget(self.additional_info_label)

    @staticmethod
    def get_weather_picture(weather_id):
        if weather_id in [200, 201, 202, 230, 231, 232]:
            return "D:/PyCharmProjects/PythonProject/Icons/ThunderstormWithRain.png"
        elif weather_id in [210, 211, 212, 221]:
            return "D:/PyCharmProjects/PythonProject/Icons/Thunderstorm.png"
        elif weather_id in [300, 301, 302, 310, 311, 312, 313, 314, 321]:
            return "D:/PyCharmProjects/PythonProject/Icons/ThunderstormWithRain.png"
        elif weather_id in [500, 501, 502, 503, 504]:
            return "D:/PyCharmProjects/PythonProject/Icons/Rain.png"
        elif weather_id == 511:
            return "D:/PyCharmProjects/PythonProject/Icons/FreezingRain.png"
        elif weather_id in [520, 521]:
            return "D:/PyCharmProjects/PythonProject/Icons/HeavyShowerRain.png"
        elif weather_id in [522, 531]:
            return "D:/PyCharmProjects/PythonProject/Icons/HeavyShowerRain.png"
        elif weather_id in [600, 601, 602, 620, 621, 622]:
            return "D:/PyCharmProjects/PythonProject/Icons/Snow.png"
        elif weather_id in [611, 612, 613, 615, 616]:
            return "D:/PyCharmProjects/PythonProject/Icons/Sleet.png"
        elif weather_id in [701, 711, 721, 731, 741, 751, 761]:
            return "D:/PyCharmProjects/PythonProject/Icons/Mist.png"
        elif weather_id == 762:
            return "D:/PyCharmProjects/PythonProject/Icons/VolcanicAsh.png"
        elif weather_id == 771:
            return "D:/PyCharmProjects/PythonProject/Icons/Squalls.png"
        elif weather_id == 781:
            return "D:/PyCharmProjects/PythonProject/Icons/Tornado.png"
        elif weather_id == 800:
            return "D:/PyCharmProjects/PythonProject/Icons/ClearSky.png"
        elif weather_id == 801:
            return "D:/PyCharmProjects/PythonProject/Icons/FewClouds.png"
        elif weather_id == 802:
            return "D:/PyCharmProjects/PythonProject/Icons/FewClouds.png"
        elif weather_id == 803:
            return "D:/PyCharmProjects/PythonProject/Icons/FewClouds.png"
        elif weather_id == 804:
            return "D:/PyCharmProjects/PythonProject/Icons/Overcast.png"
        else:
            return ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())


