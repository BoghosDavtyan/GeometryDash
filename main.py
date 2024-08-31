from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.clock import Clock
from kivy.core.window import Window
from random import randint


class GeometryDashGame(Widget):
    player = ObjectProperty(None)
    obstacle = ObjectProperty(None)
    score = NumericProperty(0)
    score_text = StringProperty("Score: 0")

    def __init__(self, **kwargs):
        super(GeometryDashGame, self).__init__(**kwargs)
        self.gravity = -0.5
        self.jump_strength = 15
        self.player_velocity = 0
        Window.bind(on_key_down=self.on_key_down)

    def on_key_down(self, window, key, *args):
        if key == 32:
            self.jump()

    def jump(self):
        if self.player.y == 0:
            self.player_velocity = self.jump_strength

    def update(self, dt):
        self.player_velocity += self.gravity
        self.player.y += self.player_velocity

        if self.player.y < 0:
            self.player.y = 0
            self.player_velocity = 0

        self.obstacle.x -= 4
        if self.obstacle.x < -self.obstacle.width:
            self.obstacle.x = self.width
            self.obstacle.height = randint(50, 200)
            self.score += 1
            self.score_text = f"Score: {self.score}"

        if self.player.collide_widget(self.obstacle):
            print("Game Over! Final Score:", self.score)
            App.get_running_app().stop()


class Player(Widget):
    pass


class Obstacle(Widget):
    pass


class GeometryDashApp(App):
    def build(self):
        game = GeometryDashGame()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    GeometryDashApp().run()
