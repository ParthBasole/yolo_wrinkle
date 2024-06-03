import argparse

from segment.predict import run_default,run

class WrinkleDetector:
    @staticmethod
    def get_wrinkles(source, weights_path,name):
        return run_default(source,weights_path,name)

def main():
    parser = argparse.ArgumentParser(description='Wrinkle Detection Tool')
    parser.add_argument('--source', type=str, help='Path to the image or video for wrinkle detection')
    parser.add_argument('--weights_path', type=str, help='Path to the weights file for the detection model')
    parser.add_argument('--name', type=str, help='Model Name')
    args = parser.parse_args()

    print(WrinkleDetector.get_wrinkles(args.source, args.weights_path,args.name))

if __name__ == "__main__":
    main()
