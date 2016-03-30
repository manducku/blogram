from tags.models import Tag


def get_tags_all(content):
    tag_list = [
            tag_name[1:]
            for tag_name
            in content.split(" ")
            if tag_name.startswith("#")
            ]
    return tag_list
