import os
import frontmatter
from markdown2 import Markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

curr_dir = os.getcwd()
posts_dir = os.path.join(curr_dir, 'posts')
blog_dir = os.path.join(curr_dir, 'blog')
templates_dir = os.path.join(curr_dir, 'templates')
posts = os.listdir(posts_dir)
markdowner = Markdown()
jinja_env = Environment(
    loader = FileSystemLoader(templates_dir),
    autoescape=select_autoescape()
)

def render_post(frontmatter, content):
    post_path = os.path.join(blog_dir, frontmatter['title'] + '.html')
    with open(post_path, 'w') as file_object:
        template = jinja_env.get_template('post.html')
        post_content = template.render(title=frontmatter['title'], tags=frontmatter['tags'], content=content)
        file_object.write(post_content)

def build_blog():
    for post_name in posts:
        post_path = os.path.join(posts_dir, post_name)
        with open(post_path, 'r') as file_object:
            content_md = file_object.read()
            post_fm = frontmatter.loads(content_md)
            content_html = markdowner.convert(post_fm.content)
            render_post(post_fm, content_html)

build_blog()
