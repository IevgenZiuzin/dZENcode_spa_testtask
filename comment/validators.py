from html.parser import HTMLParser


class TagChecker(HTMLParser):
    allowed_tags = ['a', 'code', 'i', 'strong']
    has_forbidden_tags = False
    counter = 0

    def check_tag(self, tag):
        if tag not in self.allowed_tags:
            self.has_forbidden_tags = True
        for char in tag:
            if char.isupper():
                self.has_forbidden_tags = True

    def check_attrs(self, attrs):
        for attr in attrs:
            for char in attr:
                if char.isupper():
                    self.has_forbidden_tags = True

    def handle_starttag(self, tag, attrs):
        self.check_tag(tag)
        self.check_attrs(attrs)
        self.counter += 1

    def handle_endtag(self, tag):
        self.check_tag(tag)
        self.counter -= 1

    def check(self, string):
        self.feed(string)
        if not self.has_forbidden_tags:
            return self.counter == 0
        return False


def validate_content(string):
    checker = TagChecker()
    return checker.check(string)


a = '<a href=”” title=””> </a> <code> </code> <i> </i> <strong> </strong>'
print(validate_content(a))
