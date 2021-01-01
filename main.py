import os
import argparse
import sys


def createTheKvFiles(args):
    if args.n == None:
        args.n = "Trial"
    if args.p == None:
        args.p = os.getcwd()

    try:
        os.makedirs(f"{args.p}/{args.n}")

        with open(f"{args.p}/{args.n}/main.py", "w", encoding = 'utf-8') as p:
            p.write(f"from kivy.app import App\nfrom kivy.lang import Builder\nfrom kivy.uix.widget import Widget\n\nBuilder.load_file('{args.n}.kv')\n\nclass Main(Widget):\n\tpass\n\nclass MyApp(App):\n\tdef build(self):\n\t\treturn Main()\n\nMyApp().run()")

        with open(f"{args.p}/{args.n}/{args.n}.kv", "w", encoding='utf-8') as k:
            k.write("#:kivy 2.0.0\n\n<Main>:")
        
        return "Done"

    except Exception as e:
        whyNotDone = e
        return whyNotDone

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Name for your file")
    parser.add_argument('--n', type=str, default=None, help="Enter name of the project")
    parser.add_argument('--p', type=str, default=None, help="Enter path of the project")

    args = parser.parse_args()
    print(args)

    sys.stdout.write(str(createTheKvFiles(args)))