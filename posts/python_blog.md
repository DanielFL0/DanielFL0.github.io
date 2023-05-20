---
title: Building my blog
tags: ['python']
---

For a couple of weeks now I've playing with the idea of writing my own
personal blog where I can write about the projects I'm working on and the
development challenges I solve along the way. I looked at several existing
frameworks/libraries that help you generate your own static site like Hugo and Jekyll, however I found these tools too complicated and overkill
for the site I wanted to make, in reality I just needed a markdown to html compiler, a templating library and perhaps a frontmatter parser, so currently my blog runs using **python-frontmatter**, **jinja2** and **markdown2**.