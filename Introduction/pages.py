from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time

# Pages are responsible for retrieving and passing back data from models to templates and vice versa.
# If you need to show something to a participant or to get his/her input, you need to indicate this in pages.py

#If you want to display something other than text (e.g. a variable) you need to use the function
#vars_for_template and make it return a dictionary. The index of the dictionary can then be used to display it on the page with {{ index }}.
# it is key that you indicate from which model you return a variable, here our treatment is defined on the subsession level while the pool is defined in the constants
class Welcome(Page):

    def vars_for_template(self):
        return {'pool': Constants.pool,
                'players': 3,
                'factor': Constants.efficiency_factor,
                'max': Constants.max,
                'treatment': self.subsession.treatment,
                'base': Constants.base*100,
                'addition_per_give': Constants.addition_per_give*100,
                'show_up_fee': Constants.fee,
                'per_point': Constants.per_point}

    timeout_seconds = 120

    def before_next_page(self):
        if self.timeout_happened:
            self.player.timeout_welcome = True

# I split the Pages for the comprehension tests since the structure looks nicer. Does not have a practical meaning.
# For each Question and Answer pair i created a new page. You can decide if you want to show the page by the
# id _displayed line.

## a form field is something the participant can interact with. Since we defined it on a player level, we must specify it in the form_model section.

class Test1_init(Page):
    form_model = 'player'

    timeout_seconds = 120

    def before_next_page(self):
        if self.timeout_happened:
            self.player.timeout_test1_init = True

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

class Results_Test1(Page):
    def vars_for_template(self):
        return {'test1': self.player.test1}

    timeout_seconds = 120

    def before_next_page(self):
        if self.timeout_happened:
            self.player.timeout_result1 = True

class Results_Test2(Page):
    def vars_for_template(self):
        return {'test2': self.player.test2}

    timeout_seconds = 120

    def before_next_page(self):
        self.participant.vars['wait_page_arrival'] = time.time()
        if self.timeout_happened:
            self.player.timeout_result2 = True





# Page for Framing.
class Introduction(Page):
    def vars_for_template(self):
        return {'treatment1': self.subsession.treatment1,
                'treatment2': self.subsession.treatment2}


class Instruction1(Page):
    def vars_for_template(self):
        return {'treatment1': self.subsession.treatment1,
                'treatment2': self.subsession.treatment2}

class Welcome2(Page):

    form_model = 'player'

    timeout_seconds = 120

    def before_next_page(self):
        if self.timeout_happened:
            self.player.timeout_welcome2 = True





# here we indicate in which sequence we want the pages to the played. You can repeat pages as well.
page_sequence = [Introduction,
                 Instruction1,
                 Comp1,
                 Comp2,
                 Comp3,
                 Comp3Fail
                 ]
