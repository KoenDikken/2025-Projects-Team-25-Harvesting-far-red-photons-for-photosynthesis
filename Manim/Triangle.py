from manim import *

class animations(Scene):
    def construct(self):
        t = Triangle(color = RED, fill_opacity = 1).scale(2)
        self.play(DrawBorderThenFill(t))
        self.wait(0.5)