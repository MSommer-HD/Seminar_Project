from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

# Numpy is a mathematical python library which is used from more complex calculations. When we want to call it we can use np.
import numpy as np

author = 'Moritz Sommerlad'

doc = """

"""


class Constants(BaseConstants):

    # Here we define the different values that are valid in every form of the game.

    name_in_url = 'Decision'#The name can be set to whatever you want it to be. It will show in the URL.
    players_per_group = 2 #Players per group can be set here. In our case the we play a one-shot three person game. You can change this to any INT. Just make sure you change it in the settings tab as well.
    num_rounds = 1 # You can play b more than one round, but in our case we play one.
    fee = 1 # Show up fee in USD
    completion_code = 142675

class Subsession(BaseSubsession):

        def group_by_arrival_time_method(self, waiting_players):
                if len(waiting_players) >= 2:
                    return waiting_players[:2]


class Group(BaseGroup):



    groupdecision = models.IntegerField()
    def set_groupdecision(self):
        if self.session.vars['treatment1'] == False:
            self.groupdecision = self.manager_decision
        else:
            if self.session.vars['treatment2'] == False:
                if self.worker_veto == 1:
                    self.groupdecision = 0
                else:
                    self.groupdecision = self.manager_decision
            else:
                if self.worker_decision == self.manager_decision:
                    self.groupdecision = self.manager_decision
                else:
                    self.groupdecision = 0


    def set_payoffs(self):


        if sum([p.alone for p in self.get_players()]) > 0:
                self.total_points_given = sum([p.give for p in self.get_players()]) + self.otherplayer1_give + self.otherplayer2_give
                self.resource_share = np.round(self.total_points_given * Constants.efficiency_factor / Constants.players_per_group, 0)
        else:
                self.total_points_given =  sum([p.give for p in self.get_players()])
                self.resource_share = np.round(self.total_points_given * Constants.efficiency_factor / Constants.players_per_group, 0)

        if self.breakdown == True:
            for p in self.get_players():
                p.payoff = (Constants.max - p.give)
        else:
            for p in self.get_players():
                p.payoff = sum([+ (Constants.max - p.give),
                                + self.resource_share,
                                ])

    worker_decision = models.IntegerField(choices=[[0,'Comply'],[1,'Cheat']], initial= 0, widget=widgets.RadioSelect() , label="What do you choose?",blank=True)
    manager_decision = models.IntegerField(choices=[[0,'Comply'],[1,'Cheat']], initial= 0, widget=widgets.RadioSelect() , label="What do you choose?")
    worker_feedback = models.IntegerField(choices=[[0,'I like your choice'],[1,"I don't like your choice"],[3,"send no message"]],
                                          widget=widgets.RadioSelect() , label="Which feedback do you, as worker, want to send to the manager?",blank=True)
    worker_veto = models.IntegerField(choices=[[0,'no (team will cheat)'], [1,'yes (team will comply and $0.10 are deducted from your payoff)']],
                                          widget=widgets.RadioSelect(), label="Do you want to veto the decision of the manager", blank=True)
class Player(BasePlayer):


    worker_decision = models.IntegerField(choices=[[0,'Comply'],[1,'cheat']], initial= 0, widget=widgets.RadioSelect() , label="What do you choose?",blank=True)

    def role(self):
        if self.id_in_group == 1:
            return 'Manager'
        if self.id_in_group == 2:
            return 'Worker'

    timeout_give = models.BooleanField(initial=False)
    timeout_questions = models.BooleanField(initial=False)


    question1 = models.IntegerField(widget=widgets.Slider, min=0, max=19, initial=0, label="")
    question2 = models.IntegerField(widget=widgets.Slider, min=0, max=100, initial=0, label="")
    question3 = models.IntegerField(choices=[[0,'to comply'],[1,'to cheat']], widget=widgets.RadioSelect() , label="In your own opinion - what is the morally right thing:?")
    question4 = models.IntegerField(min=14, max=120, label="What is your age?")
    question5 = models.IntegerField(choices=["Male","Famale","Other","Prefer not to tell"],
                                          widget=widgets.RadioSelect(), label="What is your gender?")
    question6 = models.IntegerField(choices=["Less than high school degree","High School degree or equivalent (e.g. GED)",
                                             "Some college, but no degree","Associate degree","Bachelor degree","Graduate degree"],
                                    widget=widgets.RadioSelect(), label="What is the highest level of school you have completed or the highest degree you have received?")

    question8 = models.IntegerField(widget=widgets.Slider, min=0, max=10, initial=0, label="")