import argparse
from application import Application

def main(args: argparse.Namespace):
    application = Application(args.address, args.width, args.height)
    application.run()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--address', help='Power outage schedule address', type=str, required=True)
    parser.add_argument('--width', help='Window width', type=int, default=480)
    parser.add_argument('--height', help='Window height', type=int, default=320)
    args = parser.parse_args()
    main(args)