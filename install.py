import os
import pip
from start_UB import get_req


def installer():
    pip.main(get_req())
    print("\n\nFoxUserBot installed.\nStart FoxUserbot... (if you get error, writte 'python3 main.py' in the terminal)")
    os.system("python main.py" if os.name == "nt" else "python3 main.py")


def check():
    pip.main(get_req())


if __name__ == "__main__":
    installer()
