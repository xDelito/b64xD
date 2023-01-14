<hr><h1>
<p align="center">
b64xD
</p>
<hr>

# **Base64 encrypt .exe files**

This project is a desktop application developed in Python that allows for encrypting .exe files in base64.

The application features a graphical user interface (GUI) developed with Tkinter, where the user can select a .exe file, encrypt it in base64, and view the result in a pop-up window. It also has a button to copy the result to the clipboard and a custom icon for the application.

To use the application, you can either use the Python script or the generated .exe executable file. If you choose to use the script, you will need to have Python installed on your machine, along with the Tkinter and base64 libraries. To run the script, open the terminal or cmd and execute the command:
```
python b64xD.py
```
If you choose to use the .exe file, you don't need to have Python installed, just double click on the executable file and it will launch the application.

To convert the script to a .exe executable file, it is recommended to use the "pyinstaller" tool as follows:
```
pyinstaller --onefile --noconsole --icon=C:/b64xD/icon.ico .\b64xD.py
```
**Note that the icon file must be in the same folder as the script.**

I hope this project is useful for you, if you have any questions or suggestions, please don't hesitate to contact me.
