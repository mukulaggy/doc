import sys
import os
import subprocess
import socket
import time
import re
import json
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *

# === CONSTANTS ===
class Colors:
    DARK_BACKGROUND = "#0d1117"
    DARKER_BACKGROUND = "#010409"
    CARD_BACKGROUND = "#161b22"
    PRIMARY = "#58a6ff"
    SECONDARY = "#1f6feb"
    ACCENT = "#79c0ff"
    ACCENT_SECONDARY = "#a5f3fc"
    TEXT = "#f0f6fc"
    TEXT_SECONDARY = "#8b949e"
    ERROR = "#f85149"
    SUCCESS = "#3fb950"
    WARNING = "#d29922"
    BORDER = "#30363d"
    GLOW = "rgba(88, 166, 255, 0.4)"

class Paths:
    DEP = '.'
    BACKEND_LOG = os.path.join(DEP, "backend.log")
    FRONTEND_DIR = os.path.join(DEP, "pipecm-frontend")
    FRONTEND_LOG = os.path.join(DEP, "frontend.log")
    QUERIES_SQL = os.path.join(DEP, "queries.sql")
    APPLICATION_PROPERTIES = os.path.join(DEP, "application.properties")
    CONFIG_TS = os.path.join(FRONTEND_DIR,"src","utilities","config.ts")

class DockerConfig:
    IMAGE_NAME ="pipecm_image"
    CONTAINER_NAME = "my_container"
    DEBS = [
        os.path.join(Paths.DEP, "docker-ce_26.0.0-1~ubuntu.24.04~noble_amd64.deb"),
        os.path.join(Paths.DEP, "docker-ce-cli_26.0.0-1~ubuntu.24.04~noble_amd64.deb"),
        os.path.join(Paths.DEP, "containerd.io_1.6.28-2_amd64.deb")
    ]

STYLESHEET = f"""
    QWidget {{
        background-color: {Colors.DARK_BACKGROUND};
        color: {Colors.TEXT};
        font-family: 'Inter', 'Segoe UI', Arial, sans-serif;
        font-size: 13px;
    }}
    
    QLabel {{
        color: {Colors.TEXT};
        font-weight: 500;
    }}
    
    QPushButton {{
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
            stop:0 {Colors.CARD_BACKGROUND}, stop:1 {Colors.DARKER_BACKGROUND});
        color: {Colors.TEXT};
        border: 1px solid {Colors.BORDER};
        border-radius: 8px;
        padding: 12px 24px;
        min-width: 120px;
        font-weight: 600;
        font-size: 13px;
    }}
    
    QPushButton:hover {{
        background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
            stop:0 {Colors.PRIMARY}, stop:1 {Colors.SECONDARY});
        border: 1px solid {Colors.ACCENT};
    }}
    
    QPushButton:pressed {{
        background: {Colors.SECONDARY};
    }}
    
    QPushButton:disabled {{
        background-color: {Colors.DARKER_BACKGROUND};
        color: {Colors.TEXT_SECONDARY};
        border: 1px solid #21262d;
    }}
    
    QProgressBar {{
        border: 1px solid {Colors.BORDER};
        border-radius: 8px;
        text-align: center;
        background-color: {Colors.DARKER_BACKGROUND};
        height: 24px;
        font-weight: 600;
    }}
    
    QProgressBar::chunk {{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 {Colors.PRIMARY}, stop:0.5 {Colors.ACCENT}, stop:1 {Colors.ACCENT_SECONDARY});
        border-radius: 7px;
        margin: 1px;
    }}
    
    QTextEdit, QLineEdit {{
        background-color: {Colors.CARD_BACKGROUND};
        color: {Colors.TEXT};
        border: 1px solid {Colors.BORDER};
        border-radius: 8px;
        padding: 12px;
        font-family: 'JetBrains Mono', 'Consolas', monospace;
        selection-background-color: {Colors.PRIMARY};
    }}
    
    QTextEdit:focus, QLineEdit:focus {{
        border: 2px solid {Colors.PRIMARY};
    }}
    
    QGroupBox {{
        background-color: {Colors.CARD_BACKGROUND};
        border: 1px solid {Colors.BORDER};
        border-radius: 12px;
        margin-top: 16px;
        padding-top: 20px;
        font-weight: 600;
    }}
    
    QGroupBox::title {{
        subcontrol-origin: margin;
        left: 16px;
        padding: 0 8px;
        color: {Colors.ACCENT};
        font-size: 14px;
        font-weight: 700;
        background-color: {Colors.CARD_BACKGROUND};
    }}
    
    QDialog {{
        background-color: {Colors.DARK_BACKGROUND};
        border: 1px solid {Colors.BORDER};
        border-radius: 16px;
    }}
    
    QFrame[frameShape="4"] {{
        background-color: {Colors.BORDER};
        max-height: 2px;
        border: none;
    }}
"""

