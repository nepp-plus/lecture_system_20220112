from server import db

# 강의의 리뷰에 대한 기능만 모아두는 별도의 파이썬 파일.

def write_review(params):
    
    # 파라미터가 제대로 들어오는가? 검증
    # 1. 평점은 1~5 사이로만 가능.
    
    # 2. 제목의 길이는 최소 5자 이상.
    
    # 3. 내용의 길이는 최소 10자 이상.
    
    # DB내부 조회 결과 활용
    # 4. 수강을 했어야만 리뷰 작성 가능.
    
    
    # 리뷰 실제 등록
    
    return {
        '임시' : '강의 리뷰 작성 기능'
    }