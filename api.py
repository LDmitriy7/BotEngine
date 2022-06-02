class Tags:
    _a = '<a href="{url}">{text}</a>'
    _pre = '<pre>{}</pre>'
    _textarea = '<textarea cols="{cols}" rows="{rows}">{}</textarea>'

    def a(self, text: str, url: str):
        return self._a.format(text=text, url=url)

    def pre(self, text: str):
        return self._pre.format(text)

    def textarea(self, text: str = '', cols: str = '', rows: str = '', ):
        return self._textarea.format(text, cols=cols, rows=rows)


tags = Tags()