# === UTILITY FUNCTIONS ===
def run_cmd(cmd, shell=False, check=False):
    res = subprocess.run(cmd, shell=shell, check=check, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return res.stdout.strip(), res.stderr.strip()

def get_system_ip():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))
            return s.getsockname()[0]
    except Exception:
        return "localhost"

def is_service_running(port):
    out, _ = run_cmd(f"netstat -tulnp 2>/dev/null | grep ':{port}'", shell=True)
    return bool(out)

def tail_log(path, lines=1000):
    if not os.path.exists(path):
        return [f"Missing log: {path}"]
    with open(path, "r", errors="ignore") as f:
        return f.readlines()[-lines:]

def update_upload_dir_in_config(upload_path):
    config = ConfigManager.read()
    config['file.uploadDir'] = upload_path
    ConfigManager.save(config)

def force_update_ip_in_config():
    config_values = ConfigManager.read()
    ip_address = get_system_ip()
    if "://" in config_values["API_LINK"]:
        parts = config_values["API_LINK"].split("://")
        proto = parts[0]
        after_proto = parts[1]
        if ":" in after_proto:
            port = after_proto.split(":")[-1]
            config_values["API_LINK"] = f"{proto}://{ip_address}:{port}"
        else:
            config_values["API_LINK"] = f"{proto}://{ip_address}"
    if "://" in config_values["WEB_SOCKET_LINK"]:
        parts = config_values["WEB_SOCKET_LINK"].split("://")
        proto = parts[0]
        after_proto = parts[1]
        if ":" in after_proto:
            port = after_proto.split(":")[-1]
            config_values["WEB_SOCKET_LINK"] = f"{proto}://{ip_address}:{port}"
        else:
            config_values["WEB_SOCKET_LINK"] = f"{proto}://{ip_address}"
    if "localhost" in config_values["spring.datasource.url"]:
        config_values["spring.datasource.url"] = config_values["spring.datasource.url"].replace("localhost", ip_address)
    ConfigManager.save(config_values)

PATH_CONFIG_FILE = "volume_paths.json"

def save_paths_to_json(upload_path, db_path):
    data = {"upload_path": upload_path, "db_path": db_path}
    with open(PATH_CONFIG_FILE, "w") as f:
        json.dump(data, f)

def load_paths_from_json():
    if not os.path.exists(PATH_CONFIG_FILE):
        return None, None
    try:
        with open(PATH_CONFIG_FILE, "r") as f:
            data = json.load(f)
        return data.get("upload_path", ""), data.get("db_path", "")
    except Exception:
        return None, None

inputPath = ''
inputhPath1 = ''

class PathSelectionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Volume Paths")
        self.setStyleSheet(STYLESHEET)
        self.setMinimumWidth(500)
        layout = QFormLayout()
        self.upload_dir_edit = QLineEdit()
        self.upload_dir_btn = QPushButton("Browse...")
        self.upload_dir_btn.clicked.connect(self.browse_upload_dir)
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.upload_dir_edit)
        hbox1.addWidget(self.upload_dir_btn)
        layout.addRow("Upload Directory Path:", hbox1)
        self.pg_dir_edit = QLineEdit()
        self.pg_dir_btn = QPushButton("Browse...")
        self.pg_dir_btn.clicked.connect(self.browse_pg_dir)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.pg_dir_edit)
        hbox2.addWidget(self.pg_dir_btn)
        layout.addRow("PostgreSQL Data Directory Path:", hbox2)
        button_box = QHBoxLayout()
        self.ok_btn = ModernGlowButton("OK")
        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn = ModernGlowButton("Cancel")
        self.cancel_btn.clicked.connect(self.reject)
        button_box.addWidget(self.ok_btn)
        button_box.addWidget(self.cancel_btn)
        layout.addRow(button_box)
        self.setLayout(layout)
    def browse_upload_dir(self):
        path = QFileDialog.getExistingDirectory(self, "Select Upload Directory", os.path.expanduser("~"), QFileDialog.Option.ShowDirsOnly)
        if path:
            self.upload_dir_edit.setText(path)
    def browse_pg_dir(self):
        path = QFileDialog.getExistingDirectory(self, "Select PostgreSQL Data Directory", os.path.expanduser("~"), QFileDialog.Option.ShowDirsOnly)
        if path:
            self.pg_dir_edit.setText(path)
    def get_paths(self):
        return self.upload_dir_edit.text(), self.pg_dir_edit.text()

