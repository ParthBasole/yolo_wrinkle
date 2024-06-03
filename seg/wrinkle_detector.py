import argparse
from detect import parse_opt, run

class WrinkleDetector:
    @staticmethod
    def get_wrinkles(source, weights_path,name):
        print(weights_path)
        print(source)
        print(name)
        parser = argparse.ArgumentParser(description='Wrinkle Detection Tool')
        args = parser.parse_args()
        print(**vars(args))
        opt = parse_opt()
        run(source=source, weights=weights_path,name=name)

def main():
    parser = argparse.ArgumentParser(description='Wrinkle Detection Tool')
    parser.add_argument('--source', type=str, help='Path to the image or video for wrinkle detection')
    parser.add_argument('--weights_path', type=str, help='Path to the weights file for the detection model')
    parser.add_argument('--name', type=str, help='Model Name')



    WrinkleDetector.get_wrinkles(args.source, args.weights_path,args.name)

if __name__ == "__main__":
    main()
