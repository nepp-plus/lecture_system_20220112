from server import db
from server.model import Posts

# 모든 게시글 조회
def get_all_posts(params):
    
    sql = f"SELECT * FROM posts ORDER BY created_at DESC"
    
    post_data_list = db.executeAll(sql)
    
    post_list = [ Posts(row).get_data_object()  for row in post_data_list ]
    
    return {
        'code': 200,
        'message': '모든 게시글 조회',
        'data': {
            'posts': post_list
        }
    }
    

# 특정 게시글 상세 조회 - GET - /post/5
def view_post(post_id, params):
    
    sql = f"SELECT * FROM posts WHERE id = {post_id}"
    
    post_data = db.executeOne(sql)
    
    return {
        'code': 200,
        'message': '특정 게시글 상세 조회',
        'data': {
            'post': Posts(post_data).get_data_object()
        }
    }
    

# 게시글 등록
def add_post(params):
    
    # 도전과제 : 입력값 검증? (ex. 제목 최소 5글자 등등.)
    
    sql = f"""
    INSERT INTO  posts
    ( user_id, title, content )
    VALUES
    ( {params['user_id']}, '{params['title']}', '{params['content']}' )
    """
    
    db.executeQueryAndCommit(sql)
    
    return {
        'code': 200,
        'message': '게시글 등록'
    }
    

# 게시글 수정
def modify_post(params):
    
    # 파라미터 사전검증
    # 실존 하는 글인가? 내가 쓴 글이 맞는가? + 제목/내용이 비어있는가? 입력 문구가 최소 1자 이상이어야 등록.
    
    sql = f"""
    UPDATE posts
    SET title = '{params['title']}', content='{params['content']}'
    WHERE id = {params['post_id']}
    """
    
    db.executeQueryAndCommit(sql)
    
    return {
        'code': 200,
        'message': '게시글 수정하기'
    }
    

# 게시글 삭제
def delete_post(params):
    
    # 파라미터 검증 -> 본인이 쓴 글이 맞는지? + 지우려는 글이 실존하는지?
    
    sql = f"SELECT * FROM posts WHERE id = {params['post_id']}"
    
    post_data = db.executeOne(sql)
    
    if post_data == None:
        return {
            'code': 400,
            'message': '해당 게시글은 존재하지 않습니다.'
        }, 400
        
    if post_data['user_id'] != int(params['user_id']):
        return {
            'code': 400,
            'message': '본인이 작성한 게시글만 삭제할 수 있습니다.'
        }, 400
    
    sql = f"DELETE FROM posts WHERE id = {params['post_id']}"
    
    db.executeQueryAndCommit(sql)
    
    return {
        'code': 200,
        'message': '게시글 삭제'
    }