# === DOCKER MANAGEMENT ===
class DockerManager:
    @staticmethod
    def is_installed():
        out, _ = run_cmd(["which", "docker"])
        if not out:
            return False
        out, _ = run_cmd(["docker", "--version"])
        return "Docker version" in out
    @staticmethod
    def install():
        if not all(os.path.exists(deb) for deb in DockerConfig.DEBS):
            return "❌ One or more Docker .deb files missing", "error"
        _, err = run_cmd(["sudo", "dpkg", "-i"] + DockerConfig.DEBS)
        if err:
            _, err = run_cmd(["sudo", "apt-get", "-f", "install", "-y"])
            if err:
                return f"❌ Failed to fix dependencies: {err}", "error"
        return ("✅ Docker installed", "success") if DockerManager.is_installed() else ("❌ Installation failed", "error")
    @staticmethod
    def is_image_loaded(image_name):
        out, _ = run_cmd(["sudo", "docker", "images", "-q", image_name])
        return bool(out.strip())
    @staticmethod
    def load_image(tar_path):
        out, err = run_cmd(["sudo", "docker", "load", "-i", tar_path])
        return ("✅ Image loaded", "success") if not err else (f"❌ Failed to load image: {err}", "error")
    @staticmethod
    def is_container_running(container_name=DockerConfig.CONTAINER_NAME):
        out, _ = run_cmd(["sudo", "docker", "ps", "-q", "-f", f"name=^{container_name}$"])
        return bool(out)
    @staticmethod
    def start_container(image_name=DockerConfig.IMAGE_NAME, container_name=DockerConfig.CONTAINER_NAME, input_path=None, inputh_path1=None):
        out, _ = run_cmd(["sudo", "docker", "ps", "-a", "-q", "-f", f"name=^{container_name}$"])
        if out:
            run_cmd(["sudo", "docker", "rm", "-f", container_name])
        img_out, _ = run_cmd(["sudo", "docker", "images", "-q", image_name])
        if not img_out:
            return f"❌ Image '{image_name}' not found", "error"
        input_path = input_path or inputPath
        inputh_path1 = inputh_path1 or inputhPath1
        if not input_path or not inputh_path1:
            return "❌ Missing volume mount paths", "error"
        cmd = (f"sudo docker run --network host -it -d "
               f"-v {input_path}:/uploadDir "
               f"-v {inputh_path1}:/var/lib/postgresql/data "
               f"--name {container_name} {image_name}")
        run_cmd(cmd, shell=True)
        time.sleep(2)
        if DockerManager.is_container_running(container_name):
            return f"✅ Container '{container_name}' started", "success"
        else:
            logs, _ = run_cmd(["sudo", "docker", "logs", container_name])
            return f"❌ Failed to start container. Logs:\n{logs[-500:]}", "error"
    @staticmethod
    def stop_container(container_name=DockerConfig.CONTAINER_NAME):
        if not DockerManager.is_container_running(container_name):
            return f"❌ Container '{container_name}' not running", "error"
        run_cmd(["sudo", "docker", "stop", container_name])
        time.sleep(2)
        if not DockerManager.is_container_running(container_name):
            return f"✅ Container '{container_name}' stopped", "success"
        return f"❌ Failed to stop container '{container_name}'", "error"
# === SERVICE MANAGEMENT ===
class ServiceManager:
    @staticmethod
    def run_in_container(cmd, container_name=DockerConfig.CONTAINER_NAME):
        full_cmd = f"sudo docker exec {container_name} bash -c \"{cmd}\""
        return run_cmd(full_cmd, shell=True)
    @staticmethod
    def start_backend():
        cmd = ("nohup java -jar /home/pipecm-1.0.0.jar "
              "--spring.config.location=file:/home/application.properties "
              "> /deps/backend.log 2>&1 &")
        out, err = ServiceManager.run_in_container(cmd)
        time.sleep(3)
        out_check, _ = ServiceManager.run_in_container("pgrep -f pipecm-1.0.0.jar")
        if out_check.strip():
            return "✅ Backend started", "success"
        return f"❌ Failed to start backend: {err}", "error"
    @staticmethod
    def stop_backend():
        out, err = ServiceManager.run_in_container("pkill -f pipecm-1.0.0.jar")
        time.sleep(1)
        out_check, _ = ServiceManager.run_in_container("pgrep -f pipecm-1.0.0.jar")
        if not out_check.strip():
            return "✅ Backend stopped", "success"
        return "❌ Failed to stop backend", "error"
    @staticmethod
    def start_frontend():
        cmd = "cd /home/pipecm-frontend && nohup npm run start > /deps/frontend.log 2>&1 &"
        out, err = ServiceManager.run_in_container(cmd)
        time.sleep(3)
        out_check, _ = ServiceManager.run_in_container("netstat -tulnp | grep ':3000'")
        if out_check.strip():
            return "✅ Frontend started", "success"
        return f"❌ Failed to start frontend: {err}", "error"
    @staticmethod
    def stop_frontend():
        cmd = "fuser -k 3000/tcp || pkill -f 'npm run start'"
        out, err = ServiceManager.run_in_container(cmd)
        time.sleep(1)
        out_check, _ = ServiceManager.run_in_container("netstat -tulnp | grep ':3000'")
        if not out_check.strip():
            return "✅ Frontend stopped", "success"
        return "❌ Failed to stop frontend", "error"
    @staticmethod
    def build_frontend():
        cmd = "cd /home/pipecm-frontend && npm run build"
        out, err = ServiceManager.run_in_container(cmd)
        return ("✅ Frontend built", "success") if not err else (f"❌ Build failed: {err}", "error")
    @staticmethod
    def start_database():
        out, err = ServiceManager.run_in_container("service postgresql start")
        time.sleep(2)
        out_check, _ = ServiceManager.run_in_container("netstat -tulnp | grep ':5432'")
        if out_check.strip():
            return "✅ Database started", "success"
        return f"❌ Failed to start database: {err}", "error"
    @staticmethod
    def stop_database():
        out, err = ServiceManager.run_in_container("service postgresql stop")
        time.sleep(1)
        out_check, _ = ServiceManager.run_in_container("netstat -tulnp | grep ':5432'")
        if not out_check.strip():
            return "✅ Database stopped", "success"
        return "❌ Failed to stop database", "error"

