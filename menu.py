from kivy.app import App
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from functools import partial
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.properties import StringProperty, DictProperty


class MenuButton(ButtonBehavior, BoxLayout):

    # code inspired from:
        # https://github.com/kivy/kivy/wiki/Menu-on-long-touch

    # example use:
        # MenuButton(text = 'Button Text', action = 'function_as_string', options = { 'Option 1': 'function_as_string', 'Option 2': 'other_fun_as_str' } )
        # text will be applied to the buttons label, and action will only occur if the menu isn't triggered
        # in options, the keys are used as the menu options, and their values are the functions you wish to call


    text = StringProperty('')                                                           # stores the button text
    action = StringProperty('')                                                         # stores the button release action
    options = DictProperty({})                                                          # stores menu button text and actions

    def __init__(self, **kwargs):
        super(MenuButton,self).__init__(**kwargs)
        # by default, contains a button and relative layout
        # the menu() function adds the menu to the relative layout
        # this way, the menu can appear below the button
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.button = Button(text=self.text, size_hint_y=None, height=32)
        self.add_widget(self.button)
        self.height = self.button.height
        self.bind(on_touch_down=self.create_clock, on_touch_up=self.delete_clock)
        self.m = RelativeLayout()
        self.m.size_hint_y = None
        self.m.height = 0
        self.add_widget(self.m)

    def create_clock(self, widget, touch, *args):
        if self.children[1].collide_point(touch.x, touch.y):
            callback = partial(self.menu, touch)
            Clock.schedule_once(callback, .3)
            touch.ud['event'] = callback


    def delete_clock(self, widget, touch, *args):
        if self.children[1].collide_point(touch.x, touch.y):
            if 'event' in touch.ud:   # avoid non-existent key errors
                Clock.unschedule(touch.ud['event'])
            if self.m.children == []:
                eval(self.action)

    def menu(self, touch, *args):
        menu = BoxLayout(orientation='vertical')
        height_calc  = 0   # calculate the total height needed when the menu is opened
        for text, fun_pass in self.options.iteritems():
            but = Button(id=fun_pass, text=text, height=32, size_hint_y=None)
            height_calc += but.height
            but.bind(on_release=partial(self.close_menu, menu))
            but.bind(on_release=self.call_function)
            menu.add_widget(but)
        close = Button(text='close', height=32, size_hint_y=None)
        height_calc += close.height
        close.bind(on_release=partial(self.close_menu, menu))
        menu.add_widget(close)
        self.m.add_widget(menu)

        # adjust position and height of expanded MenuButton
        self.m.height = height_calc
        self.height = self.button.height + self.m.height
        self.pos = (0, self.orig_y - self.m.height)

        # make sure this MenuButton is drawn on top of any other MenuButtons
        app = App.get_running_app()
        app.root.remove_widget(self)
        app.root.add_widget(self)


    def close_menu(self, widget, *args):                                                # clears all menu widgets from the relative layout
        self.m.clear_widgets()

        # reset height and position of MenuButton when not expanded
        self.m.height = 0
        self.height = self.button.height
        self.pos = (0, self.orig_y)

    def call_function(self, widget, *args):                                             # calls function in the app by literally evaluating the string
        eval(widget.id)


class Test(App):

    def build(self):
        f = FloatLayout()
        self.mb1 = MenuButton(text='Testing1', action='App.get_running_app().pp("going")', options={ '1': 'App.get_running_app().pp("a")', '2': 'App.get_running_app().pp("b")' } )
        self.mb1.orig_y = f.height - self.mb1.button.height    # save the original y position, so it can be restored later
        self.mb1.pos = (0, self.mb1.orig_y)
        f.add_widget(self.mb1)
        self.mb2 = MenuButton(text='Testing2', action='App.get_running_app().pp("going")', options={ '1': 'App.get_running_app().pp("a")', '2': 'App.get_running_app().pp("b")' } )
        self.mb2.orig_y = f.height - self.mb1.button.height - self.mb2.button.height    # save the original y position, so it can be restored later
        self.mb2.pos = (0, self.mb2.orig_y)
        f.add_widget(self.mb2)
        self.root = f

        f.bind(size=self.sizeChanged)    # handle size adjustments when app is displayed

    def sizeChanged(self, *args):
        # make sure the MenuButtons are always at the top
        self.mb1.orig_y = self.root.height - self.mb1.button.height
        self.mb2.orig_y = self.root.height - self.mb1.button.height - self.mb2.button.height
        self.mb1.pos = (0, self.mb1.orig_y)
        self.mb2.pos = (0, self.mb2.orig_y)

    def pp(self,text):
        print(text)

if __name__ == '__main__':
    Test().run()