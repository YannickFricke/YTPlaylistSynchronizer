# Main entry file
from container import Application

if __name__ == '__main__':
    application: Application = Application.Applications.application()
    application.run()
