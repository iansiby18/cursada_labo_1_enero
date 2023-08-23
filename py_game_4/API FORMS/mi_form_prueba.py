import pygame
from pygame.locals import *

from GUI_widget import *
from GUI_textbox import *
from GUI_slider import *
from GUI_label import *
from GUI_form import *
from GUI_button import *
from GUI_button_image import *

class FormPrueba(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border = "black", border_size = -1, active = True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.volumen = 0.2
        self.flag_play = True
        pygame.mixer.init()

        ######## CONTROLES ########
        self.txtbox = TextBox(self._slave, x, y, 50, 50, 150, 30, "Gray", "White", "Red", "Blue", 2, font= "Comic Sans", font_size= 15, font_color= "Black")
        self.btn_play = Button(self._slave, x, y,  100, 100, 100, 50, "Red", "Blue", self.btn_play_click, "Nombre", "Pausa", font= "Verdana", font_size= 15, font_color= "White")

        ###########################
        ## LOS AGREGAMOS A LA LISTA ##
        self.lista_widgets.append(self.txtbox)
        self.lista_widgets.append(self.btn_play)

        pygame.mixer.music.load("API FORMS\Vengeance.wav")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        self.render()
    
    def update(self, lista_eventos):
        if self.active:
            self.draw()
            self.render()
            for widget in self.lista_widgets:
                widget.update(lista_eventos)


    def render(self):
        self._slave.fill(self._color_background)
    
    def btn_play_click(self, texto):
        if self.flag_play:
            pygame.mixer.music.pause()
            self.btn_play._color_background = "Cian"
            self.btn_play._font_color = "Red"
            self.btn_play.set_text("Play")
        else:
            pygame.mixer.music.unpause()
            self.btn_play._color_background = "Red"
            self.btn_play._font_color = "White"
            self.btn_play.set_text("Pause")
        self.flag_play = not self.flag_play