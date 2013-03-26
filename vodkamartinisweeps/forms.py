from django import forms
#from django.core.urlresolvers import reverse
from .models import Sweep, SweepEntry

class SweepEntryForm(forms.Form):

    #def __init__(self, author, quiz_id=0, request=None, *args, **kwargs):
    #    super(SweepEntryForm, self).__init__(*args, **kwargs)
    #    self.quiz_id = quiz_id
    #    self.request = request

    title = forms.CharField()
    #body = forms.CharField(widget=forms.Textarea, label='Enter a description for your quiz')

    #def save(self):
    #    quiz = {'title': self.cleaned_data['title'], 'body': self.cleaned_data['body']}
    #    return quiz

    #def save(self):
    #    if self.quiz_id:
    #        """ existing quiz, no need to change author or status """
    #        quiz = Quiz.objects.get(pk=self.quiz_id)
    #        quiz.title = self.cleaned_data['title']
    #        quiz.body = self.cleaned_data['body']
    #    else:
    #        quiz = Quiz(title=self.cleaned_data['title'], body=self.cleaned_data['body'], author=self.author, status=Quiz.LIVE_STATUS)

    #    quiz.save()

    #    return quiz

#class QuestionForm(forms.Form):
#
#    answer = forms.ModelChoiceField(queryset=Answer.objects.none(), widget=forms.RadioSelect, empty_label=None, label='What would be your answer?')
#
#    def __init__(self, *args, **kwargs):
#        """
#        Notice how we need to call __init__ from superclass first, if we don't do this
#        then we won't be able to access attributes such as fields and instance.
#        """
#        super(QuestionForm, self).__init__(*args, **kwargs)
#        if self.initial:
#            self.question = self.initial['question']
#            self.user = self.initial['user']
#            self.next_question_id = self.initial['next_question_id']
#            self.fields['answer'].queryset = self.question.answer_set.all().order_by('letter')
#
#    def save(self):
#        try:
#            userquizanswer = UserQuizAnswer.objects.get(user=self.user, quiz=self.question.quiz, answer__question=self.question)
#            userquizanswer.answer = self.cleaned_data['answer']
#        except UserQuizAnswer.DoesNotExist:
#            userquizanswer = UserQuizAnswer(user=self.user, quiz=self.question.quiz, answer=self.cleaned_data['answer'])
#        userquizanswer.save()
#
#        if self.next_question_id:
#            success_url = reverse('vodkamartiniquiz_question_detail', kwargs={'slug': self.question.quiz.slug, 'pk': self.next_question_id})
#        else:
#            success_url = reverse('vodkamartiniquiz_quizresult_detail', kwargs={'slug': self.question.quiz.slug})
#        return success_url
#
#    #def save(self):
#    #    if self.question_id:
#    #        """ existing question, no need to change author or status """
#    #        question = Question.objects.get(pk=self.question_id)
#    #        question.title = self.cleaned_data['title']
#    #        question.body = self.cleaned_data['body']
#    #    else:
#    #        question = Question(title=self.cleaned_data['title'], body=self.cleaned_data['body'], author=self.author, status=Question.LIVE_STATUS)
#
#    #    question.save()
#
#    #    return question
