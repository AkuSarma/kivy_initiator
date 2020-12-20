import os

name = input("Enter the name of the project:")
place = input("Enter path:")

if not name:
    name = "kivy_initiator"
if not place:
    place = os.getcwd()

os.makedirs(f"{place}/{name}")

try:
    with open(f"{place}/{name}/main.py", "w", encoding = 'utf-8') as p:
        p.write(f"from kivy.app import App\nfrom kivy.lang import Builder\nfrom kivy.uix.widget import Widget\n\nBuilder.loadfile('{name}.kv')\n\nclass Main(Widget):\n\tpass\n\nclass MyApp(App):\n\tdef build(self):\n\t\treturn Main()\n\nMyApp().run()")

    with open(f"{place}/{name}/{name}.kv", "w", encoding='utf-8') as k:
        k.write("#:kivy 2.0.0\n\n<Main>:")

except Exception as e:
    print(e)