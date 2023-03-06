from flask import Blueprint, session, request, redirect
from app.forms import PostForm
from app.models import Post


post_routes = Blueprint('post', __name__)

@post_routes.route('/post/ping', methods=['GET'])
def get_status():
    return {'status': 'good'}


@post_routes.route('/post', methods=['GET'])
def get_all_posts():
    # get index of all coffees in asc order by name
    posts = Post.query.all()
    return {'posts': [items.post_date().sort() for items in posts]}

@post_routes.route('/post/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get(id)
    return post.to_dict()

@post_routes.route('/post', methods=['POST'])
def post_post():

    form = PostForm()
    allPosts = Post.query.all()

    if form.validate_on_submit():
        new_post = Post(
            title: form.data['title'],
            rating: form.data['rating'],
            coffee: form.data['coffee'],
            post: form.data['post']
        )
        db.session.add(new_post)
        db.session.commit()
        return {'posts': [items.to_dict() for items in allPosts]}
    return {'error': validation_errors_to_error_message(PostForm.errors)}, 400



@post_routes.route('/post/<int:id>', methods=['DELETE'])
def delete_post(id):
    postId = Post.query.get(id)

    if postId == None:
        return {"error": "post couldn't be found"}, 404
    db.session.delete(postId)
    db.session.commit()
    return {'message': Successfully deleted}
