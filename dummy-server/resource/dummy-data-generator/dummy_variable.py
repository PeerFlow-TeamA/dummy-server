
# 생성될 csv 파일 이름
csv_dir = './resource/'
csv_name = {
    'writter': 'writter_data.csv',
    'question': 'question_data.csv',
    'answer': 'answer_data.csv',
    'question_comment': 'question_comment_data.csv',
    'answer_comment': 'answer_comment_data.csv',
}

# 더미 데이터 생성 사이즈
dummy_size = {
    'writter': 30,
    'question': 100,
    'answer': 300,
    'answer_comment': 1000,
    'question_comment': 1000
}

# 더미 데이터 생성 옵션
generate_sentence_lang = 'en'
generate_text_lang = 'en'
recomment_min = 0
recomment_max = 100000
views_min = 0
views_max = 10000000
date_random_min = {
    'year': 2022,
    'month': 1,
    'day': 1,
    'hour': 0,
    'minute': 0,
    'second': 0,
}
date_random_max = {
    'year': 2023,
    'month': 12,
    'day': 28,
    'hour': 23,
    'minute': 59,
    'second': 59,
}

# 생성할 csv 파일들의 헤드 정보
csv_head = {
    'writter': ['pk', 'nickname', 'password'],
    'question': ['pk', 'title', 'content', 'nickname', 'password', 'views', 'recomment', 'created_at', 'updated_at'],
    'answer': ['pk', 'question_id', 'content', 'nickname', 'password', 'recomment', 'isAdopted', 'created_at', 'updated_at'],
    'question_comment': ['pk', 'question_id', 'content', 'nickname', 'password', 'created_at', 'updated_at'],
    'answer_comment': ['pk', 'answer_id', 'content', 'nickname', 'password', 'created_at', 'updated_at'],
}

# 성씨와 영문 대응 매핑
last_names = {
    '김': 'kim',
    '이': 'lee',
    '박': 'park',
    '수': 'soo',
    '성': 'sung',
    '최': 'choi',
    '정': 'jung',
    '장': 'jang',
    '임': 'lim',
    '오': 'oh',
    '한': 'han',
    '신': 'shin',
    '서': 'seo',
}