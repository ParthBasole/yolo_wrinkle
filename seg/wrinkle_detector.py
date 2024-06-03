import argparse
from detect import parse_opt, run

class WrinkleDetector:
    @staticmethod
    def get_wrinkles(source, weights_path,name):
        parser = argparse.ArgumentParser(description='Wrinkle Detection Tool')
        print(weights_path)
        print(source)
        print(name)
        args = parser.parse_args()
        opt = parse_opt()
        run(**vars(opt))

def main():
    parser = argparse.ArgumentParser(description='Wrinkle Detection Tool')
    parser.add_argument('--source', type=str, help='Path to the image or video for wrinkle detection')
    parser.add_argument('--weights_path', type=str, help='Path to the weights file for the detection model')
    parser.add_argument('--name', type=str, help='Model Name')

    args = parser.parse_args()

    WrinkleDetector.get_wrinkles(args.source, args.weights_path,args.name)

if __name__ == "__main__":
    main()
