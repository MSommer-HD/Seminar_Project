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
This is the second out of three experiments for the Seminar on Experimental Economics in the WS 2020 at the AWI Heidelberg
"""


class Constants(BaseConstants):

    # Here we define the different values that are valid in every form of the game.

    name_in_url = 'Introduction'#The name can be set to whatever you want it to be. It will show in the URL.
    players_per_group = None #Players per group can be set here. In our case the we play a one-shot three person game. You can change this to any INT. Just make sure you change it in the settings tab as well.
    num_rounds = 1 # You can play more than one round, but in our case we play one.
    pool = 30 #This defines how big the pool is. You can use any INT or String here
    efficiency_factor = 2 # This is a INT that indicates how the resource increases the leftover points. You can use any INT or String here
    base= 30/100 #This is the baseline for the tipping point. The first number indicates the percentage, which you can adjust.
    addition_per_give = 2/100 #This is the percentage the tipping point will increase per point taken. The first number indicates the percentage, which you can adjust.
    common_pool = 0 #This is the common pool that is empty at the beginning
    fee = 1 # Show up fee in USD
    per_point = 0.12 # Amount of USD players get for every point
    max = 10
    # np.floor rounds it down and int converts it to an integer. The last step is not necessary, but it looks better.
    completion_code = 142675 # Please change this number in your live version. This is just a random code all participants in the live version get
    #after they complete the experiment.

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


    give = models.IntegerField(label="How many points do you want to give?")

    def give_choices(self):
        return range(11)

    completion_code = models.IntegerField() # Do not worry about this. it does not effect the functionality

    #Now we implement the test questions. For this we use radioselect and a couple of choices.

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

    timeout_framing = models.BooleanField(initial=False)
    timeout_welcome = models.BooleanField(initial=False)
    timeout_test1 = models.BooleanField(initial=False)
    timeout_result1 = models.BooleanField(initial=False)
    timeout_test2 = models.BooleanField(initial=False)
    timeout_result2 = models.BooleanField(initial=False)
    timeout_test1_init = models.BooleanField(initial=False)
    timeout_welcome2 = models.BooleanField(initial=False)

