from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time

# Pages are responsible for retrieving and passing back data from models to templates and vice versa.
# If you need to show something to a participant or to get his/her input, you need to indicate this in pages.py


class Comp1(Page):
    form_model = 'player'
    form_fields = ['test1','test2']

    timeout_seconds = 120

    def before_next_page(self):
        self.player.set_comp1()
        if self.timeout_happened:
            self.player.timeout_test1 = True


class Comp2(Page):
    def is_displayed(self):
        return self.player.comp1 == 0

    form_model = 'player'
    form_fields = ['test12','test22']

    timeout_seconds = 120

    def before_next_page(self):
        self.player.set_comp2()
        if self.timeout_happened:
            self.player.timeout_test1 = True

class Comp3(Page):

    def is_displayed(self):
        return self.player.comp2 == 0

    form_model = 'player'
    form_fields = ['test13','test23']

    timeout_seconds = 120

    def before_next_page(self):
        self.player.set_comp3()
        if self.timeout_happened:
            self.player.timeout_test1 = True

class Comp3Fail(Page):
    def is_displayed(self):
        return self.player.comp3 == 0


class Introduction(Page):
    def vars_for_template(self):
        return {'treatment1': self.subsession.treatment1,
                'treatment2': self.subsession.treatment2}


class Instruction1(Page):
    def vars_for_template(self):
        return {'treatment1': self.subsession.treatment1,
                'treatment2': self.subsession.treatment2}






# here we indicate in which sequence we want the pages to the played. You can repeat pages as well.
page_sequence = [Introduction,
                 Instruction1,
                 Comp1,
                 Comp2,
                 Comp3,
                 Comp3Fail
                 ]
