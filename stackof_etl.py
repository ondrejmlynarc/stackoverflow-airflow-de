
from stackapi import StackAPI
import pandas as pd
SITE = StackAPI('stackoverflow')


# Fetch questions meeting specific criteria
questions = SITE.fetch(
    'questions',
    min=30,            # Minimum score of 20

    tagged='cloud',    # Questions tagged with 'cloud'
    sort='votes',
    pagesize = 50
    )

print(questions)



question_list = []
for question in questions['items']:
    question_data = {
        'question_id': question['question_id'],
        'title': question['title'],
        'view_count': question['view_count'],
        'tags': question['tags'],
        'owner_account_id': question['owner']['account_id'],
        'owner_reputation': question['owner']['reputation'],
        'owner_user_id': question['owner']['user_id'],
        'owner_user_type': question['owner']['user_type'],
        'owner_accept_rate': question['owner'].get('accept_rate', None),
        'is_answered': question['is_answered'],
        'accepted_answer_id': question.get('accepted_answer_id', None),
        'answer_count': question['answer_count'],
        'score': question['score'],
        'last_activity_date': question['last_activity_date'],
        'creation_date': question['creation_date'],
        'question_link': question['link']
    }
    question_list.append(question_data)
# Create DataFrame
df = pd.DataFrame(question_list)
df.to_csv("output.csv")
# Display DataFrame
print(df)
print(df.columns)