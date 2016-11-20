from system.init import initialize_app
import subprocess
application = initialize_app()

if __name__ == "__main__":
	application.run(host='0.0.0.0',port=3001)
