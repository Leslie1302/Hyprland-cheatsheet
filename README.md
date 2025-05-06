Hyprland Cheat Sheet Web App
============================

This is a lightweight Flask web app that displays a custom cheat sheet for Hyprland keybindings. It's meant for local use as a quick reference while using your tiling window manager.

Features
--------
- Keybindings organized by category (window management, workspaces, media, etc.)
- Clean, readable HTML layout
- Simple to run and modify
- Fully local – no internet required

Requirements
------------
- Python 3.7+
- Flask

Installation
------------
1. Clone or download this repo:
   git clone https://github.com/Leslie1302/hyprland-cheatsheet.git
   cd hyprland-cheatsheet

2. Install Flask if not already installed:
   pip install flask

3. Run the app:
   python app.py

4. Open your browser and visit:
   http://localhost:5000

File Structure
--------------
hyprland-cheatsheet/
├── app.py

├── templates/

│   └── cheatsheet.html

└── README.txt

Customization
-------------
To edit or update your keybindings, just open the `templates/cheatsheet.html` file and adjust the tables as needed.

License
-------
MIT – do whatever you want, just give credit if you share it.

Made with love by Leslie Nii-Adjetey.
