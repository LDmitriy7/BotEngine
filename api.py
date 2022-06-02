class Tags:
    _a = '<a href="{url}">{text}</a>'
    _pre = '<pre>{}</pre>'

    def a(self, text: str, url: str):
        return self._a.format(text=text, url=url)

    def pre(self, text: str):
        return self._pre.format(text)


tags = Tags()
