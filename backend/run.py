from project.config import DevelopmentConfig, ProductionConfig
from project import create_app

if __name__ == "__main__":                
    app = create_app(DevelopmentConfig())
    app.run()