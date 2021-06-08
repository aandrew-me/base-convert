from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen


class FirstWindow(Screen):

    decimal = ObjectProperty(None)
    binary = ObjectProperty(None)
    octal = ObjectProperty(None)
    hex = ObjectProperty(None)

    decimal_length = 0
    binary_length = 0
    octal_length = 0
    hex_length = 0

    binary_list = ['0', '1']
    octal_list = ['0', '1', '2', '3', '4', '5', '6', '7']
    hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', 'a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F']

    is_binary = True
    is_octal = True
    is_hex = True

####################
# Testing values   #
####################

    def binary_testing(self):
        self.is_binary = True
        binary = self.binary.text
        binary = list(binary)
        for i in binary:
            if i not in self.binary_list:
                self.is_binary = False
                break

    def octal_testing(self):
        self.is_octal = True
        octal = self.octal.text
        octal = list(octal)
        for i in octal:
            if i not in self.octal_list:
                self.is_octal = False
                break

    def hex_testing(self):
        self.is_hex = True
        hexa = self.hex.text
        hexa = list(hexa)
        for i in hexa:
            if i not in self.hex_list:
                self.is_hex = False
                break

#####################
# Convert methods   #
#####################

    def dec_to_bin(self):
        deci = self.decimal.text
        binary = bin(int(deci))
        binary = binary[2:]
        self.binary.text = binary

    def dec_to_oct(self):
        deci = self.decimal.text
        octal = oct(int(deci))
        octal = octal[2:]
        self.octal.text = octal

    def dec_to_hex(self):
        deci = self.decimal.text
        hexa = hex(int(deci))
        hexa = hexa[2:].upper()
        self.hex.text = hexa

    def bin_to_dec(self):
        binary = self.binary.text
        binary = list(binary)
        binary.reverse()
        decimal = 0
        index = 0
        for i in binary:
            decimal += int(i) * (2 ** index)
            index += 1
        self.decimal.text = str(decimal)

    def oct_to_dec(self):
        octal = self.octal.text
        octal = list(octal)
        octal.reverse()
        decimal = 0
        index = 0
        for i in octal:
            decimal += int(i) * (8 ** index)
            index += 1
        self.decimal.text = str(decimal)

    def hex_to_dec(self):
        hexa = self.hex.text
        hexa = hexa.lower()
        hexa = list(hexa)
        hexa.reverse()
        decimal = 0
        index = 0
        alph = {
            'a': 10,
            'b': 11,
            'c': 12,
            'd': 13,
            'e': 14,
            'f': 15,
        }
        for i in hexa:
            decimal += int(alph.get(i, i)) * (16 ** index)
            index += 1
        self.decimal.text = str(decimal)

    def reset(self):
        self.decimal.text = ''
        self.binary.text = ''
        self.octal.text = ''
        self.hex.text = ''

######################
#   Test and Convert #
######################

    def conversion(self):

        try:
            # from decimal
            if len(self.decimal.text) > 0 and len(self.binary.text) == 0 and len(self.octal.text) == 0 and len(
                    self.octal.text) == 0:
                self.dec_to_bin()
                self.dec_to_oct()
                self.dec_to_hex()

            # from binary
            if len(self.binary.text) > 0 and len(self.decimal.text) == 0 and len(self.octal.text) == 0 and len(
                    self.octal.text) == 0:
                self.binary_testing()
                if self.is_binary:
                    self.bin_to_dec()
                    self.dec_to_oct()
                    self.dec_to_hex()

            # from octal
            if len(self.octal.text) > 0 and len(self.decimal.text) == 0 and len(self.binary.text) == 0 and len(
                    self.hex.text) == 0:
                self.octal_testing()
                if self.is_octal:
                    self.oct_to_dec()
                    self.dec_to_bin()
                    self.dec_to_hex()

            # from hexadecimal
            if len(self.hex.text) > 0 and len(self.decimal.text) == 0 and len(self.binary.text) == 0 and len(
                    self.octal.text) == 0:
                self.hex_testing()
                if self.is_hex:
                    self.hex_to_dec()
                    self.dec_to_bin()
                    self.dec_to_oct()

        except ValueError:
            pass


class WindowManager(ScreenManager):
    pass


class MainWidget(Widget):
    pass


class BaseConverter(App):
    icon = 'icon.png'



BaseConverter().run()
