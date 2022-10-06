# Question
class Question:
    def __init__(self,text,choises,answer):
        self.text = text
        self.choises = choises
        self.answer = answer
    def chechAnswer(self,answer):
        return self.answer == answer
        
# Quiz
class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex+1}: {question.text}")

        for q in question.choises:
            print('-'+ q)
        
        answer = input('Cevap: ')
        self.quess(answer)
        self.loadQuestion()

    def quess(self,answer):
        question = self.getQuestion()

        if question.chechAnswer(answer):
            self.score +=1
    
        self.questionIndex +=1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print(f"Skorunuz: {self.score}")
    
    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print('Quiz Bitti')
        else:
            print(f" Question {questionNumber}/{totalQuestion} ".center(50,'*'))


q1 = Question('En iyi programlama dili hangisidir',['C#','Python','Java','Javascript'],'Python')
q2 = Question('En Popüler programlama dili hangisidir',['Python','Java','C#','Javascript'],'Java')
q3 = Question('En Çok Kazandıran programlama dili hangisidir',['Javascript','C#','Python','Java'],'Python')
questions = [q1,q2,q3]

quiz = Quiz(questions)
quiz.loadQuestion()