class ConfigManager:
    @staticmethod
    def read():
        config = {
            'spring.datasource.url': '',
            'file.uploadDir': '',
            'API_LINK': '',
            'WEB_SOCKET_LINK': ''
        }
        if os.path.exists(Paths.APPLICATION_PROPERTIES):
            with open(Paths.APPLICATION_PROPERTIES, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip().lstrip('\ufeff')  # Remove BOM if present
                    if line.startswith('spring.datasource.url='):
                        config['spring.datasource.url'] = line.split('=', 1)[1].strip()
                    elif line.startswith('file.uploadDir='):
                        config['file.uploadDir'] = line.split('=', 1)[1].strip("'").strip()
        if os.path.exists(Paths.CONFIG_TS):
            with open(Paths.CONFIG_TS, 'r', encoding='utf-8') as f:
                content = f.read()
                api_match = re.search(r"export const API_LINK = '([^']+)'", content)
                ws_match = re.search(r"export const WEB_SOCKET_LINK = '([^']+)'", content)
                if api_match:
                    config['API_LINK'] = api_match.group(1)
                if ws_match:
                    config['WEB_SOCKET_LINK'] = ws_match.group(1)
        return config
    @staticmethod
    def save(config):
        if os.path.exists(Paths.APPLICATION_PROPERTIES):
            with open(Paths.APPLICATION_PROPERTIES, 'r') as f:
                lines = f.readlines()
            with open(Paths.APPLICATION_PROPERTIES, 'w') as f:
                for line in lines:
                    if line.startswith('spring.datasource.url='):
                        f.write(f"spring.datasource.url={config['spring.datasource.url']}\n")
                    elif line.startswith('file.uploadDir='):
                        # Only write file.uploadDir if value is not empty
                        if config['file.uploadDir']:
                            f.write(f"file.uploadDir='{config['file.uploadDir']}'\n")
                        else:
                            f.write(line)
                    else:
                        f.write(line)
        if os.path.exists(Paths.CONFIG_TS):
            with open(Paths.CONFIG_TS, 'r') as f:
                content = f.read()
            content = re.sub(
                r"export const API_LINK = '[^']*'",
                f"export const API_LINK = '{config['API_LINK']}'",
                content
            )
            content = re.sub(
                r"export const WEB_SOCKET_LINK = '[^']*'",
                f"export const WEB_SOCKET_LINK = '{config['WEB_SOCKET_LINK']}'",
                content
            )
            with open(Paths.CONFIG_TS, 'w') as f:
                f.write(content)

class ModernBanner(QWidget):
    """Modern banner widget with gradient background"""
    def __init__(self, title, subtitle, parent=None):
        super().__init__(parent)
        self.title = title
        self.subtitle = subtitle
        self.setMinimumHeight(120)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 20, 40, 20)
        layout.setSpacing(8)
        
        # Main title
        self.title_label = QLabel(title)
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setFont(QFont("Inter", 32, QFont.Weight.ExtraBold))
        self.title_label.setStyleSheet(f"color: {Colors.TEXT}; background: transparent; padding: 8px;")
        
        # Subtitle
        self.subtitle_label = QLabel(subtitle)
        self.subtitle_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitle_label.setFont(QFont("Inter", 14, QFont.Weight.Medium))
        self.subtitle_label.setStyleSheet(f"""
            color: {Colors.TEXT_SECONDARY};
            background: transparent;
            letter-spacing: 2px;
        """)
        
        layout.addWidget(self.title_label)
        layout.addWidget(self.subtitle_label)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Create gradient background
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0, QColor(Colors.PRIMARY).darker(300))
        gradient.setColorAt(0.3, QColor(Colors.SECONDARY).darker(200))
        gradient.setColorAt(0.7, QColor(Colors.ACCENT).darker(400))
        gradient.setColorAt(1, QColor(Colors.DARK_BACKGROUND))
        
        # Draw rounded rectangle
        painter.setBrush(gradient)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(self.rect(), 16, 16)
        
        # Add subtle border glow
        pen = painter.pen()
        pen.setWidth(2)
        pen.setColor(QColor(Colors.PRIMARY).lighter(150))
        painter.setPen(pen)
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.drawRoundedRect(self.rect().adjusted(1, 1, -1, -1), 15, 15)
        
        painter.end()

