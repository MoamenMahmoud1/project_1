import os
import subprocess
import signal
import sys
import platform
# ✨ تأكد من وضع اسم مشروعك الفعلي بدلاً من `project`
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
def is_windows():
    """ التحقق مما إذا كان النظام Windows """
    return platform.system() == "Windows"

def start_postgresql():
    """ تشغيل PostgreSQL Server """
    print("Starting PostgreSQL Server...")
    if is_windows():
        subprocess.run(["pg_ctl", "start", "-D", "C:/Program Files/PostgreSQL/15/data"], shell=True)
    else:
        subprocess.run(["sudo", "service", "postgresql", "start"])

def stop_postgresql():
    """ إيقاف PostgreSQL Server """
    print("\nStopping PostgreSQL Server...")
    if is_windows():
        subprocess.run(["pg_ctl", "stop", "-D", "C:/Program Files/PostgreSQL/15/data"], shell=True)
    else:
        subprocess.run(["sudo", "service", "postgresql", "stop"])

def start_redis():
    """ تشغيل Redis Server """
    print("Starting Redis Server...")
    if is_windows():
        subprocess.Popen(["redis-server"], creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        subprocess.run(["sudo", "service", "redis-server", "start"])

def stop_redis():
    """ إيقاف Redis Server """
    print("\nStopping Redis Server...")
    if is_windows():
        subprocess.run(["taskkill", "/F", "/IM", "redis-server.exe"], shell=True)
    else:
        subprocess.run(["sudo", "service", "redis-server", "stop"])

def stop_servers():
    """ إيقاف كل السيرفرات """
    stop_postgresql()
    stop_redis()
    sys.exit(0)

if __name__ == "__main__":
    # تشغيل PostgreSQL و Redis عند تشغيل Django
    start_postgresql()
    start_redis()

    # التقاط إشارة CTRL+C لإيقاف السيرفرات
    signal.signal(signal.SIGINT, lambda sig, frame: stop_servers())

    # تشغيل Django Server
    try:
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
    except KeyboardInterrupt:
        stop_servers()
