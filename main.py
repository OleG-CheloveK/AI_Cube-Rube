import random
from ursina import *
from istochnik import *
from time import sleep


class Game(Ursina):

    def __init__(self):
        super().__init__()
        window.fullscreen = True
        Entity(model='sphere', scale=100, color = color.rgb(175, 192, 215), double_sided=True)
        self.model, self.texture = 'custom_cube', 'rubik_texture'
        EditorCamera()
        camera.world_position = (0, 0, -15)
        self.load_game()

    def load_game(self):
        button1 = Button(
            text='Рандом',
            color=color.rgb(55, 139, 164),
            scale=.15,
            position=(-0.55, -0.39),
            on_click=self.randomposition
        )
        button = Button(
            text='Решить',
            color=color.rgb(55, 139, 164),
            scale = .15,
            position=(-0.75, -0.39),
            on_click=self.reshenie
        )
        button2 = Button(
            text='Действия',
            color=color.rgb(3, 98, 128),
            scale= (0.2, 0.15),
            position=(0.75, 0.39),
            on_click=self.activation
        )
        self.PARENT = Entity(model='cube')
        self.cube = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    if (x == 0) and (y == 0) and (z == 0):
                        continue
                    else:
                        self.cube.append(Entity(model=self.model, texture=self.texture, position=(x, y, z)))
        self.rotq = 0
        self.txt1 = Text(text="Поворот правой грани вверх, вниз = 'q','w'", x=.32, y=.30, color=color.black, scale=1, enabled = False)
        self.txt2 = Text(text="Поворот нижней грани вправо, влево = 'e','r'", x=.32, y=.24, color=color.black, scale=1, enabled = False)
        self.txt3 = Text(text="Поворот верхней грани вправо, влево = 's','a'", x=.32, y=.18, color=color.black, scale=1, enabled = False)
        self.txt4= Text(text="Поворот левой грани вверх, вниз = 'd','f'", x=.32, y=.12, color=color.black, scale=1, enabled = False)
        self.txt5 = Text(text="Поворот передней грани вправо, влево = 'g','t'", x=.32, y=.06, color=color.black, scale=1, enabled = False)
        self.txt6 = Text(text="Поворот задней грани вправо, влево = 'z','x'", x=.32, y=0, color=color.black, scale=1, enabled = False)
        self.r_pressed = False
        self.e_pressed = False
        self.q_pressed = False
        self.a_pressed = False
        self.w_pressed = False
        self.s_pressed = False
        self.d_pressed = False
        self.f_pressed = False
        self.t_pressed = False
        self.g_pressed = False
        self.z_pressed = False
        self.x_pressed = False
        self.c_pressed = False
        self.my_button = Button(text='', on_click=lambda: self.show_info(clown, clown1, clown2, clown3, clown4),scale = (1.1, 0.19), position=(0.32, -0.39), color=color.rgb(232, 237, 231), highlight_color = color.rgb(232, 237, 231), pressed_color = color.rgb(232, 237, 231))
        self.info_text = Text(text='', y=.2, scale=0.7, origin=(-0.3, 30.5), color=color.black, enabled=False)
        self.info_text1 = Text(text='', y=.2, scale=0.7, origin=(-0.3, 32.5), color=color.black, enabled=False)
        self.info_text2 = Text(text='', y=.2, scale=0.7, origin=(-0.3, 34.5), color=color.black, enabled=False)
        self.info_text3 = Text(text='', y=.2, scale=0.7, origin=(-0.3, 36.5), color=color.black, enabled=False)
        self.info_text4 = Text(text='', y=.2, scale=0.7, origin=(-0.3, 38.5), color=color.black, enabled=False)

    def activation(self):
        if self.txt1.enabled == False:
            self.txt5.enabled = True
            self.txt1.enabled = True
            self.txt2.enabled = True
            self.txt3.enabled = True
            self.txt4.enabled = True
            self.txt6.enabled = True
        else:
            self.txt5.enabled = False
            self.txt1.enabled = False
            self.txt2.enabled = False
            self.txt3.enabled = False
            self.txt4.enabled = False
            self.txt6.enabled = False

    def show_info(self, clown, clown1, clown2, clown3, clown4):
        self.info_text.text = clown
        self.info_text1.text = clown1
        self.info_text2.text = clown2
        self.info_text3.text = clown3
        self.info_text4.text = clown4
        self.info_text.enabled = True
        self.info_text1.enabled = True
        self.info_text2.enabled = True
        self.info_text3.enabled = True
        self.info_text4.enabled = True

    def hide_info(self):
        self.info_text.enabled = False

    def reshenie(self):
        decision()
        for i in range(0, len(end_decision)):
            if end_decision[i].__name__ == "back_e_l":
                self.PARENT = Entity(model='cube')
                self.important1()
                for cube in self.cube:
                    if cube.position[2] == 1:
                        cube.parent = self.PARENT
                self.PARENT.rotation_z = -90
                self.important1()
            elif end_decision[i].__name__ == "back_e_r":
                self.PARENT = Entity(model='cube')
                self.important1()
                for cube in self.cube:
                    if cube.position[2] == 1:
                        cube.parent = self.PARENT
                self.PARENT.rotation_z = 90
                self.important1()
            elif end_decision[i].__name__ == "right_e_b":
                self.PARENT = Entity(model='cube')
                self.important1()
                for cube in self.cube:
                    if cube.position[0] == 1:
                        cube.parent = self.PARENT
                self.PARENT.rotation_x = -90
                self.important1()
            elif end_decision[i].__name__ == "right_e_f":
                self.PARENT = Entity(model='cube')
                self.important1()
                for cube in self.cube:
                    if cube.position[0] == 1:
                        cube.parent = self.PARENT
                self.PARENT.rotation_x = 90
                self.important1()
            elif end_decision[i].__name__ == "bot_e_l":
                self.PARENT = Entity(model='cube')
                self.important1()
                for cube in self.cube:
                    if cube.position[1] == -1:
                        cube.parent = self.PARENT
                self.PARENT.rotation_y = 90
                self.important1()
            elif end_decision[i].__name__ == "bot_e_r":
                self.PARENT = Entity(model='cube')
                self.important1()
                for cube in self.cube:
                    if cube.position[1] == -1:
                        cube.parent = self.PARENT
                self.PARENT.rotation_y = -90
                self.important1()
            elif end_decision[i].__name__ == "top_e_r":
                self.PARENT = Entity(model='cube')
                self.important1()
                for cube in self.cube:
                    if cube.position[1] == 1:
                        cube.parent = self.PARENT
                self.PARENT.rotation_y = -90
                self.important1()
            elif end_decision[i].__name__ == "front_e_r":
                self.PARENT = Entity(model='cube')
                self.important1()
                for cube in self.cube:
                    if cube.position[2] == -1:
                        cube.parent = self.PARENT
                self.PARENT.rotation_z = 90
                self.important1()
            elif end_decision[i].__name__ == "front_e_l":
                self.PARENT = Entity(model='cube')
                self.important1()
                for cube in self.cube:
                    if cube.position[2] == -1:
                        cube.parent = self.PARENT
                self.PARENT.rotation_z = -90
                self.important1()
            elif end_decision[i].__name__ == "top_e_l":
                self.PARENT = Entity(model='cube')
                self.important1()
                for cube in self.cube:
                    if cube.position[1] == 1:
                        cube.parent = self.PARENT
                self.PARENT.rotation_y = 90
                self.important1()
            elif end_decision[i].__name__ == "left_e_b":
                self.PARENT = Entity(model='cube')
                self.important1()
                for cube in self.cube:
                    if cube.position[0] == -1:
                        cube.parent = self.PARENT
                self.PARENT.rotation_x = -90
                self.important1()
            elif end_decision[i].__name__ == "left_e_f":
                self.PARENT = Entity(model='cube')
                self.important1()
                for cube in self.cube:
                    if cube.position[0] == -1:
                        cube.parent = self.PARENT
                self.PARENT.rotation_x = 90
                self.important1()
            elif end_decision[i].__name__ == "centre_e_r":
                self.PARENT = Entity(model='cube')
                self.important1()
                for cube in self.cube:
                    if cube.position[1] == 0:
                        cube.parent = self.PARENT
                self.PARENT.rotation_y = -90
                self.important1()
        clown, clown1, clown2, clown3, clown4 = transformation(end_decision)
        self.show_info(clown, clown1, clown2, clown3, clown4)
        combined_list.clear()
        end_decision.clear()

    def input(self, key, is_raw=False):
        if key == 'q':
            if not self.q_pressed:
                right_e_f(list)
                self.important1()
                self.q_pressed = True
                self.rotq = 0
                self.PARENT.rotation = 0
                for cube in self.cube:
                    if cube.position[0] == 1:
                        cube.parent = self.PARENT
                self.rotq += 90
                self.PARENT.animate_rotation_x(self.rotq, duration=0.5)
                self.reallyimportant()
                invoke(self.important, delay=0.6)
                invoke(self.important1, delay=0.6)
        if key == 'w':
            if not self.w_pressed:
                right_e_b(list)
                self.important1()
                self.w_pressed = True
                self.rotq = 0
                self.PARENT.rotation = 0
                for cube in self.cube:
                    if cube.position[0] == 1:
                        cube.parent = self.PARENT
                self.rotq -= 90
                self.PARENT.animate_rotation_x(self.rotq, duration=0.5)
                self.reallyimportant()
                invoke(self.important, delay=0.6)
                invoke(self.important1, delay=0.6)
        if key == 'e':
            if not self.e_pressed:
                bot_e_r(list)
                self.important1()
                self.e_pressed = True
                self.rotq = 0
                self.PARENT.rotation = 0
                for cube in self.cube:
                    if cube.position[1] == -1:
                        cube.parent = self.PARENT
                self.rotq -= 90
                self.PARENT.animate_rotation_y(self.rotq, duration=0.5)
                self.reallyimportant()
                invoke(self.important, delay=0.6)
                invoke(self.important1, delay=0.6)
        if key == 'r':
            if not self.r_pressed:
                bot_e_l(list)
                self.important1()
                self.rotq = 0
                self.PARENT.rotation = 0
                self.r_pressed = True
                for cube in self.cube:
                    if cube.position[1] == -1:
                        cube.parent = self.PARENT
                self.rotq += 90
                self.PARENT.animate_rotation_y(self.rotq, duration=0.5)
                self.reallyimportant()
                invoke(self.important, delay=0.6)
                invoke(self.important1, delay=0.6)
        if key == 'a':
            if not self.a_pressed:
                top_e_l(list)
                self.important1()
                self.rotq = 0
                self.PARENT.rotation = 0
                self.a_pressed = True
                for cube in self.cube:
                    if cube.position[1] == 1:
                        cube.parent = self.PARENT
                self.rotq += 90
                self.PARENT.animate_rotation_y(self.rotq, duration=0.5)
                self.reallyimportant()
                invoke(self.important, delay=0.6)
                invoke(self.important1, delay=0.6)
        if key == 's':
            if not self.s_pressed:
                top_e_r(list)
                self.important1()
                self.rotq = 0
                self.PARENT.rotation = 0
                self.s_pressed = True
                for cube in self.cube:
                    if cube.position[1] == 1:
                        cube.parent = self.PARENT
                self.rotq -= 90
                self.PARENT.animate_rotation_y(self.rotq, duration=0.5)
                self.reallyimportant()
                invoke(self.important, delay=0.6)
                invoke(self.important1, delay=0.6)
        if key == 'd':
            if not self.d_pressed:
                left_e_f(list)
                self.important1()
                self.rotq = 0
                self.PARENT.rotation = 0
                self.d_pressed = True
                for cube in self.cube:
                    if cube.position[0] == -1:
                        cube.parent = self.PARENT
                self.rotq += 90
                self.PARENT.animate_rotation_x(self.rotq, duration=0.5)
                self.reallyimportant()
                invoke(self.important, delay=0.6)
                invoke(self.important1, delay=0.6)
        if key == 'f':
            if not self.f_pressed:
                left_e_b(list)
                self.important1()
                self.rotq = 0
                self.PARENT.rotation = 0
                self.f_pressed = True
                for cube in self.cube:
                    if cube.position[0] == -1:
                        cube.parent = self.PARENT
                self.rotq -= 90
                self.PARENT.animate_rotation_x(self.rotq, duration=0.5)
                self.reallyimportant()
                invoke(self.important, delay=0.6)
                invoke(self.important1, delay=0.6)
        if key == 't':
            if not self.t_pressed:
                front_e_l(list)
                self.important1()
                self.rotq = 0
                self.PARENT.rotation = 0
                self.t_pressed = True
                for cube in self.cube:
                    if cube.position[2] == -1:
                        cube.parent = self.PARENT
                self.rotq -= 90
                self.PARENT.animate_rotation_z(self.rotq, duration=0.5)
                self.reallyimportant()
                invoke(self.important, delay=0.6)
                invoke(self.important1, delay=0.6)
        if key == 'g':
            if not self.g_pressed:
                front_e_r(list)
                self.important1()
                self.rotq = 0
                self.PARENT.rotation = 0
                self.g_pressed = True
                for cube in self.cube:
                    if cube.position[2] == -1:
                        cube.parent = self.PARENT
                self.rotq += 90
                self.PARENT.animate_rotation_z(self.rotq, duration=0.5)
                self.reallyimportant()
                invoke(self.important, delay=0.6)
                invoke(self.important1, delay=0.6)
        if key == 'z':
            if not self.z_pressed:
                back_e_r(list)
                self.important1()
                self.rotq = 0
                self.PARENT.rotation = 0
                self.z_pressed = True
                for cube in self.cube:
                    if cube.position[2] == 1:
                        cube.parent = self.PARENT
                self.rotq += 90
                self.PARENT.animate_rotation_z(self.rotq, duration=0.5)
                self.reallyimportant()
                invoke(self.important, delay=0.6)
                invoke(self.important1, delay=0.6)
        if key == 'x':
            if not self.x_pressed:
                back_e_l(list)
                self.important1()
                self.rotq = 0
                self.PARENT.rotation = 0
                self.x_pressed = True
                for cube in self.cube:
                    if cube.position[2] == 1:
                        cube.parent = self.PARENT
                self.rotq -= 90
                self.PARENT.animate_rotation_z(self.rotq, duration=0.5)
                self.reallyimportant()
                invoke(self.important, delay=0.6)
                invoke(self.important1, delay=0.6)

        if key == 'c':
            if not self.c_pressed:
                centre_e_r(list)
                self.important1()
                self.rotq = 0
                self.PARENT.rotation = 0
                self.c_pressed = True
                for cube in self.cube:
                    if cube.position[1] == 0:
                        cube.parent = self.PARENT
                self.rotq -= 90
                self.PARENT.animate_rotation_y(self.rotq, duration=0.5)
                self.reallyimportant()
                invoke(self.important, delay=0.6)
                invoke(self.important1, delay=0.6)

        super().input(key)

    def reallyimportant(self):
        self.c_pressed = True
        self.x_pressed = True
        self.z_pressed = True
        self.g_pressed = True
        self.r_pressed = True
        self.e_pressed = True
        self.q_pressed = True
        self.a_pressed = True
        self.w_pressed = True
        self.s_pressed = True
        self.d_pressed = True
        self.f_pressed = True
        self.t_pressed = True

    def important(self):
        self.c_pressed = False
        self.x_pressed = False
        self.z_pressed = False
        self.g_pressed = False
        self.r_pressed = False
        self.e_pressed = False
        self.q_pressed = False
        self.a_pressed = False
        self.w_pressed = False
        self.s_pressed = False
        self.d_pressed = False
        self.f_pressed = False
        self.t_pressed = False

    def important1(self):
        for cube in self.cube:
            world_pos1, world_rot1 = round(cube.world_position, 1), cube.world_rotation
            cube.parent = scene
            cube.position, cube.rotation = world_pos1, world_rot1


    def one(self):
        right_e_f(list)
        self.PARENT = Entity(model='cube')
        for cube in self.cube:
            if cube.position[0] == 1:
                cube.parent = self.PARENT
        self.PARENT.rotation_x = 90
        self.important1()

    def two(self):
        right_e_b(list)
        self.PARENT = Entity(model='cube')
        for cube in self.cube:
            if cube.position[0] == 1:
                cube.parent = self.PARENT
        self.PARENT.rotation_x = -90
        self.important1()

    def three(self):
        bot_e_l(list)
        self.PARENT = Entity(model='cube')
        for cube in self.cube:
            if cube.position[1] == -1:
                cube.parent = self.PARENT
        self.PARENT.rotation_y = 90
        self.important1()

    def four(self):
        bot_e_r(list)
        self.PARENT = Entity(model='cube')
        for cube in self.cube:
            if cube.position[1] == -1:
                cube.parent = self.PARENT
        self.PARENT.rotation_y= -90
        self.important1()

    def five(self):
        top_e_l(list)
        self.PARENT = Entity(model='cube')
        for cube in self.cube:
            if cube.position[1] == 1:
                cube.parent = self.PARENT
        self.PARENT.rotation_y= 90
        self.important1()

    def six(self):
        top_e_r(list)
        self.PARENT = Entity(model='cube')
        for cube in self.cube:
            if cube.position[1] == 1:
                cube.parent = self.PARENT
        self.PARENT.rotation_y = -90
        self.important1()


    def seven(self):
        left_e_f(list)
        self.PARENT = Entity(model='cube')
        for cube in self.cube:
            if cube.position[0] == -1:
                cube.parent = self.PARENT
        self.PARENT.rotation_x = 90
        self.important1()

    def eight(self):
        left_e_b(list)
        self.PARENT = Entity(model='cube')
        for cube in self.cube:
            if cube.position[0] == -1:
                cube.parent = self.PARENT
        self.PARENT.rotation_x = -90
        self.important1()
    def nine(self):
        front_e_r(list)
        self.PARENT = Entity(model='cube')
        for cube in self.cube:
            if cube.position[2] == -1:
                cube.parent = self.PARENT
        self.PARENT.rotation_z = 90
        self.important1()

    def ten(self):
        front_e_l(list)
        self.PARENT = Entity(model='cube')
        for cube in self.cube:
            if cube.position[2] == -1:
                cube.parent = self.PARENT
        self.PARENT.rotation_z = -90
        self.important1()
    def eleven(self):
        back_e_r(list)
        self.PARENT = Entity(model='cube')
        for cube in self.cube:
            if cube.position[2] == 1:
                cube.parent = self.PARENT
        self.PARENT.rotation_z = 90
        self.important1()

    def twelve(self):
        back_e_l(list)
        self.PARENT = Entity(model='cube')
        for cube in self.cube:
            if cube.position[2] == 1:
                cube.parent = self.PARENT
        self.PARENT.rotation_z = -90
        self.important1()



    def randomposition(self):
        for i in range(0, 15):
            rand = random.randint(1, 12)
            if rand == 1:
                self.one()
            if rand == 2:
                self.two()
            if rand == 3:
                self.three()
            if rand == 4:
                self.four()
            if rand == 5:
                self.five()
            if rand == 6:
                self.six()
            if rand == 7:
                self.seven()
            if rand == 8:
                self.eight()
            if rand == 9:
                self.nine()
            if rand == 10:
                self.ten()
            if rand == 11:
                self.eleven()
            if rand == 12:
                self.twelve()

if __name__ == '__main__':
    game = Game()
    game.run()