class ModernGlowButton(QPushButton):
    """Modern button with enhanced glow effects"""
    def __init__(self, text, button_type="default", parent=None):
        super().__init__(text, parent)
        self.button_type = button_type
        self.setFont(QFont("Inter", 13, QFont.Weight.DemiBold))
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        if button_type == "primary":
            self.setStyleSheet(f"""
                QPushButton {{
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                        stop:0 {Colors.PRIMARY}, stop:1 {Colors.SECONDARY});
                    color: white;
                    border: 2px solid {Colors.ACCENT};
                    border-radius: 10px;
                    padding: 14px 28px;
                    font-weight: 700;
                    letter-spacing: 1px;
                }}
                QPushButton:hover {{
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                        stop:0 {Colors.ACCENT}, stop:1 {Colors.PRIMARY});
                    border: 2px solid {Colors.ACCENT_SECONDARY};
                }}
                QPushButton:pressed {{
                    background: {Colors.SECONDARY};
                }}
            """)
        elif button_type == "success":
            self.setStyleSheet(f"""
                QPushButton {{
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                        stop:0 {Colors.SUCCESS}, stop:1 #2ea043);
                    color: white;
                    border: 2px solid #56d364;
                    border-radius: 10px;
                    padding: 14px 28px;
                    font-weight: 700;
                }}
                QPushButton:hover {{
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                        stop:0 #56d364, stop:1 {Colors.SUCCESS});
                }}
            """)
        elif button_type == "danger":
            self.setStyleSheet(f"""
                QPushButton {{
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                        stop:0 {Colors.ERROR}, stop:1 #da3633);
                    color: white;
                    border: 2px solid #ff7b72;
                    border-radius: 10px;
                    padding: 14px 28px;
                    font-weight: 700;
                }}
                QPushButton:hover {{
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                        stop:0 #ff7b72, stop:1 {Colors.ERROR});
                }}
            """)

class ModernStatusIndicator(QLabel):
    """Modern status indicator with animated icons"""
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.setFont(QFont("Inter", 12, QFont.Weight.Medium))
        self.setMinimumHeight(40)
        self.setStyleSheet(f"""
            QLabel {{
                background-color: {Colors.CARD_BACKGROUND};
                border: 1px solid {Colors.BORDER};
                border-radius: 8px;
                padding: 12px 16px;
                margin: 4px 0;
            }}
        """)
        self.set_status(False)
    
    def set_status(self, is_running):
        """Update status display with modern styling"""
        if is_running:
            status_text = "● ONLINE"
            color = Colors.SUCCESS
            bg_color = "rgba(63, 185, 80, 0.1)"
        else:
            status_text = "● OFFLINE"
            color = Colors.ERROR  
            bg_color = "rgba(248, 81, 73, 0.1)"
            
        service_name = self.text().split(':')[0] if ':' in self.text() else self.text()
        
        self.setText(f"""
            <div style='display: flex; justify-content: space-between; align-items: center;'>
                <span style='font-weight: 600; color: {Colors.TEXT};'>{service_name}</span>
                <span style='color: {color}; font-weight: 700; font-size: 11px; 
                      background-color: {bg_color}; padding: 4px 8px; border-radius: 4px;'>
                    {status_text}
                </span>
            </div>
        """)

