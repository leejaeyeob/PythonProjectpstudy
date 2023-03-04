try:
    raise Exception('강제로 발생시킨 에외')
except Exception as e:
    print('발생한 에외 메시지는 다음과 같습니다.')
    print(e)