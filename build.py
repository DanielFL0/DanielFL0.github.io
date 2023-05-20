import os
import frontmatter
from markdown2 import Markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

curr_dir = os.getcwd()
posts_dir = os.path.join(curr_dir, "posts")
templates_dir = os.path.join(curr_dir, "templates")
posts = os.listdir(posts_dir)
markdowner = Markdown()
jinja_env = Environment(
    loader=FileSystemLoader(templates_dir), autoescape=select_autoescape()
)


def render_post(file_name, frontmatter, content):
    post_path = os.path.join(posts_dir, file_name)
    with open(post_path, "w") as file_object:
        template = jinja_env.get_template("post.html")
        post_content = template.render(
            title=frontmatter["title"], tags=frontmatter["tags"], content=content
        )
        file_object.write(post_content)
    print("generated %s" % file_name)


def build_blog():
    for post_name in posts:
        post_path = os.path.join(posts_dir, post_name)
        name = post_name.split(".")[0]
        with open(post_path, "r") as file_object:
            content_md = file_object.read()
            post_fm = frontmatter.loads(content_md)
            content_html = markdowner.convert(post_fm.content)
            render_post(name + ".html", post_fm, content_html)


build_blog()