class ConfigEditorDialog(QDialog):
    def __init__(self, config_values, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Configuration Editor")
        self.setMinimumWidth(600)
        self.setStyleSheet(STYLESHEET)
        layout = QVBoxLayout()
        form = QFormLayout()
        self.db_url_edit = self._create_line_edit(config_values['spring.datasource.url'])
        self.api_link_edit = self._create_line_edit(config_values['API_LINK'])
        self.ws_link_edit = self._create_line_edit(config_values['WEB_SOCKET_LINK'])
        form.addRow("Database URL:", self.db_url_edit)
        form.addRow("API Link:", self.api_link_edit)
        form.addRow("WebSocket Link:", self.ws_link_edit)
        layout.addLayout(form)
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        separator.setStyleSheet(f"color: {Colors.PRIMARY};")
        layout.addWidget(separator)
        button_box = QHBoxLayout()
        self.save_btn = ModernGlowButton("Save")
        self.save_btn.clicked.connect(self.accept)
        self.cancel_btn = ModernGlowButton("Cancel")
        self.cancel_btn.clicked.connect(self.reject)
        button_box.addWidget(self.save_btn)
        button_box.addWidget(self.cancel_btn)
        layout.addLayout(button_box)
        self.setLayout(layout)
    def _create_line_edit(self, text):
        edit = QLineEdit()
        edit.setText(text)
        edit.setStyleSheet(f"border: 1px solid {Colors.PRIMARY};")
        return edit
    def get_config_values(self):
        return {
            'spring.datasource.url': self.db_url_edit.text(),
            'file.uploadDir': '',  # Don't change it; handled elsewhere
            'API_LINK': self.api_link_edit.text(),
            'WEB_SOCKET_LINK': self.ws_link_edit.text()
        }

class BootstrapThread(QThread):
    request_paths = pyqtSignal()
    paths_provided = False
    input_path = ''
    inputh_path1 = ''
    progress = pyqtSignal(int, str)
    result = pyqtSignal(bool, str)
    request_paths = pyqtSignal()
    def run(self):
        try:
            self._step(10, "Checking Docker...", self._install_docker)
            self._step(50, "Checking Docker images...", self._load_docker_image)
            upath, dbpath = load_paths_from_json()
            if upath and dbpath:
                self.input_path = upath
                self.inputh_path1 = dbpath
                self.paths_provided = True
                update_upload_dir_in_config(self.input_path)
            else:
                self.request_paths.emit()
                for _ in range(60):
                    if self.paths_provided:
                        break
                    self.msleep(500)
                if not self.paths_provided or not self.input_path or not self.inputh_path1:
                    self.result.emit(False, "Volume mount paths not provided. Aborting.")
                    return
                save_paths_to_json(self.input_path, self.inputh_path1)
                update_upload_dir_in_config(self.input_path)
            self._step(80, "Initializing container...", self._init_container)
            self.progress.emit(100, "Bootstrap completed")
            self.result.emit(True, "All services started successfully")
        except Exception as e:
            self.result.emit(False, str(e))
    def _step(self, progress, message, action):
        self.progress.emit(progress - 10, message)
        msg, mtype = action()
        self.progress.emit(progress, msg)
        if mtype != "success":
            self.result.emit(False, msg)
            raise RuntimeError(msg)
        self.msleep(1000)
    def _install_docker(self):
        if DockerManager.is_installed():
            return "✅ Docker installed", "success"
        return DockerManager.install()
    def _load_docker_image(self):
        if DockerManager.is_image_loaded(DockerConfig.IMAGE_NAME):
            return f"✅ Image '{DockerConfig.IMAGE_NAME}' loaded", "success"
        for file in os.listdir('.'):
            if file.endswith('.tar'):
                return DockerManager.load_image(file)
        return "❌ No Docker image files found", "error"
    def _init_container(self):
        return DockerManager.start_container(
            input_path=self.input_path,
            inputh_path1=self.inputh_path1
        )
class ServiceWorker(QThread):
    log_signal = pyqtSignal(str)
    done_signal = pyqtSignal(str)

    def __init__(self, action):
        super().__init__()
        self.action = action

    def run(self):
        if self.action == "start_all":
            self.log_signal.emit("Starting database...")
            msg_db, _ = ServiceManager.start_database()
            self.log_signal.emit(msg_db)
            self.msleep(2000)
            self.log_signal.emit("Starting backend...")
            msg_be, _ = ServiceManager.start_backend()
            self.log_signal.emit(msg_be)
            self.msleep(2000)
            self.log_signal.emit("Building frontend...")
            msg_build, _ = ServiceManager.build_frontend()
            self.log_signal.emit(msg_build)
            self.msleep(2000)
            self.log_signal.emit("Starting frontend...")
            msg_fe, _ = ServiceManager.start_frontend()
            self.log_signal.emit(msg_fe)
            self.done_signal.emit(f"{msg_db}\n{msg_be}\n{msg_build}\n{msg_fe}")
        elif self.action == "stop_all":
            self.log_signal.emit("Stopping frontend...")
            msg_fe, _ = ServiceManager.stop_frontend()
            self.log_signal.emit(msg_fe)
            self.msleep(1000)
            self.log_signal.emit("Stopping backend...")
            msg_be, _ = ServiceManager.stop_backend()
            self.log_signal.emit(msg_be)
            self.msleep(1000)
            self.log_signal.emit("Stopping database...")
            msg_db, _ = ServiceManager.stop_database()
            self.log_signal.emit(msg_db)
            self.done_signal.emit(f"{msg_fe}\n{msg_be}\n{msg_db}")

class ServerManagerUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Server Manager - Control Center")
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
        self.setStyleSheet(STYLESHEET)
        self._init_ui()
        self._setup_connections()
        self._start_bootstrap()
    def _init_ui(self):
        self.layout = QVBoxLayout(self)
        # ascii_art = """
        # ██████╗ ██╗██████╗ ███████╗ ██████╗███╗   ███╗
        # ██╔══██╗██║██╔══██╗██╔════╝██╔════╝████╗ ████║
        # ██████╔╝██║██████╔╝█████╗  ██║     ██╔████╔██║
        # ██╔═══╝ ██║██╔═══╝ ██╔══╝  ██║     ██║╚██╔╝██║
        # ██║     ██║██║     ███████╗╚██████╗██║ ╚═╝ ██║
        # ╚═╝     ╚═╝╚═╝     ╚══════╝ ╚═════╝╚═╝     ╚═╝
        # """
        banner = ModernBanner("SERVER CONTROL CENTER", "PIPECM - Modern Server Management")
        self.layout.addWidget(banner)
        self._init_progress_group()
        self._init_control_group()
        self._init_log_tabs()
    def _init_progress_group(self):
        progress_group = QGroupBox("System Initialization")
        progress_layout = QVBoxLayout()
        self.progress_bar = QProgressBar()
        self.progress_bar.setStyleSheet(f"""
            QProgressBar {{
                border: 1px solid {Colors.PRIMARY};
                border-radius: 4px;
                text-align: center;
                height: 20px;
            }}
            QProgressBar::chunk {{
                background-color: qlineargradient(
                    x1:0, y1:0, x2:1, y2:0,
                    stop:0 {Colors.PRIMARY}, stop:1 {Colors.SECONDARY}
                );
                width: 10px;
            }}
        """)
        progress_layout.addWidget(self.progress_bar)
        progress_group.setLayout(progress_layout)
        self.layout.addWidget(progress_group)
    def _init_control_group(self):
        control_group = QGroupBox("Control Panel")
        control_layout = QGridLayout()
        self.btn_start_all = ModernGlowButton("Start All Services")
        self.btn_stop_all = ModernGlowButton("Stop All Services")
        self.btn_edit_config = ModernGlowButton("Edit Config")
        self.btn_start_all.setStyleSheet(f"""
            QPushButton {{
                background-color: {Colors.SUCCESS};
                color: {Colors.DARK_BACKGROUND};
                font-weight: bold;
            }}
        """)
        self.btn_stop_all.setStyleSheet(f"""
            QPushButton {{
                background-color: {Colors.ERROR};
                color: {Colors.DARK_BACKGROUND};
                font-weight: bold;
            }}
        """)
        self.btn_start_all.setEnabled(False)
        self.btn_stop_all.setEnabled(False)
        self.btn_edit_config.setEnabled(False)
        control_layout.addWidget(self.btn_start_all, 0, 0)
        control_layout.addWidget(self.btn_stop_all, 0, 1)
        control_layout.addWidget(self.btn_edit_config, 1, 0, 1, 2)
        control_group.setLayout(control_layout)
        self.layout.addWidget(control_group)
    def _init_log_tabs(self):
        self.tabs = QTabWidget()
        self.system_log_view = QTextEdit()
        self.system_log_view.setReadOnly(True)
        self.system_log_view.setStyleSheet(f"""
            QTextEdit {{
                background-color: {Colors.DARKER_BACKGROUND};
                color: {Colors.TEXT};
                border: 1px solid {Colors.PRIMARY};
                font-family: 'Consolas', monospace;
                font-size: 10pt;
            }}
        """)
        self.tabs.addTab(self.system_log_view, "System Log")
        self.frontend_log_view = QTextEdit()
        self.frontend_log_view.setReadOnly(True)
        self.frontend_log_view.setStyleSheet(f"""
            QTextEdit {{
                background-color: {Colors.DARKER_BACKGROUND};
                color: {Colors.TEXT};
                border: 1px solid {Colors.PRIMARY};
                font-family: 'Consolas', monospace;
                font-size: 10pt;
            }}
        """)
        self.tabs.addTab(self.frontend_log_view, "Frontend Log")
        self.backend_log_view = QTextEdit()
        self.backend_log_view.setReadOnly(True)
        self.backend_log_view.setStyleSheet(f"""
            QTextEdit {{
                background-color: {Colors.DARKER_BACKGROUND};
                color: {Colors.TEXT};
                border: 1px solid {Colors.PRIMARY};
                font-family: 'Consolas', monospace;
                font-size: 10pt;
            }}
        """)
        self.tabs.addTab(self.backend_log_view, "Backend Log")
        self.layout.addWidget(self.tabs)
    def _setup_connections(self):
        self.btn_start_all.clicked.connect(self.start_all_services)
        self.btn_stop_all.clicked.connect(self.stop_all_services)
        self.btn_edit_config.clicked.connect(self.edit_configuration)
    def _start_bootstrap(self):
        self.bootstrap_thread = BootstrapThread()
        self.bootstrap_thread.progress.connect(self.on_progress)
        self.bootstrap_thread.result.connect(self.on_bootstrap_done)
        self.bootstrap_thread.request_paths.connect(self._show_path_dialog)
        self.bootstrap_thread.start()
    def _show_path_dialog(self):
        dialog = PathSelectionDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            up, pg = dialog.get_paths()
            self.bootstrap_thread.input_path = up
            self.bootstrap_thread.inputh_path1 = pg
            self.bootstrap_thread.paths_provided = True
        else:
            self.bootstrap_thread.input_path = ''
            self.bootstrap_thread.inputh_path1 = ''
            self.bootstrap_thread.paths_provided = False
    def on_progress(self, value, msg):
        self.progress_bar.setValue(value)
        self.system_log_view.append(f"[{value}%] {msg}")
    def on_bootstrap_done(self, success, msg):
        self.system_log_view.append(msg)

        self.progress_bar.setValue(100)
        self._refresh_log_tabs()
        if not success:
            QMessageBox.critical(self, "Bootstrap Failed", msg)
            self.btn_start_all.setEnabled(False)
            self.btn_stop_all.setEnabled(False)
            self.btn_edit_config.setEnabled(False)
        else:
            QMessageBox.information(self, "Success", msg)
    def _refresh_log_tabs(self):
        try:
            if os.path.exists(Paths.FRONTEND_LOG):
                with open(Paths.FRONTEND_LOG, 'r', errors='ignore') as f:
                    self.frontend_log_view.setPlainText(f.read())
            else:
                self.frontend_log_view.setPlainText("Frontend log not found.")
        except Exception as e:
            self.frontend_log_view.setPlainText(f"Error reading frontend log: {str(e)}")
        try:
            if os.path.exists(Paths.BACKEND_LOG):
                with open(Paths.BACKEND_LOG, 'r', errors='ignore') as f:
                    self.backend_log_view.setPlainText(f.read())
            else:
                self.backend_log_view.setPlainText("Backend log not found.")
        except Exception as e:
            self.backend_log_view.setPlainText(f"Error reading backend log: {str(e)}")
    def start_all_services(self):
    	self.btn_start_all.setEnabled(False)
    	self.btn_stop_all.setEnabled(False)
    	self.worker = ServiceWorker("start_all")
    	self.worker.log_signal.connect(self.system_log_view.append)
    	self.worker.done_signal.connect(self._on_services_started)
    	self.worker.start()

    def stop_all_services(self):	
    	self.btn_start_all.setEnabled(False)
    	self.btn_stop_all.setEnabled(False)
    	self.worker = ServiceWorker("stop_all")
    	self.worker.log_signal.connect(self.system_log_view.append)
    	self.worker.done_signal.connect(self._on_services_stopped)
    	self.worker.start()
        
    def edit_configuration(self):
        config_values = ConfigManager.read()
        dialog = ConfigEditorDialog(config_values, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            ConfigManager.save(dialog.get_config_values())
            QMessageBox.information(self, "Success", "Configuration saved!")
            self.system_log_view.append("Configuration updated.")
            self.btn_start_all.setEnabled(True)
            self.btn_stop_all.setEnabled(True)

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(Colors.DARK_BACKGROUND))
    palette.setColor(QPalette.ColorRole.WindowText, QColor(Colors.TEXT))
    palette.setColor(QPalette.ColorRole.Base, QColor(Colors.DARKER_BACKGROUND))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(Colors.DARK_BACKGROUND))
    palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(Colors.DARK_BACKGROUND))
    palette.setColor(QPalette.ColorRole.ToolTipText, QColor(Colors.TEXT))
    palette.setColor(QPalette.ColorRole.Text, QColor(Colors.TEXT))
    palette.setColor(QPalette.ColorRole.Button, QColor(Colors.DARKER_BACKGROUND))
    palette.setColor(QPalette.ColorRole.ButtonText, QColor(Colors.TEXT))
    palette.setColor(QPalette.ColorRole.BrightText, QColor(Colors.ACCENT))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(Colors.PRIMARY))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(Colors.DARK_BACKGROUND))
    app.setPalette(palette)
    force_update_ip_in_config()
    window = ServerManagerUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
