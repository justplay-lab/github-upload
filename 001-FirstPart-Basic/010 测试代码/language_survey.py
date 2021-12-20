#coding=gbk
#
# ver 11.2.2

from survey import AnonymouseSurvey

# ����һ�����⣬������һ����ʾ�����AnonymousSurvey����
question = "What language did you first learn to speak?"
my_survey = AnonymouseSurvey(question)

# ��ʾ���Ⲣ�洢��
my_survey.show_question()
print("Enter 'q' at any time to quit.\n") 
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# ��ʾ������
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
