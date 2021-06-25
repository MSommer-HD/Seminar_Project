from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
)

# Numpy is a mathematical python library which is used from more complex calculations. When we want to call it we can use np.
import numpy as np

author = 'Moritz Sommerlad'

doc = """

"""


class Constants(BaseConstants):

    # Here we define the different values that are valid in every form of the game.

    name_in_url = 'Introduction'#The name can be set to whatever you want it to be. It will show in the URL.
    players_per_group = None #Players per group can be set here. In our case the we play a one-shot three person game. You can change this to any INT. Just make sure you change it in the settings tab as well.
    num_rounds = 1 # You can play more than one round, but in our case we play one.


class Subsession(BaseSubsession): # Ideally you do not need to change anything here.

    treatment1 = models.BooleanField()
    treatment2 = models.BooleanField()


    def creating_session(self):
        self.treatment1 = self.session.config.get('treatment1')
        self.treatment2 = self.session.config.get('treatment2')
        self.session.vars['treatment1'] = self.session.config.get('treatment1')
        self.session.vars['treatment2'] = self.session.config.get('treatment2')



class Group(BaseGroup):
    pass

class Player(BasePlayer):







    test1 = models.IntegerField(choices=[[0,'False'],[1,'True']], widget=widgets.RadioSelect() , label="Text for Question 1")
    test2 = models.IntegerField(choices=[[0,'False'],[1,'True']], widget=widgets.RadioSelect() , label="Text for Question 2")
    test12 = models.IntegerField(choices=[[0,'False'],[1,'True']], widget=widgets.RadioSelect() , label="Text for Question 1")
    test22 = models.IntegerField(choices=[[0,'False'],[1,'True']], widget=widgets.RadioSelect() , label="Text for Question 2")
    test13 = models.IntegerField(choices=[[0,'False'],[1,'True']], widget=widgets.RadioSelect() , label="Text for Question 1")
    test23 = models.IntegerField(choices=[[0,'False'],[1,'True']], widget=widgets.RadioSelect() , label="Text for Question 2")
    comp1 = models.IntegerField()
    comp2 = models.IntegerField()
    comp3 = models.IntegerField()

    def set_comp1(self):
        if self.test1 == 1 and self.test2 == 1:
            self.comp1 = 1
        else:
            self.comp1 = 0

    def set_comp2(self):
        if self.test12 == 1 and self.test22 == 1:
            self.comp2 = 1
        else:
            self.comp2 = 0

    def set_comp3(self):
        if self.test13 == 1 and self.test23 == 1:
            self.comp3 = 1
        else:
            self.comp3 = 0
    #Now we implement a boolean condition for timeouts for all pages



