from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Grouping(WaitPage):
    group_by_arrival_time = True

    body_text = "Waiting for one other participants to begin the real task.\
      This wait should be fairly short, though in some cases it could last a couple of minutes (max 5 min)."

    def before_next_page(self):
        self.player.role()

class Manager(Page):

    def is_displayed(self):
        return self.player.id_in_group == 1

    form_model = 'group'
    form_fields = ['manager_decision']

    def vars_for_template(self):
        return {'treatment1': self.session.vars['treatment1'],
                'treatment2': self.session.vars['treatment2']}





class ManagerFeedback(Page):

    def is_displayed(self):
        return self.player.id_in_group == 1

    def vars_for_template(self):
        return {'treatment1': self.session.vars['treatment1'],
                'treatment2': self.session.vars['treatment2'],
                'mdecision': self.group.manager_decision,
                'wdecision': self.group.worker_decision,
                'wfeedback':self.group.worker_feedback,
                'wveto':self.group.worker_veto}





class Worker(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2

    form_model = 'group'
    form_fields = ['worker_decision']


    def vars_for_template(self):
        return {'treatment1': self.session.vars['treatment1'],
                'treatment2': self.session.vars['treatment2'],
                'id': self.player.id_in_group}





class WorkerFeedback(Page):
    def is_displayed(self):
        return self.player.id_in_group == 2

    form_model = 'group'
    form_fields = ['worker_veto','worker_feedback']

    def vars_for_template(self):
        return {'treatment1': self.session.vars['treatment1'],
                'treatment2': self.session.vars['treatment2'],
                'mdecision': self.group.manager_decision,
                'wfeedback':self.group.worker_feedback,
                'wveto':self.group.worker_veto}


    def before_next_page(self):
        self.group.set_groupdecision()


class Wait1(WaitPage):
    body_text = "Please wait while we match your action to your co-player’s action."

class Wait2(WaitPage):
    body_text = "Please wait while we match your action to your co-player’s action."

class Results(Page):
    def vars_for_template(self):
        return {'groupdecision':self.group.groupdecision}

class Questions(Page):

    form_model = 'player'
    form_fields = ['question3','question4','question5','question6',]










page_sequence = [Grouping,
                 Manager,
                 Worker,
                 Wait1,
                 WorkerFeedback,
                 Wait2,
                 ManagerFeedback,
                 Results,
                 Questions]
