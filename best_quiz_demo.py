class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self,answer):
        return self.answer == answer

class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.index = 0

    def get_question(self):
        return self.questions[self.index]

    def display_question(self):
        question=self.get_question() 
        print(f'Soru {self.index + 1}: {question.text} ')

        for q in question.choices:
            print('-'+ q)

        answer = input('Cevap: ')
        self.guess(answer)
        self.load_question()

    def guess(self,answer):
        question = self.get_question()
        if question.check_answer(answer):
            self.score+=1
            
        self.index+=1
    
    def load_question(self):
        if (len(self.questions) == self.index):
            self.show_score()
        else :
            self.display_progress()
            self.display_question()
    def show_score(self):
        print(f'Score : {self.score}')
     
    def display_progress(self):
        total_question=len(self.questions)
        question_number = self.index + 1
        if question_number > total_question:
            print('Quiz bitti')
        else:
            print(f'Question {question_number} of {total_question}'.center(80,'*'))


q1 = Question('En iyi programlama dili hangisidir?',['C#','Python','Java','PHP'],'Python')
q2 = Question('En popüler programlama dili hangisidir?',['C#','Python','Java','PHP'],'Python')
q3 = Question('En çok kazandıran programlama dili hangisidir?',['C#','Python','Java','PHP'],'Python')

questions = [q1,q2,q3]
quiz=Quiz(questions)
quiz.load_question()